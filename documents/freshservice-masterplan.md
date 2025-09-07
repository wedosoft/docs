# 📋 Freshservice 문서 변환 프로젝트 마스터플랜

> **최종 업데이트**: 2024년 12월 19일  
> **현재 단계**: 1단계 완료, 2단계 준비 중  
> **담당자**: GitHub Copilot + Alan

---

## 🎯 프로젝트 개요

### 목표
CSV 형태의 Freshservice 기술문서를 Docusaurus 기반 웹사이트로 자동 변환하여 실무자용 기술문서 포털 구축

### 전체 규모 (CSV 분석 기준)
- **총 카테고리**: 20개
- **총 폴더**: 180개  
- **총 문서**: 1,557개
- **예상 작업 기간**: 6-8개월 (주 20시간 기준)

### 현재 진행 현황
- **1단계**: ✅ 템플릿 표준화 완료 (74개 문서)
- **2단계**: 🔄 대량 변환 시스템 준비 중

---

## 📈 진행 단계별 현황

### ✅ **1단계: 문서 템플릿 표준화** (완료)
**기간**: 2024년 12월  
**성과**: 74개 문서 v3.0 템플릿 적용 완료

| 폴더명 | 문서 수 | 상태 | 완료일 |
|--------|---------|------|--------|
| **Form fields** | 16 | ✅ 완료 | 12/19 |
| **Form templates** | 16 | ✅ 완료 | 12/19 |
| **User-management** | 20 | ✅ 완료 | 12/19 |
| **Setting-up-freshservice** | 9 | ✅ 완료 | 12/19 |
| **Self-service-portal-introduction** | 5 | ✅ 완료 | 12/19 |
| **Freshservice (root)** | 8 | ✅ 완료 | 12/19 |
| **총계** | **74** | **✅ 100%** | **12/19** |

**기술적 성과**:
- v3.0 템플릿 표준화 (sidebar_position only)
- MDX 호환성 문제 해결 (한글 중괄호 이스케이프)
- 문서 품질 표준화 (부제목 형식 통일)
- 사이드바 구조 논리적 재구성

### 🔄 **2단계: 대량 변환 시스템** (준비 중)
**예상 기간**: 2024년 12월 말 ~ 2025년 1월  
**목표**: CSV → Markdown 자동 변환 파이프라인 구축

| 작업 단계 | 상태 | 예상 일정 |
|-----------|------|-----------|
| CSV 데이터 분석 및 스키마 파악 | 📋 대기 | 12월 말 |
| Python 변환 스크립트 개발 | 📋 대기 | 12월 말 |
| 이미지 링크 처리 자동화 | 📋 대기 | 1월 초 |
| 자동 분류 시스템 구축 | 📋 대기 | 1월 초 |
| 대량 변환 및 검증 | � 대기 | 1월 중 |
| 품질 검사 자동화 | 📋 대기 | 1월 말 |

### 🚀 **3단계: 전체 문서 포털 완성** (계획)
**예상 기간**: 2025년 1월 ~ 6월  
**목표**: 1,557개 문서 완전 변환 및 포털 완성

---

## �️ 2단계 작업 계획 (CSV 변환 자동화)

### 🎯 **2.1 CSV 데이터 분석** (1주)
**목표**: 5개 CSV 파일 구조 완전 파악

```bash
# CSV 파일 위치
/raw_data/merged_articles_links_replaced_freshservice_part1.csv
/raw_data/merged_articles_links_replaced_freshservice_part2.csv
/raw_data/merged_articles_links_replaced_freshservice_part3.csv
/raw_data/merged_articles_links_replaced_freshservice_part4.csv
/raw_data/merged_articles_links_replaced_freshservice_part5.csv
```

**분석 항목**:
- [ ] 컬럼 스키마 확인
- [ ] 데이터 품질 검사
- [ ] 카테고리 분류 규칙 파악
- [ ] 이미지 링크 패턴 분석
- [ ] HTML 태그 사용 현황 조사

### 🎯 **2.2 변환 엔진 개발** (2주)
**목표**: Python 기반 자동 변환 시스템 구축

**핵심 모듈**:
```python
modules/
├── csv_parser.py          # CSV 데이터 파싱
├── html_to_markdown.py    # HTML → Markdown 변환
├── image_processor.py     # 이미지 링크 처리
├── category_mapper.py     # 카테고리 자동 분류
├── quality_validator.py   # 품질 검증
└── bulk_converter.py      # 대량 변환 실행
```

**기능 요구사항**:
- [ ] HTML 콘텐츠 → 실무 중심 한국어 번역
- [ ] 이미지 링크 자동 변환 및 검증
- [ ] Freshservice 자리표시자 처리
- [ ] 카테고리별 폴더 자동 생성
- [ ] sidebars.ts 자동 업데이트
- [ ] MDX 호환성 자동 검증

### 🎯 **2.3 품질 보증 시스템** (1주)
**목표**: 변환 결과 자동 검증 및 품질 관리

**검증 항목**:
- [ ] Markdown 문법 준수
- [ ] MDX 빌드 오류 검사
- [ ] 이미지 링크 유효성 검사
- [ ] 한국어 번역 품질 검토
- [ ] 중복 문서 탐지
- [ ] 링크 일관성 검사

---

## 📊 예상 변환 결과 (1,557개 문서)

### 카테고리별 우선순위
| 순위 | 카테고리 | 문서 수 | 중요도 | 예상 기간 |
|------|----------|---------|--------|----------|
| 1 | Getting started with Freshservice | 115 | ⭐⭐⭐⭐⭐ | 1개월 |
| 2 | User Guide - Agent/Admin/End User | 62 | ⭐⭐⭐⭐⭐ | 3주 |
| 3 | Support Guide: IT Service Management | 187 | ⭐⭐⭐⭐ | 1.5개월 |
| 4 | Support Guide: IT Asset Management | 95 | ⭐⭐⭐⭐ | 3주 |
| 5 | Freshservice FAQs | 508 | ⭐⭐⭐ | 2개월 |
| 6 | Enterprise Service Management | 69 | ⭐⭐⭐ | 2주 |
| 7 | IT Operations Management | 95 | ⭐⭐⭐ | 3주 |
| 8 | Platform | 101 | ⭐⭐⭐ | 3주 |
| 9 | Apps and Integrations | 87 | ⭐⭐ | 2주 |
| 10 | 기타 카테고리들 | 238 | ⭐⭐ | 1개월 |

### 변환 목표 일정
```
Phase 1: 핵심 기능      (177개 문서) - 2025년 2월
Phase 2: 서비스 관리    (282개 문서) - 2025년 3월  
Phase 3: FAQ 및 지원    (508개 문서) - 2025년 4월
Phase 4: 고급 기능      (265개 문서) - 2025년 5월
Phase 5: 통합 및 특수   (325개 문서) - 2025년 6월
```

---

## 🎯 성공 지표 및 품질 기준

### � **진행률 추적**
```
현재 상태 (2024.12.19):
1단계 완료: ████████████████████ 100% (74/74 문서)
2단계 준비: ████░░░░░░░░░░░░░░░░ 20% (계획 수립)
전체 진행률: █░░░░░░░░░░░░░░░░░░░ 4.8% (74/1,557 문서)
```

### 🎯 **품질 기준**
- **번역 품질**: 실무진 즉시 활용 가능한 수준
- **기술 정확도**: 100% 빌드 성공률
- **사용성**: 3클릭 이내 모든 문서 접근
- **검색 효율**: 95% 이상 키워드 검색 성공률

### 📈 **마일스톤 목표**
- **2024년 12월**: 1단계 완료 ✅
- **2025년 1월**: 2단계 완료 (변환 시스템)
- **2025년 6월**: 전체 프로젝트 완료 (1,557개 문서)

---

## 🔧 기술 스택 및 도구

### **현재 사용 중**
- **빌드 시스템**: Docusaurus v3.0
- **템플릿 표준**: v3.0 간소화 템플릿 (sidebar_position only)
- **호환성 도구**: mdx_fixer.py (MDX 자동 수정)
- **버전 관리**: Git (wedosoft/docs)

### **2단계 개발 예정**
- **변환 엔진**: Python 3.9+
- **데이터 처리**: Pandas, BeautifulSoup4
- **번역 시스템**: GPT-4 기반 실무 번역
- **품질 검증**: 자동화 테스트 스위트
- **배포 자동화**: GitHub Actions CI/CD

---

## � 참고 문서

- [프로젝트 현황](./project-status.md) - 실시간 진행 현황
- [작업 지침서](./work-guidelines.md) - 표준 작업 절차
- [MDX 문제해결](./mdx-troubleshooting.md) - 기술적 문제 해결
- [마크다운 작성 지침](./.github/instructions/markdown-rewriting.instructions.md) - 상세 작성 규칙

---

> **💡 핵심 전략**: 1단계에서 확립된 고품질 템플릿 표준을 기반으로, 2단계에서는 완전 자동화된 대량 변환 시스템을 구축하여 효율성과 품질을 동시에 확보합니다.
```
전체 진행률: ████░░░░░░░░░░░░░░░░ 1.7% (3/180 폴더)

Phase 1: ██░░░░░░░░░░░░░░░░░░░░ 8.8% (3/34 폴더)
Phase 2: ░░░░░░░░░░░░░░░░░░░░░░ 0% (0/36 폴더)  
Phase 3: ░░░░░░░░░░░░░░░░░░░░░░ 0% (0/23 폴더)
Phase 4: ░░░░░░░░░░░░░░░░░░░░░░ 0% (0/35 폴더)
Phase 5: ░░░░░░░░░░░░░░░░░░░░░░ 0% (0/52 폴더)
```

### 완료된 폴더
- ✅ Getting started with Freshservice > Dark Mode
- ✅ Getting started with Freshservice > FreshThemes  
- ✅ Getting started with Freshservice > User Management

### 다음 작업 대상
- 🔄 Getting started with Freshservice > Setting up Freshservice
- ⏳ Getting started with Freshservice > Form fields and Form templates
- ⏳ Getting started with Freshservice > Single Sign On and Remote Authentication

---

## 🎯 성공 지표 (KPI)

### 품질 지표
- **마크다운 문법 준수율**: 100%
- **JSX 호환성**: 100%  
- **이미지 링크 유효성**: 100%
- **번역 품질**: 실무진 검토 통과

### 진행 지표
- **주간 폴더 완료율**: 3-5개 목표
- **전체 프로젝트 진행률**: 매월 15% 이상 증가
- **마일스톤 준수율**: 각 Phase별 일정 준수

### 사용성 지표
- **문서 검색 성공률**: 95% 이상
- **사용자 피드백 점수**: 4.5/5.0 이상
- **문서 접근성**: 모든 문서 3클릭 이내 접근

---

## 🚀 다음 액션 아이템

### 즉시 실행 (이번 주)
1. **Setting up Freshservice** 폴더 작업 시작
2. **Form fields and Form templates** 폴더 작업 계획 수립
3. 작업 템플릿 및 자동화 스크립트 개발

### 단기 계획 (1개월 내)
1. Getting started with Freshservice 카테고리 완료
2. User Guide - Agent 작업 시작
3. 진행률 추적 시스템 고도화

### 중기 계획 (3개월 내)  
1. Phase 1 완료 (기본 기능 문서)
2. Phase 2 착수 (핵심 서비스 관리)
3. 문서 품질 검증 프로세스 구축

---

> 이 마스터 플랜은 프로젝트 진행에 따라 지속적으로 업데이트됩니다.  
> 매주 진행상황을 검토하고 일정을 조정합니다.
