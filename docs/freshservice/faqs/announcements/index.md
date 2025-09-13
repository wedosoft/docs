---
sidebar_position: 1
---

# 공지사항 관리

조직 내 중요한 정보를 에이전트와 최종 사용자에게 효과적으로 전달할 수 있는 공지사항 기능입니다.

:::info 공지사항 기능 개요
공지사항을 통해 시스템 점검, 정책 변경, 중요 업데이트 등을 조직 구성원들에게 신속하고 일관되게 전달할 수 있습니다.
포털 게시와 이메일 발송을 동시에 지원하여 최대한의 가시성을 확보할 수 있습니다.
:::

## 이메일 공지사항 설정 방법

### 이메일로 공지사항 발송

### 이메일로 공지사항 발송

공지사항을 이메일로 발송하려면 공지사항 생성 시 이메일 옵션에 이메일 주소를 입력하면 됩니다.

![이메일 공지사항 설정](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50009288974/original/ZOljlDkHy4H9g5ojqZyNnPg6MB589OejFg.png?1693153686)

**1단계: 공지사항 생성**
1. Freshservice 계정의 **대시보드**로 이동
2. **공지사항** 버튼 클릭 (일반적으로 우측 상단에 위치)
3. **새 공지사항 생성** 선택

**2단계: 이메일 설정 구성**
- **제목**: 명확하고 설명적인 제목 입력
- **내용**: 적절한 형식으로 공지사항 메시지 작성
- **이메일 수신자**: 이메일 옵션 필드에 이메일 주소 입력
- **표시 대상**: 공지사항을 볼 수 있는 사람 선택 (에이전트, 요청자, 또는 모두)

**3단계: 이메일 옵션**
- **개별 이메일**: 쉼표로 구분하여 특정 이메일 주소 입력
- **그룹 이메일**: 부서 또는 그룹 이메일 목록 사용
- **외부 이메일**: 조직 외부 이해관계자 포함

### 이메일 발송 기능

- **즉시 발송**: 공지사항 생성 즉시 이메일 발송
- **예약 발송**: 특정 날짜와 시간에 이메일 발송 설정
- **HTML 형식**: 이메일에서 리치 텍스트 형식 유지
- **첨부 파일**: 관련 파일이나 문서 포함

:::tip 이메일 공지사항 모범 사례
- 명확하고 실행 지향적인 제목 사용
- 내용을 간결하고 스캔하기 쉽게 작성
- 후속 질문을 위한 연락처 정보 포함
- 소규모 그룹으로 먼저 이메일 발송 테스트
- 글로벌 조직의 경우 시간대 고려
:::

### 이메일 vs. 포털 공지사항

| 방식 | 장점 | 활용 상황 |
|------|------|-----------|
| **이메일** | 즉시 알림, 포털 외부 사용자 도달 | 긴급 공지, 외부 이해관계자 포함 |
| **포털** | 지속적 가시성, 서비스 데스크 워크플로 통합 | 정책 안내, 지속적 참조 필요 정보 |
| **결합** | 최대 도달률과 가시성 | 중요한 공지사항의 경우 |

## 조직 전체 공지사항 관리

### 전사적 공지사항 배포 전략

조직 내에서 중요한 변화나 업데이트가 있을 때 모든 구성원에게 효과적으로 정보를 전달하는 방법입니다.

**1단계: 공지사항 계획 수립**
1. **대상 분석**: 에이전트, 최종 사용자, 외부 이해관계자 구분
2. **우선순위 설정**: 공지사항의 중요도와 긴급성 평가
3. **배포 채널 결정**: 이메일, 포털, SMS 등 적절한 채널 선택
4. **타이밍 계획**: 최적의 발송 시간대 및 일정 수립

**2단계: 공지사항 작성**
1. **명확한 제목**: 핵심 내용을 한눈에 파악할 수 있는 제목
2. **구조화된 내용**: 
   - 변경사항 요약
   - 영향받는 시스템/프로세스
   - 예상 일정
   - 필요한 조치사항
   - 문의처 정보

**3단계: 다채널 배포**

:::warning 중요 공지사항 배포 시 주의사항
- 모든 채널에서 일관된 메시지 유지
- 시간대별 순차 발송으로 시스템 부하 방지
- 긴급 공지의 경우 에스컬레이션 프로세스 준비
:::

### 공지사항 템플릿

**시스템 점검 공지**
```
제목: [예정] 시스템 점검 안내 - [날짜] [시간]

안녕하세요,

[시스템명] 시스템 점검이 다음과 같이 예정되어 있습니다.

• 점검 일시: [구체적 날짜 및 시간]
• 예상 소요시간: [시간]
• 영향범위: [구체적 시스템/기능]
• 대체 방안: [임시 해결책]

문의사항: [담당자 연락처]
```

**정책 변경 공지**
```
제목: [중요] [정책명] 정책 변경 안내

안녕하세요,

[날짜]부터 [정책명] 정책이 다음과 같이 변경됩니다.

• 변경내용: [핵심 변경사항]
• 적용일자: [구체적 날짜]
• 필요조치: [사용자가 해야 할 일]
• 교육일정: [관련 교육 정보]

상세내용: [링크 또는 첨부문서]
```

## 실무 활용 예시

### 상황 1: 긴급 시스템 장애 공지
**목표**: 시스템 장애 상황을 신속하게 전파하고 대응 방안 안내
**방법**:
1. 즉시 이메일 + 포털 동시 공지
2. 진행 상황별 업데이트 공지 추가 발송
3. 복구 완료 시 최종 공지

**결과**: 혼란 최소화 및 체계적인 장애 대응

### 상황 2: 신규 시스템 도입 안내
**목표**: 새로운 시스템 도입에 대한 단계적 안내
**방법**:
1. 사전 예고 공지 (2주 전)
2. 교육 일정 공지 (1주 전)
3. 오픈 당일 공지
4. 1주 후 피드백 요청 공지

**결과**: 원활한 시스템 전환 및 사용자 적응

## 문제 해결

### 자주 발생하는 문제

#### 문제: 이메일이 발송되지 않음
**원인**: 이메일 설정 오류 또는 스팸 필터
**해결**:
1. 이메일 주소 형식 재확인
2. 스팸 폴더 확인 안내
3. 화이트리스트 등록 요청
4. 발송 로그 확인

:::success 해결 완료
이메일 설정 수정 후 공지사항이 정상적으로 발송됩니다.
:::

#### 문제: 공지사항이 너무 많아 사용자가 무시함
**원인**: 공지사항 피로도 발생
**해결**:
1. 중요도별 분류 시스템 도입
2. 발송 빈도 조절
3. 개인화된 공지사항 설정
4. 읽음 확인 기능 활용

<p dir="ltr"><span>Freshservice provides the option to create announcements on the portal to keep users posted on important information. Please click on the <strong>announcement button</strong> in the right end of the <strong dir="ltr">dashboard module</strong>. In the slide out panel that appears, you can create a new announcement, schedule it for a future date and specify who the announcements should be visible to.</span></p><p><br /></p><p dir="ltr"><span><span><img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50001069026/original/yDDwSEYFlLMoMVSuZz_7WWdmwZyjFrHFcQ.png?1588850365" width="624" height="47" class="fr-fic fr-dii" data-attachment="[object Object]" data-id="50001069026" /></span></span></p><p><br /></p><p><strong>Creating Effective Organization-Wide Announcements:</strong></p><p><br /></p><p><strong>Step 1: Access Announcement Module</strong></p><ul><li>Login to your Freshservice admin portal</li><li>Navigate to the <strong>Dashboard</strong></li><li>Click the <strong>Announcement button</strong> (typically in the top-right corner)</li><li>The announcement slide-out panel will appear</li></ul><p><br /></p><p><strong>Step 2: Configure Announcement Details</strong></p><ul><li><strong>Title:</strong> Create a clear, urgent title that catches attention</li><li><strong>Priority Level:</strong> Set appropriate priority (High, Medium, Low)</li><li><strong>Content:</strong> Write comprehensive but concise information</li><li><strong>Formatting:</strong> Use bullets, bold text, and clear structure</li></ul><p><br /></p><p><strong>Step 3: Set Visibility and Audience</strong></p><ul><li><strong>Agents Only:</strong> Internal operational updates</li><li><strong>Requesters Only:</strong> Customer-facing service impacts</li><li><strong>Both Agents and Requesters:</strong> Organization-wide changes</li><li><strong>Specific Groups:</strong> Department or role-specific information</li></ul><p><br /></p><p><strong>Step 4: Schedule and Timing</strong></p><ul><li><strong>Immediate Publication:</strong> For urgent, time-sensitive information</li><li><strong>Scheduled Release:</strong> Plan announcements for optimal timing</li><li><strong>Duration:</strong> Set start and end dates for temporary announcements</li><li><strong>Time Zone Consideration:</strong> Account for global team locations</li></ul><p><br /></p><p><strong>Types of Important Organizational Updates:</strong></p><ul><li><strong>System Maintenance:</strong> Planned downtime and service interruptions</li><li><strong>Policy Changes:</strong> New procedures or updated guidelines</li><li><strong>Emergency Situations:</strong> Security incidents or critical issues</li><li><strong>New Feature Rollouts:</strong> System updates and new capabilities</li><li><strong>Organizational Changes:</strong> Staff changes, department restructuring</li></ul><p><br /></p><p><strong>Communication Best Practices:</strong></p><ul><li><strong>Clear Messaging:</strong> Use simple, direct language</li><li><strong>Action Items:</strong> Specify what recipients need to do</li><li><strong>Contact Information:</strong> Provide escalation contacts</li><li><strong>Timeline:</strong> Include relevant dates and deadlines</li><li><strong>Follow-up:</strong> Plan for updates and progress communications</li></ul><p><br /></p><p><strong>Multi-Channel Communication Strategy:</strong></p><ul><li><strong>Portal Announcements:</strong> Primary method for logged-in users</li><li><strong>Email Notifications:</strong> Reach users outside the portal</li><li><strong>Mobile App Notifications:</strong> For users on mobile devices</li><li><strong>Slack/Teams Integration:</strong> Leverage existing communication tools</li></ul>

---

## 포털에 게시된 공지사항을 수정하거나 삭제하는 방법은?

<p dir="ltr"><span>You can click on the Announcements section on the dashboard and click edit next to each announcement and either choose to edit or delete the announcement from the portal.</span></p><p><br /></p><p dir="ltr"><span><span><img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50001069031/original/HBjsmEO187BSlgkOsvyVIZEqRQr7hBf3qw.png?1588850417" width="624" height="163" class="fr-fic fr-dii" data-attachment="[object Object]" data-id="50001069031" /></span></span></p><p><br /></p><p><strong>Managing Existing Announcements:</strong></p><p><br /></p><p><strong>Step 1: Access Announcements Dashboard</strong></p><ul><li>Navigate to your Freshservice admin dashboard</li><li>Click on the <strong>Announcements</strong> section</li><li>This will display all current and past announcements</li><li>Use filters to find specific announcements quickly</li></ul><p><br /></p><p><strong>Step 2: Edit Announcement Process</strong></p><ul><li>Locate the announcement you want to modify</li><li>Click the <strong>Edit</strong> button (pencil icon) next to the announcement</li><li>Make necessary changes to:
<ul><li>Title and content</li><li>Visibility settings</li><li>Schedule and duration</li><li>Priority level</li></ul></li><li>Click <strong>Save</strong> to apply changes</li></ul><p><br /></p><p><strong>Step 3: Delete Announcement Process</strong></p><ul><li>Find the announcement you want to remove</li><li>Click the <strong>Delete</strong> button (trash icon)</li><li>Confirm the deletion when prompted</li><li><strong>Note:</strong> Deleted announcements cannot be recovered</li></ul><p><br /></p><p><strong>Announcement Management Features:</strong></p><p><br /></p><p><strong>1. Bulk Operations</strong></p><ul><li>Select multiple announcements using checkboxes</li><li>Apply bulk actions (delete, change status)</li><li>Filter and sort for easier management</li></ul><p><br /></p><p><strong>2. Status Management</strong></p><ul><li><strong>Active:</strong> Currently visible to users</li><li><strong>Scheduled:</strong> Set to publish at future date</li><li><strong>Expired:</strong> Past end date, no longer visible</li><li><strong>Draft:</strong> Saved but not published</li></ul><p><br /></p><p><strong>3. Version Control</strong></p><ul><li>View edit history for announcements</li><li>Track who made changes and when</li><li>Revert to previous versions if needed</li></ul><p><br /></p><p><strong>Best Practices for Announcement Management:</strong></p><p><br /></p><p><strong>Before Editing:</strong></p><ul><li>Consider the impact on users who have already seen the announcement</li><li>Create a new announcement for significant changes rather than editing</li><li>Document reasons for changes in admin notes</li></ul><p><br /></p><p><strong>Before Deleting:</strong></p><ul><li>Export or save important announcements for records</li><li>Consider archiving instead of deleting for audit purposes</li><li>Notify stakeholders if the announcement contained critical information</li></ul><p><br /></p><p><strong>Maintenance Schedule:</strong></p><ul><li>Regular review of active announcements (weekly/monthly)</li><li>Remove outdated or expired announcements</li><li>Update recurring announcements with current information</li><li>Archive announcements for historical reference</li></ul><p><br /></p><p><strong>Permission Considerations:</strong></p><ul><li>Only authorized administrators should edit/delete announcements</li><li>Implement approval workflows for critical announcements</li><li>Maintain audit logs of all announcement changes</li><li>Set up notifications for announcement modifications</li></ul><p><br /></p><p><strong>Emergency Modifications:</strong></p><p>For urgent updates to existing announcements:</p><ul><li>Edit immediately for time-sensitive corrections</li><li>Add "Updated" timestamp to show recent changes</li><li>Send follow-up notifications if significant changes were made</li><li>Consider creating a new announcement for major updates</li></ul>

---

