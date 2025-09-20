---
sidebar_position: 1
---

# Analytics에서 승인 메트릭 리포팅

Freshservice Analytics에 '승인'이라는 새로운 모듈을 도입했습니다. 이제 티켓 및 변경과 관련된 승인 및 승인자에 대한 메트릭과 리포트를 생성할 수 있습니다.

:::info 주요 정보
- 이 기능을 사용하기 전에 필요한 권한과 설정을 확인하세요
- 단계별 접근을 통해 안정적으로 구현하는 것을 권장합니다
:::


Freshservice Analytics의 새로운 승인 모듈은 모든 승인에 소요되는 총 시간을 추적하고 개선하여 전체 승인 프로세스를 신속하게 처리할 수 있는 빠르고 쉬운 방법입니다. 이를 통해 티켓 해결 시간을 단축하고 서비스 데스크 메트릭을 개선할 수 있습니다.

승인 모듈에서 사용자는 다음 메트릭을 추적할 수 있습니다:

- 시스템의 총 승인 수
- 승인에 소요된 시간(캘린더 시간 기준 - 평균, 최소, 최대, 합계)
- 승인 대기 이후 경과 시간(캘린더 시간 기준 - 평균, 최소, 최대, 합계)

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50006286365/original/soBzGwjZdPeIgWg1Wvj13HqDd7XZy1EiwQ.png?1661775014" style={{ width: "296px", border: "1px solid #ccc" }} />

이러한 메트릭 외에도 승인 및 승인자와 관련된 많은 속성이 있으며, 사용자는 이를 필터 및 그룹화에 사용하여 다양한 수준에서 메트릭을 추적할 수 있습니다.

## 승인 위젯 생성 방법

승인 메트릭을 측정하고 추적하는 위젯을 생성하려면 다음과 같이 할 수 있습니다:

1. **메트릭을 추가하려는 리포트 페이지에서 편집을 클릭한 다음 +위젯 추가 옵션을 클릭합니다.**

2. **갤러리를 클릭하여 기존 템플릿에서 위젯을 선택하거나, 리포트 페이지의 처음부터 생성 옵션에서 차트를 끌어옵니다.**

3. **새 차트 위젯 옵션이 화면에 나타납니다.**

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50006286412/original/zO-_aX3JcejXfnsFpfdtB9OTkoFJfvv3GQ.png?1661775265" style={{ width: "377px", border: "1px solid #ccc" }} />

4. **확장 옵션을 클릭하여 위젯 구성 페이지를 엽니다.**

5. **제목 없는 위젯 옵션을 위젯 이름으로 바꿉니다.**

6. **위젯 페이지에서 메트릭을 검색하거나 메트릭 옵션을 스크롤하여 계산하려는 메트릭을 찾습니다.**

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50006286451/original/_EmiDyc_U_xVxHzCZkvvfM8U_jV5hIom2w.png?1661775543" style={{ width: "309px" }} />

7. **메트릭을 선택하고 심층 분석을 위한 필터 및 그룹화 옵션을 추가합니다.**

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50006286472/original/GGsCs-C0LShB5xwtgr_-K6LlE2C9CrBxgA.png?1661775652" style={{ width: "589px" }} />

8. **적용 및 저장을 클릭합니다.**

## 액세스 권한

에이전트가 Analytics에서 승인 데이터를 보려면 다음 조건 중 하나 이상이 충족되어야 합니다:

- 에이전트가 관련 티켓/변경을 볼 수 있는 액세스 권한이 있는 경우
- 에이전트가 승인의 승인자인 경우
- 에이전트가 승인의 위임자인 경우