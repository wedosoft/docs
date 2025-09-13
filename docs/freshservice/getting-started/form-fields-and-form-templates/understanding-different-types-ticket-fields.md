---
sidebar_position: 2
---

# 티켓 필드 유형 이해

Freshservice에서 제공하는 다양한 티켓 필드 유형을 이해하고 각 필드의 특성과 활용 방법을 알아봐요.

:::info 필드 분류
- **기본 필드**: 시스템에서 제공하는 필수 필드 (삭제 불가)
- **사용자 지정 필드**: 비즈니스 요구에 맞게 추가할 수 있는 필드
- **커스터마이징 가능 필드**: 기본 필드이지만 설정 변경 가능
:::

## 사용자 지정 필드 유형

사용자 지정 필드를 통해 고객으로부터 필요한 정보를 체계적으로 수집할 수 있어요.

### 기본 입력 필드

<table>
<thead>
<tr>
<th>필드 유형</th>
<th>설명</th>
<th>활용 예시</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>단일 행 텍스트</strong></td>
<td>한 줄 짧은 텍스트 입력</td>
<td>고객명, 회사명, 제품 모델</td>
</tr>
<tr>
<td><strong>단락 텍스트</strong></td>
<td>여러 줄 긴 텍스트 입력</td>
<td>추가 설명, 특별 요청사항</td>
</tr>
<tr>
<td><strong>숫자</strong></td>
<td>숫자만 입력 가능</td>
<td>주문 ID, 전화번호, 직원번호</td>
</tr>
<tr>
<td><strong>소수점</strong></td>
<td>소수점이 포함된 숫자</td>
<td>금액, 백분율, 평점</td>
</tr>
</tbody>
</table>

### 선택형 필드

<table>
<thead>
<tr>
<th>필드 유형</th>
<th>설명</th>
<th>활용 예시</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>체크박스</strong></td>
<td>단일 선택 (예/아니오)</td>
<td>서비스 구독 여부, 긴급 처리 요청</td>
</tr>
<tr>
<td><strong>드롭다운</strong></td>
<td>목록에서 하나만 선택</td>
<td>국가, 지역, 구매 제품</td>
</tr>
<tr>
<td><strong>멀티셀렉트 드롭다운</strong></td>
<td>목록에서 여러 개 선택</td>
<td>사용 애플리케이션, 취미, 여러 위치</td>
</tr>
</tbody>
</table>

### 고급 필드

<table>
<thead>
<tr>
<th>필드 유형</th>
<th>설명</th>
<th>활용 예시</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>종속 필드</strong></td>
<td>다른 필드 값에 따라 옵션 변경</td>
<td>제품 → 문제 카테고리 → 세부 이슈</td>
</tr>
<tr>
<td><strong>날짜</strong></td>
<td>날짜 선택 필드</td>
<td>보증 만료일, 계약 체결일</td>
</tr>
<tr>
<td><strong>URL</strong></td>
<td>웹 링크 입력</td>
<td>관련 지식베이스, 제품 매뉴얼</td>
</tr>
<tr>
<td><strong>콘텐츠</strong></td>
<td>리치 텍스트 정보 표시</td>
<td>안내사항, 설명서</td>
</tr>
</tbody>
</table>

## 기본 필드 (Default Fields)

시스템에서 기본 제공하는 필드로 티켓 관리의 핵심 정보를 담고 있습니다.

### 필수 기본 필드 (삭제 불가)

<table>
<thead>
<tr>
<th>필드명</th>
<th>설명</th>
<th>중요성</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>요청자</strong></td>
<td>고객의 이메일 주소</td>
<td>티켓 소유자 식별</td>
</tr>
<tr>
<td><strong>제목</strong></td>
<td>티켓의 간단한 요약</td>
<td>빠른 컨텍스트 파악</td>
</tr>
<tr>
<td><strong>소스</strong></td>
<td>티켓 생성 경로</td>
<td>이메일, 전화, 포털 등</td>
</tr>
<tr>
<td><strong>상태</strong></td>
<td>티켓 진행 상태</td>
<td>열림, 대기, 해결됨 등</td>
</tr>
<tr>
<td><strong>긴급도</strong></td>
<td>해결 시급성</td>
<td>SLA 및 우선순위 결정</td>
</tr>
<tr>
<td><strong>영향도</strong></td>
<td>서비스 수준에 미치는 영향</td>
<td>비즈니스 영향 평가</td>
</tr>
</tbody>
</table>

### 관리 관련 필드

<table>
<thead>
<tr>
<th>필드명</th>
<th>설명</th>
<th>활용 목적</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>우선순위</strong></td>
<td>긴급함+영향도로 계산</td>
<td>낮음, 보통, 높음, 긴급</td>
</tr>
<tr>
<td><strong>그룹</strong></td>
<td>할당된 상담원 그룹</td>
<td>팀별 업무 분배</td>
</tr>
<tr>
<td><strong>상담원</strong></td>
<td>담당 상담원</td>
<td>개별 책임자 지정</td>
</tr>
<tr>
<td><strong>설명</strong></td>
<td>티켓 상세 내용</td>
<td>문제 상황 파악</td>
</tr>
</tbody>
</table>

### 자산 관련 필드

<table>
<thead>
<tr>
<th>필드명</th>
<th>설명</th>
<th>활용</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>자산</strong></td>
<td>연결된 자산 정보</td>
<td>하드웨어/소프트웨어 연결</td>
</tr>
<tr>
<td><strong>자산 번호</strong></td>
<td>자산의 고유 ID</td>
<td>자산 추적 및 관리</td>
</tr>
<tr>
<td><strong>자산 유형</strong></td>
<td>자산의 분류</td>
<td>자산 카테고리별 관리</td>
</tr>
</tbody>
</table>

### 커스터마이징 가능 필드

**카테고리**: 3단계 종속 필드로 티켓 분류에 사용됩니다.
- 1단계: 대분류 (예: 하드웨어)
- 2단계: 중분류 (예: 노트북)  
- 3단계: 소분류 (예: 화면 문제)

:::warning 필드 제한사항
- **삭제 불가**: `**` 표시된 필드는 시스템 필수 필드
- **커스터마이징 가능**: `*` 표시된 필드는 설정 변경 가능
- **권한 필요**: 모든 필드 수정에는 Admin 권한 필요
:::

## 필드 선택 가이드

### 데이터 유형별 최적 필드

**짧은 텍스트**: 단일 행 텍스트
- 이름, ID, 코드 등

**긴 설명**: 단락 텍스트  
- 상세 설명, 요구사항 등

**정확한 값**: 숫자/소수점
- 수량, 금액, 측정값 등

**선택 옵션**: 드롭다운/멀티셀렉트
- 카테고리, 지역, 서비스 등

**관련 정보**: 종속 필드
- 계층적 분류가 필요한 경우

:::tip 필드 설계 모범사례
- **필수 최소화**: 사용자 편의를 위해 필수 필드는 최소한으로
- **명확한 라벨**: 필드명은 직관적이고 이해하기 쉽게
- **일관성 유지**: 비슷한 목적의 필드는 동일한 유형 사용
- **검증 규칙**: 데이터 품질을 위한 입력 규칙 설정
:::

## 관련 문서

:::info 참조 문서 작업 방침
이 섹션은 모든 관련 문서가 생성된 후 최종 작업 단계에서 링크를 추가합니다.
현재는 섹션 제목만 유지하고 broken links 방지를 위해 링크는 추가하지 않습니다.
:::

<!-- 최종 작업 시 아래 형태로 추가:
- [폼 필드 기본 설정](./setting-up-form-fields-tickets-problems-changes-releases)
- [드롭다운 필드 설정](./setting-up-dropdown-fields)
- [종속 필드 활용](./understanding-dependent-fields)
- [사용자 지정 필드 생성](./creating-custom-fields-ticket-problem-change-release-task-form)
-->
