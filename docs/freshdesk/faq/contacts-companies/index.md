---
sidebar_position: 1
---

# 연락처 및 회사 FAQ

연락처 및 회사에서 자주 발생하는 질문들과 해결 방법을 정리했습니다. 각 섹션별로 구분하여 필요한 정보를 빠르게 찾을 수 있습니다.

:::info 안내
이 FAQ는 실제 사용자들이 자주 묻는 질문들을 바탕으로 작성되었습니다. 추가 문의사항이 있으시면 고객지원팀에 문의해 주세요.
:::


## 📋 일반 질문

<details>
<summary><strong>How can I onboard my customers into Freshdesk?</strong></summary>

This can be done by navigating to **Customers-> Contacts** and choose the contact and clicking on the **send activation email **option. This will send a secure link to the customer's email, which they can use to set up a password. Your customers can then log in to the portal using these credentials.

</details>

<details>
<summary><strong>How can I send activation emails in bulk?</strong></summary>

Navigate to **Customers-> Contacts -> **Click on the hamburger menu and choose** Unverified**** contacts **from the list. Use the the check box available to  to either ‘Select all’ or select just the necessary contacts and hit the **Send activation email'** button. The selected contacts will now receive an activation email enabling them to verify their accounts.![Image](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/41173841/original/bBNUl2GFMqe9IH0JDTZpQsMxY2ZGlPUcpg.png?1539001174)![Image](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/41173859/original/UTxzcKM_zKTxt4w6iuGp2BdN9gBvAX7I1g.png?1539001204)참고: You can trigger bulk activation emails for upto 30 contacts (per page) at a time.

</details>

<details>
<summary><strong>How do I send an activation email to the customers to start using their portal?</strong></summary>

Go to **Customers > Contacts > choose 'Unverified contacts' from the hamburger menu > check the required contacts click on 'Send activation email'**.This will send a secure link to the customer's email, which they can use to set up a password.Alternatively, you can go to **Admin > Workflows > Email Notifications > Requester notifications > toggle the user activation email ON**.

</details>

<details>
<summary><strong>Can I resend an activation link to a customer?</strong></summary>

Under the Customers tab, when you hover over an **unverified contact**, you will find an option to 'Send activation email'. Clicking on it will trigger an activation email to the respective contact.![Image](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50009264731/original/waSniNYkK4bqDuV3lh4g1kzv3dlrHysibQ.png?1692859419)![Image](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50009264757/original/yQStJYDFtpXB9JzMZ4boJTbbGLdAW2XokA.png?1692859505)**참고:**It is not possible to re-send the activation link for a **verified contact **this way. However, you would be able to change the password share it with them or the contact could directly trigger a password reset.

</details>

<details>
<summary><strong>How to assign ticket to companies?</strong></summary>

When a new contact is linked to a company, the tickets that are raised by that contact will automatically get linked to the Company as well. Once a ticket is linked to a company, even if the contact is associated to a different company on a later date, the ticket will remain with that old company.

</details>

<details>
<summary><strong>How can I change the email address of an existing contact in Freshdesk?</strong></summary>

You can edit a contact and add the new email address as a secondary email address. You can then change the new email address to be the primary email address. Once this change is made, you can choose to delete the secondary (old)email address or retain it for record keeping purpose.To change the email address of a contact in Freshdesk, follow these steps:- Log in to your Freshdesk account as an administrator.
- Navigate to the "Contacts" section from the left sidebar.
- Search for the contact whose email address you want to change using the search bar or scroll through the list of contacts.
- Click on the contact's name to open their profile.
- In the contact profile, click on the "Edit" button (pencil icon) located near the top-right corner.
- Once in the edit mode, update the contact's email address to the new one you want to use.
- Make any other necessary changes to the contact's information, such as name, phone number, or organization details.
- After making the changes, click on the "Save" button to save the updated contact information.Scenarios where a contact's email address might need to be changed include:- Contact Requests Change: The contact themselves might request a change in their email address due to a personal preference, change of job, or other reasons.
- Mistaken Email Entry: An incorrect email address could have been initially entered for the contact, and it needs to be rectified.
- Email Address Update: The contact might update their email address, and you need to reflect this change in Freshdesk.
- Domain Change: The contact's organization might undergo a domain change, requiring an update to their email address.
- Duplicate Contact: Two contacts might be accidentally added with different email addresses, and you need to merge them under the correct email.
- Data Migration: During data migration from another system, the email addresses might need adjustments to match the correct records.Remember to update the email address accurately to ensure seamless communication with the contact in Freshdesk.

</details>

<details>
<summary><strong>Total time spent on company tickets</strong></summary>

You can make use of the Time Sheet summary report to get this data. Choose the date and the customer in the filters and export the report from Reports > Time sheet summary.

</details>

<details>
<summary><strong>While importing contacts, does it update the existing or create new contacts?</strong></summary>

There will not be any duplicates contacts created. When you import, the existing contacts will be updated if there are different details for the email address. If not, that particular contact will be skipped.

</details>


## 📋 문제 해결

<details>
<summary><strong>My customers are getting the error 'You are not authorized to access portal' - how can I fix this?</strong></summary>

This message is displayed to the users if their account (contact profile) is **not verified/activated. **In such a case, please go to **Customers** **>** **Contacts**, click on the contact that is seeing the error message and hit '**Send activation email**' button on the contact details page. The customer can then use the link sent via email to set up a password and log in.![Image](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/41703011/original/bF59A66ujszaQwhEKJOFT3xjwuHG6jAWCw.png?1541749638)As an **Admin**, you'll also be able to set up a password for the contact using the **'Change password**' button on the same page.To do this for multiple unverified contacts, please click on the hamburger menu on the** Contacts** page, click on '**Unverified contacts**' to retrieve the complete list of unverified contacts:![Image](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/41703273/original/nTi1EgA-theId0pAXiW3AUJsPDw-O8aJ_A.png?1541750648)You can bulk select the desired contacts from this list and click on **'Send activation email'**![Image](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/41703297/original/E_LD0nNMrn3hXVP0JsTy_-fMfk2lBapSpQ.png?1541750753)

</details>

<details>
<summary><strong>I have a problem while importing contacts. What could the issue be?</strong></summary>

As a recent user of Freshdesk, you would want to bring in all your contacts into the portal and while doing that - you get an error on the customers' tab saying "an import is already running." This is because while uploading the CSV (or excel) file, there would have been a technical glitch which would block the import. Kindly contact support (support@freshdesk.com) and ask them to kill this so that you could import the file again.Another recommendation would be to check the solution article in the "file import" page which would give you specifications about the various parameters in the file.

</details>


## 📋 사용자 관리

<details>
<summary><strong>How can we allow only logged-in users to create tickets on the portal?</strong></summary>

Please navigate to** 관리자 -> Channels -> Portals -> Settings** where you could see the user permissions listed for who could submit a new ticket on the portal.Kindly choose **logged-in **users in this so that only they would be able to submit new tickets to your portal.

</details>


## 📋 계정 및 관리

<details>
<summary><strong>How do I import contacts to my account?</strong></summary>

If you have a list of contacts that you'd like to add to your Freshdesk account, you can easily do so by following these simple steps:- Prepare the Contact Data: Before you begin the import process, make sure to organize your contact data in a supported file format such as CSV (Comma-Separated Values) or Excel. Ensure that the file contains all the necessary contact details like name, email address, phone number, and any other relevant information.
- Access the Admin Settings: Log in to your Freshdesk account as an administrator.
- Navigate to Contacts: In the left sidebar, click on "Contacts" under the "Admin" section.
- Click on "Import Contacts": Once you are in the Contacts section, look for the "Import Contacts" button. Click on it to initiate the import process.
- Upload the Contact File: In the import window, click "Upload a file" (or) "drag and drop your CSV file here" button to select the CSV or Excel file containing the contact data on your computer.
- Map the Fields: Freshdesk will prompt you to map the fields from the import file to the corresponding contact fields in Freshdesk. This step ensures that the data is imported accurately. Match the columns in your file with the appropriate fields in Freshdesk (e.g., name column with name field, email column with email field).
- Review and Validate: After mapping the fields, review the data to ensure everything is correctly aligned. Check for any missing on mapping.
- Import the Contacts: Once you are satisfied with the data mapping and review, proceed to import the contacts. Click on the "Import" button to begin the process.
- Monitor the Progress: The import process may take some time depending on the number of contacts being imported.
- Import Confirmation: Once the import is complete, you will receive a confirmation message indicating the total number of contacts successfully imported.참고: If an existing contact is found in the CSV file, their information will be updated in Freshdesk.For any errors while importing, please share the screenshot with us to troubleshoot further.

</details>


## 📋 데이터 관리

<details>
<summary><strong>Can we export contacts from Freshdesk ?</strong></summary>

You can export your contacts to a CSV file from under the Customer's tab. When a contact export is triggered, an email is sent to the event performing agent with the link to download the CSV file.![Image](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50008945284/original/0fkEnKuRDt37LTLEKM9sz99mwt5zSNvp4Q.jpeg?1689846308)
![Image](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50008945278/original/xWaYUPKLxHTQUloFH9bk1NtS8M4YQNoq5A.png?1689846286)Once you have triggered the export of contacts from Freshdesk you can track the export as shown below.![Image](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50008945304/original/0wSTwmsMkK0Ft68H2zZpEywGf8vCFjM_yg.png?1689846392)Once you receive the email, simply click on the link to download the CSV file containing your exported contacts.

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
