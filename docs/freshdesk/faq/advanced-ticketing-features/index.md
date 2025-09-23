---
sidebar_position: 1
---

# 고급 티켓 기능 FAQ

고급 티켓 기능에서 자주 발생하는 질문들과 해결 방법을 정리했습니다. 각 질문을 클릭하여 상세한 답변을 확인하실 수 있습니다.

:::info 안내
이 FAQ는 실제 사용자들이 자주 묻는 질문들을 바탕으로 작성되었습니다. 추가 문의사항이 있으시면 고객지원팀에 문의해 주세요.
:::

<details>
<summary><strong>Can related 티켓 be unlinked ?</strong></summary>

Yes it is possible. 로 unlink 티켓 에서 Tracker, 이동하다 **Linked 티켓** 및 클릭하다**Unlink**. 이 permanently unlinks 티켓 에서 그 tracker 및 CANNOT be undone. ![이미지](https://s3.amazonaws.com/cdn.freshdesk.com/데이터/헬프데스크/attachments/production/50008082321/original/02y8OJhzp0wL5LyM2RIfLFT5optAT689JA.gif?1681213289)

</details>

<details>
<summary><strong>어떻게 로 create parent 및 child 티켓?</strong></summary>

You may open 티켓, 클릭하다 에서 ‘Add Child’ 및 선택하다 between "Using Template" 및 "New Child 티켓". original 티켓 will become parent 티켓 및 child 티켓 will be created as new 티켓. 이 기능 is available 에서 Estate 요금제 onwards 에서 Freshdesk.

</details>

<details>
<summary><strong>Is it possible 로 link 티켓 에서 Freshdesk?</strong></summary>

Yes, it is possible. 에 의해 using trackers ,티켓 can be linked 에서 Freshdesk.

</details>

<details>
<summary><strong>언제 does Shared Ownership come into play?</strong></summary>

언제 거기서 are multiple 상담원 involved 에서 single 티켓, we could make use 의 Shared Ownership. Whether it is 고객 facing 상담원 또는 internal 상담원, all are kept 에서 loop 에서 any action done within 티켓.

</details>

<details>
<summary><strong>어떻게 로 보다 all related 티켓 로 specific tracker?</strong></summary>

Yes, it would be possible 로 보다 all 티켓 linked 로 tracker. 여기서 are steps: Step 1: Filter 티켓 의 tracker type 에서 Association Type 필드. Step 2: 선택하다 tracker, one you wish 로 보다 all related 티켓. Step 3: 클릭하다 에서 X Related 티켓 에서 right hand side 의 페이지.list 의 all related 티켓 is shown.여기서 X= Number 의 related 티켓. However as 의 now, 이 정보 is not available as metrics 와 함께 보고서.

</details>

<details>
<summary><strong>Sample scenario 위해 Shared Ownership?</strong></summary>

티켓 comes 에서 e-commerce 회사 has issues relating 로 bug as well query regarding 기능. Query is solved 에 의해 고객 facing 상담원(기본 상담원). Bug is solved 에 의해 internal 상담원(Developer). Shared Ownership helps 에서 dynamically checking status 의 work 에서 single 티켓, keeping both 상담원 에서 loop.

</details>

<details>
<summary><strong>언제 can we close parent 티켓?</strong></summary>

Child 티켓 is essentially subdivision 의 Parent 티켓. Parent 티켓 can be closed only if all 의 its Child 티켓 are either Closed 또는 Resolved.

</details>

<details>
<summary><strong>어디서/어떻게 do you link 티켓 ?</strong></summary>

이동하다 **티켓 탭 > 클릭하다 에서 required 티켓 > Expand 'Linked 티켓' 패널 에서 extreme right > Create new tracker 또는 선택하다 로 link it 로 existing tracker.** 이 기능 is available only 에서 the**Pro/Garden 요금제**onwards 에서 Freshdesk. ![이미지](https://s3.amazonaws.com/cdn.freshdesk.com/데이터/헬프데스크/attachments/production/50008082368/original/NbcMcB7LAHSM3Bc9hCY_NBMtaVT-EFNgnQ.gif?1681213449) 클릭하다 [여기서](https://지원.freshdesk.com/지원/solutions/articles/224695-setting-up-linked-티켓) 로 know more about Linked 티켓.

</details>

<details>
<summary><strong>Can I filter 티켓 according 로 specific tracker ?</strong></summary>

No, it is not possible 로 do so. 에서 order 로 보다 all related 티켓 의 그 tracker, 이동하다 tracker itself 및 클릭하다 에서 related 티켓.

</details>

<details>
<summary><strong>어떻게 로 add multiple child 티켓 로 parent 티켓?</strong></summary>

After creating new child 티켓, 클릭하다 에서 ’Save 및 New Child’ 로 add new child. You could also 클릭하다 에서 "Add Child" option within Parent 티켓 로 create new child 티켓.

</details>

<details>
<summary><strong>어떻게 로 set up Shared Ownership?</strong></summary>

You would have 로 install Shared Ownership App 에서 your 계정 as shown 에서 이 [해결책 article](https://지원.freshdesk.com/지원/solutions/articles/224194-enabling-shared-ownership). After 이 is done, 거기서 are two steps involved. **1. Map internal groups 로 티켓 status:** 이동하다 **관리자 > Workflows > 티켓 필드** Excluding 4 basic statuses 의 티켓, map custom statuses 하위에서 Mapped Internal Groups. NOTE: Don't forget 로 include 고객 responded. **2. Set up automation rules 로 확인하다 everyone's 에서 loop:** 이동하다 **관리자 > Workflows > Automations > 티켓 updates > New rule** **Set up new automation rule as below:** **언제 action is performed 에 의해** Requester **Involves any 의 이것들 events** Reply IS sent **에서 티켓 와 함께 이것들 properties** Status is NOT > Open 또는 Waiting 에서 Third party 또는 Waiting 에서 Sellers 팀 **Perform 이것들 actions:** Set status as > OPEN 보내다 이메일 로 상담원 > Assigned 상담원

</details>

<details>
<summary><strong>어떻게 로 보다 all related 티켓?</strong></summary>

에서 티켓 list 페이지, 티켓 와 함께 separate tag 그 indicates **Tracker** is main tracker 티켓. Also, it is possible 로 filter all tracker 티켓 에서 헬프데스크. 이 can be done 에 의해 choosing **T****racker** 에서 the**Association Type dropdown 필드**. ![이미지](https://s3.amazonaws.com/cdn.freshdesk.com/데이터/헬프데스크/attachments/production/50008082570/original/Rb9R4PaBTlFEeLQ1oQA4s9HAb1OyQ7YtOA.png?1681214393) 로 보다 related 티켓, 이동하다 **티켓**>선택하다 the**Tracker 티켓** > 클릭하다 에서 **Related****티켓.** **![이미지](https://s3.amazonaws.com/cdn.freshdesk.com/데이터/헬프데스크/attachments/production/50008082503/original/eqhZkkU-mU63zvJidlVrWLevLlvnWMP90A.png?1681214101)**

</details>

<details>
<summary><strong>Can we 편집하다 related 티켓 widget ? i.e show more 세부정보 의 tracker?</strong></summary>

No it is not possible 로 show more 세부정보 의 tracker 에서 widget. 에서 order 로 get more 세부정보 의 tracker , 상담원 can 보다 it separately.

</details>

<details>
<summary><strong>어떻게 do i know is tracker 티켓 ?</strong></summary>

에서 티켓 list 페이지, 티켓 와 함께 separate tag 그 indicates **Tracker** is main tracker 티켓. Also, it is possible 로 filter all tracker 티켓 에서 헬프데스크. 이 can be done 에 의해 choosing **T****racker** 에서 the**Association Type dropdown 필드**. ![이미지](https://s3.amazonaws.com/cdn.freshdesk.com/데이터/헬프데스크/attachments/production/50008082570/original/Rb9R4PaBTlFEeLQ1oQA4s9HAb1OyQ7YtOA.png?1681214393)

</details>

<details>
<summary><strong>어떻게 do I 보다 all related 티켓?</strong></summary>

에서 티켓 탭, 티켓 having tag Related 티켓 are related/linked 로 티켓.

</details>

<details>
<summary><strong>어떻게 로 create templates 위해 child 티켓?</strong></summary>

하위에서 **관리자 > 상담원 Productivity > 티켓 Templates > New Template**, you could add new 티켓 template 및 선택하다 "Save 및 Add Child" 로 create template 위해 Parent 티켓. Once 이 is done, you would be able 로 add Child 티켓 Templates 하위에서 이 Parent 티켓 Template. 로 apply template 로 child 티켓 클릭하다 에서 ‘**Use existing template**’ while creating new child 티켓.

</details>

<details>
<summary><strong>어떻게 로 setup Shared Ownership 위해 existing 티켓?</strong></summary>

에서 티켓 세부정보 페이지 선택하다 및 업데이트하다 following: - Internal Groups - Internal 상담원

</details>

<details>
<summary><strong>Is Linked 티켓 tracker same as 그 의 time tracker ? Are they related ?</strong></summary>

No, both trackers are completely different. first one is used 로 link 티켓 creates separate tracker 티켓.Whereas latter is used 로 calculate amount 의 time spent 에서 particular 티켓.

</details>

<details>
<summary><strong>무엇 would be source 의 child 티켓?</strong></summary>

Since 티켓 is created 에 의해 상담원, source 의 티켓 would be 전화번호.

</details>

<details>
<summary><strong>Does Linked 티켓 Actions appear 에서 activities 탭?</strong></summary>

All activities 그 are carried out 와 함께 respect 로 티켓 are shown 에서 activities 탭. 에서 이 case, even 언제 티켓 are linked 로 tracker is shown 에서 activities 탭,

</details>

<details>
<summary><strong>어떻게 can I assign large number 의 groups 및 상담원 위해 Shared Ownership?</strong></summary>

거기서 are 2 ways 로 do it. - **Bulk Mode** 선택하다 necessary 티켓 로 perform bulk actions. - **Using Scenario Automation** Option 로 execute scenario is directly available 에서 drop down menu.

</details>

<details>
<summary><strong>어떻게 many child 티켓 can be added 로 parent 티켓?</strong></summary>

We can add maximum 의 50 child 티켓 로 parent 티켓.

</details>

<details>
<summary><strong>Is 거기서 bulk action 로 unlink multiple 티켓 at once ?</strong></summary>

No. It is only possible 로 unlink 티켓 에서 티켓 세부정보 페이지. Multiple unlinks are not available as 의 now.

</details>

<details>
<summary><strong>상담원 is able 로 보다 all related 티켓 하지만 not 보다 it separately? 왜 ?</strong></summary>

그 상담원 would be having restricted 또는 group 접근하다 및 hence related 티켓 are out 의 상담원's scope. 로 can give 상담원 접근하다 로 보다 티켓, - 이동하다 **관리자 > Teams > 상담원 > 편집하다 상담원** - Scroll down 로 Scope 및 편집하다 scope 의 상담원. ![이미지](https://s3.amazonaws.com/cdn.freshdesk.com/데이터/헬프데스크/attachments/production/50008160291/original/TIFYobjfeUFvt7PXfoX9aZ6tM0TfYTMC9Q.png?1681981895) Learn more about 상담원 scope [여기서](https://지원.freshdesk.com/en/지원/solutions/articles/50000002804).

</details>

<details>
<summary><strong>Can we delete tracker ? Even if 거기서 are 티켓 related 로 it ?</strong></summary>

Yes it is possible 로 delete tracker. - 이동하다 **Tracker.** - 클릭하다 에서 three dots 위해 **More options** 및 선택하다 **Delete.** - Once you delete tracker, its related 티켓 will be permanently unlinked **cannot** be restored. ![이미지](https://s3.amazonaws.com/cdn.freshdesk.com/데이터/헬프데스크/attachments/production/50008159545/original/Dbierwi181NTLNSV3Ysus6SYeV6hp0VLrg.png?1681978661)

</details>

<details>
<summary><strong>어떻게 로 create parent 티켓 ?</strong></summary>

**Quick guide 로 set up Parent Child Ticketing:** - Log 에서 로 your Freshdesk 포털 as 관리자. - 이동하다 **관리자****> 지원 Operations > Advanced Ticketing**. - Enable toggle 위해 **Parent-Child Ticketing**. **![이미지](https://s3.amazonaws.com/cdn.freshdesk.com/데이터/헬프데스크/attachments/production/50014611980/original/XDx7Ns6N2tFvlXc-c5htt4IBVbL1_fG2sA.png?1739862101)** Parent-Child Ticketing will now be enabled 에서 your 계정. 로 create parent-child relationship, add child 티켓 로 any existing 또는 new 티켓. ![이미지](https://s3.amazonaws.com/cdn.freshdesk.com/데이터/헬프데스크/attachments/production/50008218906/original/SVLN2BZviELr6OmdDO2_F324WlXPejTnkw.gif?1682592971)

</details>

<details>
<summary><strong>무엇 happens 언제 you delete parent 티켓?</strong></summary>

parent 티켓 will be deleted 및 associated child 티켓 will be unlinked 에서 parent 티켓.

</details>

<details>
<summary><strong>무엇 is use 의 Broadcast 버튼?</strong></summary>

와 함께 all related 티켓 linked 로 Tracker, 팀 working 에서 it can notify 상담원 에서 진행 상황 에 의해 using internal broadcast message. Once message is broadcasted 에서 Tracker 티켓, it would be relayed 에서 all related 티켓 automatically. 이 broadcast message would be visible only 로 상담원 에서 계정. - 로 broadcast internal message 로 상담원 are assigned 로 related 티켓, 클릭하다 에서 **Broadcast**. **참고:** Only 상담원 have 접근하다 로 Tracker 티켓 will be able 로 보내다 broadcast message. - 입력하다 message 및 클릭하다 Broadcast. message will be sent 로 all related 티켓 그 are linked 와 함께 Tracker. ![이미지](https://s3.amazonaws.com/cdn.freshdesk.com/데이터/헬프데스크/attachments/production/50008160392/original/dBoFEUUFs7c85TkDWLle35uhswqkX9ByaA.gif?1681982296) broadcast message will be added 로 any new 티켓 linked 로 Tracker. At any point 의 time, any related 티켓 will only have last broadcasted message. 그 is, if new message is broadcasted, it will replace existing message 와 함께 new one. 상담원 can include message 에서 their replies 에서 related 티켓 using **Insert 이 message into reply** option **참고:** 언제 message is broadcasted 에서 Tracker 티켓, hardcoded 이메일 notification will be sent 로 assigned 상담원 및 [watcher(s)](https://지원.freshdesk.com/지원/solutions/articles/37560-monitoring-important-티켓-에 의해-becoming-a-watcher-) added 에서 related 티켓.

</details>

<details>
<summary><strong>Does updating status 의 parent 티켓 affect child 티켓?</strong></summary>

No, changing status 의 parent 티켓 will not impact status 의 child 티켓. However, if you wish 로 achieve 이, you can utilize automation rule. 여기서 is sample automation rule summary -![이미지](https://s3.amazonaws.com/cdn.freshdesk.com/데이터/헬프데스크/attachments/production/50008678782/original/mY2_Ecv8_bs1P_gnr9kACXz4Tv4GJI_CxQ.png?1687347180)

</details>

<details>
<summary><strong>어떻게 many number 의 티켓 can be linked 로 tracker ?</strong></summary>

로 single tracker, maximum 의 300 티켓 can be linked 로 it.

</details>

<details>
<summary><strong>Is it possible 로 link multiple 티켓 at once?</strong></summary>

로 link multiple 티켓, we have 로 goto 티켓 세부정보 페이지 separately 의 each 티켓 및 link them individually 로 tracker. As 의 now 거기서 is no option 하위에서 Bulk Actions 로 carry out 이 function.

</details>

<details>
<summary><strong>무엇 happens 언제 you mark parent 티켓 as spam?</strong></summary>

child 티켓 associated 와 함께 parent 티켓 will be unlinked 및 changes cannot be restored. However, child 티켓 would not be marked as spam.

</details>

<details>
<summary><strong>Can we filter out 티켓 based 에서 parent 및 child 티켓?</strong></summary>

Yes, we can filter out 티켓 based 에서 parent 및 child 티켓. - 이동하다**티켓**. - 하위에서 **Filters section** 에서 left hand side, 클릭하다 에서 **Association Type**. - 선택하다 type 의 association as **Parent 또는 Child** 로 filter out corresponding 티켓. ![이미지](https://s3.amazonaws.com/cdn.freshdesk.com/데이터/헬프데스크/attachments/production/50008160690/original/YBx8VYi-VxUpEaAl6xWDWLTLKEgnAl-Y0A.png?1681983393)

</details>

<details>
<summary><strong>Is it possible 로 link 티켓 using automations ?</strong></summary>

No. 티켓 cannot be linked 로 trackers 에 의해 using any 의 four automations.

</details>

<details>
<summary><strong>Can linked 티켓 also be child/parent 티켓 ?</strong></summary>

No, 티켓 can be associated via trackers 또는 parent-child method, 하지만 not both.

</details>

<details>
<summary><strong>Can we filter out child 티켓 based 에서 parent 티켓?</strong></summary>

No, you cannot filter out child 티켓 based 에서 parent 티켓. However, you can 이동하다 parent 티켓 및 보다 child 티켓 associated 와 함께 it.

</details>

<details>
<summary><strong>무엇 are mandatory 필드 while creating new tracker?</strong></summary>

Two 필드 are mandatory while creating new tracker :1. **Requester 필드** - 상담원 creating tracker 티켓 is also requester.거기서 is option 위해 상담원 로 create tracker 하위에서 their 이름 또는 이름 의 one 의 their colleagues.![이미지](https://s3.amazonaws.com/cdn.freshdesk.com/데이터/헬프데스크/attachments/production/50008676240/original/cRimC_yjTCaTKLz6xk5iVs-ViH5EKrfgHg.png?1687336095)2. **Subject 필드** - 이 defines 이름/description 의 tracker.If 거기서 are any additional 필드 designated as mandatory 하위에서 관리자 > 티켓 필드 section, 그것들 필드 should also be filled 에서 로 create tracker.

</details>

<details>
<summary><strong>Is 거기서 way 로 disable 'link 로 tracker' option 위해 specific groups/상담원?</strong></summary>

다음을 할 수 있습니다 create custom role 및 manage **티켓** 접근하다 위해 상담원 assigned 로 role 하위에서 **Permissions.** 로 disable option 위해 상담원 로 link 티켓, - 이동하다 **관리자 > Teams > Roles** - Create **New Role**또는 클릭하다 **편집하다**next 로 existing custom role. - Scroll down 로 **Permissions.** - 하위에서 티켓 탭, uncheck box next 로 **Create linked 티켓.** ![이미지](https://s3.amazonaws.com/cdn.freshdesk.com/데이터/헬프데스크/attachments/production/50008160952/original/mJCRH2QV4LV1taceyTdzCWShoLGBd8EnmA.png?1681984502) 다음을 할 수 있습니다 now, assign 이 role 로 all 상담원 should not have 접근하다 로 create linked 티켓.

</details>

<details>
<summary><strong>Can 상담원 link 티켓 로 any tracker?</strong></summary>

상담원 can only link 티켓 로 tracker 그 are present 에서 his/her scope. So, if 상담원 has group/restricted 접근하다 he/she wont be able 로 보다 all trackers 그 are present 에서 헬프데스크.

</details>

<details>
<summary><strong>Would 상담원 와 함께 Restricted 접근하다 be able 로 보다 Shared Ownership 티켓?</strong></summary>

언제 상담원 has restricted 접근하다, still he would be able 로 보다 티켓 assigned 로 him as internal 상담원 even if he is not assigned 상담원 에서 티켓.

</details>

<details>
<summary><strong>Would 상담원 와 함께 Group 접근하다 be able 로 보다 Shared Ownership 티켓?</strong></summary>

언제 상담원 has group 접근하다, he will have 접근하다 로 티켓 have internal group assigned as 상담원’s group even though 티켓 belongs 로 different group.

</details>

<details>
<summary><strong>Can internal group 또는 상담원 be included 에서 automation rules?</strong></summary>

Internal groups 또는 상담원 can be set 에서 Conditions 및 Actions 에서 automation rules 그 run 에서 티켓 creation 또는 티켓 updates.

</details>

<details>
<summary><strong>Is it possible 로 trigger action using 티켓 업데이트하다 automation if Internal group is changed?</strong></summary>

Within 티켓 업데이트하다 automation rule, Internal group can be included 에서 Conditions 및 Actions sections, 하지만 it is not possible 로 trigger Event specifically 언제 internal group is changed.

</details>

<details>
<summary><strong>어떻게 do I enable Linked 티켓 기능 에서 my 계정?</strong></summary>

로 enable Linked 티켓, 이동하다 **관리자>지원 operation>Advanced ticketing>**toggle 에서**Linked 티켓** **![이미지](https://s3.amazonaws.com/cdn.freshdesk.com/데이터/헬프데스크/attachments/production/50008161191/original/gJ5yCAjOibRrFXCrBilcySKTavEOr2KxqA.png?1681985565)**

</details>

<details>
<summary><strong>Can I use template 로 create new 티켓?</strong></summary>

We understand 그 you might want 로 create 티켓 에서-the-go. Freshdesk allows you 로 create templates 에서 **관리자 > 상담원 Productivity > 티켓 Templates**. 이것들 templates can be used while creating 티켓 에서 **“선택하다 template”** option. [이](https://지원.freshdesk.com/지원/solutions/articles/220141-creating-및-using-티켓-templates) article will give you more 세부정보 에서 its usage.

</details>

<details>
<summary><strong>Can linked 티켓 be merged 와 함께 another 티켓?</strong></summary>

Yes, you can merge 티켓 로 티켓 linked 로 tracker.

</details>

<details>
<summary><strong>왜 am I not able 로 link 티켓 로 tracker?</strong></summary>

티켓 cannot be linked 로 tracker 언제 any 의 following is true : - 언제 **mandatory 또는 required 티켓 필드 are not filled** 에서 위해 티켓, 티켓 cannot be linked 로 tracker. 다음을 확인하십시오 all mandatory 티켓 필드 are filled 에서 위해 티켓 before linking it 로 tracker 티켓. - 언제 티켓 is **already associated 와 함께 parent 또는 child 티켓**, it will not be possible 로 link such 티켓 로 tracker. - 언제 티켓 is **merged 와 함께 another 티켓**. 기본 티켓 is closed will not have Linked 티켓 option. 에서 그것들 cases, please use secondary 티켓 위해 linking it 로 tracker.

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
