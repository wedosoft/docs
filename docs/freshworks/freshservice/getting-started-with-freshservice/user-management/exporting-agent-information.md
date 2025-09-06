---
id: exporting-agent-information
title: 상담원 정보 내보내기
sidebar_label: 상담원 정보 내보내기
---

<div class="subtitle">
  이 문서는 "상담원 정보 내보내기(Exporting Agent Information)" 기능의 개념과 설정 방법을 안내하는 문서입니다.
</div>

## 개요

Freshservice에서 상담원 정보를 CSV 파일로 내보내어 외부 시스템과의 데이터 연동, 보고서 작성, 백업 등의 목적으로 활용할 수 있습니다. 필요한 필드만 선택하여 효율적으로 데이터를 추출할 수 있습니다.

## 상담원 정보 내보내기 방법

### 1. 내보내기 페이지 접근

1. **관리자 → 사용자 관리 → 상담원**으로 이동합니다.
2. **내보내기(Export)** 버튼을 클릭합니다.
3. 계정에 여러 워크스페이스가 있는 경우:
   - **관리자 → 전역 설정 → 사용자 관리 → 상담원**으로 이동합니다.

### 2. 내보낼 필드 선택

1. 팝업창에서 계정에서 사용 가능한 **필드 목록**이 표시됩니다.
2. 필요한 필드를 선택합니다.
3. **내보내기(Export)**를 클릭합니다.

### 3. CSV 파일 수신

- 선택한 필드가 포함된 **CSV 파일**이 이메일로 전송됩니다.
- 시스템의 모든 상담원 정보가 포함됩니다.

## 내보낼 수 있는 필드 정보

### 기본 정보 필드

<table>
<thead>
<tr><th>필드명</th><th>설명</th><th>가능한 값</th></tr>
</thead>
<tbody>
<tr>
  <td><strong>전체 이름</strong></td>
  <td>상담원의 이름</td>
  <td>텍스트 형식</td>
</tr>
<tr>
  <td><strong>이메일</strong></td>
  <td>기본 이메일 주소</td>
  <td>username@domain.ext 형식</td>
</tr>
<tr>
  <td><strong>임시 상담원</strong></td>
  <td>정규직/임시직 구분</td>
  <td>FALSE (정규직)<br/>TRUE (임시직)</td>
</tr>
<tr>
  <td><strong>직급</strong></td>
  <td>직무 제목</td>
  <td>텍스트 형식</td>
</tr>
<tr>
  <td><strong>업무용 전화</strong></td>
  <td>업무용 전화번호</td>
  <td>텍스트 형식</td>
</tr>
<tr>
  <td><strong>휴대폰</strong></td>
  <td>휴대폰 번호</td>
  <td>텍스트 형식</td>
</tr>
<tr>
  <td><strong>위치</strong></td>
  <td>상담원의 근무 위치</td>
  <td>관리자 → 자산 관리 → 위치에서 설정된 위치명</td>
</tr>
<tr>
  <td><strong>보고 관리자</strong></td>
  <td>직속 상관의 이메일</td>
  <td>username@domain.ext 형식</td>
</tr>
</tbody>
</table>

### 그룹 및 역할 필드

<table>
<thead>
<tr><th>필드명</th><th>설명</th><th>가능한 값</th></tr>
</thead>
<tbody>
<tr>
  <td><strong>그룹</strong></td>
  <td>소속 그룹 목록</td>
  <td>여러 그룹인 경우 쉼표로 구분<br/>"그룹1, 그룹2, 그룹3"</td>
</tr>
<tr>
  <td><strong>역할</strong></td>
  <td>할당된 기본/맞춤 역할</td>
  <td>여러 역할인 경우 쉼표로 구분<br/>"역할1, 역할2, 역할3"</td>
</tr>
</tbody>
</table>

### 접근 권한 필드

<table>
<thead>
<tr><th>필드명</th><th>설명</th><th>가능한 값</th></tr>
</thead>
<tbody>
<tr>
  <td><strong>티켓 범위</strong></td>
  <td>티켓 가시성 권한</td>
  <td>전역 접근<br/>그룹 접근<br/>제한된 접근</td>
</tr>
<tr>
  <td><strong>문제 범위</strong><br/>(Pro/Enterprise)</td>
  <td>문제 가시성 권한</td>
  <td>전역 접근<br/>그룹 접근<br/>제한된 접근</td>
</tr>
<tr>
  <td><strong>변경 범위</strong><br/>(Pro/Enterprise)</td>
  <td>변경 가시성 권한</td>
  <td>전역 접근<br/>그룹 접근<br/>제한된 접근</td>
</tr>
<tr>
  <td><strong>릴리스 범위</strong><br/>(Pro/Enterprise)</td>
  <td>릴리스 가시성 권한</td>
  <td>전역 접근<br/>그룹 접근<br/>제한된 접근</td>
</tr>
</tbody>
</table>

### 개인화 설정 필드

<table>
<thead>
<tr><th>필드명</th><th>설명</th><th>가능한 값</th></tr>
</thead>
<tbody>
<tr>
  <td><strong>시간대</strong><br/>(Growth/Pro/Enterprise)</td>
  <td>상담원 근무 시간대</td>
  <td>Freshservice 지원 시간대 목록<br/>(예: Asia/Seoul)</td>
</tr>
<tr>
  <td><strong>언어</strong><br/>(Growth/Pro/Enterprise)</td>
  <td>인터페이스 언어</td>
  <td>Freshservice 지원 언어 목록<br/>(예: ko, en)</td>
</tr>
<tr>
  <td><strong>레벨</strong><br/>(리더보드 활성화 시)</td>
  <td>Arcade 모듈 달성 레벨</td>
  <td>초보자<br/>중급자<br/>전문가<br/>숙련자<br/>마스터<br/>구루</td>
</tr>
</tbody>
</table>

## 실무 활용 시나리오

### 시나리오 1: 인사 시스템 연동
```
선택 필드: 전체 이름, 이메일, 직급, 업무용 전화, 위치, 보고 관리자
목적: 외부 인사 관리 시스템과 데이터 동기화
```

### 시나리오 2: 권한 감사
```
선택 필드: 전체 이름, 이메일, 그룹, 역할, 티켓 범위, 문제 범위
목적: 보안 감사 및 권한 검토
```

### 시나리오 3: 성과 관리
```
선택 필드: 전체 이름, 그룹, 레벨, 위치
목적: 팀별 성과 분석 및 리더보드 현황 파악
```

### 시나리오 4: 조직도 작성
```
선택 필드: 전체 이름, 이메일, 직급, 그룹, 보고 관리자, 위치
목적: 조직 구조 시각화 및 보고 체계 파악
```

## 내보내기 모범 사례

### 데이터 정확성 보장
- 내보내기 전에 상담원 정보가 최신인지 확인
- 중복 계정이나 비활성 계정 정리
- 필수 정보 누락 여부 점검

### 보안 고려사항
- 개인정보가 포함된 CSV 파일의 안전한 보관
- 접근 권한이 있는 담당자만 내보내기 수행
- 정기적인 데이터 정리 및 보존 정책 준수

### 효율적인 활용
- 필요한 필드만 선택하여 파일 크기 최적화
- 정기적인 백업 및 변경 사항 추적
- 내보낸 데이터의 버전 관리

## 주의사항

> **플랜별 제한사항**
> - 일부 필드는 특정 플랜(Growth, Pro, Enterprise)에서만 사용 가능합니다.
> - 리더보드 레벨은 Arcade 모듈이 활성화된 경우에만 표시됩니다.

> **권한 정보 해석**
> - 접근 범위 필드는 할당된 모든 역할 중 가장 넓은 권한을 기준으로 표시됩니다.
> - 여러 그룹이나 역할이 있는 경우 쉼표로 구분되어 표시됩니다.

## 관련 문서

- [상담원 정보 가져오기](./importing-agents.md)
- [상담원 역할 및 권한 설정](./setting-agent-roles-permissions.md)
- [상담원 그룹 생성 및 관리](./create-manage-agent-groups.md)
- [CSV 가져오기 가이드라인](./csv-import-guidelines.md)
