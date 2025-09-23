---
sidebar_position: 1
---

# 로그인 및 SSO 도움말 FAQ

로그인 및 SSO 도움말에서 자주 발생하는 질문들과 해결 방법을 정리했습니다. 각 섹션별로 구분하여 필요한 정보를 빠르게 찾을 수 있습니다.

:::info 안내
이 FAQ는 실제 사용자들이 자주 묻는 질문들을 바탕으로 작성되었습니다. 추가 문의사항이 있으시면 고객지원팀에 문의해 주세요.
:::


## 📋 계정 및 관리

<details>
<summary><strong>How can I login to my account?</strong></summary>

You can login to your Freshdesk account using the Login option at the top-right on your Freshdesk Portal, which will be available in the URL **yourcompanyname.freshdesk.com**.This will take you to the login page where you can use your login credentials - email address and password, to access the helpdesk.You can also login from [https://freshdesk.com/login](https://freshdesk.com/login).

</details>

<details>
<summary><strong>Why am I not able to login to my Freshdesk account?</strong></summary>

There could be several reasons why you're unable to log in to your Freshdesk account. Here are some common issues and their solutions:- **Incorrect Credentials:** Double-check that you're entering the correct email and password. Make sure there are no typos or extra spaces.
- **Password Reset:** If you've forgotten your password, use the "Forgot Password" link on the login page to reset it. If you're not receiving the password reset email for your Freshdesk account, here are some steps you can take to resolve the issue:
- **Check Spam/Junk Folder:** Sometimes, password reset emails can be filtered into your spam or junk folder. Make sure to check these folders in your email account.
- **Verify Email Address:** Ensure that you're entering the correct email address associated with your Freshdesk account. A typo can prevent the email from being sent to the correct address.
- **Resend the Email:** Try requesting the password reset email again. Sometimes, there might be a delay, or the email might not have been sent properly the first time.
- **Whitelist Freshdesk Email Address:** Add the Freshdesk email address (usually support@freshdesk.com or similar) to your email contacts or whitelist to ensure it doesn't get blocked by your email provider.
- **Check Email Filters:** Ensure that you don't have any email filters set up that might be redirecting the password reset email to another folder or automatically deleting it.- **Account Locked:** After multiple failed login attempts, your account might be temporarily locked. Wait for a while and try again or contact your admin.
- **Browser Issues:** Clear your browser cache and cookies, or try logging in from a different device/browser.
- **Network Issues: **Ensure you have a stable internet connection. Sometimes network issues can prevent successful login attempts.
- **Account Deactivation:** Check if your account has been deactivated or suspended. Contact your Freshdesk admin or support for assistance.
- **Two-Factor Authentication:** If two-factor authentication is enabled, ensure you're entering the correct verification code sent to your email or mobile device.**Contact customer support:** If you've tried all of the above and still can't log in, please reach out to [support@freshdesk.com](mailto:support@freshdesk.com) with the following details,- Account URL to which you're trying to log in, and
- Error message screenshot/video grab highlighting what happens when you try to log in to your account

</details>

<details>
<summary><strong>I see the error 'Sorry we couldn’t locate your account' when I try to login. What is the issue here?</strong></summary>

If the email address that was entered for login, is not an agent/contact in the account, then this error would be displayed. You could sign up for a new account, using the Sign Up option on the Portal, or ask to be added as an Agent from under **Admin >Team > Agents** in your account. Once this is done, you could log in to your Freshdesk Account.If you continue to face issues with login, reach out to Freshdesk support through support@freshdesk.com to know the Agents on your Freshdesk account and we would assist you in getting over this instance.

</details>

<details>
<summary><strong>When will the data be deleted once I cancel my account?</strong></summary>

When an account is deleted, all associated data is destroyed within 14 days.

</details>

<details>
<summary><strong>How to sign up for a Freshdesk Account</strong></summary>

To open or create a Freshdesk account, start with the free trial at [https://freshdesk.com/signup](https://freshdesk.com/signup)

</details>


## 📋 일반 질문

<details>
<summary><strong>How does SSO in Freshdesk work?</strong></summary>

The Single Sign-On capability in Freshdesk lets the users arriving at your support portal login with their credentials saved on your database.This saves them the time and effort involved in creating a separate account for your support portal. You can also set up an[ ](https://support.freshdesk.com/support/solutions/articles/31166-single-sign-on-remote-authentication-in-freshdesk)**[](https://support.freshdesk.com/support/solutions/articles/31166-single-sign-on-remote-authentication-in-freshdesk)[SSO mechanism ](https://support.freshdesk.com/support/solutions/articles/50000001658-single-sign-on-in-freshdesk)**to validate users trying to log into your portal for Freshdesk using a locally hosted script. These could be the users who already have an account in your web application or whose information you have stored in your internal application like ActiveDirectory.

</details>

<details>
<summary><strong>How to reset my password?</strong></summary>

- Type your URL in the address bar, hit enter and select Login. Then choose the option **Are you an Agent? Login here** and it will redirect you to the Freshworks page.
- Select **Forgot password** option, enter your email address and a password reset link will be sent to your email.
- Reset the password using the link and you can log in to the account.Please reach out to *support@freshdesk.com* for further help and clarifications.If your customers are facing login issues, here's how you can reset their password via support videos.

</details>

<details>
<summary><strong>Where do I configure Single Sign On within Freshdesk?</strong></summary>

Using Single Sign-On, your users could get automatically authenticated while logged in to your common Login option. For example, if you have a website or dashboard where your users log in and would like to use the same to access Freshdesk, you could make use of Single Sign-On.You could configure Single Sign-On within Freshdesk by going through your Freshworks Org page. You can access the Org page by clicking on the Freshworks switcher icon on the bottom left corner and click on Security under your Freshworks Org URL and turning on "Single-Sign-On". You could then choose between Simple or SAML SSO to proceed with the configuration.![Image](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50008957735/original/OcZ95RsuLrBSxuoAQk-RDXHNDDWdNQWg0w.png?1689935654)

</details>

<details>
<summary><strong>How can I bypass SSO login when I have it enabled?</strong></summary>

You can make use of the companyname.freshdesk.com/login/normal and enter your valid Freshdesk credentials to access the account.

</details>

<details>
<summary><strong>What is the Remote Login URL?</strong></summary>

While setting up an SSO, the users would have to login from a common login URL, to be authenticated using SSO. The Remote Login URL is that URL to which your users would be redirected when they hit the Login button on your portal after you have set up an SSO.You would have to update this field with the common login URL, while setting up SSO for your Freshdesk Account.

</details>

<details>
<summary><strong>SSO is not working and getting the message 'Session expired. Please login again'</strong></summary>

We use the UTC timestamp to generate the hash for validation. Before we were allowing the hash to be valid for 30 minutes, but now we have updated it to be valid for 30 seconds alone. Please check if your SSO server is in sync with the UTC time.If your server is in sync, and you're still getting the session expired error, please drop an email to support@freshdesk.com.

</details>

<details>
<summary><strong>There is a not secure message when accessing the system from Chrome</strong></summary>

If this is happening for your vanity URL, then you have to set up an SSL certificate for your custom domain.SSL options for custom domains are available from the Blossom Plan. Please write to us at  **support@freshdesk.com**,  and our support team will help you in obtaining the SSL certificate..Once you receive the email, please follow the instructions to confirm your request for an SSL certificate.Click [here](https://support.freshdesk.com/en/support/solutions/articles/90479-configuring-a-custom-ssl-certificate-for-your-support-portal) to read more on Configuring a custom SSL certificate for your support portal.

</details>


## 📋 데이터 관리

<details>
<summary><strong>Where is your data servers located?</strong></summary>

Our Data Centres are located in the US, EEA, UAE, IND, and AU. To learn more about our Data hosting you, refer to [https://www.freshworks.com/privacy/data-hosting/](https://www.freshworks.com/privacy/data-hosting/)You can choose your preferred data location when you sign up for your account.![Image](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50012706959/original/LLKRrTD8Jq6cBuK3sP2WiPwy5LF3klesCg.png?1723118643)If there are any specific regulatory requirements and performance considerations, and you are looking to migrate your data to a different data center region, contact [support@freshdesk.com](mailto:support@freshdesk.com).

</details>


## 📋 문제 해결

<details>
<summary><strong>I get the 'Unable to allocate day pass' error while logging in. How do I resolve this?</strong></summary>

If you have been added as an Occasional Agent in your account, and if your account does not have sufficient day passes to log in, you will encounter this error.![Image](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50009297562/original/mkdFEgNk-DWkn-_1XGWIh0ReJ5wGmhSpHw.png?1693234132)You can get in touch with your Account Administrators, and they can assist you in purchasing day passes for logging in. A new day pass can be added to your account from within **Admin > Account > Day passes**. You can also view the day pass Usage History on the same page.![Image](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50009297555/original/NfM5szmg2E7kodMBWheWlfNkQL99zYHYeQ.png?1693234122)

</details>

<details>
<summary><strong>Why am I getting ‘You’re not allowed to access this page’ error?</strong></summary>

You will encounter the error ‘You’re not allowed to access this page,’ if you click on a link you don’t have access to or do not have the right to view. Let us consider the following scenarios.[](https://docs.google.com/document/d/1TkgdOi7mpoUrb-i9DH2VbF-eSPoJ5g91BYqgf1wN4ws/edit#heading=h.yrkszl4y4q1j)[Error displayed for agents](#Error-displayed-for-agents)[Error displayed for customers](#Error-displayed-for-customers)**Error displayed for agents**
If you are an agent and receive this error message after you click on a ticket to view its details, you do not have permission to view the ticket. Please check if you have the correct ticket scope (Group level or Global access) under the Agents page.
**Error displayed for customers**
As a customer, when you click on the URL of a solution article displayed only to a specific company (Restricted Access) and you are not part of that company, then this error would appear.Please reach out to [support@freshdesk.com](mailto:support@freshdesk.com) if the error appears in scenarios other than those mentioned above.

</details>

<details>
<summary><strong>Why am I getting the error 'Portal is not available at your location' while trying to access a Freshdesk page?</strong></summary>

The error message "Portal is not available at your location" typically occurs when you try to access a Freshdesk page, but the page is restricted or not accessible from your current location. There are several possible reasons for this error:- Geographical Restrictions: Some Freshdesk pages or features may have geographical restrictions, and they may not be available in certain regions or countries due to legal or compliance reasons.
- IP Restrictions: Your IP address might be from a location that is blocked or restricted from accessing specific Freshdesk pages or services.
- Limited Access Permissions: Your user account or role might not have the necessary permissions to access the particular page you are trying to view.
- Page Unavailability: The page you are trying to access could be temporarily unavailable due to maintenance or other technical issues.
- Network or Firewall Restrictions: Your network or firewall settings could be preventing access to certain Freshdesk pages.To resolve the issue:- Check Permissions: Ensure that your user account has the appropriate permissions to access the page in question. If needed, contact your Freshdesk account administrator to verify and adjust your permissions.
- Verify Page Availability: Confirm if the page you are trying to access is indeed available and not undergoing maintenance or restricted for specific locations.
- Check Network Settings: If you are accessing Freshdesk from a workplace or public network, check if any network or firewall settings are blocking access to the page.
- Use a VPN: If the page is restricted in your current location, you can try using a virtual private network (VPN) to access Freshdesk from a different location.
- Contact Freshdesk Support: It will be shown if your account has the IP whitelisting feature enabled or if your IP has been blocked. If the issue persists, reach out to Freshdesk support with your Public IP address for assistance. They can investigate the specific error and provide further guidance to resolve the problem.In case of the latter, please contact Freshdesk support with your Public IP address and we would assist you further regarding this instance.

</details>

<details>
<summary><strong>Why am I getting the 'Invalid Time Stamp' error when I try to login using an SSO?</strong></summary>

You will be prompted with  **'Invalid Time Stamp**' error when the difference between the UTC timestamp generated by your server and ours is more than 30 seconds. Ensuring that your servers stay in sync with the NTP server ([https://en.wikipedia.org/wiki/Network_Time_Protocol](https://en.wikipedia.org/wiki/Network_Time_Protocol)) will sort out this issue.If you continue to face issues, kindly write to **support@freshdesk.com** and one of our agents will assist you further.

</details>

<details>
<summary><strong>Why am I getting a 'Login unsuccessful' error on the AD SSO?</strong></summary>

This error message denoting authentication failure would be because of an error in setting up the SSO. To analyse this, we would require the debug log. Please enter **?debug=1 **at the end of the URL that is generated, to retrieve the debug log**. **Also, please check the constructed URL after the login, to see if the Hash is generated or not.If the issue persists, please send an email to [support@freshdesk.com](mailto:support@freshdesk.com).

</details>

<details>
<summary><strong>SSO error: Login was unsuccessful! - Validation Failed : Invalid Signature on SAML Response</strong></summary>

This error occurs when there is a mismatch in the signature.To extract the SHA signature from Google,- In the Google Admin console, navigate to Security > Set up single sign on and click on the download Certificate.
- Open the downloaded .pem extension file using notepad/sublime text editor.- Copy the certificate from the notepad/sublime text-editor and paste it in the X.509 certificate section in [https://www.samltool.com/fingerprint.php](https://www.samltool.com/fingerprint.php)- Make sure that you’ve selected SHA256 as the algorithm and click on calculate fingerprint.- Enter the key displayed in the formatted fingerprint text box in your Freshdesk account under Admin > Security > SAML >Security Certificate Fingerprint > Save.

</details>


## 📋 사용자 관리

<details>
<summary><strong>Why are my agents not able to login through AD SSO?</strong></summary>

Please check if the agent who is logging in is using their email address which is part of the AD. Also, if they are a user on the AD, you would have to make sure if their user profile on the AD has permissions to use SSO. The email address from your AD is the parameter that Freshdesk checks while authenticating the login, to locate their profile on Freshdesk.

</details>

<details>
<summary><strong>Why are the names under my agents' profiles automatically changed every time they log in?</strong></summary>

After every login with an SSO, Freshdesk will sync the name of the agents with the names in your SSO database. Hence, the names in Freshdesk would automatically be updated.To fix this, please check how the names of the agents are configured on your SSO database.Also, we support UTF-8 encoded special characters only; so if the name contains any unsupported special characters, we would change it to the English equivalent.

</details>

<details>
<summary><strong>Why are my agents logged back in to the portal automatically after they log out?</strong></summary>

This would be because of an incorrect **Remote Logout URL**.** **If you have entered the login page of the portal as the Remote Logout URL, please have that modified and give this another try.

</details>

<details>
<summary><strong>How can I authenticate WordPress users to login to Freshdesk?</strong></summary>

You can set up single sign-on for your WordPress users to easily log in to Freshdesk using the Freshdesk plugin for WordPress.You can use the plugin to enable your users to seamlessly and securely log in to Freshdesk. To do so, you first need to install the [Freshdesk WordPress plugin](https://wordpress.org/plugins/freshdesk-support/). You can install the plugin from the plugins directory if your site runs on self-hosted WordPress. If you use WordPress.com, you need to be on the [Business plan or above](https://wordpress.com/pricing/) to install this plugin.Click here to read a step-by-step guide on [authenticating WordPress users into your Freshdesk account](https://support.freshdesk.com/en/support/solutions/articles/50000001053) in more detail.

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
