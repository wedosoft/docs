---
sidebar_position: 1
---

# 로그인 및 SSO 도움말 FAQ

로그인 및 SSO 도움말에서 자주 발생하는 질문들과 해결 방법을 정리했습니다. 각 질문을 클릭하여 상세한 답변을 확인하실 수 있습니다.

:::info 안내
이 FAQ는 실제 사용자들이 자주 묻는 질문들을 바탕으로 작성되었습니다. 추가 문의사항이 있으시면 고객지원팀에 문의해 주세요.
:::

<details>
<summary><strong>내 계정에 로그인하는 방법은 무엇인가요?</strong></summary>

Freshdesk 포털 우측 상단의 로그인 옵션을 사용하여 Freshdesk 계정에 로그인할 수 있습니다, which will be available in the URL **yourcompanyname.freshdesk.com**.로그인 페이지로 이동하여 이메일 주소와 비밀번호인 로그인 정보를 사용해 헬프데스크에 접속할 수 있습니다.You can also 로그인 from [https://freshdesk.com/로그인](https://freshdesk.com/로그인).

</details>

<details>
<summary><strong>Freshdesk 계정에 로그인할 수 없는 이유는 무엇인가요?</strong></summary>

Freshdesk 계정에 로그인할 수 없는 이유는 여러 가지가 있을 수 있습니다. 다음은 일반적인 문제와 해결책입니다:- **Incorrect Credentials:** 올바른 이메일과 비밀번호를 입력하고 있는지 다시 한 번 확인하십시오. 오타나 불필요한 공백이 없는지 확인하십시오.
- **비밀번호 Reset:** 비밀번호를 잊으셨다면 로그인 페이지의 "비밀번호 찾기" 링크를 사용하여 재설정하십시오. If you're not receiving the 비밀번호 reset 이메일 for your Freshdesk 계정, here are some steps you can take to resolve the 문제:
- **Check Spam/Junk Folder:** Sometimes, 비밀번호 reset emails can be filtered into your spam or junk folder. Make sure to check these folders in your 이메일 계정.
- **Verify 이메일 Address:** Ensure that you're entering the correct 이메일 address associated with your Freshdesk 계정. A typo can prevent the 이메일 from being sent to the correct address.
- **Resend the 이메일:** Try requesting the 비밀번호 reset 이메일 again. Sometimes, there might be a delay, or the 이메일 might not have been sent properly the first time.
- **Whitelist Freshdesk 이메일 Address:** Add the Freshdesk 이메일 address (usually 지원@freshdesk.com or similar) to your 이메일 연락처 or whitelist to ensure it doesn't get blocked by your 이메일 provider.
- **Check 이메일 Filters:** Ensure that you don't have any 이메일 filters set up that might be redirecting the 비밀번호 reset 이메일 to another folder or automatically deleting it.- **계정 Locked:** After multiple failed 로그인 attempts, your 계정 might be temporarily locked. Wait for a while and try again or contact your 관리자.
- **Browser Issues:** Clear your browser cache and cookies, or try logging in from a different device/browser.
- **Network Issues: **Ensure you have a stable internet connection. Sometimes network issues can prevent successful 로그인 attempts.
- **계정 Deactivation:** Check if your 계정 has been deactivated or suspended. Contact your Freshdesk 관리자 or 지원 for assistance.
- **Two-Factor Authentication:** If two-factor authentication is enabled, ensure you're entering the correct verification code sent to your 이메일 or mobile device.**Contact 고객 지원:** If you've tried all of the above and still can't log in, please reach out to [지원@freshdesk.com](mailto:지원@freshdesk.com) with the following details,- 계정 URL to which you're trying to log in, and
- 오류 message screenshot/video grab highlighting what happens when you try to log in to your 계정

</details>

<details>
<summary><strong>Freshdesk의 SSO는 어떻게 작동하나요?</strong></summary>

The Single Sign-On capability in Freshdesk lets the users arriving at your 지원 포털 로그인 with their credentials saved on your database.This saves them the time and effort involved in creating a separate 계정 for your 지원 포털. You can also set up an[ ](https://지원.freshdesk.com/지원/solutions/articles/31166-single-sign-on-remote-authentication-in-freshdesk)**[](https://지원.freshdesk.com/지원/solutions/articles/31166-single-sign-on-remote-authentication-in-freshdesk)[SSO mechanism ](https://지원.freshdesk.com/지원/solutions/articles/50000001658-single-sign-on-in-freshdesk)**to validate users trying to log into your 포털 for Freshdesk using a locally hosted script. These could be the users who already have an 계정 in your web application or whose information you have stored in your internal application like ActiveDirectory.

</details>

<details>
<summary><strong>비밀번호를 재설정하는 방법은 무엇인가요?</strong></summary>

- Type your URL in the address bar, hit enter and select 로그인. Then choose the option **Are you an Agent? 로그인 here** and it will redirect you to the Freshworks page.
- Select **Forgot 비밀번호** option, enter your 이메일 address and a 비밀번호 reset link will be sent to your 이메일.
- Reset the 비밀번호 using the link and you can log in to the 계정.Please reach out to *지원@freshdesk.com* for further help and clarifications.If your customers are facing 로그인 issues, here's how you can reset their 비밀번호[https://www.youtube.com/watch?v=oJTcbYch5T8&list=PLsYJ3BsyR4qGFujlW0iDtOBOf4IPVsAqt&index=2](If%20your%20customers%20are%20facing%20login%20issues,%20here)

</details>

<details>
<summary><strong>Freshdesk에서 Single Sign On을 어디서 구성하나요?</strong></summary>

Using Single Sign-On, your users could get automatically authenticated while logged in to your common 로그인 option. For example, if you have a website or 대시보드 where your users log in and would like to use the same to access Freshdesk, you could make use of Single Sign-On.You could configure Single Sign-On within Freshdesk by going through your Freshworks Org page. You can access the Org page by clicking on the Freshworks switcher icon on the bottom left corner and click on Security under your Freshworks Org URL and turning on "Single-Sign-On". You could then choose between Simple or SAML SSO to proceed with the configuration.![이미지](https://s3.amazonaws.com/cdn.freshdesk.com/data/헬프데스크/attachments/production/50008957735/original/OcZ95RsuLrBSxuoAQk-RDXHNDDWdNQWg0w.png?1689935654)

</details>

<details>
<summary><strong>Where is your data servers located?</strong></summary>

Our Data Centres are located in the US, EEA, UAE, IND, and AU. To learn more about our Data hosting you, refer to [https://www.freshworks.com/privacy/data-hosting/](https://www.freshworks.com/privacy/data-hosting/)You can choose your preferred data location when you sign up for your 계정.![이미지](https://s3.amazonaws.com/cdn.freshdesk.com/data/헬프데스크/attachments/production/50012706959/original/LLKRrTD8Jq6cBuK3sP2WiPwy5LF3klesCg.png?1723118643)If there are any specific regulatory requirements and performance considerations, and you are looking to migrate your data to a different data center region, contact [지원@freshdesk.com](mailto:지원@freshdesk.com).

</details>

<details>
<summary><strong>bypass SSO 로그인 when I have it enabled하는 방법은 무엇인가요?</strong></summary>

You can make use of the companyname.freshdesk.com/로그인/normal and enter your valid Freshdesk credentials to access the 계정.

</details>

<details>
<summary><strong>I get the 'Unable to allocate day pass' 오류 while logging in. How do I resolve this?</strong></summary>

If you have been added as an Occasional Agent in your 계정, and if your 계정 does not have sufficient day passes to log in, you will encounter this 오류.![이미지](https://s3.amazonaws.com/cdn.freshdesk.com/data/헬프데스크/attachments/production/50009297562/original/mkdFEgNk-DWkn-_1XGWIh0ReJ5wGmhSpHw.png?1693234132)You can get in touch with your 계정 Administrators, and they can assist you in purchasing day passes for logging in. A new day pass can be added to your 계정 from within **관리자 > 계정 > Day passes**. You can also view the day pass Usage History on the same page.![이미지](https://s3.amazonaws.com/cdn.freshdesk.com/data/헬프데스크/attachments/production/50009297555/original/NfM5szmg2E7kodMBWheWlfNkQL99zYHYeQ.png?1693234122)

</details>

<details>
<summary><strong>I see the 오류 'Sorry we couldn’t locate your 계정' when I try to 로그인. What is the 문제 here?</strong></summary>

If the 이메일 address that was entered for 로그인, is not an agent/contact in the 계정, then this 오류 would be displayed. You could sign up for a new 계정, using the Sign Up option on the 포털, or ask to be added as an Agent from under **관리자 >팀 > 상담원** in your 계정. Once this is done, you could log in to your Freshdesk 계정.If you continue to face issues with 로그인, reach out to Freshdesk 지원 through 지원@freshdesk.com to know the 상담원 on your Freshdesk 계정 and we would assist you in getting over this instance.

</details>

<details>
<summary><strong>왜 am I getting ‘You’re not allowed to access this page’ 오류인가요?</strong></summary>

You will encounter the 오류 ‘You’re not allowed to access this page,’ if you click on a link you don’t have access to or do not have the right to view. Let us consider the following scenarios.[](https://docs.google.com/document/d/1TkgdOi7mpoUrb-i9DH2VbF-eSPoJ5g91BYqgf1wN4ws/edit#heading=h.yrkszl4y4q1j)[오류 displayed for 상담원](#오류-displayed-for-상담원)[오류 displayed for customers](#오류-displayed-for-customers)**오류 displayed for 상담원**
If you are an agent and receive this 오류 message after you click on a ticket to view its details, you do not have permission to view the ticket. Please check if you have the correct ticket scope (Group level or Global access) under the 상담원 page.
**오류 displayed for customers**
As a 고객, when you click on the URL of a 해결책 article displayed only to a specific company (Restricted Access) and you are not part of that company, then this 오류 would appear.Please reach out to [지원@freshdesk.com](mailto:지원@freshdesk.com) if the 오류 appears in scenarios other than those mentioned above.

</details>

<details>
<summary><strong>왜 am I getting the 오류 '포털 is not available at your location' while trying to access a Freshdesk page인가요?</strong></summary>

The 오류 message "포털 is not available at your location" typically occurs when you try to access a Freshdesk page, but the page is restricted or not accessible from your current location. There are several possible reasons for this 오류:- Geographical Restrictions: Some Freshdesk pages or features may have geographical restrictions, and they may not be available in certain regions or countries due to legal or compliance reasons.
- IP Restrictions: Your IP address might be from a location that is blocked or restricted from accessing specific Freshdesk pages or services.
- Limited Access Permissions: Your user 계정 or role might not have the necessary permissions to access the particular page you are trying to view.
- Page Unavailability: The page you are trying to access could be temporarily unavailable due to maintenance or other technical issues.
- Network or Firewall Restrictions: Your network or firewall 설정 could be preventing access to certain Freshdesk pages.To resolve the 문제:- Check Permissions: Ensure that your user 계정 has the appropriate permissions to access the page in question. If needed, contact your Freshdesk 계정 관리자 to verify and adjust your permissions.
- Verify Page Availability: Confirm if the page you are trying to access is indeed available and not undergoing maintenance or restricted for specific locations.
- Check Network 설정: If you are accessing Freshdesk from a workplace or public network, check if any network or firewall 설정 are blocking access to the page.
- Use a VPN: If the page is restricted in your current location, you can try using a virtual private network (VPN) to access Freshdesk from a different location.
- Contact Freshdesk 지원: It will be shown if your 계정 has the IP whitelisting feature enabled or if your IP has been blocked. If the 문제 persists, reach out to Freshdesk 지원 with your Public IP address for assistance. They can investigate the specific 오류 and provide further guidance to resolve the 문제.In case of the latter, please contact Freshdesk 지원 with your Public IP address and we would assist you further regarding this instance.

</details>

<details>
<summary><strong>the Remote 로그인 URL은 무엇인가요?</strong></summary>

While setting up an SSO, the users would have to 로그인 from a common 로그인 URL, to be authenticated using SSO. The Remote 로그인 URL is that URL to which your users would be redirected when they hit the 로그인 button on your 포털 after you have set up an SSO.You would have to update this field with the common 로그인 URL, while setting up SSO for your Freshdesk 계정.

</details>

<details>
<summary><strong>왜 am I getting the 'Invalid Time Stamp' 오류 when I try to 로그인 using an SSO인가요?</strong></summary>

You will be prompted with  **'Invalid Time Stamp**' 오류 when the difference between the UTC timestamp generated by your server and ours is more than 30 seconds. Ensuring that your servers stay in sync with the NTP server ([https://en.wikipedia.org/wiki/Network_Time_Protocol](https://en.wikipedia.org/wiki/Network_Time_Protocol)) will sort out this 문제.If you continue to face issues, kindly write to **지원@freshdesk.com** and one of our 상담원 will assist you further.

</details>

<details>
<summary><strong>왜 am I getting a '로그인 unsuccessful' 오류 on the AD SSO인가요?</strong></summary>

This 오류 message denoting authentication failure would be because of an 오류 in setting up the SSO. To analyse this, we would require the debug log. Please enter **?debug=1 **at the end of the URL that is generated, to retrieve the debug log**. **Also, please check the constructed URL after the 로그인, to see if the Hash is generated or not.If the 문제 persists, please send an 이메일 to [지원@freshdesk.com](mailto:지원@freshdesk.com).

</details>

<details>
<summary><strong>왜 are my 상담원 not able to 로그인 through AD SSO인가요?</strong></summary>

Please check if the agent who is logging in is using their 이메일 address which is part of the AD. Also, if they are a user on the AD, you would have to make sure if their user profile on the AD has permissions to use SSO. The 이메일 address from your AD is the parameter that Freshdesk checks while authenticating the 로그인, to locate their profile on Freshdesk.

</details>

<details>
<summary><strong>왜 are the names under my 상담원' profiles automatically changed every time they log in인가요?</strong></summary>

After every 로그인 with an SSO, Freshdesk will sync the name of the 상담원 with the names in your SSO database. Hence, the names in Freshdesk would automatically be updated.To fix this, please check how the names of the 상담원 are configured on your SSO database.Also, we 지원 UTF-8 encoded special characters only; so if the name contains any unsupported special characters, we would change it to the English equivalent.

</details>

<details>
<summary><strong>왜 are my 상담원 logged back in to the 포털 automatically after they log out인가요?</strong></summary>

This would be because of an incorrect **Remote Logout URL**.** **If you have entered the 로그인 page of the 포털 as the Remote Logout URL, please have that modified and give this another try.

</details>

<details>
<summary><strong>SSO is not working and getting the message 'Session expired. Please 로그인 again'</strong></summary>

We use the UTC timestamp to generate the hash for validation. Before we were allowing the hash to be valid for 30 minutes, but now we have updated it to be valid for 30 seconds alone. Please check if your SSO server is in sync with the UTC time.If your server is in sync, and you're still getting the session expired 오류, please drop an 이메일 to 지원@freshdesk.com.

</details>

<details>
<summary><strong>SSO 오류: 로그인 was unsuccessful! - Validation Failed : Invalid Signature on SAML Response</strong></summary>

This 오류 occurs when there is a mismatch in the signature.To extract the SHA signature from Google,- In the Google 관리자 console, navigate to Security > Set up single sign on and click on the download Certificate.
- Open the downloaded .pem extension file using notepad/sublime text editor.- Copy the certificate from the notepad/sublime text-editor and paste it in the X.509 certificate section in [https://www.samltool.com/fingerprint.php](https://www.samltool.com/fingerprint.php)- Make sure that you’ve selected SHA256 as the algorithm and click on calculate fingerprint.- Enter the key displayed in the formatted fingerprint text box in your Freshdesk 계정 under 관리자 > Security > SAML >Security Certificate Fingerprint > Save.

</details>

<details>
<summary><strong>There is a not secure message when accessing the system from Chrome</strong></summary>

If this is happening for your vanity URL, then you have to set up an SSL certificate for your custom domain.SSL options for custom domains are available from the Blossom 요금제. Please write to us at  **지원@freshdesk.com**,  and our 지원 팀 will help you in obtaining the SSL certificate..Once you receive the 이메일, please follow the instructions to confirm your request for an SSL certificate.Click [here](https://지원.freshdesk.com/en/지원/solutions/articles/90479-configuring-a-custom-ssl-certificate-for-your-지원-포털) to read more on Configuring a custom SSL certificate for your 지원 포털.

</details>

<details>
<summary><strong>계정을 취소하면 데이터는 언제 삭제되나요?</strong></summary>

When an 계정 is deleted, all associated data is destroyed within 14 days.

</details>

<details>
<summary><strong>Freshdesk 계정에 가입하는 방법</strong></summary>

To open or create a Freshdesk 계정, start with the free trial at [https://freshdesk.com/signup](https://freshdesk.com/signup)

</details>

<details>
<summary><strong>authenticate WordPress users to 로그인 to Freshdesk하는 방법은 무엇인가요?</strong></summary>

You can set up single sign-on for your WordPress users to easily log in to Freshdesk using the Freshdesk plugin for WordPress.You can use the plugin to enable your users to seamlessly and securely log in to Freshdesk. To do so, you first need to install the [Freshdesk WordPress plugin](https://wordpress.org/plugins/freshdesk-지원/). You can install the plugin from the plugins directory if your site runs on self-hosted WordPress. If you use WordPress.com, you need to be on the [Business 요금제 or above](https://wordpress.com/pricing/) to install this plugin.Click here to read a step-by-step guide on [authenticating WordPress users into your Freshdesk 계정](https://지원.freshdesk.com/en/지원/solutions/articles/50000001053) in more detail.

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
