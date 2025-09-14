# Liquid 필터를 활용한 강력한 플레이스홀더

Liquid 필터는 웹 애플리케이션에서 사용자가 서버에서 안전하지 않은 코드를 실행하지 않고 애플리케이션의 외관을 편집할 수 있도록 하는 안전하고 고객 대면 템플릿 언어입니다. Liquid는 Liquid 템플릿 파일 내에서 태그, 객체 및 필터의 조합을 사용하여 동적 콘텐츠를 로드합니다.

## Freshservice의 Liquid 필터

Freshservice의 liquid 필터를 사용하면 사용되는 타사 웹 애플리케이션의 요구 사항에 따라 노트, 웹훅, 앱 액션, 이메일 등과 같은 워크플로우 자동화의 플레이스홀더 값을 사용자 정의할 수 있습니다.

이를 통해 플레이스홀더 값에 대해 다양한 문자열, 숫자 및 날짜 작업을 수행할 수 있습니다.

Liquid 필터의 전체 목록은 [여기](https://shopify.github.io/liquid/basics/introduction/)에서 확인할 수 있습니다.

다음은 인기 있는 Liquid 필터의 몇 가지 예시입니다:

## 예시 1: 부분 문자열

**1.1** 'Vishal Abraham'을 Azure AD에서 'vabraham@domainname.com'으로 사용자 생성 - liquid 필터 사용

{{ticket.ri_49_cf_employee_first_name | **first**}} {{ticket.ri_49_cf_employee_last_name }}@domainname.com

**1.2** **truncate** 필터를 사용하여 문자열에서 처음 3글자 추출

{{ticket.ri_49_cf_employee_first_name | **truncate:3 ,''**}}

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50002706324/original/LzhknwNWKZS7EV0nor7kYcBj02iNMaXdNQ.png?1616562538" style="width: auto;" class="fr-fic fr-fil fr-dib" data-attachment="[object Object]" data-id="50002706324">

## 예시 2: 대소문자 변환

Slack 채널을 티켓 ID(예: inc-123)로 생성합니다.

여기서 문제는 Slack이 채널명에 대해 소문자 형식만 허용하므로 **downcase** liquid 필터를 사용하여 티켓 ID를 변환해야 한다는 것입니다.

{{ticket.id | **downcase**}}

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50002706335/original/g4l2NFkUaeGqFFBftb3bgicIRLwc8ygduQ.png?1616562595" style="width: auto;" class="fr-fic fr-fil fr-dib" data-attachment="[object Object]" data-id="50002706335">

## 예시 3: 수학 연산

**times** 필터를 사용하여 비용과 수량의 간단한 곱셈을 수행합니다.

{{ticket.quantity | **times**: ticket.cost}}

## 예시 4: 텍스트 분할

**split** 필터를 사용하여 텍스트 덩어리에서 n번째 항목을 추출합니다.

{% assign value = {{A2.meta.system_message}} | **split**: ' ' %}{{value[n-1]}}

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50002706339/original/sx0fL90KJ11et4N328iBrAeGSrQFErgEEg.png?1616562636" style="width: auto;" class="fr-fic fr-fil fr-dib" data-attachment="[object Object]" data-id="50002706339">

## 예시 5: 쉼표로 구분된 값 처리

**split** 필터를 사용하여 쉼표로 구분된 값 목록에서 n번째 항목을 추출합니다.

{% assign value = {{ticket.associated_asset_names}} | **split**: ',' %}{{value[n-1]}}

## 예시 6: Google 캘린더 이벤트 생성

Google 캘린더 이벤트 생성의 경우 날짜-시간 형식을 RFC 3339 호환 형식(예: **2021-02-01T09:00:00**)으로 변경해야 합니다.

이는 **date** liquid 필터를 사용하여 수행할 수 있습니다.

{{change.planned_start_date | date: '%Y-%m-%dT%H:%M:%S'}}

<img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50002706359/original/FFJzPTNnwZQ025c0rv16YMJZRzc9S6YeuQ.png?1616562891" style="width: auto;" class="fr-fic fr-fil fr-dib" data-attachment="[object Object]" data-id="50002706359">

## 예시 7: HTML 콘텐츠 정리

sanitize_html Liquid 플레이스홀더를 사용하여 HTML 콘텐츠를 정리합니다.

**sanitize_html** liquid 필터를 사용하여 HTML 플레이스홀더를 처리하여 무효한 JSON 오류가 발생하지 않고 API 요청 본문 내에서 사용할 수 있도록 합니다.

예를 들어:

**{{ticket.description}}** 결과:

```
"<div style='font-size: 14px; font-family: -apple-system, BlinkMacSystemFont, \"Segoe UI\", Roboto, \"Helvetica Neue\", Arial, sans-serif;'>\n<div>This is test.</div>\n</div>"
```

**{{ticket.description | sanitize_html}}** 결과:

```
"<div style='font-size: 14px; font-family: -apple-system, BlinkMacSystemFont, \\\"Segoe UI\\\", Roboto, \\\"Helvetica Neue\\\", Arial, sans-serif;'>\\n<div>This is test.</div>\\n</div>"
```

따라서 API 요청 본문 내에서 사용할 수 있습니다.

이러한 Liquid 필터를 활용하면 워크플로우 자동화에서 더욱 강력하고 유연한 데이터 처리가 가능합니다.