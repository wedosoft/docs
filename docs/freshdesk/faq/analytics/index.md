---
sidebar_position: 1
---

# 분석 및 리포트 FAQ

분석 및 리포트에서 자주 발생하는 질문들과 해결 방법을 정리했습니다. 각 질문을 클릭하여 상세한 답변을 확인하실 수 있습니다.

:::info 안내
이 FAQ는 실제 사용자들이 자주 묻는 질문들을 바탕으로 작성되었습니다. 추가 문의사항이 있으시면 고객지원팀에 문의해 주세요.
:::

<details>
<summary><strong>I belong to Estate 요금제. But, why am I not able to create a custom report?</strong></summary>

Custom 보고서 are part of the **Estate’19 요금제**. If you belong to the Estate’17 요금제 (annual 결제), you can choose to upgrade to Estate’19 요금제 for free. If you belong to Estate’17 요금제 (monthly 결제), you can upgrade by paying an extra of **$6/agent/month** in addition to **$59/agent/month**.

</details>

<details>
<summary><strong>the difference between Curated and Custom 보고서은 무엇인가요?</strong></summary>

Curated 보고서Freshdesk's curated 보고서 provide you with a 360 view of your 지원 performance. Monitor your 팀's performance along with the metrics most relevant to you. It also provides you with the essential information to chart better 고객 experiences.Custom 보고서With multiple ways to look at 헬프데스크 reporting, Freshdesk's 분석 lets you [customize and build your 보고서](https://지원.freshdesk.com/en/지원/solutions/articles/50000001028-custom-reporting-%E2%80%93-basics) the way you want them - with minimal effort. It offers the flexibility to pick the metric(s) you wish to study, the adaptability to select the suitable filters you want to apply, and the capability to employ the perfect dimensions to analyze your data.Learn more about the [Basics of 분석](https://freshdesk.com/webinars/get-the-most-out-of-freshdesk-분석-recording) through our webinar with insights on curated 보고서, creating custom 보고서 for your 헬프데스크, learning to apply filters on 보고서, and much more.You can also refer to our [분석 guide](https://freshdesk.com/assets/resources/freshdesk/Make-informed-decisions-with-Freshdesk-분석.pdf) for various use cases to implement in your 헬프데스크.

</details>

<details>
<summary><strong>find out the raw data belonging to a particular widget하는 방법은 무엇인가요?</strong></summary>

Based on the type of widget data, Freshdesk will automatically visualize it in a relevant format. So, reading the data from the widget is a straightforward process.Click on the widget to read the data. You also have the option to customize the visualization of certain widgets the way you want. You can select any graphical representation: Bar chart, Horizontal bar chart, Donut chart, Summary table, and Tabular.If you want to take a closer look at the widget data, click Show underlying data below the widget. You can use the **Edit Column** button to add or remove the Fields present in the table. You can use the filters to drill-down further into the underlying data.![이미지](https://s3.amazonaws.com/cdn.freshdesk.com/data/헬프데스크/attachments/production/50011677426/original/TbpIAzuQFBbbYX_NQar5QNLRwbP0yZQu_g.png?1714388080)

</details>

<details>
<summary><strong>export the report data from 분석하는 방법은 무엇인가요?</strong></summary>

Inside every report, you have the Export icon below the search bar. You can click this icon to export the report as a PDF but not as a CSV. However, you will be able to export both the Graph data as well as the Tabular data (Underlying data) present in the widgets in the form of a CSV.**Underlying data: **The underlying data refers to the original, detailed information stored within the platform's database. Essentially, it serves as the raw material from which insights and 보고서 are derived. This data provides the foundation for deeper analysis and understanding of 고객 interactions and 지원 processes. It can be exported by selecting the CSV of tabular data from the widget.**Graph data: **Graph data represents the summarized and visualized insights drawn from the underlying data. This visual representation offers a distilled view of key performance indicators, making it easier for users to grasp trends and make informed decisions without delving into the detailed raw data. It can be exported by selecting the CSV of graph data.**Steps t****o export the complete report as PDF**- Go to **분석**.
- Select a report you would like to export and click on it.
- Inside the report, navigate to the export icon and select **Export report **from the dropdown.
- Here you can select the pages in the report you want to export and click **Ex****port**.![이미지](https://s3.amazonaws.com/cdn.freshdesk.com/data/헬프데스크/attachments/production/50008538563/original/Ty8VTeMNRh3lqG1Q3r2Mx-8ylzlVf9WoFA.gif?1686030405)The report will now be sent as a PDF file to your registered 이메일 address.**Steps t****o export the widget level report**- Go to 분석
- Open the report
- Expand the desired widget
- Click the options for the widget represented as three horizontal dots.
- Select **Export to 이메일/****Download > CSV/PDF of graph/tabular data** accordinglyBelow are the items you need to consider when exporting 보고서.- Make sure the date range of the export is correct and valid across Widget level/Page level/Report level filters. If the date filter is set different in the Page level/Report level filters, than the one in Widget level, the exported data may not have the expected results.
- Make sure you are selecting Graph data for the trend numbers you see in a widget and the Underlying data for the complete data set of the widget. You can select up to 20 fields as columns for the export from the underlying data by editing the report, and adding fields using the 'Gear' icon as shown below.Based on the volume of data, it may take several minutes to export and send the data to your mailbox.![이미지](https://s3.amazonaws.com/cdn.freshdesk.com/data/헬프데스크/attachments/production/50011764334/original/bpdGfr616jWZxG5Op9aMFOYDTmTjOe7WSQ.jpeg?1715147318)참고: If the date range is correctly set and you still do not receive the export for the specified date range, try this troubleshooting step: edit the report, remove the date range filter, save the report, then edit it again and reapply the desired date range. Finally, save the report and proceed with the export. If you still face issues, reach out to our 지원.
---
**To schedule a data export:**
-
로그인 to your 지원 포털 as an **관리자/Supervisor.**-
Go to **분석 > **click the** gear icon(****설정) **on the top right corner **>** choose** Data**** Exports.**-
Click on **Create Export.**- Give it a **Name**, **Description** and choose a **Module** from which you want to export data: 티켓, Timesheet, Surveys, Survey results, Articles, and Triage.
- Choose when you'd like to receive the export from the **Schedule** dropdown field (**Daily, Weekly or Monthly**) and then set the required time.
- Set any** Filters **of your choice. All your **dropdown** and **dependent fields** will be displayed.
- Choose the **Ticket** fields and/or **Tag fields** you want to include in the **CSV **file.참고: It is not possible to use the date range dimension filter when creating an export via Data Exports in 분석**To receive the export file via API**
-
Copy and paste the URL in your Business Intelligence tool.-
Once you hit the **API** from your **BI tool**, you will receive a response in the following format:\{ "export":\{    "url":"..."\}\}
The URL parameter holds the link to the latest export file for that schedule. The file will be available for 30 days from the date of creation.**To access your data exports:**
-
To view the exports that you had scheduled, go to **분석 > **click the** gear icon (****설정) **on the top right corner** > **choose** Data**** Exports.**-
You'll be able to view the **Title**, **Frequency**, and the **Status** of your data export here.-
Click on the **Title** to open a data export schedule, and use the **Active** toggle to deactivate a schedule.-
Use the **download** button that appears when you hover over a scheduled export to download the available data exports.-
An export once scheduled, cannot be edited. You will have to delete it altogether and create one afresh. Use the **delete** button that appears when you hover over a scheduled export.**참고**: You might need assistance from a developer to hit the API, so please ensure that they have access to the API key of the person who created the schedule.You can view the following video to understand how to export 보고서 from 분석.Learn more about the [Basics of 분석](https://freshdesk.com/webinars/get-the-most-out-of-freshdesk-분석-recording) through our webinar with insights on curated 보고서, creating custom 보고서 for your 헬프데스크, learning to apply filters on 보고서, and much more.You can also refer to our [분석 guide](https://freshdesk.com/assets/resources/freshdesk/Make-informed-decisions-with-Freshdesk-분석.pdf) for various use cases to implement in your 헬프데스크.

</details>

<details>
<summary><strong>schedule a report in 분석할 수 있나요?</strong></summary>

To schedule your custom 보고서 and the widgets.- Click and open a **custom report.**
- Click on the **Export** icon on the top right corner.
- Select **Schedule Report **from the drop down**.**
- Set the **cadence, customize the time of delivery, subject, and description** to suit your business.
- Under Send to, add your 이메일 address. You can add additional 이메일 addresses by typing the required ones.
- Click **Save.****참고**: Curated 보고서 cannot be scheduled. You can only schedule custom 보고서.![이미지](https://s3.amazonaws.com/cdn.freshdesk.com/data/헬프데스크/attachments/production/50008161285/original/rjB2lJS3fmzFZIR-lRQXay9Q1JmYV0nLqA.gif?1681986047)

</details>

<details>
<summary><strong>Will I be able to schedule report widgets?</strong></summary>

Yes, you can schedule the widgets of custom 보고서 using the Schedule option. You will be able to choose the Report Schedule date, its frequency, and the 이메일 content. You can also choose the report widget to be scheduled in the form of a PDF or CSV. Please 참고 that you will not be able to schedule the widgets of curated 보고서.

</details>

<details>
<summary><strong>Can the data in 보고서/widgets be made realtime?</strong></summary>

The 보고서 and widgets in 분석 have a refresh time of 30 minutes which is standard across all the Freshdesk 요금제. Hence the widgets/보고서 cannot be configured to reflect live data unlike the 대시보드 feature, which is based on live data.

</details>

<details>
<summary><strong>configure widgets with the time period greater than the corresponding report time frame할 수 있나요?</strong></summary>

The Time period/date range of the 분석 report will be the superset of the time period specified in the widgets associated with the 보고서. In other words, the widget date range needs to be a subset of the report date range.

</details>

<details>
<summary><strong>Can the 보고서 in 분석 be shared with others in the 헬프데스크?</strong></summary>

Yes, when creating a New report in 분석, you can choose between either creating the report just for yourself or for Everyone. If the latter option is chosen then the 상담원 who have access to the 분석 will be able to see them under the Shared 보고서 section under 분석.

</details>

<details>
<summary><strong>How many custom 보고서 can I create at the maximum?</strong></summary>

You can create as many custom 보고서 you want in 분석. There’s no fixed limit.

</details>

<details>
<summary><strong>How many widgets can I add to a custom report?</strong></summary>

You can add as many widgets you want in 분석. There’s no fixed limit.

</details>

<details>
<summary><strong>export the ticket activities using 분석하는 방법은 무엇인가요?</strong></summary>

분석 in Freshdesk lets you identify problems and keep tabs on all the metrics that matter to you. With Freshdesk 분석, you can analyze your entire 헬프데스크 and, most importantly, come to conclusions. From identifying areas of improvement to creating data-driven 요금제, you can back your 지원 instincts using 분석.You can export your 헬프데스크 ticket activities using the Data exports option in the 설정 icon. Once you click on the Create Export button, you can set the export based on basic modules such as 티켓, Timesheets, Surveys, Survey Results, Articles, Triage, etc. Apart from this, you can-
customize the export based on filters,-
select the ticket field needed in the export, and-
schedule the frequency and schedule for the 보고서.![You can export your 헬프데스크 ticket activities using the Data exports option in the 설정 icon. Once you click on the Create Export button, you can set the export based on basic modules such as 티켓, Timesheets, Surveys, Survey Results, Articles, Triage, etc.](https://s3.amazonaws.com/cdn.freshdesk.com/data/헬프데스크/attachments/production/50008538588/original/kBiDMlgXWyL4ibW9_528LVwekqh1rxfezQ.gif?1686030602)Please 참고 that this option is available only for the 계정 관리자 agent and inaccessible to other 헬프데스크 상담원.Learn more about the [Basics of 분석](https://freshdesk.com/webinars/get-the-most-out-of-freshdesk-분석-recording) through our webinar with insights on curated 보고서, creating custom 보고서 for your 헬프데스크, learning to apply filters on 보고서, and much more.You can also refer to our [분석 guide](https://freshdesk.com/assets/resources/freshdesk/Make-informed-decisions-with-Freshdesk-분석.pdf) for various use cases to implement in your 헬프데스크.If you have any further questions or clarifications, please drop an 이메일 to [지원@freshdesk.com](mailto:지원@freshdesk.com) and our Product Specialist will be happy to assist you.

</details>

<details>
<summary><strong>왜 am I not able to save the filters that I apply to curated 보고서인가요?</strong></summary>

Curated 보고서 are for one-time insights. Freshdesk lets you clone any curated report or widget you want. You can **clone a curate report and customize it** by applying the required filters and then save it accordingly.

</details>

<details>
<summary><strong>clone a curated report하는 방법은 무엇인가요?</strong></summary>

Once you go inside a curated report, switch from **Viewing** mode to **Editing** mode. Now, click on the report name (say Ticket Volume Trends) to get the Clone Report option.![이미지](https://s3.amazonaws.com/cdn.freshdesk.com/data/헬프데스크/attachments/production/50000818423/original/Vq_fl2BO6tsH5NVtgtLC-_sTavS9Dr_GUA.png?1583734322)

</details>

<details>
<summary><strong>view and edit mode in 분석하는 방법은 무엇인가요?</strong></summary>

You can control your 팀's access to 분석 under 관리자 > 팀 > Roles > 보고서 section.You can provide them with View, Edit, or Manage (includes edit and exports) access.![이미지](https://s3.amazonaws.com/cdn.freshdesk.com/data/헬프데스크/attachments/production/50008401377/original/89oBKLdVdPX1d3CfJ1TLYenzyn6SS6pfwQ.png?1684492983)View - You can access curated 보고서 and custom 보고서 (based on your visibility). With view access, you cannot add Filters but can view underlying data. You can still change visualizations, subscribe to 보고서, add the widget to another report, and drill down on data.![이미지](https://s3.amazonaws.com/cdn.freshdesk.com/data/헬프데스크/attachments/production/50008538534/original/hmJTVPat_gZs-GE6BRXtBt3J-PL1LVpQjQ.gif?1686030127)Edit - In addition to view access, you can add widgets, create custom 보고서, add/edit filters in existing curated and custom 보고서 (based on your visibility), and delete custom 보고서. Underlying data will also be visible.![이미지](https://s3.amazonaws.com/cdn.freshdesk.com/data/헬프데스크/attachments/production/50008538545/original/2iOZIP-3a61-TbSfO62Aj204Vgx4W2WZ_w.gif?1686030188)Manage (includes edit and exports) - Along with edit access, you can access 분석 설정 and create/edit/delete and enable/disable schedules and exports.

</details>

<details>
<summary><strong>분석 features across various 요금제</strong></summary>

For a detailed comparison of 분석 features across each 요금제, please refer to the article [here](https://지원.freshdesk.com/지원/solutions/articles/50000001108-분석-features-for-each-요금제).**참고:** If you're a Freshdesk 고객 before the year 2019, you need to upgrade to Estate'19 요금제 to access custom 보고서.

</details>

<details>
<summary><strong>I need to schedule data exports</strong></summary>

You can schedule data export using **설정 > Data export**. You will find the 설정 option near the New Report on 분석 homepage. You can create a data export, select the fields you want, apply the necessary filters and set the schedule.

</details>

<details>
<summary><strong>find out how much time a ticket spent on each status하는 방법은 무엇인가요?</strong></summary>

You can choose the metric 'Time spent in business hours' and sort by the filter 'Status' to know the amount of time spent by each ticket in each ticket status.

</details>

<details>
<summary><strong>measure resolution time for a ticket excluding the time spent on waiting for the 고객하는 방법은 무엇인가요?</strong></summary>

You can get this data in two ways:1. Choose the Metric: Resolved time spent in business hours
Sort by Filter: Status does not include waiting on 고객
Group by: Status
From underlying data, you can find out how much time was spent on the SLA status at a ticket level2. Choose the Metric: Resolved time spent in business hours
Sort by Filter: Status does not include SLA Status: Off
Group by: StatusFrom underlying data, you can find out how much time was spent on the SLA status at a ticket level

</details>

---

## 🔗 관련 자료

추가적인 도움이 필요하시면 다음 자료들을 참고해 주세요:

- [Freshdesk 도움말 센터](https://support.freshdesk.com)
- [커뮤니티 포럼](https://community.freshworks.com)
- [고객지원팀 문의](mailto:support@freshdesk.com)

:::tip 도움말
더 자세한 정보나 개별 상담이 필요하시면 고객지원팀으로 연락해 주세요.
:::
