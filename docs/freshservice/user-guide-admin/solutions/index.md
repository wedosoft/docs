---
title: 솔루션 (지식 베이스)
description: Freshservice 솔루션 및 지식 베이스 관리 가이드
sidebar_position: 1
---

# 솔루션 (지식 베이스)

## 📋 개요

모든 서비스 데스크는 잘 관리되고 업데이트된 지식 베이스가 필요합니다. 지식 베이스는 일관된 응답 제공과 사용자 자가 해결을 통한 지원 부하 감소라는 두 가지 핵심 문제를 해결합니다.

<h2 dir="ltr">Solutions</h2><p><br></p><p dir="ltr">Every service desk requires a well maintained knowledge base. A well maintained and updated knowledge base solves two of the biggest problems that take place every day. First, with all agents having access to a common place for sharing solutions, you can be sure that responses are consistent throughout. Second, since requesters have access to the knowledge base, they might find a solution even as they type out the problem to report it. As a result, your support load reduces making lives easier.</p><p dir="ltr"><br>With Freshservice, you can add both permanent solutions as well as temporary workarounds to your knowledge base from the <strong>Solutions</strong> tab.&nbsp;</p><p><br></p><p dir="ltr">You can make sure that all the information your agents come across everyday get documented properly into solution articles.</p><p dir="ltr">Once you have populated your knowledge base entries, you can setup your support portal to<br>"auto-suggest" solutions based on the requester's subject line before they submit a ticket.&nbsp;</p><p><br></p><p dir="ltr">You can enable auto-suggest from <strong>Admin → Customer Portal</strong>. You can also get Freshservice to suggest the best possible solutions in response to a ticket by using "Suggest Solutions" inside a ticket.</p><p dir="ltr">Solutions can be public or private. Public solutions are visible in the Self Service Portal and also appear in Search results. Private solutions are agent-only solutions used for internal knowledge sharing.</p><p dir="ltr">Solutions have a 3 level hierarchy: <strong>Category → Folder → Article<br></strong></p><p dir="ltr">Solutions can be of two types: &nbsp;<strong>Workaround</strong> and <strong>Permanent solutions.</strong></p><p dir="ltr">A Solution can have a <strong>Draft</strong> status when you are working on it and can be changed to Published<br>status once it is finished and reviewed.</p><p><br></p><p><br></p>

## 🎯 한국 기업 활용 시나리오

### 시나리오 1: 대기업 통합 지식 관리
**회사**: 현대자동차 IT서비스센터
- **다국어 지원**: 한국어, 영어, 중국어 솔루션 아티클 제공
- **부서별 카테고리**: 생산, 영업, 연구개발 부서별 전용 솔루션
- **자동 제안**: 티켓 제목 기반 관련 솔루션 자동 추천
- **품질 관리**: 정기적 솔루션 검토 및 업데이트 프로세스

### 시나리오 2: 금융권 고객 셀프서비스
**회사**: KB국민은행 디지털채널팀
- **고객 FAQ**: 인터넷뱅킹, 모바일앱 사용법 상세 가이드
- **단계별 가이드**: 스크린샷과 함께 제공하는 상세 매뉴얼
- **보안 가이드**: 피싱 메일 식별, 안전한 거래 방법 안내
- **24시간 접근**: 고객이 언제든지 셀프서비스로 문제 해결

### 시나리오 3: IT 서비스 회사 기술 문서
**회사**: NHN 기술지원팀
- **개발자 가이드**: API 사용법, 개발 환경 설정 가이드
- **운영 매뉴얼**: 서버 관리, 배포 절차, 모니터링 방법
- **트러블슈팅**: 자주 발생하는 문제와 해결 방법 정리
- **버전 관리**: 서비스 업데이트에 따른 문서 버전 관리

## 💡 지식 베이스 구축 전략

### 솔루션 아티클 구조
```markdown
📁 3단계 계층 구조:
Category (대분류)
└── Folder (중분류)
    └── Article (솔루션 아티클)

예시 구조:
IT 지원
├── 하드웨어
│   ├── 데스크톱 문제
│   │   ├── 부팅 오류 해결방법
│   │   └── 성능 저하 진단
│   └── 프린터 문제
└── 소프트웨어
    ├── Office 프로그램
    └── 보안 소프트웨어
```

### 솔루션 유형별 활용

#### 🔧 Workaround (임시 해결책)
```markdown
특징:
- 근본 원인은 해결되지 않음
- 빠른 임시 해결 방법 제공
- 영구 해결책 개발 시까지 활용

활용 예시:
- 알려진 소프트웨어 버그 우회 방법
- 시스템 업데이트 전 임시 설정 변경
- 긴급 상황에서의 대안 절차
```

#### ✅ Permanent Solution (영구 해결책)
```markdown
특징:
- 근본 원인을 완전히 해결
- 재발 방지 효과
- 표준 프로세스로 활용

활용 예시:
- 검증된 문제 해결 절차
- 공식 설정 변경 가이드
- 업계 표준 모범사례
```

### 솔루션 상태 관리
```markdown
📝 Draft (초안):
- 작성 중인 솔루션
- 내부 검토 대상
- 외부 공개 안됨

✅ Published (게시):
- 검토 완료된 솔루션
- 에이전트/고객 모두 접근 가능
- 검색 결과에 표시

🔒 Private:
- 에이전트 전용 솔루션
- 내부 지식 공유용
- 고객 포털에서 비공개
```

## 🚀 고급 기능 활용

### 자동 제안 (Auto-suggest) 설정
```markdown
설정 경로: Admin → Customer Portal

기능:
✅ 티켓 제목 기반 솔루션 자동 추천
✅ 고객이 티켓 제출 전 해결 가능
✅ 지원팀 업무 부하 감소
✅ 고객 만족도 향상

최적화 팁:
- 키워드별 솔루션 매핑 정확도 높이기
- 자주 검색되는 키워드 분석
- 제안 정확도 지속적 개선
```

### 솔루션 검색 최적화
```markdown
검색 성능 향상:
✅ 명확한 제목 작성
✅ 핵심 키워드 태그 추가
✅ 동의어 및 유사 용어 포함
✅ 단계별 구조화된 내용

사용자 경험 개선:
✅ 스크린샷 및 이미지 활용
✅ 단계별 번호 매기기
✅ 중요 정보 하이라이트
✅ 관련 솔루션 연결
```

## 📊 지식 베이스 운영 관리

### 콘텐츠 생명주기 관리
```markdown
생성 단계:
1. 문제 패턴 식별
2. 솔루션 작성 및 검증
3. 내부 검토 진행
4. 승인 후 게시

유지보수 단계:
1. 정기적 내용 검토 (분기별)
2. 사용 통계 분석
3. 피드백 반영 업데이트
4. 구식 정보 아카이브

폐기 단계:
1. 더 이상 관련 없는 내용 식별
2. 대체 솔루션 확인
3. 아카이브 또는 삭제
4. 리다이렉션 설정
```

### 품질 관리 체크리스트
```markdown
✅ 내용 정확성:
- 최신 정보 반영
- 단계별 검증 완료
- 스크린샷 최신화

✅ 사용성:
- 명확한 단계별 설명
- 기술 용어 설명 포함
- 다양한 시나리오 고려

✅ 완성도:
- 시작부터 완료까지 전체 과정
- 예외 상황 대처 방법
- 관련 솔루션 링크

✅ 접근성:
- 적절한 카테고리 분류
- 검색하기 쉬운 키워드
- 권한 설정 적절성
```

## 📈 성과 측정 지표

| KPI | 목표 수치 | 측정 방법 |
|-----|-----------|-----------|
| **솔루션 활용률** | > 60% | 솔루션 조회 후 티켓 미생성률 |
| **검색 만족도** | > 4.0/5.0 | 솔루션 유용성 평가 점수 |
| **Self-Service 비율** | > 40% | 티켓 없이 해결된 문의 비율 |
| **솔루션 최신성** | < 6개월 | 마지막 업데이트 이후 경과 시간 |

### ROI 측정 방법
```markdown
비용 절감 효과:
✅ 티켓 감소로 인한 에이전트 시간 절약
✅ 반복 문의 처리 시간 단축
✅ 고객 대기 시간 감소

생산성 향상:
✅ 에이전트 응답 속도 개선
✅ 일관된 해결 방법 제공
✅ 신입 에이전트 교육 시간 단축

고객 만족도:
✅ 24시간 셀프서비스 가능
✅ 즉시 해결 가능한 문제 증가
✅ 개인화된 솔루션 추천
```

## ⚠️ 운영 시 주의사항

:::warning 지식 베이스 관리 포인트
- **정보 보안**: 민감한 내부 정보는 Private 솔루션으로 분류
- **정확성 유지**: 부정확한 정보로 인한 추가 문제 발생 방지
- **접근 권한**: 부서별, 역할별 적절한 접근 권한 설정
- **지속적 업데이트**: 시스템 변경 시 관련 솔루션 즉시 업데이트
:::

## 🔗 관련 문서

- [Admin Settings](../admin-settings/)
- [User Management](../admin-settings/user-management)
- [Reports](../reports/)
- [Service Desk Productivity](../admin-settings/service-desk-productivity)