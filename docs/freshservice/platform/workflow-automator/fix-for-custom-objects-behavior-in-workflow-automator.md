---
sidebar_position: 27
---

# 워크플로우 자동화에서 사용자 정의 객체 동작 수정 사항

이 문서에서는 리더 노드를 활용하는 워크플로우에서 사용자 정의 객체(Custom Object, CO)에서 값을 가져오는 방식의 변경 사항을 설명합니다.

:::info 주요 정보
- 이 기능을 사용하기 전에 필요한 권한과 설정을 확인하세요
- 단계별 접근을 통해 안정적으로 구현하는 것을 권장합니다
:::


## 변경 사항 개요

이전에는 리더 노드가 데이터를 처리하는 방식의 문제로 인해 워크플로우가 사용자 정의 객체에서 중복된 값을 반환했습니다. 이번 업데이트로 고유한 값이 가져와지고 워크플로우 노드 전반에 반영되도록 했습니다. 이러한 설정을 사용하고 있다면 워크플로우가 계속 예상대로 작동하도록 조정이 필요할 수 있습니다.

## 사용자 정의 객체 작동 방식

예시를 통해 이해해보겠습니다.

### 사용자 정의 객체 1 (CO 1) - 기본 데이터 소스

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50013443208/original/F93q4cb37U9Op_S2aKGy7ivdL8wSxnZstw.png?1729432494" width="624" height="185" class="fr-fic fr-dii" data-attachment="[object Object]" data-id="50013443208" style={{ maxWidth: "100%" }} />

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50013443209/original/FPQId1OKM58VT59mlPMMepqHIUy_RcnoZg.png?1729432496" width="624" height="180" class="fr-fic fr-dii" data-attachment="[object Object]" data-id="50013443209" style={{ maxWidth: "100%" }} />

### 사용자 정의 객체 2 (CO 2) - 종속 객체

CO 2는 종속 객체로 CO 1에서 값을 조회합니다.

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50013443207/original/ONNhRJM2fpUvZn0y3CQa_QueJRuGugf7WA.png?1729432494" width="624" height="157" class="fr-fic fr-dii" data-attachment="[object Object]" data-id="50013443207" style={{ maxWidth: "100%" }} />

리더 노드에서 CO 2를 사용하여 CO 1에서 값을 읽는 워크플로우를 고려해보세요.

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50013443210/original/JIKOdCyp3oOunoy27pycLS946-hMF1tTXw.png?1729432498" width="624" height="205" class="fr-fic fr-dii" data-attachment="[object Object]" data-id="50013443210" style={{ maxWidth: "100%" }} />

## 이전 동작

이전에는 리더 노드가 CO 2에 접근할 때, 요청자 1과 요청자 2와 같은 필드에 대해 가져온 값이 동일했습니다. 예를 들어, 실제 데이터와 관계없이 **마지막으로 수정된** CO 레코드 값을 노드가 읽어서 요청자 1과 요청자 2 모두에 대해 Read_Write 값이 가져와졌습니다.

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50013443212/original/f346iQP0MOgMtHfaOLKmhWATX078quBsPw.png?1729432499" width="624" height="349" class="fr-fic fr-dii" data-attachment="[object Object]" data-id="50013443212" style={{ maxWidth: "100%" }} />

## 현재 동작

리더 노드는 이제 CO 2를 처리하여 각 필드에 대해 해당하는 고유한 값을 가져오도록 합니다. 첫 번째 값을 복제하는 대신, 워크플로우는 이제 CO 2에서 고유한 값을 반환합니다.

다음 리더 노드 출력은 요청자 1과 요청자 2에 대해 서로 다른 값(Read와 Write)을 보여줍니다.

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50013443211/original/z-pkOfRwbX-pulgKgRQxGPUVQ8QeQWanLQ.png?1729432498" width="624" height="332" class="fr-fic fr-dii" data-attachment="[object Object]" data-id="50013443211" style={{ maxWidth: "100%" }} />

## 수정 후 구성 변경사항

워크플로우에서 플레이스홀더(예: `R1.value`)와 함께 리더 노드를 사용하는 경우 구성을 조정해야 할 수 있습니다. 이 변경으로 인해 리더 노드는 서로 다른 고유한 값을 생성하며, 후속 노드에서 사용되는 플레이스홀더는 이제 이 동작을 반영합니다.

## 수행해야 할 작업

### 1. 워크플로우 검토
CO 2에서 데이터를 가져오기 위해 리더 노드를 사용하는 설정이 있는 경우, 수정 후 워크플로우가 예상대로 작동하는지 확인하기 위해 워크플로우를 검토하세요.

### 2. 플레이스홀더 업데이트
후속 노드에서 `R1.value`와 같은 플레이스홀더를 사용하고 있다면, 이들이 새로운 고유한 값을 반영하도록 하세요.

### 3. 워크플로우 테스트
이 업데이트 후 워크플로우가 올바른 결과를 생성하는지 확인하기 위해 몇 가지 테스트를 실행하는 것이 좋습니다.

이 변경사항으로 사용자 정의 객체를 활용하는 워크플로우의 정확성과 신뢰성이 향상됩니다.