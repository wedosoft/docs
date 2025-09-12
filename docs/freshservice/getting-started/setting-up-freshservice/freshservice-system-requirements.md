---
sidebar_position: 2
---

# Freshservice 시스템 요구사항

Freshservice는 웹 브라우저나 모바일 앱을 통해 접근할 수 있는 클라우드 기반 서비스 데스크 애플리케이션입니다. 원활한 Freshservice 사용을 위한 시스템 요구사항을 안내합니다.

:::info 클라우드 서비스 특성
Freshservice는 클라우드 기반 서비스로 별도의 서버 설치 없이 웹 브라우저만으로 즉시 사용할 수 있습니다.
:::

## 웹 애플리케이션 지원 브라우저

### 권장 브라우저 버전

- **Chrome/Firefox/Safari/Microsoft Edge**: 최신 2개 버전

:::tip 브라우저 업데이트 권장
최적의 성능과 보안을 위해 항상 최신 버전의 브라우저 사용을 권장합니다.
:::

### 네트워크 접근

기본적으로 Freshservice 웹 포털은 **포트 443**을 통해 접근 가능합니다.

## 모바일 앱 지원 운영체제

### iOS 환경
- **최소 요구사항**: iOS 10 이상

### Android 환경
- **최소 요구사항**: Android 7.1.1 이상

:::warning 구버전 지원 제한
명시된 최소 버전 이하의 운영체제에서는 정상적인 동작을 보장하지 않습니다.
:::

## Discovery Probe 시스템 요구사항

네트워크 자산 검색을 위한 Discovery Probe 설치 시스템 요구사항은 [Discovery Probe 시스템 요구사항 문서](https://support.freshservice.com/support/solutions/articles/158680)에서 확인할 수 있습니다.

### 포트 및 프로토콜 요구사항

성공적인 디스커버리를 위해 Probe는 장치에 ping을 할 수 있어야 합니다. 장치에 대한 세부 정보를 수집하기 위해 WMI, SSH, SNMP 등 다양한 프로토콜을 사용합니다.

<table>
<thead>
<tr>
<th style={{ textAlign: 'center' }}>프로토콜</th>
<th style={{ textAlign: 'center' }}>포트</th>
<th style={{ textAlign: 'center' }}>권한</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>WMI (Windows 플랫폼)</strong></td>
<td>135, 445 및 1024 이상</td>
<td>WMI 자격 증명용 로컬 관리자 또는 도메인 관리자 역할</td>
</tr>
<tr>
<td><strong>SSH (Mac, Linux)</strong></td>
<td>22</td>
<td>SSH 자격 증명</td>
</tr>
<tr>
<td><strong>SNMP (프린터, 라우터, 스위치 등 네트워크 장치)</strong></td>
<td>161</td>
<td>읽기 전용</td>
</tr>
</tbody>
</table>

:::warning WMI 포트 설정 주의사항
WMI는 RPC 및 DCOM 설정에 의해 제어됩니다. RPC 동적 포트 할당은 1024 이상의 임의 포트를 사용합니다. 1024 이상의 모든 포트를 여는 것은 실용적이지 않으므로, 레지스트리에 수동으로 항목을 추가하여 액세스를 제한할 수 있습니다. 자세한 지침은 [Microsoft 문서](https://support.microsoft.com/en-us/kb/154596)를 참조하세요.
:::

## Discovery Agents 시스템 요구사항

Discovery Agents 설치를 위한 시스템 요구사항은 [Discovery Agents 시스템 요구사항 문서](https://support.freshservice.com/support/solutions/articles/200393)에서 확인할 수 있습니다.

:::info 네트워크 접근성 요구사항
디스커버리 도구가 작동하려면 Probe 서버 또는 에이전트 머신에서 Freshservice 포털에 접근할 수 있어야 합니다.
:::

## 실무 활용 예시

### 상황 1: 중소기업 IT 부서 환경 준비
**목표**: 30명 규모 회사의 Freshservice 도입
**시스템 준비사항**:
1. 관리자 PC: Chrome 최신 버전 설치
2. 직원들 모바일: iOS 12+ 또는 Android 8+ 확인
3. 방화벽: 포트 443 outbound 허용
4. Discovery 불필요 시 추가 포트 설정 생략

**결과**: 별도 서버 설치 없이 즉시 서비스 시작 가능

### 상황 2: 대기업 IT 자산 관리 환경
**목표**: 1000대 이상 PC/서버 자동 검색 및 관리
**시스템 준비사항**:
1. Discovery Probe 전용 서버 준비
2. 네트워크 관리자와 포트 135, 445, 1024+ 개방 협의
3. 도메인 관리자 계정으로 WMI 접근 권한 설정
4. Linux/Mac 서버용 SSH 키 또는 계정 준비

**결과**: 전체 IT 자산 자동 검색 및 실시간 모니터링 구현

### 상황 3: 하이브리드 환경 (클라우드 + 온프레미스)
**목표**: 클라우드와 온프레미스 혼재 환경의 통합 관리
**시스템 준비사항**:
1. 각 사이트별 Discovery Agent 설치
2. VPN 또는 전용선을 통한 Freshservice 포털 접근 확보
3. 클라우드 인스턴스는 API 연동으로 자산 정보 수집
4. 모바일 앱으로 현장 지원 시 자산 바코드 스캔 활용

**결과**: 위치에 관계없이 모든 IT 자산의 통합 가시성 확보

## 문제 해결

### 자주 발생하는 시스템 요구사항 관련 문제

#### 문제: 브라우저에서 Freshservice 포털 접근 불가
**원인**: 방화벽에서 포트 443 차단 또는 구버전 브라우저 사용
**해결**: 
1. 네트워크 관리자에게 포트 443 outbound 허용 요청
2. 브라우저를 최신 버전으로 업데이트
3. 다른 브라우저(Chrome, Firefox, Edge)로 테스트

#### 문제: Discovery Probe가 Windows PC를 검색하지 못함
**원인**: WMI 포트 차단 또는 권한 부족
**해결**:
1. 포트 135, 445 및 1024+ 범위 확인
2. 로컬 관리자 또는 도메인 관리자 권한 확인
3. Windows 방화벽에서 WMI 예외 설정
4. DCOM 설정에서 WMI 원격 접근 허용

#### 문제: 모바일 앱이 정상 동작하지 않음
**원인**: 운영체제 버전 불호환 또는 네트워크 제한
**해결**:
1. iOS 10+ 또는 Android 7.1.1+ 버전 확인
2. 모바일 데이터 또는 Wi-Fi로 포트 443 접근 테스트
3. 앱 최신 버전으로 업데이트
4. 기기 재시작 후 재시도

:::success 시스템 준비 완료
모든 시스템 요구사항을 확인하셨다면 이제 안정적인 Freshservice 환경 구축이 가능합니다.
:::

## 관련 문서

:::info 참조 문서 작업 방침
이 섹션은 모든 관련 문서가 생성된 후 최종 작업 단계에서 링크를 추가합니다.
현재는 섹션 제목만 유지하고 broken links 방지를 위해 링크는 추가하지 않습니다.
:::

<!-- 최종 작업 시 아래 형태로 추가:
- [Freshservice 온보딩 흐름](./freshservice-onboarding-flow)
- [커스텀 메일박스 설정](./setting-up-custom-mailbox)
- [상담원 관리](./managing-agents-freshservice)
- [감사 로그 접근](./access-audit-log)
-->
