---
sidebar_position: 5
---

# Freddy 리포트 지원 속성

Freshservice는 간단히 질문을 던지는 것만으로 즉석 리포트를 생성할 수 있는 Ask Freddy 기능을 제공합니다. 현재 이 기능은 다음 모듈을 쿼리하는 데 사용할 수 있습니다: **Tickets, Problems, Changes, Release, Tasks**.

:::info 주요 정보
- 이 기능을 사용하기 전에 필요한 권한과 설정을 확인하세요
- 단계별 접근을 통해 안정적으로 구현하는 것을 권장합니다
:::


다음은 Freddy가 Ticket, Problem, Change, Release 모듈을 쿼리하기 위해 지원하는 속성들입니다.

## 주요 모듈별 지원 속성

### Tickets (티켓)

<table border="1" style={{borderCollapse: 'collapse', width: '100%'}}>
<thead>
<tr style={{backgroundColor: '#08c7fb', fontWeight: 'bold', color: '#000', textAlign: 'center'}}>
<td rowSpan="13" style={{border: '3px solid #08c7fb', padding: '4px'}}>Tickets</td>
<td style={{border: '3px solid #08c7fb', padding: '4px'}}>Property Type</td>
<td colSpan="4" style={{border: '3px solid #08c7fb', padding: '4px'}}>Properties</td>
</tr>
</thead>
<tbody>
<tr>
<td rowSpan="2" style={{border: '2px solid #08c7fb', padding: '4px', fontWeight: 'bold', textAlign: 'center'}}>General</td>
<td style={{border: '1px solid #08c7fb', padding: '4px', textAlign: 'center'}}>ID</td>
<td style={{border: '1px solid #08c7fb', padding: '4px', textAlign: 'center'}}>Priority</td>
<td style={{border: '1px solid #08c7fb', padding: '4px', textAlign: 'center'}}>Impact</td>
<td style={{border: '1px solid #08c7fb', padding: '4px', textAlign: 'center'}}>Urgency</td>
</tr>
<tr>
<td style={{border: '1px solid #08c7fb', padding: '4px', textAlign: 'center'}}>Source</td>
<td style={{border: '1px solid #08c7fb', padding: '4px', textAlign: 'center'}}>Subject</td>
<td style={{border: '1px solid #08c7fb', padding: '4px', textAlign: 'center'}}>Status</td>
<td style={{border: '1px solid #08c7fb', padding: '4px', textAlign: 'center'}}>Type</td>
</tr>
<tr>
<td style={{border: '2px solid #08c7fb', padding: '4px', fontWeight: 'bold', textAlign: 'center'}}>Category</td>
<td style={{border: '1px solid #08c7fb', padding: '4px', textAlign: 'center'}}>Category</td>
<td style={{border: '1px solid #08c7fb', padding: '4px', textAlign: 'center'}}>Sub Category</td>
<td style={{border: '1px solid #08c7fb', padding: '4px', textAlign: 'center'}}>Item Category</td>
<td style={{border: '1px solid #08c7fb', padding: '4px'}}></td>
</tr>
<tr>
<td style={{border: '2px solid #08c7fb', padding: '4px', fontWeight: 'bold', textAlign: 'center'}}>Service Request Properties</td>
<td style={{border: '1px solid #08c7fb', padding: '4px', textAlign: 'center'}}>Service Category</td>
<td style={{border: '1px solid #08c7fb', padding: '4px', textAlign: 'center'}}>Service Item</td>
<td style={{border: '1px solid #08c7fb', padding: '4px'}}></td>
<td style={{border: '1px solid #08c7fb', padding: '4px'}}></td>
</tr>
<tr>
<td style={{border: '2px solid #08c7fb', padding: '4px', fontWeight: 'bold', textAlign: 'center'}}>Status</td>
<td style={{border: '1px solid #08c7fb', padding: '4px', textAlign: 'center'}}>Approval status</td>
<td style={{border: '1px solid #08c7fb', padding: '4px', textAlign: 'center'}}>Resolution Status</td>
<td style={{border: '1px solid #08c7fb', padding: '4px', textAlign: 'center'}}>First Response Status</td>
<td style={{border: '1px solid #08c7fb', padding: '4px'}}></td>
</tr>
<tr>
<td rowSpan="2" style={{border: '2px solid #08c7fb', padding: '4px', fontWeight: 'bold', textAlign: 'center'}}>Time</td>
<td style={{border: '1px solid #08c7fb', padding: '4px', textAlign: 'center'}}>First Response time in Bhrs</td>
<td style={{border: '1px solid #08c7fb', padding: '4px', textAlign: 'center'}}>First Response Time in Chrs</td>
<td style={{border: '1px solid #08c7fb', padding: '4px', textAlign: 'center'}}>Avg Response Time in Bhrs</td>
<td style={{border: '1px solid #08c7fb', padding: '4px', textAlign: 'center'}}>Avg Response Time in Chrs</td>
</tr>
<tr>
<td style={{border: '1px solid #08c7fb', padding: '4px', textAlign: 'center'}}>First Response Due In</td>
<td style={{border: '1px solid #08c7fb', padding: '4px', textAlign: 'center'}}>Resolution Time in Bhrs</td>
<td style={{border: '1px solid #08c7fb', padding: '4px'}}></td>
<td style={{border: '1px solid #08c7fb', padding: '4px'}}></td>
</tr>
<tr>
<td rowSpan="2" style={{border: '2px solid #08c7fb', padding: '4px', fontWeight: 'bold', textAlign: 'center'}}>Date</td>
<td style={{border: '1px solid #08c7fb', padding: '4px', textAlign: 'center'}}>Created Date</td>
<td style={{border: '1px solid #08c7fb', padding: '4px', textAlign: 'center'}}>Assigned Date</td>
<td style={{border: '1px solid #08c7fb', padding: '4px', textAlign: 'center'}}>Resolved Date</td>
<td style={{border: '1px solid #08c7fb', padding: '4px', textAlign: 'center'}}>Closed Date</td>
</tr>
<tr>
<td style={{border: '1px solid #08c7fb', padding: '4px', textAlign: 'center'}}>First Response Date</td>
<td style={{border: '1px solid #08c7fb', padding: '4px', textAlign: 'center'}}>Due By</td>
<td style={{border: '1px solid #08c7fb', padding: '4px'}}></td>
<td style={{border: '1px solid #08c7fb', padding: '4px'}}></td>
</tr>
<tr>
<td rowSpan="3" style={{border: '2px solid #08c7fb', padding: '4px', fontWeight: 'bold', textAlign: 'center'}}>Count</td>
<td style={{border: '1px solid #08c7fb', padding: '4px', textAlign: 'center'}}>Agent Reassign Count</td>
<td style={{border: '1px solid #08c7fb', padding: '4px', textAlign: 'center'}}>Group Reassign Count</td>
<td style={{border: '1px solid #08c7fb', padding: '4px', textAlign: 'center'}}>Agent Reply Count</td>
<td style={{border: '1px solid #08c7fb', padding: '4px', textAlign: 'center'}}>Customer Reply Count</td>
</tr>
<tr>
<td style={{border: '1px solid #08c7fb', padding: '4px', textAlign: 'center'}}>Associated Assets Count</td>
<td style={{border: '1px solid #08c7fb', padding: '4px', textAlign: 'center'}}>Child Tickets Count</td>
<td style={{border: '1px solid #08c7fb', padding: '4px', textAlign: 'center'}}>Private Notes Count</td>
<td style={{border: '1px solid #08c7fb', padding: '4px', textAlign: 'center'}}>Public Notes Count</td>
</tr>
<tr>
<td style={{border: '1px solid #08c7fb', padding: '4px', textAlign: 'center'}}>Task Count</td>
<td style={{border: '1px solid #08c7fb', padding: '4px', textAlign: 'center'}}>Reopen Count</td>
<td style={{border: '1px solid #08c7fb', padding: '4px'}}></td>
<td style={{border: '1px solid #08c7fb', padding: '4px'}}></td>
</tr>
<tr>
<td style={{border: '2px solid #08c7fb', padding: '4px', fontWeight: 'bold', textAlign: 'center'}}>Total</td>
<td style={{border: '1px solid #08c7fb', padding: '4px', textAlign: 'center'}}>Total Cost</td>
<td style={{border: '1px solid #08c7fb', padding: '4px', textAlign: 'center'}}>Total Quantity</td>
<td style={{border: '1px solid #08c7fb', padding: '4px'}}></td>
<td style={{border: '1px solid #08c7fb', padding: '4px'}}></td>
</tr>
</tbody>
</table>

### Changes (변경)

<table border="1" style={{borderCollapse: 'collapse', width: '100%', marginTop: '20px'}}>
<thead>
<tr style={{backgroundColor: '#08c7fb', fontWeight: 'bold', color: '#000', textAlign: 'center'}}>
<td rowSpan="9" style={{border: '3px solid #08c7fb', padding: '4px'}}>Changes</td>
<td style={{border: '3px solid #08c7fb', padding: '4px'}}>Property Type</td>
<td colSpan="4" style={{border: '3px solid #08c7fb', padding: '4px'}}>Properties</td>
</tr>
</thead>
<tbody>
<tr>
<td rowSpan="2" style={{border: '2px solid #08c7fb', padding: '4px', fontWeight: 'bold', textAlign: 'center'}}>General</td>
<td style={{border: '1px solid #08c7fb', padding: '4px', textAlign: 'center'}}>ID</td>
<td style={{border: '1px solid #08c7fb', padding: '4px', textAlign: 'center'}}>Priority</td>
<td style={{border: '1px solid #08c7fb', padding: '4px', textAlign: 'center'}}>Impact</td>
<td style={{border: '1px solid #08c7fb', padding: '4px', textAlign: 'center'}}>Risk</td>
</tr>
<tr>
<td style={{border: '1px solid #08c7fb', padding: '4px', textAlign: 'center'}}>Status</td>
<td style={{border: '1px solid #08c7fb', padding: '4px', textAlign: 'center'}}>Subject</td>
<td style={{border: '1px solid #08c7fb', padding: '4px', textAlign: 'center'}}>Type</td>
<td style={{border: '1px solid #08c7fb', padding: '4px'}}></td>
</tr>
<tr>
<td style={{border: '2px solid #08c7fb', padding: '4px', fontWeight: 'bold', textAlign: 'center'}}>Category</td>
<td style={{border: '1px solid #08c7fb', padding: '4px', textAlign: 'center'}}>Category</td>
<td style={{border: '1px solid #08c7fb', padding: '4px', textAlign: 'center'}}>Sub Category</td>
<td style={{border: '1px solid #08c7fb', padding: '4px', textAlign: 'center'}}>Item Category</td>
<td style={{border: '1px solid #08c7fb', padding: '4px'}}></td>
</tr>
<tr>
<td style={{border: '2px solid #08c7fb', padding: '4px', fontWeight: 'bold', textAlign: 'center'}}>Status</td>
<td style={{border: '1px solid #08c7fb', padding: '4px', textAlign: 'center'}}>Approval Status</td>
<td style={{border: '1px solid #08c7fb', padding: '4px'}}></td>
<td style={{border: '1px solid #08c7fb', padding: '4px'}}></td>
<td style={{border: '1px solid #08c7fb', padding: '4px'}}></td>
</tr>
<tr>
<td style={{border: '2px solid #08c7fb', padding: '4px', fontWeight: 'bold', textAlign: 'center'}}>Time</td>
<td style={{border: '1px solid #08c7fb', padding: '4px', textAlign: 'center'}}>Resolution Time in Bhrs</td>
<td style={{border: '1px solid #08c7fb', padding: '4px'}}></td>
<td style={{border: '1px solid #08c7fb', padding: '4px'}}></td>
<td style={{border: '1px solid #08c7fb', padding: '4px'}}></td>
</tr>
<tr>
<td rowSpan="2" style={{border: '2px solid #08c7fb', padding: '4px', fontWeight: 'bold', textAlign: 'center'}}>Date</td>
<td style={{border: '1px solid #08c7fb', padding: '4px', textAlign: 'center'}}>Created Date</td>
<td style={{border: '1px solid #08c7fb', padding: '4px', textAlign: 'center'}}>Assigned Date</td>
<td style={{border: '1px solid #08c7fb', padding: '4px', textAlign: 'center'}}>Planned Start Date</td>
<td style={{border: '1px solid #08c7fb', padding: '4px', textAlign: 'center'}}>Planned End Date</td>
</tr>
<tr>
<td style={{border: '1px solid #08c7fb', padding: '4px', textAlign: 'center'}}>Approved Date</td>
<td style={{border: '1px solid #08c7fb', padding: '4px', textAlign: 'center'}}>Closed Date</td>
<td style={{border: '1px solid #08c7fb', padding: '4px'}}></td>
<td style={{border: '1px solid #08c7fb', padding: '4px'}}></td>
</tr>
<tr>
<td style={{border: '2px solid #08c7fb', padding: '4px', fontWeight: 'bold', textAlign: 'center'}}>Status Since</td>
<td style={{border: '1px solid #08c7fb', padding: '4px', textAlign: 'center'}}>In Planning since</td>
<td style={{border: '1px solid #08c7fb', padding: '4px', textAlign: 'center'}}>Pending Release Since</td>
<td style={{border: '1px solid #08c7fb', padding: '4px', textAlign: 'center'}}>Pending Review Since</td>
<td style={{border: '1px solid #08c7fb', padding: '4px'}}></td>
</tr>
<tr>
<td style={{border: '2px solid #08c7fb', padding: '4px', fontWeight: 'bold', textAlign: 'center'}}>Count</td>
<td style={{border: '1px solid #08c7fb', padding: '4px', textAlign: 'center'}}>Incidents Initiated Count</td>
<td style={{border: '1px solid #08c7fb', padding: '4px', textAlign: 'center'}}>Incidents Caused Count</td>
<td style={{border: '1px solid #08c7fb', padding: '4px', textAlign: 'center'}}>Associated Problem Count</td>
<td style={{border: '1px solid #08c7fb', padding: '4px', textAlign: 'center'}}>Associated Asset Count</td>
</tr>
</tbody>
</table>

### Problems (문제)

<table border="1" style={{borderCollapse: 'collapse', width: '100%', marginTop: '20px'}}>
<thead>
<tr style={{backgroundColor: '#08c7fb', fontWeight: 'bold', color: '#000', textAlign: 'center'}}>
<td rowSpan="5" style={{border: '3px solid #08c7fb', padding: '4px'}}>Problems</td>
<td style={{border: '3px solid #08c7fb', padding: '4px'}}>Property Type</td>
<td colSpan="4" style={{border: '3px solid #08c7fb', padding: '4px'}}>Properties</td>
</tr>
</thead>
<tbody>
<tr>
<td rowSpan="2" style={{border: '2px solid #08c7fb', padding: '4px', fontWeight: 'bold', textAlign: 'center'}}>General</td>
<td style={{border: '1px solid #08c7fb', padding: '4px', textAlign: 'center'}}>ID</td>
<td style={{border: '1px solid #08c7fb', padding: '4px', textAlign: 'center'}}>Priority</td>
<td style={{border: '1px solid #08c7fb', padding: '4px', textAlign: 'center'}}>Impact</td>
<td style={{border: '1px solid #08c7fb', padding: '4px', textAlign: 'center'}}>Status</td>
</tr>
<tr>
<td style={{border: '1px solid #08c7fb', padding: '4px', textAlign: 'center'}}>Subject</td>
<td style={{border: '1px solid #08c7fb', padding: '4px'}}></td>
<td style={{border: '1px solid #08c7fb', padding: '4px'}}></td>
<td style={{border: '1px solid #08c7fb', padding: '4px'}}></td>
</tr>
<tr>
<td style={{border: '2px solid #08c7fb', padding: '4px', fontWeight: 'bold', textAlign: 'center'}}>Category</td>
<td style={{border: '1px solid #08c7fb', padding: '4px', textAlign: 'center'}}>Category</td>
<td style={{border: '1px solid #08c7fb', padding: '4px', textAlign: 'center'}}>Sub Category</td>
<td style={{border: '1px solid #08c7fb', padding: '4px', textAlign: 'center'}}>Item Category</td>
<td style={{border: '1px solid #08c7fb', padding: '4px'}}></td>
</tr>
<tr>
<td style={{border: '2px solid #08c7fb', padding: '4px', fontWeight: 'bold', textAlign: 'center'}}>Date</td>
<td style={{border: '1px solid #08c7fb', padding: '4px', textAlign: 'center'}}>Created Date</td>
<td style={{border: '1px solid #08c7fb', padding: '4px', textAlign: 'center'}}>Assigned Date</td>
<td style={{border: '1px solid #08c7fb', padding: '4px', textAlign: 'center'}}>Closed Date</td>
<td style={{border: '1px solid #08c7fb', padding: '4px', textAlign: 'center'}}>Due By</td>
</tr>
<tr>
<td style={{border: '2px solid #08c7fb', padding: '4px', fontWeight: 'bold', textAlign: 'center'}}>Count</td>
<td style={{border: '1px solid #08c7fb', padding: '4px', textAlign: 'center'}}>Associated Assets Count</td>
<td style={{border: '1px solid #08c7fb', padding: '4px', textAlign: 'center'}}>Associated Ticket Count</td>
<td style={{border: '1px solid #08c7fb', padding: '4px'}}></td>
<td style={{border: '1px solid #08c7fb', padding: '4px'}}></td>
</tr>
</tbody>
</table>

### Release (릴리스)

<table border="1" style={{borderCollapse: 'collapse', width: '100%', marginTop: '20px'}}>
<thead>
<tr style={{backgroundColor: '#08c7fb', fontWeight: 'bold', color: '#000', textAlign: 'center'}}>
<td rowSpan="7" style={{border: '3px solid #08c7fb', padding: '4px'}}>Release</td>
<td style={{border: '3px solid #08c7fb', padding: '4px'}}>Property Type</td>
<td colSpan="4" style={{border: '3px solid #08c7fb', padding: '4px'}}>Properties</td>
</tr>
</thead>
<tbody>
<tr>
<td rowSpan="2" style={{border: '2px solid #08c7fb', padding: '4px', fontWeight: 'bold', textAlign: 'center'}}>General</td>
<td style={{border: '1px solid #08c7fb', padding: '4px', textAlign: 'center'}}>ID</td>
<td style={{border: '1px solid #08c7fb', padding: '4px', textAlign: 'center'}}>Priority</td>
<td style={{border: '1px solid #08c7fb', padding: '4px', textAlign: 'center'}}>Status</td>
<td style={{border: '1px solid #08c7fb', padding: '4px', textAlign: 'center'}}>Subject</td>
</tr>
<tr>
<td style={{border: '1px solid #08c7fb', padding: '4px', textAlign: 'center'}}>Type</td>
<td style={{border: '1px solid #08c7fb', padding: '4px'}}></td>
<td style={{border: '1px solid #08c7fb', padding: '4px'}}></td>
<td style={{border: '1px solid #08c7fb', padding: '4px'}}></td>
</tr>
<tr>
<td style={{border: '2px solid #08c7fb', padding: '4px', fontWeight: 'bold', textAlign: 'center'}}>Category</td>
<td style={{border: '1px solid #08c7fb', padding: '4px', textAlign: 'center'}}>Category</td>
<td style={{border: '1px solid #08c7fb', padding: '4px', textAlign: 'center'}}>Sub Category</td>
<td style={{border: '1px solid #08c7fb', padding: '4px', textAlign: 'center'}}>Item Category</td>
<td style={{border: '1px solid #08c7fb', padding: '4px'}}></td>
</tr>
<tr>
<td rowSpan="2" style={{border: '2px solid #08c7fb', padding: '4px', fontWeight: 'bold', textAlign: 'center'}}>Date</td>
<td style={{border: '1px solid #08c7fb', padding: '4px', textAlign: 'center'}}>Created Date</td>
<td style={{border: '1px solid #08c7fb', padding: '4px', textAlign: 'center'}}>Assigned Date</td>
<td style={{border: '1px solid #08c7fb', padding: '4px', textAlign: 'center'}}>Planned Start Date</td>
<td style={{border: '1px solid #08c7fb', padding: '4px', textAlign: 'center'}}>Planned End Date</td>
</tr>
<tr>
<td style={{border: '1px solid #08c7fb', padding: '4px', textAlign: 'center'}}>Closed Date</td>
<td style={{border: '1px solid #08c7fb', padding: '4px'}}></td>
<td style={{border: '1px solid #08c7fb', padding: '4px'}}></td>
<td style={{border: '1px solid #08c7fb', padding: '4px'}}></td>
</tr>
<tr>
<td style={{border: '2px solid #08c7fb', padding: '4px', fontWeight: 'bold', textAlign: 'center'}}>Status</td>
<td style={{border: '1px solid #08c7fb', padding: '4px', textAlign: 'center'}}>Approval Status</td>
<td style={{border: '1px solid #08c7fb', padding: '4px'}}></td>
<td style={{border: '1px solid #08c7fb', padding: '4px'}}></td>
<td style={{border: '1px solid #08c7fb', padding: '4px'}}></td>
</tr>
<tr>
<td style={{border: '2px solid #08c7fb', padding: '4px', fontWeight: 'bold', textAlign: 'center'}}>Count</td>
<td style={{border: '1px solid #08c7fb', padding: '4px', textAlign: 'center'}}>Associated Assets Count</td>
<td style={{border: '1px solid #08c7fb', padding: '4px'}}></td>
<td style={{border: '1px solid #08c7fb', padding: '4px'}}></td>
<td style={{border: '1px solid #08c7fb', padding: '4px'}}></td>
</tr>
</tbody>
</table>

## 연관 속성 (Association Properties)

위에서 언급한 속성 외에도 다음 속성들을 위의 모듈과 연관시켜 Freddy에게 질문을 던질 수 있습니다.

<table border="1" style={{borderCollapse: 'collapse', width: '100%', marginTop: '20px'}}>
<thead>
<tr style={{backgroundColor: '#08c7fb', fontWeight: 'bold', color: '#000', textAlign: 'center'}}>
<td rowSpan="6" style={{border: '3px solid #08c7fb', padding: '4px'}}>Association</td>
<td style={{border: '3px solid #08c7fb', padding: '4px'}}>Property</td>
<td colSpan="4" style={{border: '3px solid #08c7fb', padding: '4px'}}>Sub-Properties</td>
</tr>
</thead>
<tbody>
<tr>
<td style={{border: '2px solid #08c7fb', padding: '4px', fontWeight: 'bold', textAlign: 'center'}}>Agent Group</td>
<td style={{border: '1px solid #08c7fb', padding: '4px', textAlign: 'center'}}>Name</td>
<td style={{border: '1px solid #08c7fb', padding: '4px', textAlign: 'center'}}>Ticket Assignment Type</td>
<td style={{border: '1px solid #08c7fb', padding: '4px'}}></td>
<td style={{border: '1px solid #08c7fb', padding: '4px'}}></td>
</tr>
<tr>
<td rowSpan="3" style={{border: '2px solid #08c7fb', padding: '4px', fontWeight: 'bold', textAlign: 'center'}}>Agent/Requester</td>
<td style={{border: '1px solid #08c7fb', padding: '4px', textAlign: 'center'}}>Name</td>
<td style={{border: '1px solid #08c7fb', padding: '4px', textAlign: 'center'}}>Address</td>
<td style={{border: '1px solid #08c7fb', padding: '4px', textAlign: 'center'}}>Location</td>
<td style={{border: '1px solid #08c7fb', padding: '4px', textAlign: 'center'}}>Language</td>
</tr>
<tr>
<td style={{border: '1px solid #08c7fb', padding: '4px', textAlign: 'center'}}>Job Title</td>
<td style={{border: '1px solid #08c7fb', padding: '4px', textAlign: 'center'}}>Time Zone</td>
<td style={{border: '1px solid #08c7fb', padding: '4px', textAlign: 'center'}}>User Type</td>
<td style={{border: '1px solid #08c7fb', padding: '4px', textAlign: 'center'}}>User Scope</td>
</tr>
<tr>
<td style={{border: '1px solid #08c7fb', padding: '4px', textAlign: 'center'}}>Mobile</td>
<td style={{border: '1px solid #08c7fb', padding: '4px', textAlign: 'center'}}>Phone</td>
<td style={{border: '1px solid #08c7fb', padding: '4px'}}></td>
<td style={{border: '1px solid #08c7fb', padding: '4px'}}></td>
</tr>
<tr>
<td style={{border: '2px solid #08c7fb', padding: '4px', fontWeight: 'bold', textAlign: 'center'}}>Department</td>
<td style={{border: '1px solid #08c7fb', padding: '4px', textAlign: 'center'}}>Name</td>
<td style={{border: '1px solid #08c7fb', padding: '4px'}}></td>
<td style={{border: '1px solid #08c7fb', padding: '4px'}}></td>
<td style={{border: '1px solid #08c7fb', padding: '4px'}}></td>
</tr>
</tbody>
</table>

## Tasks (작업) 지원 속성

다음은 Freddy가 Tasks에 대한 질문을 처리하기 위해 지원하는 속성들입니다.

<table border="1" style={{borderCollapse: 'collapse', width: '100%', marginTop: '20px'}}>
<thead>
<tr style={{backgroundColor: '#08c7fb', fontWeight: 'bold', color: '#000', textAlign: 'center'}}>
<td rowSpan="2" style={{border: '3px solid #08c7fb', padding: '4px'}}>Task</td>
<td style={{border: '3px solid #08c7fb', padding: '4px'}}>Property Type</td>
<td colSpan="4" style={{border: '3px solid #08c7fb', padding: '4px'}}>Properties</td>
</tr>
</thead>
<tbody>
<tr>
<td style={{border: '2px solid #08c7fb', padding: '4px', fontWeight: 'bold', textAlign: 'center'}}>General</td>
<td style={{border: '1px solid #08c7fb', padding: '4px', textAlign: 'center'}}>ID</td>
<td style={{border: '1px solid #08c7fb', padding: '4px', textAlign: 'center'}}>Status</td>
<td style={{border: '1px solid #08c7fb', padding: '4px', textAlign: 'center'}}>Module</td>
<td style={{border: '1px solid #08c7fb', padding: '4px', textAlign: 'center'}}>Task Title</td>
</tr>
<tr>
<td style={{border: '2px solid #08c7fb', padding: '4px', fontWeight: 'bold', textAlign: 'center'}}>Date</td>
<td style={{border: '1px solid #08c7fb', padding: '4px', textAlign: 'center'}}>Created Date</td>
<td style={{border: '1px solid #08c7fb', padding: '4px', textAlign: 'center'}}>Closed Date</td>
<td style={{border: '1px solid #08c7fb', padding: '4px', textAlign: 'center'}}>Due By</td>
<td style={{border: '1px solid #08c7fb', padding: '4px'}}></td>
</tr>
</tbody>
</table>

### Task 연관 속성

<table border="1" style={{borderCollapse: 'collapse', width: '100%', marginTop: '10px'}}>
<thead>
<tr style={{backgroundColor: '#08c7fb', fontWeight: 'bold', color: '#000', textAlign: 'center'}}>
<td rowSpan="2" style={{border: '3px solid #08c7fb', padding: '4px'}}>Association</td>
<td style={{border: '3px solid #08c7fb', padding: '4px'}}>Property</td>
<td colSpan="4" style={{border: '3px solid #08c7fb', padding: '4px'}}>Sub-Properties</td>
</tr>
</thead>
<tbody>
<tr>
<td style={{border: '2px solid #08c7fb', padding: '4px', fontWeight: 'bold', textAlign: 'center'}}>Agent Group</td>
<td style={{border: '1px solid #08c7fb', padding: '4px', textAlign: 'center'}}>Name</td>
<td style={{border: '1px solid #08c7fb', padding: '4px', textAlign: 'center'}}>Ticket Assignment Type</td>
<td style={{border: '1px solid #08c7fb', padding: '4px'}}></td>
<td style={{border: '1px solid #08c7fb', padding: '4px'}}></td>
</tr>
</tbody>
</table>

## 활용 예시

### 질문 예시

다음과 같은 자연어 질문으로 Ask Freddy를 활용할 수 있습니다:

1. **티켓 관련**: "지난 주에 생성된 긴급 티켓은 몇 개인가요?"
2. **상담원 성과**: "각 상담원의 평균 해결 시간은 얼마인가요?"
3. **변경 관리**: "승인 대기 중인 변경 요청은 몇 개인가요?"
4. **문제 추적**: "열린 상태의 문제 중 우선순위가 높은 것은 몇 개인가요?"

### 효과적인 질문 작성 팁

:::tip 자연어 질문 작성 방법
- 명확하고 구체적인 질문 사용
- 날짜 범위나 상태 등의 필터 조건 포함
- 측정하고자 하는 메트릭을 명시
- 간단하고 직관적인 표현 사용
:::

## 제한사항

:::warning 주의사항
- 일부 사용자 정의 필드는 Ask Freddy에서 지원되지 않을 수 있습니다.
- 복잡한 조건이나 여러 모듈을 결합한 질문은 제한될 수 있습니다.
- 실시간 데이터보다는 최근 동기화된 데이터를 기반으로 응답합니다.
:::

이 속성들을 활용하여 Ask Freddy에 질문을 던지면 즉석에서 필요한 리포트와 인사이트를 얻을 수 있어 업무 효율성을 크게 향상시킬 수 있습니다.