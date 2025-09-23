---
sidebar_position: 1
---

# 문제 해결 및 오류 FAQ

문제 해결 및 오류에서 자주 발생하는 질문들과 해결 방법을 정리했습니다. 각 섹션별로 구분하여 필요한 정보를 빠르게 찾을 수 있습니다.

:::info 안내
이 FAQ는 실제 사용자들이 자주 묻는 질문들을 바탕으로 작성되었습니다. 추가 문의사항이 있으시면 고객지원팀에 문의해 주세요.
:::


## 📋 문제 해결

<details>
<summary><strong>What should I do if I get an error message in Freshdesk?</strong></summary>

If you get an error message while using Freshdesk, you will need to send us the Console Logs and X-Request ID so that we can troubleshoot effectively.**To access Console Logs: **1. Right-click on the page where the error appears.2. Choose Inspect ->Console.3. Now perform the action that you want to do.4. Take a screenshot of the errors displayed in the console and send it to us at [support@freshdesk.com](mailto:support@freshdesk.com).**To access X-Request ID: **
1. Right-click on the page where the error appears.2. Choose Inspect ->Network -> Preserve Log.3. Now perform the action that you want to do.4. In the logs that appear, click on the error log that is highlighted in red.5. In that error logs click on Fetch Headers-> Response Headers ->X-Request ID and send it to us at [support@freshdesk.com](mailto:support@freshdesk.com).![Image](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50001520299/original/1cUCs8RX6dW_QkO-7feiLKit90UJY72szQ.png?1596177050)*참고: Mention the timeframe of when both the data were captured.*

</details>


## 📋 일반 질문

<details>
<summary><strong>My Freshdesk page is loading very slowly, what should I do?</strong></summary>

When a Freshdesk page takes time to load, or you experience a timeout before performing certain tasks, try logging in to the account via an Incognito Window.If the issue persists, we will need the HAR file to troubleshoot effectively.HAR, short for HTTP Archive format, tracks all the logging of a web browser’s interaction with a site.Here’s how you can easily generate a HAR file using different browsers.-
Chrome-
Firefox-
Safari**Note**: *A HAR file includes data such as the content of your cookies and the pages you downloaded while making the recording. Anyone with access to the HAR file can view the data submitted while recording, which may include personal data or other sensitive data. Make sure that you secure your HAR files accordingly. Cloudflare has released a [HAR sanitizer](https://blog.cloudflare.com/introducing-har-sanitizer-secure-har-sharing/) that can be used to strip any sensitive information. ***To generate the HAR file for Chrome:**-
Open Google Chrome and go to the page where you are experiencing trouble.-
From the Chrome menu bar (![Image](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50001547328/original/YpBc-cGWv3SWR2ljZLqeaqs_j4lIjY8j6w.png?1596715273)) select **More Tools > Developer Tools**.-
Select **Network**.-
Make sure that the Record button ( ![Image](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50001547326/original/ztHnRRiT4d8pVPpG36NR7-kUxEzZURn6Gg.png?1596715273) ) on the upper left corner of the tab is red. If it is grey, click on it to start recording.-
Check the **Preserve log** box.-
Click the Clear button ( ![Image](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50001547327/original/0Kr5vWOkODOebaqKrN-ocNTDXmPCjmS7Sw.png?1596715273) ) to clear any existing logs from the Network tab.-
Reproduce the issue that you were experiencing before.-
Once you have reproduced the issue, right-click anywhere on the grid of network requests, select **Save as HAR with Content**, and save the file on your computer.-
Send the HAR file to us at **support@freshdesk.com**.**To generate the HAR file for Firefox:**-
Open Firefox and go to the page where you are experiencing trouble.-
Select the Firefox menu (three horizontal parallel lines) at the top-right of your browser window, then select **Web Developer > Network**.-
The Developer Network Tools opens as a docked panel at the side or bottom of Firefox. Click the **Network** tab.-
The recording autostarts when you start performing actions in the browser.-
Once you have reproduced the issue and you see that all of the actions have been generated in the Developer Network Panel (should just take a few seconds), right-click anywhere under the **File** column, and click on **Save all as Har**.-
Save the HAR file on your computer.-
Write to us at **support@freshdesk.com** along with the HAR file.**To generate the HAR file for Safari:**Before generating the HAR file, make sure you can see the **Develop** menu in Safari. If it is not there, follow the instructions under Use the developer tools in the Develop menu in Safari on Mac.-
Open the **Develop** menu and select **Show Web Inspector**.-
Click the **Network** tab and complete the activity that is causing issues.-
Click the **Export** icon on the far right of the network tab and save the HAR file.-
Write to us at **support@freshdesk.com** along with the HAR file.

</details>

<details>
<summary><strong>I am facing a latency issue with Freshdesk and it is not loading</strong></summary>

When a Freshdesk page takes time to load, or if there is a timeout before performing certain tasks, try logging in to the account via an Incognito Window.If the issue persists, we will need the traceroute results to diagnose the problem.Here is how you can fetch the traceroute results. Write to us at **support@freshdesk.com** along with the traceroute data.

</details>

<details>
<summary><strong>Steps to Clear Local and Browser DNS cache</strong></summary>

**Steps to clear the Browser DNS Cache (Browser Specific):****Chrome:**
- Launch chrome browser
- Type ***chrome://net-internals/#dns****** ***in the address bar, then press Enter.
- Click on ***Clear host cache*** button
- Chrome Browser DNS cache will be cleared**Opera:**
- Launch Opera on your Computer
- Type ***opera://net-internals/#dns*** in the address bar, then press Enter.
- You’ll be taken to the DNS section of Opera’s internal settings page.
- Click the button labelled ***Clear Host Cache*** to flush the DNS cache.
- Open a new tab, then type in the address ***opera://net-internals/#sockets*** and press Enter.
- You’ll be taken to the section of Opera’s internal settings page for cached socket pools.
- Now click the button labelled ***Flush Socket Pools***.
- Now restart Opera browser.**Firefox:**
- Launch Firefox on your Computer.
- In the address bar, type ***about:config* **and press Enter.
- Click *“I accept the risk!”* on a warning page.
- Use the search field at the top to search for ***network.dnsCacheExpiration***.
- Your search should return two variables, named ***network.dnsCacheExpiration* **and** *network.dnsCacheExpirationGracePeriod*. **
- Double-click on each variable’s value part so you can edit it, then change the value from the default ***60 to 0***, which will prompt Firefox to immediately clear out its DNS cache.
- After doing this, now set both variables back to ***60***.
- Now restart the Firefox browser.**Steps to clear the Local DNS cache (OS Specific):**
**Windows OS:**
- Search for ***command prompt*** in start menu
- Right-click and Select "Run as administrator"
- Type the command
ipconfig /flushdns
- If the command succeeds, you will receive the following message “*Successfully flushed the DNS Resolver Cache.*"**Mac OS:**
- Open your command line interface or Terminal
- Type the below commandsudo killall -HUP mDNSResponder- You may need to enter your administrator password
- If the command succeeds the system will not return any output.

</details>

<details>
<summary><strong>Custom domain failure due to Geoblocking</strong></summary>

Freshworks uses LetsEncrypt as its Certificate Authority Authorization (CAA) to get certificates for custom domains.In March 2024, the CAA updated its validation process to verify domain ownership.- Previously, they sent 3 validation calls from a singular region.
- Now, they send 5 validation calls from multiple regions. [This is a more secure process](https://community.letsencrypt.org/t/lets-encrypt-is-adding-two-new-remote-perspectives-for-domain-validation/214123).However, if you use geoblocking or have firewall rules to block requests from unknown regions, the new process may cause your certificate validation to fail. To fix this issue:- (Preferred) Allow all traffic on **HTTP/TCP Port 80** for request path **/.well-known/acme-challenge/** from all regions.
- (Alternative) Avoid Geoblocking and Firewall rules based on specific regions.
- (Unfeasible) The [DNS-01 challenge](https://letsencrypt.org/docs/challenge-types/#dns-01-challenge) is another alternative approach. However, manual intervention is inherently required for every certificate procurement.[Learn more from the CAA.](https://community.letsencrypt.org/t/multi-perspective-validation-geoblocking-faq/218158)

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
