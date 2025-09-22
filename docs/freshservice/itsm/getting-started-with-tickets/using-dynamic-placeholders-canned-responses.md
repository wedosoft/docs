---
sidebar_position: 2
---

# 준비된 응답에서 동적 플레이스홀더 사용하기

Freshservice의 플레이스홀더는 동적 콘텐츠를 추가하고 자동화된 이메일을 개인화하는 훌륭한 방법입니다. 고객을 이름으로 지칭하고, 상태 변경에 대해 업데이트하며, 해당 티켓에 대한 링크를 추가하는 이메일은 대화의 맥락을 유지하는 뛰어난 방법입니다. [여기를 클릭](https://support.freshservice.com/en/support/solutions/articles/157147-creating-common-reply-templates-with-canned-responses)하여 준비된 응답을 구성하는 방법을 알아보세요. 이들은 워크스페이스 수준에서만 구성할 수 있습니다. 에이전트가 액세스할 수 있는 모든 워크스페이스의 모든 준비된 응답이 준비된 응답 설정 내에 채워집니다.

예를 들어, 다음에 여러 사람에게 보낼 이메일(이메일 알림이나 준비된 응답 등)을 작성할 때 `{{ticket.requester.firstname}}`을 사용하여 이름으로 사람들을 부르거나 `{{ticket.id}}`로 티켓 ID를 템플릿에 자동으로 삽입할 수 있습니다.

이 기능을 사용하려면 텍스트 상자 위의 **플레이스홀더 삽입** 버튼을 클릭하세요. 플레이스홀더는 활성화될 때 고객에게 자동으로 전송되는 이메일 알림, 티켓 답변에 수동으로 삽입되는 준비된 응답, 그리고 자동화의 미리 서식화된 답변 템플릿과 함께 사용할 수 있습니다.

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/38426113/original/tLbzh-PIgQaJMK6Bn50aauB8uEpYSGj_Ew.png?1524816236"  />

다음은 Freshservice에서 사용할 수 있는 플레이스홀더의 전체 목록입니다.

**참고:** 특정 플레이스홀더(`{{ticket.billable_hours}}`, `{{ticket.total_time_spent}}` 등)는 플랜/기능에 따라 달라집니다.

## 사용 가능한 플레이스홀더

| 플레이스홀더 텍스트 | 설명 |
|---|---|
| `{{ticket.id}}` | 각 티켓에 대해 생성되는 고유 티켓 ID |
| `{{ticket.subject}}` | 티켓의 제목 |
| `{{ticket.description}}` | 티켓의 설명 내용 |
| `{{ticket.description_text}}` | 텍스트 형태의 티켓 설명 (Slack과 같은 외부 통합용) |
| `{{ticket.description_html}}` | HTML 형태의 티켓 설명 (Slack과 같은 외부 통합용) |
| `{{ticket.url}}` | 로그인한 사용자를 위한 티켓 URL |
| `{{ticket.public_url}}` | 로그인 없이 티켓을 볼 수 있는 공개 URL |
| `{{ticket.portal_url}}` | 포털별 URL |
| `{{ticket.from_email}}` | 티켓의 이메일 발신자 주소 |
| `{{ticket.requester.email}}` | 요청자의 기본 이메일 주소 (여러 이메일 주소가 있는 경우) |
| `{{ticket.status}}` | 서비스 데스크에서 티켓의 현재 상태 (숫자 값) |
| `{{ticket.requester_status_name}}` | 고객 포털에 표시되는 티켓 상태 |
| `{{ticket.status_changed_on}}` | 티켓 상태가 최근에 변경된 타임스탬프 |
| `{{ticket.priority}}` | 티켓의 현재 우선순위 |
| `{{ticket.source}}` | 티켓의 소스를 나타내는 숫자 값 (1 - 이메일, 2 - 포털 등) |
| `{{ticket.source_name}}` | 티켓 소스의 이름 (이메일, 트위터, 페이스북, 전화 등) |
| `{{ticket.ticket_type}}` | 티켓의 유형 |
| `{{ticket.tags}}` | 티켓에 추가된 태그 |
| `{{ticket.created_on}}` | 티켓 생성 시간 |
| `{{ticket.due_by_time}}` | 해결이 필요한 날짜 및 시간 (SLA 규칙에 의해 설정) |
| `{{ticket.due_by_hrs}}` | 해결이 필요한 시간 |
| `{{ticket.sla_policy_name}}` | 티켓에 적용되는 SLA 정책 |
| `{{ticket.attachments}}` | 티켓에 있는 첨부 파일 |
| `{{ticket.total_time_spent}}` | 티켓에서 추적된 총 시간 |
| `{{ticket.billable_hours}}` | 티켓에서 추적된 청구 가능 시간 |
| `{{ticket.requester.name}}` | 요청자의 전체 이름 |
| `{{ticket.requester.firstname}}` | 요청자의 이름 |
| `{{ticket.requester.lastname}}` | 요청자의 성 |
| `{{ticket.requester.phone}}` | 요청자의 직장 전화번호 |
| `{{ticket.requester.mobile}}` | 요청자의 휴대폰 번호 |
| `{{ticket.requester.address}}` | 요청자의 주소 |
| `{{ticket.requester.job_title}}` | 요청자의 직책 |
| `{{helpdesk_name}}` | 헬프데스크 아래에 지정된 지원 포털 이름 |

이들은 Freshservice에서 기본적으로 사용할 수 있는 플레이스홀더입니다. `{{comment.body}}`와 `{{comment.commenter.name}}`과 같은 자주 사용하는 것들이 여기에 없는 이유가 궁금하다면 [여기](https://support.freshdesk.com/support/solutions/articles/87018)에서 확인할 수 있습니다.