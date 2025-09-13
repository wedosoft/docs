---
sidebar_position: 6
---

# Freshservice 지원 시간대 목록

:::info 문서 목적
이 문서는 "Freshservice 지원 시간대 목록(List of Time Zones Supported in Freshservice)" 및 CSV 파일을 통한 요청자 가져오기에서 사용할 수 있는 시간대 정보를 안내하는 문서입니다.
:::

Freshservice에서는 전 세계 다양한 시간대를 지원해서 글로벌 서비스 데스크 운영을 가능하게 해요. 이 문서는 CSV 파일을 통해 [요청자를 가져올](https://support.freshservice.com/support/solutions/articles/210050-guidelines-to-importing-requesters-from-csv-files) 때 사용할 수 있는 시간대 목록을 제공해요.

## 개요

Freshservice는 140개 이상의 시간대를 지원하며, 각 시간대는 표준 IANA 시간대 식별자를 사용해요. CSV 가져오기 시 **Import/Export에 제공할 값** 열의 값을 사용해서 시간대를 지정할 수 있어요.

:::info 시간대 설정
- 시간대 설정은 사용자별로 개별 구성 가능합니다
- CSV 가져오기 시 시간대 정보를 함께 포함할 수 있어요
- 설정된 시간대는 티켓 생성 시간, SLA 계산 등에 영향을 줍니다
:::

## 지원 시간대 목록

다음 표는 Freshservice에서 지원하는 모든 시간대와 해당하는 IANA 시간대 식별자를 보여줍니다:

<table>
<thead>
<tr>
<th style={{ width: '55%' }}>Import/Export에 제공할 값</th>
<th style={{ width: '45%' }}>해당 시간대</th>
</tr>
</thead>
<tbody>
<tr>
<td>International Date Line West</td>
<td>Etc/GMT+12</td>
</tr>
<tr>
<td>Midway Island</td>
<td>Pacific/Midway</td>
</tr>
<tr>
<td>American Samoa</td>
<td>Pacific/Pago_Pago</td>
</tr>
<tr>
<td>Hawaii</td>
<td>Pacific/Honolulu</td>
</tr>
<tr>
<td>Alaska</td>
<td>America/Juneau</td>
</tr>
<tr>
<td>Pacific Time (US & Canada)</td>
<td>America/Los_Angeles</td>
</tr>
<tr>
<td>Tijuana</td>
<td>America/Tijuana</td>
</tr>
<tr>
<td>Mountain Time (US & Canada)</td>
<td>America/Denver</td>
</tr>
<tr>
<td>Arizona</td>
<td>America/Phoenix</td>
</tr>
<tr>
<td>Chihuahua</td>
<td>America/Chihuahua</td>
</tr>
<tr>
<td>Mazatlan</td>
<td>America/Mazatlan</td>
</tr>
<tr>
<td>Central Time (US & Canada)</td>
<td>America/Chicago</td>
</tr>
<tr>
<td>Saskatchewan</td>
<td>America/Regina</td>
</tr>
<tr>
<td>Guadalajara</td>
<td>America/Mexico_City</td>
</tr>
<tr>
<td>Mexico City</td>
<td>America/Mexico_City</td>
</tr>
<tr>
<td>Monterrey</td>
<td>America/Monterrey</td>
</tr>
<tr>
<td>Central America</td>
<td>America/Guatemala</td>
</tr>
<tr>
<td>Eastern Time (US & Canada)</td>
<td>America/New_York</td>
</tr>
<tr>
<td>Indiana (East)</td>
<td>America/Indiana/Indianapolis</td>
</tr>
<tr>
<td>Bogota</td>
<td>America/Bogota</td>
</tr>
<tr>
<td>Lima</td>
<td>America/Lima</td>
</tr>
<tr>
<td>Quito</td>
<td>America/Lima</td>
</tr>
<tr>
<td>Atlantic Time (Canada)</td>
<td>America/Halifax</td>
</tr>
<tr>
<td>Caracas</td>
<td>America/Caracas</td>
</tr>
<tr>
<td>La Paz</td>
<td>America/La_Paz</td>
</tr>
<tr>
<td>Santiago</td>
<td>America/Santiago</td>
</tr>
<tr>
<td>Newfoundland</td>
<td>America/St_Johns</td>
</tr>
<tr>
<td>Brasilia</td>
<td>America/Sao_Paulo</td>
</tr>
<tr>
<td>Buenos Aires</td>
<td>America/Argentina/Buenos_Aires</td>
</tr>
<tr>
<td>Montevideo</td>
<td>America/Montevideo</td>
</tr>
<tr>
<td>Georgetown</td>
<td>America/Guyana</td>
</tr>
<tr>
<td>Greenland</td>
<td>America/Godthab</td>
</tr>
<tr>
<td>Mid-Atlantic</td>
<td>Atlantic/South_Georgia</td>
</tr>
<tr>
<td>Azores</td>
<td>Atlantic/Azores</td>
</tr>
<tr>
<td>Cape Verde Is.</td>
<td>Atlantic/Cape_Verde</td>
</tr>
<tr>
<td>Dublin</td>
<td>Europe/Dublin</td>
</tr>
<tr>
<td>Edinburgh</td>
<td>Europe/London</td>
</tr>
<tr>
<td>Lisbon</td>
<td>Europe/Lisbon</td>
</tr>
<tr>
<td>London</td>
<td>Europe/London</td>
</tr>
<tr>
<td>Casablanca</td>
<td>Africa/Casablanca</td>
</tr>
<tr>
<td>Monrovia</td>
<td>Africa/Monrovia</td>
</tr>
<tr>
<td>UTC</td>
<td>Etc/UTC</td>
</tr>
<tr>
<td>Belgrade</td>
<td>Europe/Belgrade</td>
</tr>
<tr>
<td>Bratislava</td>
<td>Europe/Bratislava</td>
</tr>
<tr>
<td>Budapest</td>
<td>Europe/Budapest</td>
</tr>
<tr>
<td>Ljubljana</td>
<td>Europe/Ljubljana</td>
</tr>
<tr>
<td>Prague</td>
<td>Europe/Prague</td>
</tr>
<tr>
<td>Sarajevo</td>
<td>Europe/Sarajevo</td>
</tr>
<tr>
<td>Skopje</td>
<td>Europe/Skopje</td>
</tr>
<tr>
<td>Warsaw</td>
<td>Europe/Warsaw</td>
</tr>
<tr>
<td>Zagreb</td>
<td>Europe/Zagreb</td>
</tr>
<tr>
<td>Brussels</td>
<td>Europe/Brussels</td>
</tr>
<tr>
<td>Copenhagen</td>
<td>Europe/Copenhagen</td>
</tr>
<tr>
<td>Madrid</td>
<td>Europe/Madrid</td>
</tr>
<tr>
<td>Paris</td>
<td>Europe/Paris</td>
</tr>
<tr>
<td>Amsterdam</td>
<td>Europe/Amsterdam</td>
</tr>
<tr>
<td>Berlin</td>
<td>Europe/Berlin</td>
</tr>
<tr>
<td>Bern</td>
<td>Europe/Zurich</td>
</tr>
<tr>
<td>Rome</td>
<td>Europe/Rome</td>
</tr>
<tr>
<td>Stockholm</td>
<td>Europe/Stockholm</td>
</tr>
<tr>
<td>Vienna</td>
<td>Europe/Vienna</td>
</tr>
<tr>
<td>West Central Africa</td>
<td>Africa/Algiers</td>
</tr>
<tr>
<td>Bucharest</td>
<td>Europe/Bucharest</td>
</tr>
<tr>
<td>Cairo</td>
<td>Africa/Cairo</td>
</tr>
<tr>
<td>Helsinki</td>
<td>Europe/Helsinki</td>
</tr>
<tr>
<td>Kyiv</td>
<td>Europe/Kiev</td>
</tr>
<tr>
<td>Riga</td>
<td>Europe/Riga</td>
</tr>
<tr>
<td>Sofia</td>
<td>Europe/Sofia</td>
</tr>
<tr>
<td>Tallinn</td>
<td>Europe/Tallinn</td>
</tr>
<tr>
<td>Vilnius</td>
<td>Europe/Vilnius</td>
</tr>
<tr>
<td>Athens</td>
<td>Europe/Athens</td>
</tr>
<tr>
<td>Istanbul</td>
<td>Europe/Istanbul</td>
</tr>
<tr>
<td>Minsk</td>
<td>Europe/Minsk</td>
</tr>
<tr>
<td>Jerusalem</td>
<td>Asia/Jerusalem</td>
</tr>
<tr>
<td>Harare</td>
<td>Africa/Harare</td>
</tr>
<tr>
<td>Pretoria</td>
<td>Africa/Johannesburg</td>
</tr>
<tr>
<td>Kaliningrad</td>
<td>Europe/Kaliningrad</td>
</tr>
<tr>
<td>Moscow</td>
<td>Europe/Moscow</td>
</tr>
<tr>
<td>St. Petersburg</td>
<td>Europe/Moscow</td>
</tr>
<tr>
<td>Volgograd</td>
<td>Europe/Volgograd</td>
</tr>
<tr>
<td>Samara</td>
<td>Europe/Samara</td>
</tr>
<tr>
<td>Kuwait</td>
<td>Asia/Kuwait</td>
</tr>
<tr>
<td>Riyadh</td>
<td>Asia/Riyadh</td>
</tr>
<tr>
<td>Nairobi</td>
<td>Africa/Nairobi</td>
</tr>
<tr>
<td>Baghdad</td>
<td>Asia/Baghdad</td>
</tr>
<tr>
<td>Tehran</td>
<td>Asia/Tehran</td>
</tr>
<tr>
<td>Abu Dhabi</td>
<td>Asia/Muscat</td>
</tr>
<tr>
<td>Muscat</td>
<td>Asia/Muscat</td>
</tr>
<tr>
<td>Baku</td>
<td>Asia/Baku</td>
</tr>
<tr>
<td>Tbilisi</td>
<td>Asia/Tbilisi</td>
</tr>
<tr>
<td>Yerevan</td>
<td>Asia/Yerevan</td>
</tr>
<tr>
<td>Kabul</td>
<td>Asia/Kabul</td>
</tr>
<tr>
<td>Ekaterinburg</td>
<td>Asia/Yekaterinburg</td>
</tr>
<tr>
<td>Islamabad</td>
<td>Asia/Karachi</td>
</tr>
<tr>
<td>Karachi</td>
<td>Asia/Karachi</td>
</tr>
<tr>
<td>Tashkent</td>
<td>Asia/Tashkent</td>
</tr>
<tr>
<td>Chennai</td>
<td>Asia/Kolkata</td>
</tr>
<tr>
<td>Kolkata</td>
<td>Asia/Kolkata</td>
</tr>
<tr>
<td>Mumbai</td>
<td>Asia/Kolkata</td>
</tr>
<tr>
<td>New Delhi</td>
<td>Asia/Kolkata</td>
</tr>
<tr>
<td>Kathmandu</td>
<td>Asia/Kathmandu</td>
</tr>
<tr>
<td>Astana</td>
<td>Asia/Dhaka</td>
</tr>
<tr>
<td>Dhaka</td>
<td>Asia/Dhaka</td>
</tr>
<tr>
<td>Sri Jayawardenepura</td>
<td>Asia/Colombo</td>
</tr>
<tr>
<td>Almaty</td>
<td>Asia/Almaty</td>
</tr>
<tr>
<td>Novosibirsk</td>
<td>Asia/Novosibirsk</td>
</tr>
<tr>
<td>Rangoon</td>
<td>Asia/Rangoon</td>
</tr>
<tr>
<td>Bangkok</td>
<td>Asia/Bangkok</td>
</tr>
<tr>
<td>Hanoi</td>
<td>Asia/Bangkok</td>
</tr>
<tr>
<td>Jakarta</td>
<td>Asia/Jakarta</td>
</tr>
<tr>
<td>Krasnoyarsk</td>
<td>Asia/Krasnoyarsk</td>
</tr>
<tr>
<td>Beijing</td>
<td>Asia/Shanghai</td>
</tr>
<tr>
<td>Chongqing</td>
<td>Asia/Chongqing</td>
</tr>
<tr>
<td>Hong Kong</td>
<td>Asia/Hong_Kong</td>
</tr>
<tr>
<td>Urumqi</td>
<td>Asia/Urumqi</td>
</tr>
<tr>
<td>Kuala Lumpur</td>
<td>Asia/Kuala_Lumpur</td>
</tr>
<tr>
<td>Singapore</td>
<td>Asia/Singapore</td>
</tr>
<tr>
<td>Taipei</td>
<td>Asia/Taipei</td>
</tr>
<tr>
<td>Perth</td>
<td>Australia/Perth</td>
</tr>
<tr>
<td>Irkutsk</td>
<td>Asia/Irkutsk</td>
</tr>
<tr>
<td>Ulaanbaatar</td>
<td>Asia/Ulaanbaatar</td>
</tr>
<tr>
<td>Seoul</td>
<td>Asia/Seoul</td>
</tr>
<tr>
<td>Osaka</td>
<td>Asia/Tokyo</td>
</tr>
<tr>
<td>Sapporo</td>
<td>Asia/Tokyo</td>
</tr>
<tr>
<td>Tokyo</td>
<td>Asia/Tokyo</td>
</tr>
<tr>
<td>Yakutsk</td>
<td>Asia/Yakutsk</td>
</tr>
<tr>
<td>Darwin</td>
<td>Australia/Darwin</td>
</tr>
<tr>
<td>Adelaide</td>
<td>Australia/Adelaide</td>
</tr>
<tr>
<td>Canberra</td>
<td>Australia/Melbourne</td>
</tr>
<tr>
<td>Melbourne</td>
<td>Australia/Melbourne</td>
</tr>
<tr>
<td>Sydney</td>
<td>Australia/Sydney</td>
</tr>
<tr>
<td>Brisbane</td>
<td>Australia/Brisbane</td>
</tr>
<tr>
<td>Hobart</td>
<td>Australia/Hobart</td>
</tr>
<tr>
<td>Vladivostok</td>
<td>Asia/Vladivostok</td>
</tr>
<tr>
<td>Guam</td>
<td>Pacific/Guam</td>
</tr>
<tr>
<td>Port Moresby</td>
<td>Pacific/Port_Moresby</td>
</tr>
<tr>
<td>Magadan</td>
<td>Asia/Magadan</td>
</tr>
<tr>
<td>Srednekolymsk</td>
<td>Asia/Srednekolymsk</td>
</tr>
<tr>
<td>Solomon Is.</td>
<td>Pacific/Guadalcanal</td>
</tr>
<tr>
<td>New Caledonia</td>
<td>Pacific/Noumea</td>
</tr>
<tr>
<td>Fiji</td>
<td>Pacific/Fiji</td>
</tr>
<tr>
<td>Kamchatka</td>
<td>Asia/Kamchatka</td>
</tr>
<tr>
<td>Marshall Is.</td>
<td>Pacific/Majuro</td>
</tr>
<tr>
<td>Auckland</td>
<td>Pacific/Auckland</td>
</tr>
<tr>
<td>Wellington</td>
<td>Pacific/Auckland</td>
</tr>
<tr>
<td>Nuku'alofa</td>
<td>Pacific/Tongatapu</td>
</tr>
<tr>
<td>Tokelau Is.</td>
<td>Pacific/Fakaofo</td>
</tr>
<tr>
<td>Chatham Is.</td>
<td>Pacific/Chatham</td>
</tr>
<tr>
<td>Samoa</td>
<td>Pacific/Apia</td>
</tr>
</tbody>
</table>

## 지역별 시간대 그룹

### 아메리카 대륙
- **북미**: Pacific Time, Mountain Time, Central Time, Eastern Time
- **중미**: Tijuana, Mexico City, Central America
- **남미**: Brasilia, Buenos Aires, Santiago, Lima

### 유럽 및 아프리카
- **서유럽**: London, Paris, Madrid, Amsterdam
- **중유럽**: Berlin, Prague, Warsaw, Vienna
- **동유럽**: Moscow, Kiev, Helsinki, Athens
- **아프리카**: Cairo, Johannesburg, Nairobi, Casablanca

### 아시아 태평양
- **동아시아**: Beijing, Tokyo, Seoul, Hong Kong
- **동남아시아**: Bangkok, Singapore, Jakarta, Manila
- **남아시아**: New Delhi, Mumbai, Dhaka, Colombo
- **중앙아시아**: Tashkent, Almaty, Baku, Tehran
- **오세아니아**: Sydney, Melbourne, Auckland, Perth

## 사용 가이드

### CSV 가져오기 시 시간대 설정

CSV 파일을 통해 요청자를 가져올 때 시간대 열에 위 표의 **Import/Export에 제공할 값** 열의 정확한 값을 사용하세요.

**예시**:
```csv
Name,Email,Time Zone
John Doe,john@company.com,Eastern Time (US & Canada)
Jane Smith,jane@company.com,Pacific Time (US & Canada)
김철수,kim@company.co.kr,Seoul
```

### 일반적인 시간대 설정

가장 자주 사용되는 시간대들:

#### 한국 및 동아시아
- **Seoul** (Asia/Seoul) - 한국 표준시
- **Tokyo** (Asia/Tokyo) - 일본 표준시
- **Beijing** (Asia/Shanghai) - 중국 표준시

#### 미국 및 캐나다
- **Eastern Time (US & Canada)** - 동부 표준시
- **Central Time (US & Canada)** - 중부 표준시
- **Mountain Time (US & Canada)** - 산악 표준시
- **Pacific Time (US & Canada)** - 태평양 표준시

#### 유럽
- **London** (Europe/London) - 그리니치 표준시
- **Paris** (Europe/Paris) - 중앙유럽 표준시
- **Berlin** (Europe/Berlin) - 중앙유럽 표준시

:::tip 시간대 선택 가이드
1. **정확한 지역 선택**: 동일한 UTC 오프셋이라도 일광절약시간(DST) 적용 여부가 다를 수 있습니다
2. **DST 고려**: 일광절약시간을 적용하는 지역의 경우 해당 지역 시간대를 선택하세요
3. **표준 형식 사용**: 표에 명시된 정확한 값을 사용해서 오류를 방지하세요
:::

## 시간대 관련 기능

### SLA 계산
시간대 설정은 다음 기능에 영향을 줍니다:

- **SLA 마감 시간**: 사용자의 시간대에 따른 정확한 마감 시간 계산
- **비즈니스 시간**: 각 시간대의 근무 시간 적용
- **에스컬레이션**: 시간대별 에스컬레이션 스케줄링

### 보고서 및 분석
- **시간별 티켓 분포**: 각 시간대별 티켓 생성 패턴 분석
- **근무 시간 분석**: 지역별 서비스 이용 패턴 파악
- **글로벌 커버리지**: 24시간 서비스 커버리지 분석

:::warning 주의사항
- 시간대 변경 시 기존 데이터의 시간 정보는 소급 적용되지 않습니다
- SLA 계산에 영향을 줄 수 있으므로 변경 전 충분한 검토가 필요합니다
- 일광절약시간 전환 시기에는 SLA 계산에 주의가 필요합니다
:::

## 관련 문서

:::info 참조 문서 작업 방침
이 섹션은 모든 관련 문서가 생성된 후 최종 작업 단계에서 링크를 추가해요.
현재는 섹션 제목만 유지하고 broken links 방지를 위해 링크는 추가하지 않어요.
:::

<!-- 최종 작업 시 아래 형태로 추가:
- [CSV 파일을 통한 요청자 가져오기 가이드](./importing-requesters-csv)
- [사용자 프로필 관리](./user-profile-management)
- [SLA 정책 설정](./sla-policy-configuration)
- [비즈니스 시간 설정](./business-hours-configuration)
-->
