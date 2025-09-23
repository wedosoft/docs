---
sidebar_position: 21
---

# 자산 활동 보고

자산 활동 보고는 자산에 대한 모든 변경 사항의 상세하고 지속적인 기록을 제공하여 수명주기에 대한 귀중한 통찰력을 제공합니다. 이러한 지속적인 추적은 수정 사항의 정확한 이력을 유지하는 데 도움이 되며 감사 및 규정 준수 검토 시 중요한 역할을 합니다.

## 목차

1. [자산 활동 분석 용어집](#자산-활동-분석-용어집)
2. [위치 변경 모니터링 및 추적 보고서 생성](#사용-사례-1---위치-변경-모니터링-및-추적-보고서-생성)
3. [지난 X개월 동안 배포 또는 폐기된 자산 수 추적 보고서 생성](#사용-사례-2---지난-x개월-동안-배포-또는-폐기된-자산-수-추적-보고서-생성)
4. [모든 자산에 걸쳐 지난 X개월 동안의 모든 활동 내보내기](#사용-사례-3---모든-자산에-걸쳐-지난-x개월-동안의-모든-활동-내보내기)

이 문서에서는 샘플 사용 사례를 사용하여 자산 활동 보고서를 생성하는 방법을 살펴보겠습니다.

## 자산 활동 분석 용어집

| 속성 | 설명 |
|------|------|
| **Performed at** | 활동이 수행된 시간 |
| **Performed by User Name** | 업데이트를 수행한 사용자, 워크플로우 또는 검색 소스. 예: Discovery Agent, Intune, Probe 등 |
| **Action** | 자산에 대해 수행된 특정 작업<br/>예: Asset created, Restored, tickets associated, \<Attribute\> updated |
| **Performed by User Type** | 작업을 수행한 사용자의 유형 (User, Workflow 또는 Discovery Source) |
| **From Value** | 업데이트 이전 속성의 이전 값 |
| **To Value** | 업데이트 이후 속성의 새 값 |
| **Performed by (association)** | 작업을 수행하는 사용자의 속성을 기반으로 활동을 필터링할 수 있습니다. 예: IT 부서 사용자가 수행한 활동 필터링 |

**참고:** 분석에서는 지난 12개월의 활동만 보고할 수 있으므로 이 데이터를 주기적으로 활용해야 합니다.

## 샘플 사용 사례

### 사용 사례 1 - 위치 변경 모니터링 및 추적 보고서 생성

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50012743415/original/Zu-fvk_GPk7-9ppGAVrtExcitXPEJn5-fQ.png?1723525282"  className="fr-fic fr-dii" data-attachment="[object Object]" data-id="50012743415" />

1. **Admin → Reporting → Analytics**로 이동하여 사용자 정의 보고서를 생성합니다.

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50012743424/original/GO6h5fxp-7sCGd0RhefYKdS0nF4itaYbow.png?1723525285"  className="fr-fic fr-dii" data-attachment="[object Object]" data-id="50012743424" />

2. 오른쪽 상단 모서리에서 **New Report**를 클릭합니다.

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50012743422/original/Ewoc7SFK3u7ByqaZKx4i68iuhZ2wpHIXSw.png?1723525285"  className="fr-fic fr-dii" data-attachment="[object Object]" data-id="50012743422" />

3. 위젯을 끌어다 놓아 보고서를 생성합니다.

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50012743418/original/cEhq6247YfRH4ChIYorfwM-uzDbgT3AfMA.png?1723525285"  className="fr-fic fr-dii" data-attachment="[object Object]" data-id="50012743418" />

4. 드롭다운 필드에서 자산 메트릭을 선택합니다.

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50012743417/original/r4LcwT--6DfN0-PcSxxa-QqkVtwqnf8rMg.png?1723525285"  className="fr-fic fr-dii" data-attachment="[object Object]" data-id="50012743417" />

5. **+ filter**를 클릭하고 아래 조건을 사용하여 자산의 위치 변경을 추적합니다.

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50012743419/original/LP7TbH2hyp8OxPj3Ojfk72RYj_RPti_uog.png?1723525285"  className="fr-fic fr-dii" data-attachment="[object Object]" data-id="50012743419" />

6. 마지막으로 **Asset Name**을 기준으로 자산을 그룹화하고 **Apply**를 클릭합니다.

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50012743421/original/UG74GN3Ugb2uKLYwX1gntEBHir1aYG11jA.png?1723525285"  className="fr-fic fr-dii" data-attachment="[object Object]" data-id="50012743421" />

### 사용 사례 2 - 지난 X개월 동안 배포 또는 폐기된 자산 수 추적 보고서 생성

1. **Admin → Reporting → Analytics**로 이동하여 사용자 정의 보고서를 생성합니다.

2. 위젯을 끌어다 놓아 보고서를 생성합니다.

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50012743423/original/HnwMDSohV8xMPiHGD7B3qYCSn6e7jbwpOw.png?1723525285"  className="fr-fic fr-dii" data-attachment="[object Object]" data-id="50012743423" />

3. 드롭다운 필드에서 Asset 메트릭을 선택합니다.

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50012743416/original/U0zRpFVajdow3eapUUTc4rIDWp_JwjeRFw.png?1723525285"  className="fr-fic fr-dii" data-attachment="[object Object]" data-id="50012743416" />

4. **+ filter**를 클릭하고 아래 조건을 사용하여 지난 3개월 동안 폐기된 자산 수를 추적합니다.

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50012743426/original/kZzORgYDHsVkfQ5IO87vuNBZugerpYZJ_g.png?1723525285"  className="fr-fic fr-dii" data-attachment="[object Object]" data-id="50012743426" />

5. 마지막으로 **Apply**를 클릭하여 보고서를 생성합니다.

### 사용 사례 3 - 모든 자산에 걸쳐 지난 X개월 동안의 모든 활동 내보내기

1. **Admin → Reporting → Analytics**로 이동하여 사용자 정의 보고서를 생성합니다.

2. 화면 왼쪽 하단 모서리에서 **Settings**를 클릭합니다.

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50012743425/original/44MMuS74e7xkfzwARugeuz82LgejzUeHAQ.png?1723525285"  className="fr-fic fr-dii" data-attachment="[object Object]" data-id="50012743425" />

3. **Data Export → Create Export**를 선택합니다.

4. 이름을 입력하고 보고서를 내보낼 시간을 예약합니다.

5. 필터를 적용하고 자산 필드를 선택하여 보고서에 포함될 데이터를 세분화합니다.

- CI Type is Hardware 조건은 내보내기에서 시리얼 번호와 같은 속성에 액세스할 수 있도록 보장합니다
- Asset Family 기반 조건은 Hardware, Cloud 및 Services 하위의 모든 자산을 가져옵니다

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50012743420/original/X7N6qg_j0Uj-YwU8PLaNO9XRdXFq7chx8g.png?1723525285"  className="fr-fic fr-dii" data-attachment="[object Object]" data-id="50012743420" />

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50012743414/original/pQGNoYYoqfHMvfeMOToCy4753-yqs2eD5Q.png?1723525280"  className="fr-fic fr-dii" data-attachment="[object Object]" data-id="50012743414" />

6. 마지막으로 보고서를 받을 기본 방법을 선택합니다.

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50012743413/original/AgZroOTElypi4tqmmuMrNnZx79dn9qk0og.png?1723525269"  className="fr-fic fr-dii" data-attachment="[object Object]" data-id="50012743413" />