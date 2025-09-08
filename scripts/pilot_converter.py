#!/usr/bin/env python3
"""
Freshservice CSV → Markdown 변환 엔진 (v3.0 템플릿 기반)
- 현재 74개 문서 품질 수준 100% 유지
- HTML → MDX 완전 호환 변환
- 이미지, 테이블, 링크 자동 처리
- v3.0 템플릿 적용 (sidebar_position만 사용)
"""

import pandas as pd
import json
import re
import os
from pathlib import Path
from bs4 import BeautifulSoup
import html
from urllib.parse import unquote

class FreshserviceConverter:
    def __init__(self):
        self.conversion_stats = {
            'total_processed': 0,
            'successful': 0,
            'errors': 0,
            'warnings': []
        }
        
    def create_slug(self, title):
        """제목을 slug로 변환 (기존 74개 문서 방식 따름)"""
        # 한국어 및 특수문자 처리
        slug = title.lower()
        slug = re.sub(r'[^\w\s-]', '', slug)  # 특수문자 제거
        slug = re.sub(r'[-\s]+', '-', slug)   # 공백과 하이픈을 단일 하이픈으로
        slug = slug.strip('-')               # 앞뒤 하이픈 제거
        
        return slug
    
    def create_frontmatter_v3(self, row, position):
        """v3.0 템플릿 frontmatter 생성 (sidebar_position만 사용)"""
        return f"""---
sidebar_position: {position}
---

"""
    
    def create_subtitle(self, category_name, folder_name):
        """subtitle div 생성"""
        return f"""<div class="subtitle">
  이 문서는 "{category_name}" 카테고리의 "{folder_name}" 기능에 대한 가이드입니다.
</div>

"""
    
    def clean_html_content(self, html_content):
        """HTML 콘텐츠를 MDX 호환 Markdown으로 변환"""
        if pd.isna(html_content) or not html_content:
            return ""
        
        content = str(html_content)
        
        # BeautifulSoup로 HTML 파싱
        soup = BeautifulSoup(content, 'html.parser')
        
        # 1. 이미지 처리 (Markdown 형식으로 변환)
        for img in soup.find_all('img'):
            src = img.get('src', '')
            alt = img.get('alt', '이미지')
            
            if src:
                # Markdown 이미지 형식으로 변환
                markdown_img = f"![{alt}]({src})"
                img.replace_with(markdown_img)
        
        # 2. 링크 처리
        for link in soup.find_all('a'):
            href = link.get('href', '')
            text = link.get_text()
            
            if href and text:
                markdown_link = f"[{text}]({href})"
                link.replace_with(markdown_link)
        
        # 3. 강조 처리
        for strong in soup.find_all('strong'):
            text = strong.get_text()
            strong.replace_with(f"**{text}**")
        
        for em in soup.find_all('em'):
            text = em.get_text()
            em.replace_with(f"*{text}*")
        
        # 4. 코드 처리
        for code in soup.find_all('code'):
            text = code.get_text()
            code.replace_with(f"`{text}`")
        
        # 5. 리스트 처리
        for ul in soup.find_all('ul'):
            items = ul.find_all('li')
            list_text = '\n'.join([f"- {li.get_text().strip()}" for li in items])
            ul.replace_with(f"\n{list_text}\n")
        
        for ol in soup.find_all('ol'):
            items = ol.find_all('li')
            list_text = '\n'.join([f"{i+1}. {li.get_text().strip()}" for i, li in enumerate(items)])
            ol.replace_with(f"\n{list_text}\n")
        
        # 6. 헤더 처리
        for i in range(1, 7):
            for header in soup.find_all(f'h{i}'):
                text = header.get_text().strip()
                markdown_header = f"{'#' * i} {text}"
                header.replace_with(f"\n{markdown_header}\n")
        
        # 7. 테이블 처리 (복잡한 경우 HTML 유지)
        for table in soup.find_all('table'):
            # 테이블이 복잡한지 확인
            has_complex_content = False
            for cell in table.find_all(['td', 'th']):
                cell_html = str(cell)
                if any(tag in cell_html for tag in ['<img', '<a', '<ul', '<ol', '<br']):
                    has_complex_content = True
                    break
            
            if has_complex_content:
                # 복잡한 테이블은 HTML 유지하되 MDX 호환 처리
                self.fix_table_for_mdx(table)
            else:
                # 단순한 테이블은 Markdown 형식으로 변환
                self.convert_simple_table_to_markdown(table)
        
        # 8. style 속성 MDX 호환 처리
        content = str(soup)
        content = self.fix_style_attributes(content)
        
        # 9. 한국어 중괄호 이스케이프 (기존 mdx_fixer.py 로직)
        content = self.escape_korean_braces(content)
        
        # 10. 불필요한 HTML 태그 제거
        content = self.clean_remaining_html(content)
        
        # 11. 문단 정리
        content = self.normalize_paragraphs(content)
        
        return content
    
    def fix_style_attributes(self, content):
        """style 속성을 MDX 호환 형식으로 변환"""
        # style="..." → style={{...}} 변환
        def style_replacer(match):
            style_content = match.group(1)
            # CSS 속성을 camelCase로 변환
            style_content = re.sub(r'(\w+)-(\w+)', lambda m: m.group(1) + m.group(2).capitalize(), style_content)
            # 값들을 문자열로 처리
            style_content = re.sub(r'(\w+):\s*([^;]+)', r"\1: '\2'", style_content)
            return f"style={{{{{style_content}}}}}"
        
        content = re.sub(r'style="([^"]*)"', style_replacer, content)
        return content
    
    def escape_korean_braces(self, content):
        """한국어가 포함된 중괄호 이스케이프"""
        def brace_replacer(match):
            inner_content = match.group(1)
            # 한국어가 포함되어 있으면 이스케이프
            if re.search(r'[가-힣]', inner_content):
                return f"&#123;&#123;{inner_content}&#125;&#125;"
            return match.group(0)
        
        content = re.sub(r'\{\{([^}]+)\}\}', brace_replacer, content)
        content = re.sub(r'\{([^}]*[가-힣][^}]*)\}', r'&#123;\1&#125;', content)
        
        return content
    
    def fix_table_for_mdx(self, table):
        """복잡한 테이블을 MDX 호환 HTML로 수정"""
        # 테이블 내부의 콘텐츠도 MDX 호환 처리
        for cell in table.find_all(['td', 'th']):
            cell_content = str(cell)
            cell_content = self.fix_style_attributes(cell_content)
            cell_content = self.escape_korean_braces(cell_content)
            # BeautifulSoup 객체 업데이트
            new_cell = BeautifulSoup(cell_content, 'html.parser')
            cell.replace_with(new_cell)
    
    def convert_simple_table_to_markdown(self, table):
        """단순한 테이블을 Markdown 형식으로 변환"""
        rows = table.find_all('tr')
        if not rows:
            return
        
        markdown_table = []
        
        # 헤더 행 처리
        header_row = rows[0]
        headers = [cell.get_text().strip() for cell in header_row.find_all(['th', 'td'])]
        markdown_table.append('| ' + ' | '.join(headers) + ' |')
        markdown_table.append('|' + '---|' * len(headers))
        
        # 데이터 행 처리
        for row in rows[1:]:
            cells = [cell.get_text().strip() for cell in row.find_all(['td', 'th'])]
            if cells:
                markdown_table.append('| ' + ' | '.join(cells) + ' |')
        
        table_text = '\n'.join(markdown_table)
        table.replace_with(f"\n{table_text}\n")
    
    def clean_remaining_html(self, content):
        """불필요한 HTML 태그 정리"""
        # 기본 HTML 태그 제거 (이미 처리된 것들)
        content = re.sub(r'</?p[^>]*>', '\n', content)
        content = re.sub(r'<br[^>]*>', '\n', content)
        content = re.sub(r'</?div[^>]*>', '\n', content)
        content = re.sub(r'</?span[^>]*>', '', content)
        
        return content
    
    def normalize_paragraphs(self, content):
        """문단 정리 및 정규화"""
        # 연속된 빈 줄 정리
        content = re.sub(r'\n\s*\n\s*\n', '\n\n', content)
        
        # 앞뒤 공백 정리
        content = content.strip()
        
        return content
    
    def convert_single_document(self, row, position):
        """단일 문서 변환"""
        try:
            # 기본 정보 추출
            title = row['title']
            category_name = row['category_name']
            folder_name = row['folder_name']
            description = row['description']
            
            # 파일 경로 생성
            category_slug = self.create_slug(category_name)
            folder_slug = self.create_slug(folder_name)
            doc_slug = self.create_slug(title)
            
            # v3.0 템플릿 적용
            frontmatter = self.create_frontmatter_v3(row, position)
            subtitle = self.create_subtitle(category_name, folder_name)
            content = self.clean_html_content(description)
            
            # 최종 문서 구성
            final_content = frontmatter + "# " + title + "\n\n" + subtitle + content
            
            # 관련 문서 섹션 추가 (링크는 나중에 추가)
            final_content += "\n\n## 관련 문서\n\n"
            final_content += ":::info 참조 문서 작업 방침\n"
            final_content += "이 섹션은 모든 관련 문서가 생성된 후 최종 작업 단계에서 링크를 추가합니다.\n"
            final_content += "현재는 섹션 제목만 유지하고 broken links 방지를 위해 링크는 추가하지 않습니다.\n"
            final_content += ":::\n\n"
            final_content += "<!-- 최종 작업 시 아래 형태로 추가:\n"
            final_content += "- [관련 문서 1](./relative-path-1)\n"
            final_content += "- [관련 문서 2](./relative-path-2)\n"
            final_content += "-->\n"
            
            # 파일 경로 및 메타데이터 반환
            file_path = f"docs/freshservice/{category_slug}/{folder_slug}/{doc_slug}.mdx"
            
            return {
                'success': True,
                'file_path': file_path,
                'content': final_content,
                'metadata': {
                    'title': title,
                    'category': category_name,
                    'folder': folder_name,
                    'position': position
                }
            }
            
        except Exception as e:
            self.conversion_stats['errors'] += 1
            return {
                'success': False,
                'error': str(e),
                'title': row.get('title', 'Unknown')
            }
    
    def convert_pilot_samples(self, samples_file='scripts/pilot_samples.json'):
        """파일럿 샘플 일괄 변환"""
        # 샘플 로드
        with open(samples_file, 'r', encoding='utf-8') as f:
            samples = json.load(f)
        
        print(f"파일럿 변환 시작: {len(samples)}개 문서")
        
        # 전체 CSV 데이터 로드 (ID로 상세 정보 찾기용)
        all_data = self.load_all_csv_data()
        
        results = []
        
        for i, sample in enumerate(samples, 1):
            doc_id = sample['id']
            
            # 전체 데이터에서 해당 문서 찾기
            doc_row = all_data[all_data['id'] == doc_id].iloc[0]
            
            print(f"[{i:2d}/50] 변환 중: {sample['title'][:50]}...")
            
            # 문서 변환
            result = self.convert_single_document(doc_row, i)
            
            if result['success']:
                # 파일 저장
                file_path = result['file_path']
                os.makedirs(os.path.dirname(file_path), exist_ok=True)
                
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(result['content'])
                
                print(f"    ✅ 저장됨: {file_path}")
                self.conversion_stats['successful'] += 1
                
            else:
                print(f"    ❌ 오류: {result['error']}")
                self.conversion_stats['warnings'].append({
                    'title': result['title'],
                    'error': result['error']
                })
            
            results.append(result)
            self.conversion_stats['total_processed'] += 1
        
        return results
    
    def load_all_csv_data(self):
        """모든 CSV 파일 로드"""
        csv_files = [
            'raw_data/merged_articles_links_replaced_freshservice_part1.csv',
            'raw_data/merged_articles_links_replaced_freshservice_part2.csv',
            'raw_data/merged_articles_links_replaced_freshservice_part3.csv',
            'raw_data/merged_articles_links_replaced_freshservice_part4.csv',
            'raw_data/merged_articles_links_replaced_freshservice_part5.csv'
        ]
        
        all_data = []
        for file_path in csv_files:
            df = pd.read_csv(file_path)
            all_data.append(df)
        
        return pd.concat(all_data, ignore_index=True)
    
    def print_conversion_report(self):
        """변환 결과 리포트 출력"""
        print("\n" + "="*60)
        print("📊 파일럿 프로그램 변환 결과 리포트")
        print("="*60)
        print(f"총 처리 문서: {self.conversion_stats['total_processed']}")
        print(f"성공: {self.conversion_stats['successful']}")
        print(f"실패: {self.conversion_stats['errors']}")
        
        if self.conversion_stats['successful'] > 0:
            success_rate = (self.conversion_stats['successful'] / self.conversion_stats['total_processed']) * 100
            print(f"성공률: {success_rate:.1f}%")
        
        if self.conversion_stats['warnings']:
            print(f"\n⚠️  경고/오류 목록:")
            for warning in self.conversion_stats['warnings']:
                print(f"  - {warning['title']}: {warning['error']}")
        
        print("\n✅ 파일럿 프로그램 변환 완료!")

def main():
    converter = FreshserviceConverter()
    
    print("🚀 Freshservice 파일럿 프로그램 변환 시작")
    print("현재 74개 문서 품질 수준 유지 목표")
    
    # 파일럿 샘플 변환
    results = converter.convert_pilot_samples()
    
    # 결과 리포트
    converter.print_conversion_report()

if __name__ == "__main__":
    main()
