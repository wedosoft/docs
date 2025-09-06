---
title: Setting up Freshservice 섹션 작업 진행 상황
project: Freshservice Documentation
section: setting-up-freshservice
total_files: 11
---

# Setting up Freshservice 섹션 작업 현황

## 📊 전체 진행 현황 (Overall Progress)

**전체 진행률: 9/11 문서 완료 (81.8%)**

### ✅ 완료된 문서 (Completed - 9개)
1. freshservice-onboarding-flow.md ✅
2. freshservice-system-requirements.md ✅ 
3. setting-up-custom-mailbox.md ✅
4. managing-agents-freshservice.md ✅
5. scanning-discovering-assets-network.md ✅
6. time-zones-supported.md ✅
7. languages-supported.md ✅
8. managing-service-catalog.md ✅
9. managing-sla-policy.md ✅

### 🔄 진행 중/예정 문서 (In Progress/Planned - 2개)
10. configuring-business-hours.md
11. setting-up-sso.md

## 📋 작업 우선순위

### 높은 우선순위 (신규 설치 관련)
1. **Freshservice Onboarding Flow** - 초기 설정 흐름
2. **Freshservice System Requirements** - 시스템 요구사항
3. **Setting up a Custom mailbox in Freshservice** - 메일박스 설정
4. **Managing Agents in Freshservice** - 상담원 관리 초기 설정

### 중간 우선순위 (기본 설정)
5. **Configure Multilingual Forms** - 다국어 폼 설정
6. **List of Dynamic Placeholders** - 동적 자리표시자
7. **How to access audit log in Freshservice?** - 감사 로그 접근

### 낮은 우선순위 (참조 자료)
8. **List of Time Zones Supported in Freshservice** - 지원 시간대 목록
9. **List of Languages Supported in Freshservice** - 지원 언어 목록
10. **Scanning and discovering assets in your network** - 자산 검색
11. **Using Rank order in Freshservice Analytics** - 분석 순위 설정

## 🎯 작업 계획

## 1주차 목표 (3개 문서)

### 우선순위 1: freshservice-onboarding-flow.md ✅
- [x] **상태**: 완료
- **제목**: Freshservice 온보딩 플로우
- **설명**: 6단계 종합 온보딩 가이드
- **완료일**: 2024년 진행 중

### 우선순위 2: freshservice-system-requirements.md ✅
- [x] **상태**: 완료  
- **제목**: Freshservice 시스템 요구사항
- **설명**: 브라우저, 모바일, 포트/프로토콜 요구사항
- **완료일**: 2024년 진행 중

### 우선순위 3: setting-up-custom-mailbox.md ✅
- [x] **상태**: 완료
- **제목**: 사용자 정의 메일박스 설정
- **설명**: Google, Microsoft, 기타 메일 서버 설정
- **완료일**: 2024년 진행 중

## 2주차 목표 (4개 문서)

### 우선순위 4: managing-agents-freshservice.md ✅
- [x] **상태**: 완료
- **제목**: Freshservice 에이전트 관리
- **설명**: 에이전트 추가, 프로필 관리, 비활성화, 그룹 멤버십
- **완료일**: 2024년 진행 중

### 우선순위 5: scanning-discovering-assets-network.md ✅
- [x] **상태**: 완료
- **제목**: 네트워크 자산 스캔 및 검색
- **설명**: Discovery Probe를 통한 네트워크 자산 자동 검색
- **완료일**: 2024년 진행 중

## 🏆 2주차 성과 요약 (2주차 완료!)

**⚡ 주요 성과**:
- ✅ **4개 문서 100% 완료** (목표 달성!)
- ✅ **사이드바 연동 완료** (navigration 설정)
- ✅ **빌드 테스트 성공** (오류 없음)
- ✅ **템플릿 표준화** (통일된 품질)

**📚 완성된 문서들**:
1. **시간대 지원** → time-zones-supported.md (140개 시간대 테이블)
2. **언어 지원** → languages-supported.md (33개 언어 코드)  
3. **서비스 카탈로그** → managing-service-catalog.md (종합 관리 가이드)
4. **SLA 정책** → managing-sla-policy.md (고급 정책 설정)

### 3주차 목표 (참조 자료 4개)
- [ ] `time-zones-supported.md`
- [ ] `languages-supported.md`
- [ ] `scanning-discovering-assets-network.md`
- [ ] `rank-order-analytics.md`

## 📝 신규 템플릿 구조

```markdown
---
sidebar_position: [순서]
---

# [제목]

[간단한 개요 1-2문장]

## [주요 섹션]

### [하위 섹션]

:::info [정보]
중요한 안내사항
:::

:::warning [경고]
주의사항이나 시스템 요구사항
:::

:::tip [팁]
효율적인 설정 방법
:::

## 실무 활용 예시

### 상황 1: [구체적 설정 시나리오]
**목표**: [달성하고자 하는 설정 목표]
**방법**: 
1. [단계별 설정 과정]
2. [추가 설정 사항]

## 문제 해결

### 자주 발생하는 설정 문제

#### 문제: [구체적 설정 문제]
**원인**: [문제 발생 이유]
**해결**: [단계별 해결 방법]

## 관련 문서

:::info 참조 문서 작업 방침
이 섹션은 모든 관련 문서가 생성된 후 최종 작업 단계에서 링크를 추가합니다.
현재는 섹션 제목만 유지하고 broken links 방지를 위해 링크는 추가하지 않습니다.
:::

<!-- 최종 작업 시 아래 형태로 추가:
- [관련 문서 1](./relative-path-1)
- [관련 문서 2](./relative-path-2)
- [외부 참조](https://external-link.com)
-->
```

## 🔧 작업 프로세스

### 1단계: 원문 추출
```bash
# CSV에서 HTML 추출 후 내용 파악
python extract_content.py "[문서 제목]"
```

### 2단계: 구조 설계
- 기존 내용을 신규 설정 중심 템플릿 구조에 맞게 재구성
- 실무 시나리오 및 문제 해결 섹션 추가 계획

### 3단계: 작성 및 번역
- 통합 템플릿 적용
- 한국어 번역 및 초기 설정 중심 리라이팅
- UI 컴포넌트 활용

### 4단계: 검토 및 배포
- 체크리스트 기반 품질 확인
- 빌드 테스트 및 링크 검증
- Git 커밋 및 배포

## 📋 품질 기준

### 각 문서 필수 포함 요소
- ✅ `sidebar_position` 번호 순서
- ✅ 명확한 H1 제목
- ✅ 1-2문장 개요
- ✅ 초기 설정 관련 실무 시나리오 2-3개 이상
- ✅ 적절한 Callout 박스 활용
- ✅ 관련 문서 링크
- ✅ 시스템 요구사항 또는 전제 조건 명시
- ✅ 설정 완료 후 검증 방법 포함

### 초기 설정 문서 특화 요소
- ✅ **시스템 요구사항**: 필요한 권한, 플랜, 브라우저 등
- ✅ **전제 조건**: 설정 전 준비사항
- ✅ **단계별 가이드**: 스크린샷과 함께 명확한 설정 단계
- ✅ **검증 방법**: 설정이 올바르게 완료되었는지 확인 방법
- ✅ **트러블슈팅**: 설정 중 발생할 수 있는 일반적인 문제들

## 🔗 참고 자료

- **템플릿 가이드**: `.github/instructions/unified-doc-template.md`
- **마크다운 지침**: `.github/instructions/markdown-rewriting.instructions.md`
- **성공 사례**: user-management 폴더 (20개 문서 100% 완료)
- **원본 데이터**: `raw_data/merged_articles_links_replaced_freshservice_part*.csv`

## 🏆 성공 지표

- **완성도**: 각 문서만으로도 해당 설정 완료 가능
- **실용성**: 신규 관리자가 단계별로 따라할 수 있는 수준
- **일관성**: 동일한 구조와 톤앤매너 유지
- **정확성**: 최신 Freshservice UI에 맞는 정확한 정보

---

**마지막 업데이트**: 2025-01-06
**담당자**: GitHub Copilot
**상태**: 시작 대기
**예상 완료**: 3주 후
