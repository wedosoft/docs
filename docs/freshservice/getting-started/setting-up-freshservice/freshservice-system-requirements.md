---
sidebar_position: 2
---

# Freshservice 시스템 요구사항

Freshservice는 웹 브라우저나 모바일 앱을 통해 접근할 수 있는 클라우드 기반 서비스 데스크 애플리케이션이에요. 원활한 Freshservice 사용을 위한 시스템 요구사항을 안내해드려요.

:::info 클라우드 서비스 특성
Freshservice는 클라우드 기반 서비스로 별도의 서버 설치 없이 웹 브라우저만으로 즉시 사용할 수 있어요.
:::

## 웹 애플리케이션 지원 브라우저

### 권장 브라우저 버전

- **Chrome/Firefox/Safari/Microsoft Edge**: 최신 2개 버전

:::tip 브라우저 업데이트 권장
최적의 성능과 보안을 위해 항상 최신 버전의 브라우저 사용을 권장해요.
:::

### 네트워크 접근

기본적으로 Freshservice 웹 포털은 **포트 443**을 통해 접근 가능해요.

## 모바일 앱 지원 운영체제

### iOS 환경
- **최소 요구사항**: iOS 10 이상

### Android 환경
- **최소 요구사항**: Android 7.1.1 이상

:::warning 구버전 지원 제한
명시된 최소 버전 이하의 운영체제에서는 정상적인 동작을 보장하지 않아요.
:::

## Discovery Probe 시스템 요구사항

네트워크 자산 검색을 위한 Discovery Probe 설치 시스템 요구사항은 [Discovery Probe 시스템 요구사항 문서](https://support.freshservice.com/support/solutions/articles/158680)에서 확인할 수 있어요.

### 포트 및 프로토콜 요구사항

성공적인 디스커버리를 위해 Probe는 장치에 ping을 할 수 있어야 해요. 장치에 대한 세부 정보를 수집하기 위해 WMI, SSH, SNMP 등 다양한 프로토콜을 사용해요.

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
WMI는 RPC 및 DCOM 설정에 의해 제어돼요. RPC 동적 포트 할당은 1024 이상의 임의 포트를 사용해요. 1024 이상의 모든 포트를 여는 것은 실용적이지 않으므로, 레지스트리에 수동으로 항목을 추가해서 액세스를 제한할 수 있어요. 자세한 지침은 [Microsoft 문서](https://support.microsoft.com/en-us/kb/154596)를 참조하세요.
:::

## Discovery Agents 시스템 요구사항

Discovery Agents 설치를 위한 시스템 요구사항은 [Discovery Agents 시스템 요구사항 문서](https://support.freshservice.com/support/solutions/articles/200393)에서 확인할 수 있어요.

:::info 네트워크 접근성 요구사항
디스커버리 도구가 작동하려면 Probe 서버 또는 에이전트 머신에서 Freshservice 포털에 접근할 수 있어야 해요.
:::

:::success 시스템 준비 완료
모든 시스템 요구사항을 확인하셨다면 이제 안정적인 Freshservice 환경 구축이 가능해요.
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
