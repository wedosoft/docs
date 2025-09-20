---
sidebar_position: 16
---

# Analytics에서 Tableau로 데이터 내보내기

Freshservice의 Analytics 모듈을 사용하여 서비스 데스크의 직관적인 리포트를 생성할 수 있습니다.

:::info Tableau 통합 활용
Tableau와 Freshservice를 통합하면 실행 가능한 인사이트를 사용하여 비즈니스 성과를 이끄는 광범위한 대시보드와 리포트로 분석을 확장할 수 있습니다.
:::

## Analytics에서 내보내기를 예약하는 방법

### 데이터 내보내기를 예약하려면:

1. **왼쪽 사이드바에서 Analytics를 클릭합니다.**

2. **상단 오른쪽 모서리의 설정 아이콘** <img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50006284854/original/m_iFCyxeM38St8cNXdgJxCjvhs0gUSUVYg.png?1661765075" style={{ width: "auto" }} className="fr-fic fr-dii" /> **을 클릭하고 데이터 내보내기를 선택합니다.**

3. **상단 오른쪽 모서리의 내보내기 생성을 클릭하여 데이터 내보내기를 예약합니다.**

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50013908493/original/jyaAFUB0U-BnTkdWM4JZqzF1-YhjDCq9yw.jpeg?1733225931" style={{ width: "621px", display: "block", margin: "0 auto" }} />

4. **내보내기 이름과 모듈 이름을 추가합니다. 변경 모듈에 대한 데이터 내보내기를 예약하려는 경우, 모듈 이름에서 변경을 선택합니다.**

5. **예약 간격을 선택합니다. 시간별, 일별, 주별 또는 월별로 설정할 수 있습니다.**

6. **뷰와 기본 필터 옵션을 사용하여 내보내려는 데이터를 필터링합니다.**

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50006284933/original/64WjnHKu0_CBmslkbup_0H_44XHuqCiQ1g.png?1661765436" style={{ width: "644px", display: "block", margin: "10px auto" }} />

**내보낼 필드를 선택할 수 있습니다.**

7. **이메일 또는 API 링크로 내보내기를 받을지 선택합니다. API URL은 내보내기 파일의 링크를 보유합니다. API URL을 BI 도구에 제공하면 Freshservice에서 자동으로 데이터를 가져올 수 있습니다.**

8. **완료되면 저장을 클릭합니다.**

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50006284965/original/eU__A1mF-EgM2jV_4jTdY9BwDRcdwNHJ_w.png?1661765542" style={{ width: "670px", display: "block", margin: "10px auto" }} />

## Tableau와 Freshservice Analytics를 통합하는 방법

**단계 1:** Freshservice의 Analytics 모듈에서 내보내기 파일의 링크를 보유하는 API URL을 복사합니다.

**단계 2:** Tableau Desktop에 로그인하고 **웹 데이터 커넥터**를 클릭합니다. 웹 데이터 커넥터 URL을 붙여넣기: [https://fsbots.freshservice.com/tableau_bridge](https://fsbots.freshservice.com/tableau_bridge)

<div style={{ textAlign: "center" }}>
<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50001982890/original/1sAzlAqa1ojCSregbT6jQsLvldOBcHW1Bg.png?1604414688" width="624" height="391" />
</div>

**단계 3:** 사용자 이름 필드에 **FS 사용자의 API 키**를 입력하고(비밀번호는 비워둠), **URL** 필드에 Freshservice 데이터 내보내기 API URL을 붙여넣고 **제출**을 클릭합니다.

<div style={{ textAlign: "center" }}>
<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50001982892/original/ESNwntV8srqeS9ltKPizpEbdXc5VcN4_gg.png?1604414689" width="624" height="391" />
</div>

**단계 4:** 이제 Freshservice 데이터 내보내기 파일을 받게 됩니다. 이 파일을 데이터 소스로 사용하여 Tableau Desktop에서 리포트를 작성할 수 있습니다.

<div style={{ textAlign: "center" }}>
<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50001982891/original/rMoexBBHqTRhlJVffguhQSPTmf9z8_0K_A.png?1604414689" width="624" height="391" />
</div>

**단계 5:** Tableau에서 Freshservice 데이터를 새로 고치려면 이 데이터 소스를 Tableau Online 인스턴스에 게시해야 합니다. 서버 → 서버에 게시 → Tableau Online 인스턴스 선택을 클릭합니다.

<div style={{ textAlign: "center" }}>
<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50001982883/original/WHu6eNtXON-5QrSib9vedlSvMkZIWBmzdw.png?1604414688" width="624" height="391" />
</div>

**단계 6:** 프로젝트 이름, 제목 및 데이터 소스 설명을 제공합니다. 인증 → '포함된 비밀번호' 선택 후 게시를 클릭합니다.

<div style={{ textAlign: "center" }}>
<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50001982885/original/Xbp4xXdgOeQut011X0mvImlr4wH1cK_4uw.png?1604414688" width="624" height="391" />
</div>

데이터 소스가 이제 Tableau Online 인스턴스에 게시되었습니다.

**단계 7:** Tableau Online 인스턴스에 로그인하고 데이터 소스를 선택합니다. (탐색 → 프로젝트 선택 → 데이터 소스 선택)

<div style={{ textAlign: "center" }}>
<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50001982887/original/oSnW8jngNXrewE1ADc2MacpnZsQZe012lQ.png?1604414688" width="624" height="391" />
</div>

**단계 8:** 새 통합 문서를 클릭합니다.

**단계 9:** 필드를 끌어서 놓아 Freshservice 데이터의 시각화를 생성합니다.

<div style={{ textAlign: "center" }}>
<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50001982886/original/do0ik_tQFPT5jZ6xWXPo9frH7DCA6nOSlA.png?1604414688" width="624" height="391" />
</div>

## Tableau에서 데이터 소스 새로 고침 예약

**단계 1:** Tableau Online 인스턴스에 로그인하고 새로 고침을 예약할 데이터 소스를 선택합니다. 추출 새로 고침 → 새 추출 새로 고침을 클릭합니다.

<div style={{ textAlign: "center" }}>
<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50001982882/original/MWLXERj5aX4wGPqzcPGVkXHKBT2s2eQnzg.png?1604414687" width="624" height="391" />
</div>

**단계 2:** 추출 새로 고침 예약 대화상자에서 브리지(레거시)를 선택합니다.

**단계 3:** 브리지 클라이언트가 설치된 컴퓨터를 선택하고, 새로 고침 빈도를 구성한 후 새로 고침 예약을 클릭합니다.

<div style={{ textAlign: "center" }}>
<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50001982888/original/7zigpoNGU6uI993Kl292JgLo_FYabI7mFA.png?1604414688" width="624" height="391" />
</div>

<div style={{ textAlign: "center" }}>
<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50001982889/original/EFYYZPA64rl9mmCpbp5BAFurWNb_TiO2NA.png?1604414688" width="624" height="391" />
</div>