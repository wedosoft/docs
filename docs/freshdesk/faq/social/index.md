---
sidebar_position: 1
---

# 소셜 미디어 FAQ

소셜 미디어에서 자주 발생하는 질문들과 해결 방법을 정리했습니다. 각 섹션별로 구분하여 필요한 정보를 빠르게 찾을 수 있습니다.

:::info 안내
이 FAQ는 실제 사용자들이 자주 묻는 질문들을 바탕으로 작성되었습니다. 추가 문의사항이 있으시면 고객지원팀에 문의해 주세요.
:::


## 📋 일반 질문

<details>
<summary><strong>Are Facebook posts real-time?</strong></summary>

Yes, Facebook posts are real-time. If you have v2 of the Facebook integration enabled, direct messages will be real-time as well.

</details>

<details>
<summary><strong>Why am I not able to associate my Facebook page with Freshdesk?</strong></summary>

The authorization can run into trouble under the following scenarios:- When you are trying to authorize from your custom/vanity URL. Please try the authorization after logging into your Account using Freshdesk URL, which would go by YourCompanyName.freshdesk.com.- If you have SSO enabled, please try logging in using your Freshdesk credentials after bypassing your SSO, using the URL - YourCompanyName.freshdesk.com/login/normal.
- Please ensure if you are not logged into another Facebook account on your browser at the same time. The Facebook account which you are logged into would have to be an Admin of the Facebook page.- There could also be several reasons why you are unable to associate your Facebook page with Freshdesk. Here are some possible reasons and solutions:[](https://support.freshdesk.com/en/support/solutions/articles/37557-integrating-a-facebook-page-with-your-helpdesk)
- [You need to be an **Admin** of the Facebook page you are trying to integrat](https://support.freshdesk.com/en/support/solutions/articles/37557-integrating-a-facebook-page-with-your-helpdesk)e[](https://support.freshdesk.com/en/support/solutions/articles/37557-integrating-a-facebook-page-with-your-helpdesk). Please ensure that you have the necessary permissions.[](https://support.freshdesk.com/en/support/solutions/articles/37557-integrating-a-facebook-page-with-your-helpdesk)
-
[You cannot add pages that are already integrated with another Freshdesk accoun](https://support.freshdesk.com/en/support/solutions/articles/37557-integrating-a-facebook-page-with-your-helpdesk)t[](https://support.freshdesk.com/en/support/solutions/articles/37557-integrating-a-facebook-page-with-your-helpdesk). Please ensure that the page you are trying to integrate is not already associated with another Freshdesk account.-
[Sometimes, when page settings change, you may have to reauthorize the Facebook pag](https://support.freshdesk.com/en/support/solutions/articles/37557-integrating-a-facebook-page-with-your-helpdesk)e.[](https://support.freshdesk.com/en/support/solutions/articles/37557-integrating-a-facebook-page-with-your-helpdesk) Please try reauthorizing the Facebook page if you are facing issues.

</details>

<details>
<summary><strong>Why are my company's posts not being converted to tickets, even though I've selected that option?</strong></summary>

Company posts would only be converted to tickets only when an end user/customer adds a comment to the post on Facebook. The post in itself will not be immediately converted.When the post is eventually converted after a user comment, the original post is also brought-in along with the ticket inside Freshdesk.

</details>

<details>
<summary><strong>How can we choose between replying to a comment and replying to a post on Facebook?</strong></summary>

You can either reply to the post or reply to a particular comment from Freshdesk.To reply to the post, you would have to use the **"Reply"** button at the top or bottom of the ticket.To reply to a particular comment, hover over the comment and click the reply icon to the right of the yellow space.

</details>

<details>
<summary><strong>Why is the reply option not available on a few tickets created from Facebook?</strong></summary>

If a Facebook page is removed from Freshdesk, all the tickets which were created from that Facebook page will lose connection to that page. For those tickets, the **"Reply"** button would not appear, so agents will not be able to reply to that ticket anymore.

</details>

<details>
<summary><strong>Why aren't replies to direct messages from Facebook reflected in Freshdesk?</strong></summary>

If you have enabled v2 of the Facebook integration which ensures that the messages are converted to tickets in real time.To change your Facebook integration to v2, please send an email to support@freshdesk.com and we'll have this fixed.

</details>

<details>
<summary><strong>Is it possible to differentiate between Direct Messages and Posts from Facebook?</strong></summary>

Yes, it is possible to differentiate between a Facebook direct message and a Facebook post in Freshdesk. Unlike a ticket created via a Facebook post, **a lock next to the Facebook icon** will be present for a ticket created from a direct message in the ticket details page.However, it is not possible to differentiate between direct messages and posts from the List View in the Tickets tab.

</details>

<details>
<summary><strong>Is it possible to convert only those posts from Facebook which have certain hashtags?</strong></summary>

With the Facebook integration, all visitor posts will be converted to tickets automatically once the page is connected with the Freshdesk account. However, for comments on posts, you can configure filters and/or keywords to filter posts and convert them to tickets.This can be done under **관리자 -> Channels -> Facebook -> Edit **and by choosing the option **Convert only relevant posts**.

</details>

<details>
<summary><strong>Why am I not able to send replies to Facebook DMs from Freshdesk?</strong></summary>

Facebook has recently introduced a messaging policy which does not allow apps to send messages to customers 24 hours after they have messaged a page.For example, if a customer messages a page on 8th March 2020 at 5:00 PM, they have until 5:00 PM 9th March 2020 to respond. After this window, they cannot send a response. Please note that this is a rolling window. If the customer sends another message at 5:30 PM, they have until 5:30 PM the next day to respond.This change is in line with people’s expectations of faster responses from businesses. Please refer to Facebook's article for [more details around this policy](https://developers.facebook.com/docs/messenger-platform/policy/policy-overview#new_policy).We've incorporated the **closed beta API for Facebook direct messages in Freshdesk. **So now, you will be able to respond to direct messages within a **21-day window till July 15th**, considering COVID-19 post which the window would be cut short to 7 days.Also, there are other ways of coping up with this situation further.You can collect their customer's contact details (email address or phone number) with an automated message. This automated message can be fired in two ways.**1. Directly from Facebook.**If you have very few Facebook pages, you can set up an automated message to collect customer details from this specific section![Image](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50001222086/original/Z1PxG8oRGVQLhqGxHcOPCmNS7VsvmnBmYg.png?1591702091)**2. Using API**
If you have multiple Facebook pages integrated with your Freshdesk and have separate groups that handle just DM tickets, you can use webhooks to send an automatic reply. This requires the addition of a new feature from our end. Please reach out to us at [support@freshdesk.com](http://support@freshdesk.com) if you would like to get this feature enabled.

</details>

<details>
<summary><strong>Discontinuation of Twitter services on Freshdesk</strong></summary>

Freshdesk Twitter services are discontinued.Freshworks uses Twitter APIs to power tweets and DMs in Freshdesk. Over the past few weeks, Twitter has made a number of changes to its API and access tiers and recently revoked our access to Twitter. We have been engaging with Twitter to see how we can continue extending support; however, we have ultimately come to the decision that it will not be feasible due to the prohibitive cost involved and uncertainty around Twitter APIs for commercial offering.With this update, you can no longer use Twitter as a channel within Freshdesk to reply to tweets and DMs. Twitter services are completely discontinued, and we encourage you to use our alternative channels, like Facebook or WhatsApp, to continue engaging with your customers on social media platforms.We understand that this news may be disappointing. However, we hope our alternative solutions will help you continue engaging your customers effectively.We regret the inconvenience caused. Please write to us at [support@freshdesk.com](mailto:support@freshdesk.com) if you have any questions.

</details>


## 📋 사용자 관리

<details>
<summary><strong>Why are Agent signatures not present while replying to Social tickets even though they have been configured?</strong></summary>

The agent signatures will not be present when replying to a Facebook post because the replies will go from the support handle and not the agents'. Similarly, the ticket links will not be present either.

</details>

<details>
<summary><strong>Why are replies sent via an agent's mailbox not being added in Facebook?</strong></summary>

For Facebook tickets, it is mandatory that the agents are logged into the portal and that they reply from the portal as well. This ensures that the reply is sent as a message to the customer. When an agent replies from the mailbox, it will only add a public note in the ticket and this won't be reflected in Facebook.

</details>


## 📋 계정 및 관리

<details>
<summary><strong>I need to add more than one social media accounts on Freshdesk</strong></summary>

From the Blossom plan you will have the option to add multiple Facebook pages with Freshdesk. However, in the Sprout plan you will only have an option to add one page.

</details>

<details>
<summary><strong>I can't add my facebook to Freshdesk, it says it is still paired to a deleted account.</strong></summary>

In general, a facebook page or an account can be added only to one specific Freshdesk account. In case you have linked the same Facebook account to another Freshdesk account, please unlink the facebook page from that account and activate it in the current account.

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
