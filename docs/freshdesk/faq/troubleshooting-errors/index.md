---
sidebar_position: 1
---

# 문제 해결 및 오류 FAQ

문제 해결 및 오류에서 자주 발생하는 질문들과 해결 방법을 정리했습니다. 각 질문을 클릭하여 상세한 답변을 확인하실 수 있습니다.

:::info 안내
이 FAQ는 실제 사용자들이 자주 묻는 질문들을 바탕으로 작성되었습니다. 추가 문의사항이 있으시면 고객지원팀에 문의해 주세요.
:::

<details>
<summary><strong>What should I do 만약 I get 오류 message 에서 Freshdesk?</strong></summary>

만약 you get 오류 message while using Freshdesk, you will need 로 send us Console Logs 그리고 X-Request ID so that we can troubleshoot effectively. **로 access Console Logs:** 1. Right-클릭 에 page where 오류 appears. 2. 선택 Inspect ->Console. 3. Now perform action that you want 로 do. 4. Take screenshot 의 errors displayed 에서 console 그리고 send it 로 us 에서 [지원@freshdesk.com](mailto:지원@freshdesk.com). **로 access X-Request ID:** 1. Right-클릭 에 page where 오류 appears. 2. 선택 Inspect ->Network -> Preserve Log. 3. Now perform action that you want 로 do. 4. 에서 logs that appear, 클릭 에 오류 log that is highlighted 에서 red. 5. 에서 that 오류 logs 클릭 에 Fetch Headers-> Response Headers ->X-Request ID 그리고 send it 로 us 에서 [지원@freshdesk.com](mailto:지원@freshdesk.com). ![이미지](https://s3.amazonaws.com/cdn.freshdesk.com/데이터/헬프데스크/attachments/production/50001520299/original/1cUCs8RX6dW_QkO-7feiLKit90UJY72szQ.png?1596177050) *참고: Mention timeframe 의 언제 both 데이터 were captured.*

</details>

<details>
<summary><strong>My Freshdesk page is loading very slowly, what should I do?</strong></summary>

언제 Freshdesk page takes time 로 load, 또는 you experience timeout before performing certain tasks, try logging 에서 로 계정 via Incognito Window. 만약 문제 persists, we will need HAR file 로 troubleshoot effectively. HAR, short 위해 HTTP Archive format, tracks all logging 의 web browser’s interaction 와 함께 site. Here’s how you can easily generate HAR file using different browsers. - Chrome - Firefox - Safari **참고**: *HAR file includes 데이터 such as content 의 your cookies 그리고 pages you downloaded while making recording. Anyone 와 함께 access 로 HAR file can view 데이터 submitted while recording, which may include personal 데이터 또는 other sensitive 데이터. Make sure that you secure your HAR files accordingly. Cloudflare has released [HAR sanitizer](https://blog.cloudflare.com/introducing-har-sanitizer-secure-har-sharing/) that can be used 로 strip any sensitive information.* **로 generate HAR file 위해 Chrome:** - Open Google Chrome 그리고 go 로 page where you are experiencing trouble. - 에서 Chrome menu bar (![이미지](https://s3.amazonaws.com/cdn.freshdesk.com/데이터/헬프데스크/attachments/production/50001547328/original/YpBc-cGWv3SWR2ljZLqeaqs_j4lIjY8j6w.png?1596715273)) 선택 **More Tools > Developer Tools**. - 선택 **Network**. - Make sure that Record button ( ![이미지](https://s3.amazonaws.com/cdn.freshdesk.com/데이터/헬프데스크/attachments/production/50001547326/original/ztHnRRiT4d8pVPpG36NR7-kUxEzZURn6Gg.png?1596715273) ) 에 upper left corner 의 tab is red. 만약 it is grey, 클릭 에 it 로 start recording. - 확인하다 **Preserve log** box. - 클릭 Clear button ( ![이미지](https://s3.amazonaws.com/cdn.freshdesk.com/데이터/헬프데스크/attachments/production/50001547327/original/0Kr5vWOkODOebaqKrN-ocNTDXmPCjmS7Sw.png?1596715273) ) 로 clear any existing logs 에서 Network tab. - Reproduce 문제 that you were experiencing before. - Once you have reproduced 문제, right-클릭 anywhere 에 grid 의 network requests, 선택 **저장 as HAR 와 함께 Content**, 그리고 저장 file 에 your computer. - Send HAR file 로 us 에서 **지원@freshdesk.com**. **로 generate HAR file 위해 Firefox:** - Open Firefox 그리고 go 로 page where you are experiencing trouble. - 선택 Firefox menu (three horizontal parallel lines) 에서 top-right 의 your browser window, 그러면 선택 **Web Developer > Network**. - Developer Network Tools opens as docked panel 에서 side 또는 bottom 의 Firefox. 클릭 **Network** tab. - recording autostarts 언제 you start performing actions 에서 browser. - Once you have reproduced 문제 그리고 you see that all 의 actions have been generated 에서 Developer Network Panel (should just take few seconds), right-클릭 anywhere under **File** 열, 그리고 클릭 에 **저장 all as Har**. - 저장 HAR file 에 your computer. - Write 로 us 에서 **지원@freshdesk.com** along 와 함께 HAR file. **로 generate HAR file 위해 Safari:** Before generating HAR file, make sure you can see **Develop** menu 에서 Safari. 만약 it is not there, follow instructions under Use developer tools 에서 Develop menu 에서 Safari 에 Mac. - Open **Develop** menu 그리고 선택 **Show Web Inspector**. - 클릭 **Network** tab 그리고 complete activity that is causing issues. - 클릭 **내보내기** icon 에 far right 의 network tab 그리고 저장 HAR file. - Write 로 us 에서 **지원@freshdesk.com** along 와 함께 HAR file.

</details>

<details>
<summary><strong>I am facing latency 문제 와 함께 Freshdesk 그리고 it is not loading은 무엇인가요?</strong></summary>

언제 Freshdesk page takes time 로 load, 또는 만약 there is timeout before performing certain tasks, try logging 에서 로 계정 via Incognito Window. 만약 문제 persists, we will need traceroute results 로 diagnose 문제. Here is how you can fetch traceroute results. Write 로 us 에서 **지원@freshdesk.com** along 와 함께 traceroute 데이터.

</details>

<details>
<summary><strong>Steps 로 Clear Local 그리고 Browser DNS cache은 무엇인가요?</strong></summary>

**Steps 로 clear Browser DNS Cache (Browser 특정한):** **Chrome:** - Launch chrome browser - 입력 참고 자료: ***chrome://net-internals/#dns*********에서 address bar, 그러면 press 입력. - 클릭 에 ***Clear host cache*** button - Chrome Browser DNS cache will be cleared **Opera:** - Launch Opera 에 your Computer - 입력 참고 자료: ***opera://net-internals/#dns*** 에서 address bar, 그러면 press 입력. - You’ll be taken 로 DNS section 의 Opera’s internal 설정 page. - 클릭 button labelled ***Clear Host Cache*** 로 flush DNS cache. - Open new tab, 그러면 입력 에서 address 참고 자료: ***opera://net-internals/#sockets*** 그리고 press 입력. - You’ll be taken 로 section 의 Opera’s internal 설정 page 위해 cached socket pools. - Now 클릭 button labelled ***Flush Socket Pools***. - Now restart Opera browser. **Firefox:** - Launch Firefox 에 your Computer. - 에서 address bar, 입력 ***about:config***그리고 press 입력. - 클릭 *“I accept risk!”* 에 경고 page. - Use search 필드 에서 top 로 search 위해 ***network.dnsCacheExpiration***. - Your search should return two variables, named ***network.dnsCacheExpiration***그리고***network.dnsCacheExpirationGracePeriod*.** - Double-클릭 에 each variable’s value part so you can 편집 it, 그러면 change value 에서 기본값 ***60 로 0***, which will prompt Firefox 로 immediately clear out its DNS cache. - After doing this, now set both variables back 로 ***60***. - Now restart Firefox browser. **Steps 로 clear Local DNS cache (OS 특정한):** **Windows OS:** - Search 위해 ***command prompt*** 에서 start menu - Right-클릭 그리고 선택 "Run as 관리자" - 입력 command ipconfig /flushdns - 만약 command succeeds, you will receive following message “*Successfully flushed DNS Resolver Cache.*" **Mac OS:** - Open your command line interface 또는 Terminal - 입력 below command sudo killall -HUP mDNSResponder - You may need 로 입력 your 관리자 비밀번호 - 만약 command succeeds system will not return any output.

</details>

<details>
<summary><strong>사용자 정의 domain failure due 로 Geoblocking은 무엇인가요?</strong></summary>

Freshworks uses LetsEncrypt as its Certificate Authority Authorization (CAA) 로 get certificates 위해 사용자 정의 domains. 에서 March 2024, CAA updated its validation process 로 확인하다 domain ownership. - Previously, they sent 3 validation calls 에서 singular region. - Now, they send 5 validation calls 에서 다수의 regions. [This is more secure process](https://community.letsencrypt.org/t/lets-encrypt-is-adding-two-new-remote-perspectives-위해-domain-validation/214123). However, 만약 you use geoblocking 또는 have firewall rules 로 block requests 에서 unknown regions, new process may cause your certificate validation 로 fail. 로 fix this 문제: - (Preferred) Allow all traffic 에 **HTTP/TCP Port 80** 위해 request path **/.well-known/acme-challenge/** 에서 all regions. - (Alternative) Avoid Geoblocking 그리고 Firewall rules based 에 특정한 regions. - (Unfeasible) [DNS-01 challenge](https://letsencrypt.org/docs/challenge-types/#dns-01-challenge) is another alternative approach. However, 수동 intervention is inherently 필수 위해 every certificate procurement. [Learn more 에서 CAA.](https://community.letsencrypt.org/t/multi-perspective-validation-geoblocking-faq/218158)

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
