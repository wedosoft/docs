---
sidebar_position: 7
---

# 관리자 컴포넌트 재구성 및 이름 변경

Freshservice는 더 쉬운 네비게이션과 간단한 관리자 컴포넌트 구성을 위해 새롭게 개편된 관리자 페이지를 출시했습니다. 아래에서 이름 및 카테고리 변경 사항의 세부 내용을 확인하세요.

:::info 업데이트 안내
이 재구성은 관리자 컴포넌트의 동작을 변경하지 않습니다. 단지 더 나은 사용자 경험을 위한 구조적 개선입니다.
:::

## 관리자 컴포넌트 재구성

새로운 관리자 페이지는 기능별로 논리적으로 그룹화되어 더 직관적인 네비게이션을 제공합니다.

### 주요 메뉴 구조

<table style="border-collapse: collapse; width: 100%;">
<thead>
<tr style="background-color: #f5f5f5;">
<th style="border: 1px solid #ddd; padding: 8px; font-weight: bold;">메뉴</th>
<th style="border: 1px solid #ddd; padding: 8px; font-weight: bold;">하위 메뉴</th>
<th style="border: 1px solid #ddd; padding: 8px; font-weight: bold;">관리자 컴포넌트</th>
</tr>
</thead>
<tbody>
<tr>
<td style="border: 1px solid #ddd; padding: 8px;">계정 설정</td>
<td style="border: 1px solid #ddd; padding: 8px;">-</td>
<td style="border: 1px solid #ddd; padding: 8px;">계정, 플랜 및 빌링, 워크스페이스 설정, 서비스 데스크 브랜딩, 서비스 데스크 보안, 샌드박스, 일일 패스, 감사 로그, 이메일 알림</td>
</tr>
<tr>
<td style="border: 1px solid #ddd; padding: 8px;">사용자 관리</td>
<td style="border: 1px solid #ddd; padding: 8px;">-</td>
<td style="border: 1px solid #ddd; padding: 8px;">에이전트, 역할, 회사/부서, 회사/부서 필드, 연락처/요청자, 사용자 필드, CAB, 요청자 그룹, 에이전트 그룹</td>
</tr>
<tr>
<td rowspan="3" style="border: 1px solid #ddd; padding: 8px;">채널</td>
<td style="border: 1px solid #ddd; padding: 8px;">이메일</td>
<td style="border: 1px solid #ddd; padding: 8px;">이메일 설정 및 메일함</td>
</tr>
<tr>
<td style="border: 1px solid #ddd; padding: 8px;">채팅</td>
<td style="border: 1px solid #ddd; padding: 8px;">Freshchat, Virtual Agent, ChatBot</td>
</tr>
<tr>
<td style="border: 1px solid #ddd; padding: 8px;">기타 채널</td>
<td style="border: 1px solid #ddd; padding: 8px;">Freshcaller, Freshdesk, 지원 포털, 피드백 위젯</td>
</tr>
<tr>
<td rowspan="2" style="border: 1px solid #ddd; padding: 8px;">서비스 관리</td>
<td style="border: 1px solid #ddd; padding: 8px;">서비스 데스크 설정</td>
<td style="border: 1px solid #ddd; padding: 8px;">비즈니스 시간, SLA 및 OLA 정책, 우선순위 매트릭스, 필드 관리자, 양식 템플릿, 양식 비즈니스 규칙, 태그, 만족도 조사, 종료 규칙, 변경 라이프사이클</td>
</tr>
<tr>
<td style="border: 1px solid #ddd; padding: 8px;">서비스 요청 관리</td>
<td style="border: 1px solid #ddd; padding: 8px;">서비스 카탈로그, 직원 온보딩</td>
</tr>
<tr>
<td rowspan="3" style="border: 1px solid #ddd; padding: 8px;">자동화 및 생산성</td>
<td style="border: 1px solid #ddd; padding: 8px;">자동화</td>
<td style="border: 1px solid #ddd; padding: 8px;">워크플로 자동화, 감독자 규칙, 오케스트레이션 센터, 시나리오 자동화, 자격 증명</td>
</tr>
<tr>
<td style="border: 1px solid #ddd; padding: 8px;">에이전트 생산성</td>
<td style="border: 1px solid #ddd; padding: 8px;">미리 작성된 응답, 스케줄러, 필드 제안자, 응답 제안, 리더보드, 이메일 명령, 팀 허들</td>
</tr>
<tr>
<td style="border: 1px solid #ddd; padding: 8px;">확장성</td>
<td style="border: 1px solid #ddd; padding: 8px;">앱, 커스텀 객체</td>
</tr>
<tr>
<td style="border: 1px solid #ddd; padding: 8px;">자산 관리</td>
<td style="border: 1px solid #ddd; padding: 8px;">-</td>
<td style="border: 1px solid #ddd; padding: 8px;">자산 유형 및 필드, 디스커버리, 클라우드 관리, SaaS 관리, 제품 카탈로그, 벤더, 벤더 필드, 소프트웨어 필드, 계약 유형, 구매 주문 필드, 위치, 자산 감가상각, 관계 유형</td>
</tr>
<tr>
<td style="border: 1px solid #ddd; padding: 8px;">IT 운영 관리</td>
<td style="border: 1px solid #ddd; padding: 8px;">-</td>
<td style="border: 1px solid #ddd; padding: 8px;">알림 규칙, 모니터링 도구, 대기 스케줄</td>
</tr>
<tr>
<td style="border: 1px solid #ddd; padding: 8px;">프로젝트 및 워크로드 관리</td>
<td style="border: 1px solid #ddd; padding: 8px;">-</td>
<td style="border: 1px solid #ddd; padding: 8px;">프로젝트 필드, 프로젝트 협업, JIRA 가져오기, DevOps 통합, 워크로드 관리</td>
</tr>
</tbody>
</table>

## 이름 변경 사항

기존 컴포넌트들의 이름이 더 명확하고 직관적으로 변경되었습니다.

### 주요 이름 변경 목록

<table style="border-collapse: collapse; width: 100%;">
<thead>
<tr style="background-color: #f5f5f5;">
<th style="border: 1px solid #ddd; padding: 8px; font-weight: bold;">기존 이름</th>
<th style="border: 1px solid #ddd; padding: 8px; font-weight: bold;">기존 메뉴</th>
<th style="border: 1px solid #ddd; padding: 8px; font-weight: bold;">새 이름</th>
<th style="border: 1px solid #ddd; padding: 8px; font-weight: bold;">새 메뉴</th>
</tr>
</thead>
<tbody>
<tr>
<td style="border: 1px solid #ddd; padding: 8px;">Requesters Groups</td>
<td style="border: 1px solid #ddd; padding: 8px;">Groups</td>
<td style="border: 1px solid #ddd; padding: 8px;">Requester Groups</td>
<td style="border: 1px solid #ddd; padding: 8px;">User Management</td>
</tr>
<tr>
<td style="border: 1px solid #ddd; padding: 8px;">Agents Groups</td>
<td style="border: 1px solid #ddd; padding: 8px;">Groups</td>
<td style="border: 1px solid #ddd; padding: 8px;">Agent Groups</td>
<td style="border: 1px solid #ddd; padding: 8px;">User Management</td>
</tr>
<tr>
<td style="border: 1px solid #ddd; padding: 8px;">Email</td>
<td style="border: 1px solid #ddd; padding: 8px;">General Settings</td>
<td style="border: 1px solid #ddd; padding: 8px;">Email settings and Mailboxes</td>
<td style="border: 1px solid #ddd; padding: 8px;">Channels > Email</td>
</tr>
<tr>
<td style="border: 1px solid #ddd; padding: 8px;">Chat</td>
<td style="border: 1px solid #ddd; padding: 8px;">General Settings</td>
<td style="border: 1px solid #ddd; padding: 8px;">Freshchat</td>
<td style="border: 1px solid #ddd; padding: 8px;">Channels > Chat</td>
</tr>
<tr>
<td style="border: 1px solid #ddd; padding: 8px;">Phone</td>
<td style="border: 1px solid #ddd; padding: 8px;">General Settings</td>
<td style="border: 1px solid #ddd; padding: 8px;">Freshdesk contact center</td>
<td style="border: 1px solid #ddd; padding: 8px;">Channels > Other channels</td>
</tr>
<tr>
<td style="border: 1px solid #ddd; padding: 8px;">Customer satisfaction</td>
<td style="border: 1px solid #ddd; padding: 8px;">Service Desk productivity</td>
<td style="border: 1px solid #ddd; padding: 8px;">Satisfaction Survey</td>
<td style="border: 1px solid #ddd; padding: 8px;">Service Management > Service Desk Settings</td>
</tr>
<tr>
<td style="border: 1px solid #ddd; padding: 8px;">Supervisor</td>
<td style="border: 1px solid #ddd; padding: 8px;">Service Desk productivity</td>
<td style="border: 1px solid #ddd; padding: 8px;">Supervisor Rules</td>
<td style="border: 1px solid #ddd; padding: 8px;">Automation and Productivity > Automation</td>
</tr>
<tr>
<td style="border: 1px solid #ddd; padding: 8px;">Arcade</td>
<td style="border: 1px solid #ddd; padding: 8px;">Service Desk productivity</td>
<td style="border: 1px solid #ddd; padding: 8px;">Leaderboard</td>
<td style="border: 1px solid #ddd; padding: 8px;">Automation and Productivity > Agent productivity</td>
</tr>
<tr>
<td style="border: 1px solid #ddd; padding: 8px;">Financial management</td>
<td style="border: 1px solid #ddd; padding: 8px;">Asset Management</td>
<td style="border: 1px solid #ddd; padding: 8px;">Asset Depreciation</td>
<td style="border: 1px solid #ddd; padding: 8px;">Asset Management</td>
</tr>
</tbody>
</table>

## 실무 활용 예시

### 상황 1: 신규 관리자 온보딩
**목표**: 새로운 관리자가 시스템을 빠르게 익히도록 지원
**방법**: 
1. 새로운 메뉴 구조를 활용한 체계적 교육 진행
2. 기능별 그룹화를 통해 관련 설정을 한 번에 설명
3. 이름 변경 매핑 테이블을 활용한 기존 지식 연결

**결과**: 학습 시간 단축 및 관리 효율성 향상

### 상황 2: 기존 프로세스 문서 업데이트
**목표**: 내부 프로세스 문서를 새로운 구조에 맞게 업데이트
**방법**:
1. 기존 문서에서 언급된 메뉴 경로 확인
2. 이름 변경 매핑 테이블을 참조하여 새 경로로 수정
3. 관련 팀에 변경 사항 공유 및 교육

**결과**: 일관된 문서화 및 팀 간 소통 개선

### 상황 3: 자동화 설정 재검토
**목표**: 기존 자동화 설정을 새로운 구조에서 재확인
**방법**:
1. "자동화 및 생산성" 메뉴에서 기존 설정 검토
2. 하위 카테고리별로 설정을 체계적으로 정리
3. 누락된 설정이나 중복 설정 식별 및 정리

**결과**: 더 효율적인 자동화 환경 구축

## 주요 개선 사항

### 1. 논리적 그룹화
관련 기능들이 같은 메뉴 아래에 배치되어 더 직관적인 네비게이션이 가능합니다.

:::tip 네비게이션 팁
새로운 구조에서는 관련 기능들이 논리적으로 그룹화되어 있어, 하나의 작업을 완료하기 위해 여러 메뉴를 오가는 횟수가 줄어들었습니다.
:::

### 2. 명확한 이름 체계
기능을 더 정확하게 설명하는 이름으로 변경되어 혼동을 줄입니다.

### 3. 확장 가능한 구조
향후 새로운 기능 추가 시 적절한 카테고리에 배치할 수 있는 확장 가능한 구조입니다.

## 마이그레이션 가이드

### 관리자를 위한 적응 방법

1. **즐겨찾기 업데이트**: 자주 사용하는 기능의 새로운 위치를 파악하고 즐겨찾기를 업데이트하세요.

2. **팀 교육 계획**: 팀원들에게 변경 사항을 공유하고 필요시 교육을 진행하세요.

3. **문서 업데이트**: 내부 절차서나 가이드의 메뉴 경로를 새로운 구조에 맞게 수정하세요.

:::warning 중요 알림
이 재구성은 기능의 동작을 변경하지 않습니다. 단지 더 나은 사용자 경험을 위한 구조적 개선입니다.
:::

## 문제 해결

### 자주 발생하는 문제

#### 문제: 기존 기능을 찾을 수 없음
**원인**: 메뉴 구조 변경으로 인한 위치 변화
**해결**: 
1. 이름 변경 매핑 테이블 참조
2. 관련 기능 그룹에서 검색
3. 전역 검색 기능 활용

#### 문제: 기존 문서의 스크린샷과 다름
**원인**: UI 재구성으로 인한 화면 변화
**해결**:
1. 새로운 구조에 맞는 스크린샷으로 업데이트
2. 핵심 기능은 동일함을 팀에 안내
3. 필요시 새로운 가이드 문서 작성

:::success 적응 완료
새로운 구조에 적응하면 더 효율적이고 직관적인 관리 경험을 얻을 수 있습니다.
:::

## 관련 문서

:::info 참조 문서 작업 방침
이 섹션은 모든 관련 문서가 생성된 후 최종 작업 단계에서 링크를 추가합니다.
현재는 섹션 제목만 유지하고 broken links 방지를 위해 링크는 추가하지 않습니다.
:::

<!-- 최종 작업 시 아래 형태로 추가:
- [관리자 설정 개요](./index)
- [사용자 관리 가이드](./user-management)
- [자동화 설정 가이드](./service-desk-productivity)
-->