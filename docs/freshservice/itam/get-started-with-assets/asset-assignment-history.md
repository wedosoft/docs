---
sidebar_position: 18
---

# 자산 할당 이력

## 목차

1. [자산 할당 이력 개요](#1-자산-할당-이력-개요)
2. [자산 할당 이력 이해](#2-자산-할당-이력-이해)
3. [자산 할당 이력 보기](#3-자산-할당-이력-보기)
4. [자산 할당 이력의 주요 용어](#4-자산-할당-이력의-주요-용어)

## 1. 자산 할당 이력 개요

자산 할당 이력은 자산 관리의 중요한 측면으로, 특히 감사 프로세스를 간소화하고 자산의 수명주기에 대한 통찰력을 얻고자 하는 조직에게 매우 중요합니다. 사용자는 이제 자산의 수명 동안 각 자산의 사용을 자세히 설명하는 포괄적인 자산 할당 이력 기록에 액세스할 수 있습니다.

## 2. 자산 할당 이력 이해

"Used by" 필드가 변경될 때마다 새로운 할당 이력 기록이 자동으로 생성됩니다. 이를 통해 누가 자산을 사용했는지와 자산 할당이 언제 이루어졌는지를 명확하게 이해할 수 있습니다.

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50011203572/original/lJSEc_I5dGgIjcmOBo5bhUsjzjG8ICGEcQ.png?1710253931" style={{width: '624px', height: '355px'}} className="fr-fic fr-dii" data-attachment="[object Object]" data-id="50011203572" />

예를 들어, 노트북이 David Baptiste에서 Izzy Higgins로 재할당되면 이 변경 사항을 반영하는 새로운 할당 이력 기록이 생성됩니다. 에이전트는 초기 프로비저닝부터 현재 할당까지 자산의 여정을 추적할 수 있습니다.

## 3. 자산 할당 이력 보기

1. **Admin → Assets → Inventory**로 이동하여 자산 목록 보기 페이지에서 자산을 클릭합니다.

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50011203575/original/7FLFk5sYC9zb71nMuTA_8k3pDwx3JTlOzQ.png?1710253932" style={{width: '624px', height: '335px'}} className="fr-fic fr-dii" data-attachment="[object Object]" data-id="50011203575" />

2. 자산 보기 페이지에서 **Assignment 옵션**을 선택합니다.

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50011203573/original/135WzxJZr5KuiTOeRfgx6d3CZ8WB5MRc8w.png?1710253931" style={{width: '624px', height: '336px'}} className="fr-fic fr-dii" data-attachment="[object Object]" data-id="50011203573" />

4. 특정 요청자의 자산 할당 이력을 보려면 할당 이력 페이지에서 요청자 프로필을 클릭합니다.

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50011203574/original/xbvwPC0HpnfnE2hJajMLb6abzTmO2zX6cg.png?1710253932" style={{width: '624px', height: '335px'}} className="fr-fic fr-dii" data-attachment="[object Object]" data-id="50011203574" />

**참고:** 사용자는 **Admin → Requesters → Requester profile**로 이동하여 특정 사용자의 자산 할당 이력을 확인할 수도 있습니다.

## 4. 자산 할당 이력의 주요 용어

자산 할당 이력 기능은 자산이 팀에 의해 어떻게 할당되고 할당 해제되는지를 자세히 설명하여 자산 사용에 대한 포괄적인 통찰력을 제공합니다. Freshservice에서 자산 할당 이력을 조회할 때 사용되는 표준 용어는 다음과 같습니다.

| 자산 속성 | 설명 |
|-----------|------|
| **Assigned By** | "Used By" 속성을 설정하여 할당을 시작한 개인 |
| **Unassigned By** | "Used By" 속성을 수정하거나 지워서 할당 해제를 시작한 사람 |
| **Used by set on** | 할당 작업이 실행된 타임스탬프 |
| **Assigned on** | 해당 사용자에 대한 할당 날짜를 나타내는 자산 기록에 기록된 타임스탬프 |
| **Unassigned on** | 할당 해제 작업에 해당하는 타임스탬프 |
| **Assigned To** | 자산에 할당되거나 할당 해제된 사용자를 지정 |