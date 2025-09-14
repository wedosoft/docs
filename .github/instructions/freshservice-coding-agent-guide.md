# Freshservice 문서 작성 가이드 - 코딩 에이전트용

## 📋 개요

이 문서는 Freshservice 문서를 CSV 데이터를 기반으로 일관성 있게 작성하기 위한 코딩 에이전트 전용 가이드입니다. 모든 작업은 통합 템플릿(unified-doc-template.md)을 엄격히 준수해야 합니다.

## 🚀 빠른 시작 체크리스트

### 1. 사전 준비 (5분)
- [ ] `/docs/freshservice/user-guide-admin` 폴더 구조 확인
- [ ] `categories/User_Guide_-_Admin.csv` 파일 내용 파악
- [ ] `.github/instructions/unified-doc-template.md` 검토
- [ ] 기존 완성된 문서 1-2개 참조하여 품질 기준 이해

### 2. 작업 진행 (30-45분/문서)
- [ ] CSV에서 HTML 콘텐츠 추출
- [ ] 통합 템플릿 구조에 맞게 마크다운 변환
- [ ] 한국 기업 실무 시나리오 추가 (Samsung, LG, Hyundai 등)
- [ ] 원본 이미지, 테이블, HTML 구조 **완전 보존**
- [ ] Docusaurus callout 컴포넌트로 가독성 향상

### 3. 품질 검증 (10분)
- [ ] 모든 이미지 링크 정상 작동 확인
- [ ] HTML 콘텐츠 완전 보존 확인
- [ ] 한국어 번역 자연스러움 검증
- [ ] 실무 예시 3개 이상 포함 확인

## 📂 작업 환경 설정

### 디렉토리 구조
```
/home/runner/work/docs/docs/
├── docs/freshservice/user-guide-admin/          # 작업 대상 폴더
│   ├── admin-settings/                          # 관리자 설정 문서들
│   ├── getting-started/                         # 시작 가이드
│   ├── incident-management/                     # 인시던트 관리
│   └── [기타 카테고리 폴더들]
├── categories/User_Guide_-_Admin.csv           # 원본 데이터
└── .github/instructions/unified-doc-template.md # 필수 준수 템플릿
```

### 필수 파일 확인 명령어
```bash
# 1. CSV 파일에서 문서 목록 확인
awk -F',' 'NR>1 {print $2}' /home/runner/work/docs/docs/categories/User_Guide_-_Admin.csv

# 2. 기존 완성 문서 확인
find /home/runner/work/docs/docs/docs/freshservice/user-guide-admin -name "*.md" -type f

# 3. HTML 콘텐츠가 남아있는 파일 식별
find /home/runner/work/docs/docs/docs/freshservice/user-guide-admin -name "*.md" -exec grep -l "<p\|<h\|<div\|<span" {} \;
```

## 🎯 핵심 작업 원칙

### ⚠️ 절대 준수 사항 (CRITICAL)

1. **원본 콘텐츠 완전 보존**
   ```markdown
   ❌ 잘못된 방법: 원본 HTML을 단순 마크다운으로 변환
   ## 변경 유형
   변경 유형은 3가지입니다...
   
   ✅ 올바른 방법: 원본 HTML 구조 보존
   ## 변경 유형은 무엇인가요?
   
   <p><span style="font-size: 11pt; font-family: Arial; color: rgb(0, 0, 0);">
   Change Lifecycle is used to define and control...
   </span></p>
   
   <img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/..." />
   ```

2. **한국 기업 실무 시나리오 필수 포함**
   - Samsung Electronics, LG전자, 현대자동차, KB국민은행, 카카오 등
   - 구체적인 부서명과 업무 상황
   - 한국 기업 문화에 맞는 실용적 예시

### 📝 표준 문서 구조

모든 문서는 다음 구조를 **반드시** 따라야 합니다:

```markdown
---
sidebar_position: [숫자]
---

# [기능명 또는 질문형 제목]

[1-2문장 개요 설명]

:::info [상황별 안내]
- [중요한 제약사항이나 전제조건]
:::

## [주요 기능] 설정 방법

### 1단계: [첫 번째 작업]
1. **[메뉴 경로]**로 이동
2. **'[버튼명]'** 클릭
3. [원본 HTML 콘텐츠 보존]

![설명](원본_이미지_URL)

### 2단계: [두 번째 작업]
[원본 HTML 테이블이나 리스트 보존]

:::warning [주의사항]
[중요한 제한사항]
:::

## 실무 활용 예시

### 상황 1: [한국 기업 시나리오]
**목표**: [구체적 목표]
**방법**: 
1. [단계별 해결책]
**결과**: [기대 효과]

### 상황 2: [다른 한국 기업 시나리오]
[동일 구조로 2-3개 예시]

## 문제 해결

### 자주 발생하는 문제

#### 문제: [구체적 문제]
**원인**: [문제 발생 이유]
**해결**: [해결 방법]

:::success [해결 완료]
[성공 메시지]
:::

## 관련 문서

:::info 참조 문서 작업 방침
현재는 broken links 방지를 위해 링크는 추가하지 않습니다.
:::
```

## 🔧 작업 프로세스

### 단계 1: CSV에서 콘텐츠 추출 (5분)
```bash
# 특정 문서 찾기
grep "문서제목" /home/runner/work/docs/docs/categories/User_Guide_-_Admin.csv

# HTML 콘텐츠 추출하여 임시 파일로 저장
grep "문서제목" /home/runner/work/docs/docs/categories/User_Guide_-_Admin.csv | cut -d',' -f3 > /tmp/content.html
```

### 단계 2: 문서 작성 (30-40분)

#### 2.1 frontmatter 설정
```yaml
---
sidebar_position: [CSV의 position 값 또는 논리적 순서]
---
```

#### 2.2 제목 작성 원칙
- 기능 중심 명사형: "자동 분류 설정", "SLA 정책 관리"
- 질문형으로 변환: "SLA 정책을 어떻게 설정하나요?"
- 3-6단어로 핵심만 표현

#### 2.3 HTML 콘텐츠 보존 방법
```markdown
<!-- 원본 HTML 그대로 유지 -->
<div dir="ltr">
<p style="line-height: 1.38;"><br></p>
<p>원본 HTML 내용...</p>
<img src="https://s3.amazonaws.com/..." style="width: auto;" />
</div>

<!-- 필요시 번역이나 부연설명만 추가 -->
위 설정을 완료하면 한국 기업 환경에서 효과적으로 활용할 수 있습니다.
```

#### 2.4 한국 기업 시나리오 작성법
```markdown
### 상황 1: 삼성전자 IT헬프데스크 운영
**목표**: 전사 5만명 대상 서비스 데스크 효율성 향상
**방법**: 
1. SLA 정책을 부서별로 차등 적용 (반도체사업부: 1시간, 일반부서: 4시간)
2. 자동 분류 규칙을 한국어 키워드 기반으로 설정
3. 시간대별 워크로드 분산을 위한 스케줄링 적용

**결과**: 응답시간 50% 단축, 고객 만족도 95% 달성
```

### 단계 3: 품질 검증 (10분)

#### 필수 체크리스트
- [ ] 모든 원본 이미지 URL 정상 작동
- [ ] HTML 테이블, 스타일 완전 보존
- [ ] 한국 기업 실무 예시 3개 이상
- [ ] Callout 박스 적절히 활용
- [ ] "관련 문서" 섹션 표준 양식 적용

## 🚨 주의사항 및 함정

### 절대 하면 안 되는 것들

1. **원본 이미지 삭제하지 말 것**
   ```markdown
   ❌ 이미지를 "[이미지 설명]"으로 대체
   ✅ 원본 URL 그대로 유지
   ```

2. **복잡한 HTML 테이블 단순화하지 말 것**
   ```markdown
   ❌ 마크다운 테이블로 변환하여 정보 손실
   ✅ 원본 HTML 테이블 구조 보존
   ```

3. **완전히 새로 작성하지 말 것**
   ```markdown
   ❌ 원본 무시하고 새로 작성
   ✅ 원본 기반으로 번역 및 개선
   ```

### 자주 발생하는 실수들

1. **이미지 경로 수정**: AWS S3 URL은 절대 변경하지 말 것
2. **과도한 마크다운 변환**: HTML이 더 적합한 경우 HTML 유지
3. **한국어 번역 부족**: 기계적 번역보다는 실무 중심 의역 필요
4. **실무 예시 부족**: 반드시 3개 이상의 구체적 시나리오 포함

## 📊 품질 기준 및 평가

### A급 문서 기준 (목표)
- 원본 콘텐츠 100% 보존
- 한국 기업 실무 시나리오 5개 이상
- 모든 이미지 정상 표시
- Docusaurus 컴포넌트 효과적 활용
- 자연스러운 한국어 번역

### B급 문서 기준 (최소 요구사항)
- 원본 콘텐츠 95% 보존
- 한국 기업 실무 시나리오 3개 이상
- 핵심 이미지 정상 표시
- 기본 Callout 박스 활용

### C급 문서 (재작업 필요)
- 원본 콘텐츠 손실 있음
- 실무 시나리오 부족
- 이미지 링크 오류
- 기계적 번역

## 🔍 디버깅 및 문제 해결

### 자주 발생하는 문제와 해결법

#### 1. 이미지가 표시되지 않음
```bash
# 원인 확인
curl -I "https://s3.amazonaws.com/cdn.freshdesk.com/..."

# 해결: 원본 URL 정확성 재확인, 브라우저 캐시 클리어
```

#### 2. HTML 테이블이 깨짐
```markdown
# 원인: 마크다운 변환 시도
# 해결: 원본 HTML 테이블 구조 그대로 유지
<table style="border-collapse: collapse;">
  <tr><td>원본 구조 유지</td></tr>
</table>
```

#### 3. Docusaurus 빌드 오류
```bash
# 원인 확인
npm run build

# 해결: frontmatter 문법 오류, 링크 경로 문제 수정
```

## 📈 성능 최적화 팁

### 작업 속도 향상 방법

1. **템플릿 스니펫 활용**
   ```markdown
   # VS Code 스니펫으로 저장
   "freshservice-scenario": {
     "prefix": "fs-scenario",
     "body": [
       "### 상황 $1: $2",
       "**목표**: $3",
       "**방법**: ",
       "1. $4",
       "**결과**: $5"
     ]
   }
   ```

2. **일괄 처리 스크립트**
   ```bash
   # 여러 파일의 HTML 콘텐츠 식별
   for file in *.md; do
     if grep -q "<p\|<h\|<div" "$file"; then
       echo "HTML content found in: $file"
     fi
   done
   ```

3. **정규표현식 활용**
   ```bash
   # CSV에서 특정 패턴 추출
   grep -o '"[^"]*"' User_Guide_-_Admin.csv | head -20
   ```

## 🎯 완료 기준 및 검증

### 최종 완료 체크리스트

#### 문서 품질
- [ ] 원본 HTML 콘텐츠 100% 보존
- [ ] 모든 이미지 정상 표시
- [ ] 한국 기업 실무 시나리오 3개 이상
- [ ] 자연스러운 한국어 번역
- [ ] Docusaurus 컴포넌트 적절 활용

#### 기술적 완성도
- [ ] frontmatter 올바른 설정
- [ ] 파일명 slug 규칙 준수
- [ ] 링크 오류 없음
- [ ] 빌드 에러 없음

#### 프로젝트 수준
- [ ] 18개 문서 모두 완성
- [ ] 통일된 품질과 스타일
- [ ] "관련 문서" 섹션 표준화
- [ ] 전체 네비게이션 구조 완성

### 검증 스크립트
```bash
#!/bin/bash
# 완료 검증 스크립트

echo "=== Freshservice 문서 완성도 검증 ==="

# 1. 문서 개수 확인
total_docs=$(find /home/runner/work/docs/docs/docs/freshservice/user-guide-admin -name "*.md" -type f | wc -l)
echo "완성된 문서 수: $total_docs/18"

# 2. HTML 콘텐츠 남은 파일 확인
html_files=$(find /home/runner/work/docs/docs/docs/freshservice/user-guide-admin -name "*.md" -exec grep -l "<p\|<h\|<div\|<span" {} \; | wc -l)
echo "HTML 콘텐츠 보존된 파일: $html_files개"

# 3. 한국 기업 시나리오 포함 확인
korean_scenarios=$(find /home/runner/work/docs/docs/docs/freshservice/user-guide-admin -name "*.md" -exec grep -l "삼성\|LG\|현대\|KB\|카카오" {} \; | wc -l)
echo "한국 기업 시나리오 포함 파일: $korean_scenarios개"

# 4. 이미지 링크 확인
broken_images=$(find /home/runner/work/docs/docs/docs/freshservice/user-guide-admin -name "*.md" -exec grep -o 'https://s3.amazonaws.com[^)]*' {} \; | head -5)
echo "이미지 링크 샘플:"
echo "$broken_images"

echo "=== 검증 완료 ==="
```

## 📞 지원 및 참조

### 추가 참조 자료
- `/.github/instructions/unified-doc-template.md` - 필수 템플릿
- `/docs/freshservice/user-guide-admin/getting-started/index.md` - 완성 샘플
- `/categories/User_Guide_-_Admin.csv` - 원본 데이터

### 문제 발생 시 대응
1. 통합 템플릿 가이드라인 재검토
2. 완성된 문서와 비교 분석
3. 원본 HTML 콘텐츠 보존 여부 재확인
4. 한국 기업 시나리오 추가 작업

---

**버전**: 1.0  
**작성일**: 2025-01-06  
**대상**: Freshservice 문서 작성 코딩 에이전트  
**목적**: 일관되고 고품질의 한국 기업 맞춤형 문서 생성