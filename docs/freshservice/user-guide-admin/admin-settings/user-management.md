---
title: 사용자 관리
description: Freshservice 에이전트, 요청자, 그룹, 역할 관리 완벽 가이드
sidebar_position: 5
---

# 사용자 관리

## 📋 개요

사용자 관리는 Freshservice에서 에이전트와 요청자를 효과적으로 관리하는 핵심 기능입니다. 사용자 권한, 그룹 구성, 역할 설정 등을 통해 체계적인 서비스 데스크 운영이 가능합니다.

## Requesters

This page lets you handpick a set of requesters and add them to your help desk. These requesters will have selective privileges to submit requests to your helpdesk. You can restrict access such that only people who have been added here are allowed to log in to your self-service portal and access your knowledge base.

You can fill in the details of each of your new requesters manually or import a list of users from a CSV file. Once you have populated your list, your agents can open up each of your requesters and view their ticket history and contact information.

**Note:** 

## User Fields

The agent and requester forms in Freshservice let you capture important data about your agents and requesters, and thereby help you provide a better support experience. You can help your team get additional context about users quickly by including custom fields based on your type of business.

Just like your ticket fields, you can add new fields to the user sign up form and make them mandatory. You can also have private fields that are visible just to your agents.

### Agent Fields

Custom fields can be created to store information related to agents. Examples include:

- Technical skills
- Shift and availability of information

## Agents

The list shows all Agents added in your service desk. You can edit an existing agent's permissions and access rights by hovering over the agent and clicking on "**Edit**". You can add new agents by clicking on the "**New Agent**" button.

## Groups

You can organize your agents into specific Groups like "**Sales**" and "**Product Management**". Segmenting them into divisions lets you easily assign tickets, create specific canned responses, manage workflows and generate group-level reports. Note that the same agent can be a member of multiple groups as well.

### Auto-ticket assignment

Once you create homogeneous agent groups, you can choose to automatically assign new tickets in this group to the next agent in Round Robin.

To know more about the auto-ticket assignment, kindly refer our [solution article](https://support.freshservice.com/support/solutions/articles/157134).

## Working Hours

You can assign a different set of business hours and holidays to each Group. For example, you can separate agents by shifts and assign them different business hours, or create separate groups for each time zone.

## CAB (Change Advisory Board)

A Change Advisory Board or a CAB consists of a set of agents who have been nominated to verify new changes in the help desk. They help managers to assess changes and finalize them before implementation. The members of each CAB include experts in a particular area, who go through every change before they approve or reject it.

Freshservice lets you create custom CABs and fill them up with specific experts from your team. Whenever a change needs approval, the Change Manager can select any of the available CABs and also pick out individual members of the CAB who will get to review it.

## Roles

Roles allow you to create and edit access permissions for agents. You can create new roles, specify what actions agents with these roles can perform within your help desk, and assign the role to agents.

For example, you can create a role for your Support Co-ordinators, allowing them to update fields and assign tickets, and even add notes internally, but not reply to customers.

Once you create and save a new Role you will be able to assign it to agents when you create or edit their profile by clicking on the Agents icon under the admin tab.

To know more about how to create a role, kindly refer to the [solution article](https://support.freshservice.com/support/solutions/articles/156465).

## Departments

You can configure departments inside Freshservice and group your requesters based on the nature of their job or position in the company. Departments can also help you classify tickets, problems, changes, and releases from different types of employees differently, and define different workflows based on the impact and the urgency of requests.

Every department in Freshservice has a nominated head employee, who will take care of approving service requests from members of his team. In addition, you can also create a separate knowledge base and forum categories for each of your departments that can be accessed only by the members of that team.

## Department Fields

The department form in Freshservice lets you capture important data about the departments you support. You can help your team get additional context about the departments quickly by adding custom fields. For example, you can add a custom field to specify the physical location of departments to help agents provide better support.

Just like requester fields, you can add new fields to the department form and choose to make them mandatory.

## 💡 실무 활용 팁

### 요청자 관리 모범사례
```markdown
✅ 권장사항:
- CSV 대량 업로드로 신입사원 일괄 등록
- 부서별 custom field로 조직도 반영
- 퇴사자는 비활성화(삭제 금지)

❌ 주의사항:
- 개인정보는 필수 필드에만 포함
- 외부 파트너는 별도 권한 그룹으로 관리
```

### 에이전트 그룹 설계
```markdown
기술별 그룹:
- 네트워크팀: 네트워크 장애 전담
- 서버팀: 시스템 인프라 담당  
- 보안팀: 보안 사고 대응
- 헬프데스크: 일반 사용자 지원

지역별 그룹:
- 본사지원팀: 서울 본사 현장 지원
- 지사지원팀: 전국 지사 원격 지원
- 해외지원팀: 해외 법인 지원
```

## ⚠️ 보안 및 권한 관리

:::warning 중요 보안 설정
- **최소 권한 원칙**: 업무에 필요한 최소한의 권한만 부여
- **정기 권한 검토**: 분기별 사용자 권한 재검토 필수
- **임시 권한**: 프로젝트성 권한은 종료일 설정
:::

## 📊 효과 측정 지표

| 구분 | 측정 항목 | 목표 수치 |
|------|-----------|-----------|
| **응답성** | 첫 응답 시간 | < 1시간 |
| **효율성** | 해결율 | > 85% |
| **만족도** | 고객 만족도 | > 4.5/5.0 |
| **생산성** | 에이전트당 처리건수 | > 50건/월 |

## 🔗 관련 문서