---
sidebar_position: 1
---

# 현장 서비스 관리 FAQ

현장 서비스 관리에서 자주 발생하는 질문들과 해결 방법을 정리했습니다. 각 섹션별로 구분하여 필요한 정보를 빠르게 찾을 수 있습니다.

:::info 안내
이 FAQ는 실제 사용자들이 자주 묻는 질문들을 바탕으로 작성되었습니다. 추가 문의사항이 있으시면 고객지원팀에 문의해 주세요.
:::


## 📋 계정 및 관리

<details>
<summary><strong>I do not see the Field Service Management option in the Admin tab. Why?</strong></summary>

The Field Service Management module is available on **Blossom, Garden,** **Estate,** and **Forest** plans in Freshdesk. If you are on either of these plans and still cannot see the option, please write to us at [support@freshdesk.com](mailto:support@freshdesk.com).

</details>


## 📋 일반 질문

<details>
<summary><strong>How much do field technician licenses cost?</strong></summary>

It costs **USD 29** per field technician per month. You can add or remove Field Technicians by going to **Admin >  > Field Service Management > Manage**.

</details>

<details>
<summary><strong>Can I use Freshdesk without Field Service Management or Field Technician licenses?</strong></summary>

Yes, you can use Freshdesk without Field Tech licenses. The Field Service Management module is an add-on created specifically for those organizations which employ field technicians for support. If you provide only online helpdesk support, you do not need to purchase Field Technician licenses.

</details>

<details>
<summary><strong>How do I enable the scheduling dashboard feature in Freshdesk?</strong></summary>

The scheduling dashboard feature is available on **Blossom, Garden, Estate, and Forest** plans in Freshdesk. To access the Scheduling Dashboard,- Go to **Admin > Support Operations > Field Service Management**
- Click on "**Enable**"
- Scheduling Dashboard should appear in the navigation sidebar on the left-hand side under the "Field Service" icon.

</details>

<details>
<summary><strong>Can I create a service task without having to create a support ticket first?</strong></summary>

Yes, you can create a service task without having to create a support ticket first. Refer to this [article](http://support.freshdesk.com/en/support/solutions/articles/240293-a-guide-to-field-service-for-helpdesk-agents) for more details.

</details>

<details>
<summary><strong>I have created a service task directly without any ticket. Can I assign this service task to a field technician?</strong></summary>

You can assign a service task to a field technician or a support agent. This service task can be requested by a customer and created by a support agent or a field technician. Read this [article](http://support.freshdesk.com/en/support/solutions/articles/240293-a-guide-to-field-service-for-helpdesk-agents) to see how you can create a service task.

</details>

<details>
<summary><strong>Can a service task have child service tasks?</strong></summary>

Yes, you can create child service tasks under a parent service task.

</details>

<details>
<summary><strong>Can I convert a support ticket to a service task?</strong></summary>

A ticket cannot be converted to a service task and vice-versa. However, you can create a service task off that ticket. Refer to this [article](http://support.freshdesk.com/en/support/solutions/articles/240293-a-guide-to-field-service-for-helpdesk-agents) for more details.

</details>

<details>
<summary><strong>Is it possible to link service tasks in Freshdesk?</strong></summary>

Yes, it is possible. By using trackers, parent service tasks can be linked in Freshdesk.  If you have multiple service tasks with a similar problem, you can create a Tracker and link the all tasks to it.Click here to know more about [Linking](https://support.freshdesk.com/en/support/solutions/articles/224695-setting-up-linked-tickets).

</details>

<details>
<summary><strong>Can a service task be linked to a ticket?</strong></summary>

No. Independent service tasks can be linked to each other, not to tickets.

</details>

<details>
<summary><strong>Can a child service task be linked to another child service task</strong></summary>

No. Child service tasks cannot be linked to other tasks.

</details>

<details>
<summary><strong>What is the difference between Field technician and Customer service technician roles in Freshdesk?</strong></summary>

Customer Service Technicians can create service tasks and manage contacts in addition to the other privileges available to Field technicians.Field Technicians cannot see or respond to tickets. They can only respond to the service tasks assigned to them or their service group, add notes, and resolve their tasks.Field TechnicianCustomer Service TechnicianEdit everyone's time entries✔️❌Edit only their time❌✔️Create or edit contact❌✔️Create or edit contact segment or company segment❌✔️Create child service tasks❌✔️

</details>

<details>
<summary><strong>What are the default field service roles available in Freshdesk?</strong></summary>

Currently, Freshdesk has two default roles for field service - Field technician and Customer service technician.Field technician: Can view, reply, update and resolve service tasksCustomer service technician: Can create, view, reply, update and resolve service tasks and manage contacts.In addition, customers of all plans other than Blossom and Garden can create Custom roles

</details>


## 📋 사용자 관리

<details>
<summary><strong>What is the difference between a Field Technician license and a Helpdesk agent license?</strong></summary>

Support tickets from customers are not accessible to field technicians directly; they can only access service tasks or jobs assigned to them by your helpdesk agents. Field technicians also get access to a Freshdesk app that is dedicated to Field Service, with the ability to- Track service tasks and monitor their schedule
- Navigate to the customer's location
- Track time spent in the field and log billable hours for service provided
- Collect customer signatures once the job is done...and more.  These features are available only to field technicians and not to helpdesk agents via the Freshdesk mobile app.

</details>

<details>
<summary><strong>How different is login for a Field Service Agent?</strong></summary>

The login process for all agents in Freshdesk are the same, be it a Freshdesk Support Agent(Full time/ Occasional), or a Field Service Agent.

</details>

<details>
<summary><strong>Can an existing agent be converted into a Field Technician?</strong></summary>

No, it will not be possible to convert an existing agent into a Field Technician. But you will be able to convert an existing contact into a Field Technician.As a workaround, you can delete the agent, that converts them to a contact and the convert the contact to a field technician

</details>

<details>
<summary><strong>What roles and scope can be assigned to a Field service agent?</strong></summary>

For field agents, you will only be able to choose Ticket Scope, either Groups or Restricted. By default, the field technician will be associated with the Field Technician role. It will not be possible to associate the Field technician with other roles.![Image](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50000832705/original/OlSOVArNQA9xZMx8snky1LyBbcgXjECM1w.png?1583928373)

</details>

<details>
<summary><strong>Can normal agents be added to service groups?</strong></summary>

Yes, In case your helpdesk agents also go out into the field to help customers, you can add them to service groups.This ensures that any service task you assign to a particular group can be picked up by the helpdesk agents in it as well. This will also allow helpdesk agents to view their service tasks like any other ticket through their mobile apps.

</details>


---

## 🔗 관련 자료

추가적인 도움이 필요하시면 다음 자료들을 참고해 주세요:

- [Freshdesk 도움말 센터](https://support.freshdesk.com)
- [커뮤니티 포럼](https://community.freshworks.com)
- [비디오 튜토리얼](https://freshdesk.com/resources/videos)

:::tip 도움말
더 자세한 정보나 개별 상담이 필요하시면 고객지원팀(support@freshdesk.com)으로 연락해 주세요.
:::
