---
sidebar_position: 16
---

# 사용자 정의 티켓 필드 보관 및 삭제

:::info 문서 목적
사용자 정의 티켓 필드 보관 및 삭제 기능으로 필드를 효율적으로 관리하는 방법을 안내합니다.
:::

데이터 손실 없이 티켓 사용자 정의 필드를 사용 중지할 수 있어요. 필드를 보관하면 상담원과 요청자가 해당 필드를 더 이상 채울 수 없게 됩니다.

:::info 보관과 삭제의 차이점
- **보관**: 필드가 제거되지만 계정에서 영구적으로 삭제되지는 않음 (복원 가능)
- **삭제**: 필드가 영구적으로 제거됨 (복원 불가능)
:::

## 필드 보관 기능

### 보관의 특징
- **데이터 보존**: 기존 데이터는 그대로 유지돼요
- **폼에서 제거**: 상담원과 요청자가 더 이상 해당 필드를 입력할 수 없어요
- **복원 가능**: 필요할 때 언제든지 복원할 수 있어요
- **분석 데이터 유지**: Analytics에서는 계속 사용 가능해요

:::warning 기본 필드 제한사항
기본 필드는 삭제하거나 보관할 수 없습니다.
:::

### 필드 보관 방법

**단계별 가이드:**

1. **관리자 > 필드 관리자 > 폼 필드**로 이동해요
2. 보관하려는 티켓 필드에 마우스를 올리세요  
3. 보관 아이콘을 클릭하세요

![필드 보관 과정](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50006913201/original/nuTdyFkahpFWF_stdT-GMy7sseQ0itxhSQ.png?1668449001)

![보관 확인](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50006913202/original/Ni7kstGq-dpWBKu6kKBJk72cQ-sFoumPhw.png?1668449003)

## 필드 보관의 영향

### 워크플로우 자동화 및 슈퍼바이저 규칙

티켓 필드를 보관하면 해당 필드를 사용하는 자동화 규칙이 예상대로 작동하지 않아요.

**주요 영향:**
- 티켓 필드가 포함된 조건이 자동화에서 "false"로 평가돼요
- 자동화를 제대로 실행하려면 필드를 복원하고 자동화에 다시 추가해야 해요

![자동화 영향](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50006913200/original/vp0wl8UMsBAonS--qwneQmQuTW0zb0fUqw.png?1668449000)

### 기타 영향 범위

**티켓 뷰:**
- 보관된 티켓 필드는 더 이상 폼에서 볼 수 없어요

**보고서:**
- 필드 보관 시 Analytics를 제외한 모든 곳에서 제거돼요
- 상담원은 해당 필드의 기록 데이터에 대해 계속 보고할 수 있어요

:::tip 데이터 분석 지속성
보관된 필드의 기록 데이터는 Analytics에서 계속 사용할 수 있어 과거 데이터 분석이 가능합니다.
:::

## 보관된 필드 복원

### 복원 과정

보관된 티켓 필드를 복원할 수 있어요:

1. **관리자 > 필드 관리자 > 폼 필드**로 이동해요
2. 복원하려는 보관된 티켓 필드에 마우스를 올리세요
3. 복원 아이콘을 클릭하세요

![필드 복원](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50006913196/original/WWhz1aeu-_hvnLCj5xrMqBq6RLa3oooNSg.png?1668448998)

### 변경사항 저장

복원 후에는 반드시 **저장** 버튼을 클릭해서 변경사항을 저장하세요.

![변경사항 저장](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50006913199/original/XTP5YWhyZRpaDTmd4FE6wdETiZwVez0dLw.png?1668449000)

## 필드 삭제

### 삭제 방법

티켓 필드를 영구적으로 삭제하려면:

1. 삭제하려는 티켓 필드에 마우스를 올리세요
2. 휴지통 아이콘을 클릭하세요

![필드 삭제](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50006913197/original/MRtj-IccYcBwRsEdMvcbSKkuBmV6KvckCA.png?1668448999)

### 삭제 주의사항

:::danger 영구적 삭제 경고
필드 삭제는 **되돌릴 수 없는 작업**이에요. 삭제된 필드는 복구할 수 없어요.

**나중에 필드가 필요할 수 있다면 삭제 대신 보관 옵션을 사용하길 강력히 권해요.**
:::

![삭제 확인](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50006913203/original/-pKglefQNCQOgvd41-Dkkf3XmvdtqupCTg.png?1668449003)

## 보관 vs 삭제 비교

| 구분 | 보관 | 삭제 |
|------|------|------|
| **데이터 보존** | ✅ 기존 데이터 유지 | ❌ 모든 데이터 영구 삭제 |
| **복원 가능성** | ✅ 언제든지 복원 가능 | ❌ 복원 불가능 |
| **Analytics 사용** | ✅ 기록 데이터 분석 가능 | ❌ 모든 데이터 접근 불가 |
| **폼에서 표시** | ❌ 숨김 처리 | ❌ 완전 제거 |
| **자동화 영향** | ⚠️ 조건이 false로 평가 | ❌ 자동화 규칙 오류 발생 |

## 모범 사례

### 권장사항

1. **보관 우선 고려**: 확실하지 않다면 삭제보다는 보관을 선택
2. **자동화 규칙 확인**: 보관 전에 해당 필드를 사용하는 자동화 규칙이 있는지 확인
3. **데이터 백업**: 중요한 필드는 보관 전에 데이터를 별도로 백업
4. **테스트 환경 활용**: 운영 환경에서 실행하기 전에 테스트 환경에서 먼저 확인

### 사용 시나리오

**보관을 선택해야 하는 경우:**
- 일시적으로 사용하지 않는 필드
- 나중에 다시 사용할 가능성이 있는 필드
- 기록 데이터 분석이 필요한 필드
- 자동화 규칙에서 사용 중인 필드

**삭제를 선택해야 하는 경우:**
- 완전히 불필요한 필드
- 데이터 정리가 목적인 경우
- 보안상 완전 제거가 필요한 필드

:::tip 필드 관리 팁
- 정기적으로 사용하지 않는 필드를 점검해서 보관 처리하세요
- 필드 보관 시 관련 자동화 규칙도 함께 검토하세요
- 중요한 필드는 삭제하기 전에 팀원들과 충분히 논의하세요
:::

## 관련 문서

:::info 참조 문서 작업 방침
이 섹션은 모든 관련 문서가 생성된 후 최종 작업 단계에서 링크를 추가합니다.
현재는 섹션 제목만 유지하고 broken links 방지를 위해 링크는 추가하지 않습니다.
:::

<!-- 최종 작업 시 아래 형태로 추가:
- [사용자 정의 필드 생성](./creating-custom-fields-ticket-problem-change-release-task-form)
- [필드 관리자 사용법](./field-manager-guide)
- [티켓 필드 유형 이해](./understanding-different-types-ticket-fields)
- [워크플로우 자동화](./workflow-automation)
-->
