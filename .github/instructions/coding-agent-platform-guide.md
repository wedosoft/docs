# 🤖 코딩 에이전트 Platform 작업 지침서

> **목적**: 사전 지식 없이 할당받은 Platform 폴더 작업을 즉시 수행할 수 있는 완전 자립형 가이드

## 🚀 5분 빠른 시작

### 1단계: 현재 상황 파악 (1분)
```bash
# 작업 디렉터리 확인
cd /Users/alan/GitHub/docs/docs/freshservice/platform

# 할당받은 폴더의 문서 개수 확인
find [할당받은폴더명] -name "*.md" | wc -l

# 예: analytics 폴더 할당 시
find analytics -name "*.md" | wc -l
```

### 2단계: 템플릿 기준 확인 (2분)
```bash
# 이미 완료된 문서 확인 (참조용)
ls -la /Users/alan/GitHub/docs/docs/freshservice/platform/

# 완료 예시 문서들:
# - index.md
# - platform-components-overview.md  
# - analytics/getting-started-with-analytics-basic.md
# - analytics/getting-started-with-the-analytics-platform.md
# - analytics/analytics-glossary.md
```

### 3단계: 즉시 작업 시작 (2분)
```bash
# 빌드 테스트 (작업 전 상태 확인)
npm run build

# 작업 완료 후 재테스트
npm run build
```

---

## 📋 작업 표준 (무조건 준수)

### ✅ **필수 작업 체크리스트**

#### **1. Frontmatter 표준화**
```yaml
# 모든 .md 파일 상단에 추가
---
sidebar_position: [숫자]
---
```

#### **2. H1 제목 표준화**
```markdown
# 기능명 (명사형)

# ❌ 잘못된 예시
# How to Configure Analytics
# Setting Up Dashboard  

# ✅ 올바른 예시  
# Analytics 구성
# 대시보드 설정
```

#### **3. Callout 박스 추가**
```markdown
:::info 주요 기능
이 문서에서 다루는 핵심 내용을 간단히 설명
:::

:::warning 주의사항
제한사항이나 중요한 전제조건
:::

:::tip 활용 팁
실무에서 유용한 추가 정보
:::
```

---

## 🎯 폴더별 작업 특성

### **📊 Analytics (40개 문서)**
```
특성: 대시보드, 차트, 리포트 중심
주의사항: 이미지 많음, 테이블 복잡함
예상 시간: 3-4일
완료 예시: analytics/getting-started-with-analytics-basic.md
```

### **🔄 Workflow Automator (28개 문서)**
```
특성: 자동화 설정, 워크플로 구성
주의사항: 복잡한 설정 단계, 조건부 로직
예상 시간: 2-3일
```

### **📈 Reporting (16개 문서)**
```
특성: 데이터 분석, 차트 생성
주의사항: 수식, 계산 로직 포함
예상 시간: 1-2일
```

### **⚙️ 기타 폴더들 (각 1-7개 문서)**
```
- managing-freshservice-subscription (7개)
- freshworks-organization (5개)  
- custom-objects (3개)
- api-v1-deprecation (2개)
- credential-store (1개)
- security (1개)

특성: 설정/관리 중심, 상대적으로 단순
예상 시간: 각 1일 이내
```

---

## 🔧 실행 명령어 모음

### **파일 분석**
```bash
# 특정 폴더의 모든 .md 파일 나열
find [폴더명] -name "*.md" -type f

# 이미 frontmatter가 있는 파일 찾기
grep -l "sidebar_position" [폴더명]/*.md

# frontmatter가 없는 파일 찾기
grep -L "sidebar_position" [폴더명]/*.md | head -5
```

### **일괄 처리 스크립트**
```bash
# 특정 폴더의 모든 .md 파일에 기본 frontmatter 추가
for file in [폴더명]/*.md; do
    if ! grep -q "sidebar_position" "$file"; then
        echo "---\nsidebar_position: 1\n---\n$(cat $file)" > "$file"
    fi
done
```

### **품질 검증**
```bash
# 빌드 테스트
npm run build

# 링크 오류 확인 (빌드 로그에서)
npm run build 2>&1 | grep -i "error\|failed"

# 완료 현황 확인
find [폴더명] -name "*.md" -exec grep -l "sidebar_position" {} \; | wc -l
```

---

## 📝 작업 완료 기준

### **✅ 완료 체크포인트**

1. **구조 확인**
   - [ ] 모든 .md 파일에 frontmatter 추가
   - [ ] H1 제목이 명사형으로 변경됨
   - [ ] 최소 1개 이상의 callout 박스 추가

2. **품질 검증**
   - [ ] `npm run build` 성공
   - [ ] 빌드 로그에 ERROR 없음
   - [ ] 할당받은 폴더의 모든 파일 처리 완료

3. **완료 보고**
   - [ ] 이슈에 완료 코멘트 작성
   - [ ] 변경된 파일 수와 주요 개선 사항 요약
   - [ ] 빌드 테스트 성공 스크린샷 또는 로그

---

## 🚨 문제 해결

### **자주 발생하는 오류**

#### **빌드 오류 시**
```bash
# MDX 호환성 문제 해결
python3 scripts/mdx_fixer.py docs/freshservice/platform/[폴더명]/

# 캐시 정리 후 재빌드
npm run clear
npm run build
```

#### **파일이 너무 많을 때**
```bash
# 우선순위: index.md부터 처리
# 그 다음: getting-started, overview 관련 파일
# 마지막: 세부 기능 문서들

# 5개씩 나누어 처리
find [폴더명] -name "*.md" | head -5
```

#### **복잡한 HTML 구조**
```markdown
# 원본 HTML은 그대로 보존
# 필요한 경우에만 한국어 설명 추가

<원본 HTML 콘텐츠>

위 설정을 통해 한국 기업 환경에서 효과적으로 활용할 수 있습니다.
```

---

## 📚 필수 참조 문서

### **템플릿 가이드**
- `.github/instructions/unified-doc-template.md` - 상세 템플릿 규칙
- `docs/freshservice/platform/index.md` - 완료 예시

### **기술 문제 해결**
- `.github/instructions/mdx-compatibility-guide.md` - MDX 오류 해결
- `documents/mdx-troubleshooting.md` - 상세 문제 해결

### **현재 진행 상황**
- GitHub Issues: 할당받은 작업의 상세 내용과 요구사항
- GitHub Projects: 전체 진행 상황과 우선순위

---

## 🎯 성공 사례 템플릿

### **완료된 문서 예시**
```markdown
---
sidebar_position: 1
---

# Analytics 기본 설정

:::info Analytics 플랫폼 개요
Freshservice Analytics를 통해 서비스 데스크 성과를 측정하고 개선할 수 있습니다.
:::

## 주요 기능

### 대시보드 구성
[원본 HTML 콘텐츠 보존]

:::tip 실무 활용
한국 기업 환경에서는 부서별 권한 설정을 통해 보안을 강화하는 것이 좋습니다.
:::

## 설정 방법

### 1단계: 기본 설정
[단계별 가이드]

### 2단계: 고급 설정  
[상세 설정 방법]

:::warning 주의사항
데이터 보관 기간은 회사 정책에 따라 조정하세요.
:::
```

---

## ⏱️ 예상 작업 시간표

| 폴더명 | 문서 수 | 예상 시간 | 우선순위 |
|--------|---------|----------|----------|
| analytics | 40개 | 3-4일 | 높음 |
| workflow-automator | 28개 | 2-3일 | 높음 |
| reporting | 16개 | 1-2일 | 중간 |
| managing-freshservice-subscription | 7개 | 1일 | 중간 |
| freshworks-organization | 5개 | 1일 | 낮음 |
| custom-objects | 3개 | 반나절 | 낮음 |
| api-v1-deprecation | 2개 | 반나절 | 낮음 |
| credential-store | 1개 | 1시간 | 낮음 |
| security | 1개 | 1시간 | 낮음 |

---

> **💡 최종 목표**: Platform 폴더 102개 문서 모두 템플릿 표준 적용 완료
> **🎯 품질 기준**: npm run build 성공 + 일관된 구조 + 원본 콘텐츠 보존