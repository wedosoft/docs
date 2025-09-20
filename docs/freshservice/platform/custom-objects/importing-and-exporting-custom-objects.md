---
sidebar_position: 3
---

# 커스텀 객체 가져오기 및 내보내기

커스텀 객체를 생성한 후 CSV 파일을 통해 객체 레코드를 대량으로 가져오거나 기존 레코드를 내보낼 수 있습니다. 이를 통해 효율적인 데이터 관리가 가능합니다.

:::info 데이터 처리 방식
레코드 ID를 기준으로 업데이트 또는 신규 생성이 자동으로 결정됩니다.
:::

## 객체 레코드 가져오기

<p data-identifyelement="504" dir="ltr" style={{ lineHeight: "1.38", marginBottom: "0pt" }}><span data-identifyelement="505" style={{ fontSize: "11pt", fontFamily: "Arial", color: "rgb(0, 0, 0)", fontWeight: "700" }}>객체 레코드 가져오기</span></p>

<p data-identifyelement="508" dir="ltr" style={{ lineHeight: "1.38", marginBottom: "0pt" }}><span data-identifyelement="509" style={{ fontSize: "11pt", fontFamily: "Arial", color: "rgb(0, 0, 0)", fontWeight: "400" }}>객체 필드가 있는 커스텀 객체를 생성한 후에는 CSV 파일에서 객체 레코드를 가져오기로 선택할 수 있습니다. 이를 위해서는,</span></p>

### 가져오기 절차

:::tip 대량 데이터 처리
CSV 가져오기를 통해 수백 개의 레코드를 한 번에 처리할 수 있어 효율적입니다.
:::

1. 객체 레코드 탭 아래의 **가져오기**를 클릭하세요.

   ![가져오기 버튼](https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50001925422/original/VPwt1oiMGndE48ltpJYu5c8n9dLAr40X3Q.png?1603339717)

- <p data-identifyelement="514" dir="ltr" style={{ lineHeight: "1.38", marginBottom: "0pt" }}><span data-identifyelement="520" style={{ fontSize: "11pt", fontFamily: "Arial", color: "rgb(0, 0, 0)", fontWeight: "400" }}>업로드 섹션에서 CSV 파일을 업로드하세요.</span></p>

<p><span data-identifyelement="520" style={{ fontSize: "11pt", fontFamily: "Arial", color: "rgb(0, 0, 0)", fontWeight: "400" }}><img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50001925425/original/RkcM5UEYcJlOerHToS6egetLDjq7OKtmDA.png?1603339748" style={{ width: "472px" }} class="fr-fic fr-dib fr-bordered" data-attachment="[object Object]" data-id="50001925425" /></span></p>

- <p data-identifyelement="522" dir="ltr" style={{ lineHeight: "1.38", marginBottom: "0pt" }}><span data-identifyelement="523" style={{ fontSize: "11pt", fontFamily: "Arial", color: "rgb(0, 0, 0)", fontWeight: "400" }}>이제 CSV 파일에서 레코드가 올바르게 가져와지도록 하기 위해 객체 필드를 CSV 필드와 매칭하세요.</span></p>

### CSV 파일 형식 요구사항

:::warning 파일 형식 주의사항
CSV 파일 형식이 올바르지 않으면 가져오기에 실패할 수 있습니다.
:::

<p data-identifyelement="524" dir="ltr" style={{ lineHeight: "1.38", marginLeft: "36pt", marginBottom: "0pt" }}><span data-identifyelement="525" style={{ fontSize: "11pt", fontFamily: "Arial", color: "rgb(0, 0, 0)", fontWeight: "700" }}>참고: </span><span data-identifyelement="526" style={{ fontSize: "11pt", fontFamily: "Arial", color: "rgb(0, 0, 0)", fontWeight: "400" }}>CSV 파일에 다음 사항이 있는지 확인하세요</span></p>

- <p data-identifyelement="529" dir="ltr" style={{ lineHeight: "1.38", marginBottom: "0pt" }}><span data-identifyelement="530" style={{ fontSize: "11pt", fontFamily: "Arial", color: "rgb(0, 0, 0)", fontWeight: "400" }}>필드 이름이 있는 헤더 행</span></p>
- <p data-identifyelement="532" dir="ltr" style={{ lineHeight: "1.38", marginBottom: "0pt" }}><span data-identifyelement="533" style={{ fontSize: "11pt", fontFamily: "Arial", color: "rgb(0, 0, 0)", fontWeight: "400" }}>레코드 ID 전용 열. 레코드 ID는 Freshservice의 모든 객체 레코드에 추가되는 고유 식별자입니다.</span></p>

### 가져오기 완료 및 상태 확인

- <p data-identifyelement="536" dir="ltr" style={{ lineHeight: "1.38", marginBottom: "0pt" }}><span data-identifyelement="537" style={{ fontSize: "11pt", fontFamily: "Arial", color: "rgb(0, 0, 0)", fontWeight: "400" }}>모든 필드를 매칭한 후</span><span data-identifyelement="538" style={{ fontSize: "11pt", fontFamily: "Arial", color: "rgb(0, 0, 0)", fontWeight: "700" }}> 가져오기</span><span data-identifyelement="539" style={{ fontSize: "11pt", fontFamily: "Arial", color: "rgb(0, 0, 0)", fontWeight: "400" }}>를 클릭하세요.</span></p>
- <p data-identifyelement="541" dir="ltr" style={{ lineHeight: "1.38", marginBottom: "0pt" }}><span data-identifyelement="542" style={{ fontSize: "11pt", fontFamily: "Arial", color: "rgb(0, 0, 0)", fontWeight: "400" }}>커스텀 객체 내에서 바로 가져오기 상태를 추적할 수 있습니다. 가져오기 상태에 대한 이메일도 받게 됩니다.</span></p>
- <p data-identifyelement="544" dir="ltr" style={{"lineHeight": "1.38", "marginBottom": "0pt"}}><span data-identifyelement="545" style={{"fontSize": "11pt", "fontFamily": "Arial", "color": "rgb(0, 0, 0)", "fontWeight": "400"}}>가져오기가 부분적으로 완료되거나 실패한 경우 가져오기 결과와 실패한 레코드로 가져오기의 자세한 상태를 확인할 수 있습니다.</span></p>

### 레코드 ID 처리 규칙

<p data-identifyelement="546" dir="ltr" style={{ lineHeight: "1.38", marginBottom: "0pt" }}><span data-identifyelement="547" style={{ fontSize: "11pt", fontFamily: "Arial", color: "rgb(0, 0, 0)", fontWeight: "700" }}>Note:</span></p>
<p data-identifyelement="548" dir="ltr" style={{ lineHeight: "1.38", marginBottom: "0pt" }}><span data-identifyelement="549" style={{ fontSize: "11pt", fontFamily: "Arial", color: "rgb(0, 0, 0)", fontWeight: "400" }}>The record ID is used as following during an import:</span></p>

- <p data-identifyelement="552" dir="ltr" style={{ lineHeight: "1.38", marginBottom: "0pt" }}><span data-identifyelement="553" style={{ fontSize: "11pt", fontFamily: "Arial", color: "rgb(0, 0, 0)", fontWeight: "400" }}>If a matching record ID is found during import, the corresponding object record is updated with the CSV record data</span></p>
- <p data-identifyelement="555" dir="ltr" style={{ lineHeight: "1.38", marginBottom: "0pt" }}><span data-identifyelement="556" style={{ fontSize: "11pt", fontFamily: "Arial", color: "rgb(0, 0, 0)", fontWeight: "400" }}>If record ID is empty during import, an object record is inserted with the CSV record data</span></p>
- <p data-identifyelement="558" dir="ltr" style={{"lineHeight": "1.38", "marginBottom": "0pt"}}><span data-identifyelement="559" style={{"fontSize": "11pt", "fontFamily": "Arial", "color": "rgb(0, 0, 0)", "fontWeight": "400"}}>If no matching record ID is found, the CSV record is skipped during import.</span></p>

### 룩업 필드 가져오기 규칙

<p dir="ltr" style={{ lineHeight: "1.38", marginBottom: "0pt" }}><span style={{ fontSize: "11pt", fontFamily: "Arial", color: "rgb(0, 0, 0)", fontWeight: "400" }}>While importing into lookup fields, since look ups reference existing entities, ensure you use the following matching fields.</span></p>

<div align="left" dir="ltr" style={{ marginLeft: "0pt" }}><table style={{ border: "none", borderCollapse: "collapse", width: "80%", tableLayout: "fixed", marginRight: "calc(10%)", marginLeft: "calc(10%)" }}>
<colgroup><col /><col /></colgroup>
<tbody>
<tr style={{ height: "0pt" }}>
<td style={{ borderWidth: "1pt", borderStyle: "solid", borderColor: "rgb(0, 0, 0)", padding: "5pt", overflow: "hidden", overflowWrap: "break-word", backgroundColor: "rgb(164, 194, 244)" }}>
<p dir="ltr" style={{ lineHeight: "1.2", textAlign: "center", marginBottom: "0pt" }}><span style={{ fontSize: "11pt", fontFamily: "Arial", color: "rgb(0, 0, 0)", fontWeight: "700" }}>Lookup field Type</span></p>
</td>
<td style={{ borderWidth: "1pt", borderStyle: "solid", borderColor: "rgb(0, 0, 0)", padding: "5pt", overflow: "hidden", overflowWrap: "break-word", backgroundColor: "rgb(164, 194, 244)" }}>
<p dir="ltr" style={{ lineHeight: "1.2", textAlign: "center", marginBottom: "0pt" }}><span style={{ fontSize: "11pt", fontFamily: "Arial", color: "rgb(0, 0, 0)", fontWeight: "700" }}>Matching Field</span></p>
</td>
</tr>
<tr style={{ height: "0pt" }}>
<td style={{ borderWidth: "1pt", borderStyle: "solid", borderColor: "rgb(0, 0, 0)", padding: "5pt", overflow: "hidden", overflowWrap: "break-word" }}>
<p dir="ltr" style={{ lineHeight: "1.2", textAlign: "center", marginBottom: "0pt" }}><span style={{ fontSize: "11pt", fontFamily: "Arial", color: "rgb(0, 0, 0)", fontWeight: "400" }}>All Users / Agents</span></p>
</td>
<td style={{ borderWidth: "1pt", borderStyle: "solid", borderColor: "rgb(0, 0, 0)", padding: "5pt", overflow: "hidden", overflowWrap: "break-word" }}>
<p dir="ltr" style={{ lineHeight: "1.2", textAlign: "center", marginBottom: "0pt" }}><span style={{ fontSize: "11pt", fontFamily: "Arial", color: "rgb(0, 0, 0)", fontWeight: "400" }}>Email</span></p>
</td>
</tr>
<tr style={{ height: "0pt" }}>
<td style={{ borderWidth: "1pt", borderStyle: "solid", borderColor: "rgb(0, 0, 0)", padding: "5pt", overflow: "hidden", overflowWrap: "break-word" }}>
<p dir="ltr" style={{ lineHeight: "1.2", textAlign: "center", marginBottom: "0pt" }}><span style={{ fontSize: "11pt", fontFamily: "Arial", color: "rgb(0, 0, 0)", fontWeight: "400" }}>Group / Group Name</span></p>
</td>
<td style={{ borderWidth: "1pt", borderStyle: "solid", borderColor: "rgb(0, 0, 0)", padding: "5pt", overflow: "hidden", overflowWrap: "break-word" }}>
<p dir="ltr" style={{ lineHeight: "1.2", textAlign: "center", marginBottom: "0pt" }}><span style={{ fontSize: "11pt", fontFamily: "Arial", color: "rgb(0, 0, 0)", fontWeight: "400" }}>Group Name</span></p>
</td>
</tr>
<tr style={{ height: "0pt" }}>
<td style={{ borderWidth: "1pt", borderStyle: "solid", borderColor: "rgb(0, 0, 0)", padding: "5pt", overflow: "hidden", overflowWrap: "break-word" }}>
<p dir="ltr" style={{ lineHeight: "1.2", textAlign: "center", marginBottom: "0pt" }}><span style={{ fontSize: "11pt", fontFamily: "Arial", color: "rgb(0, 0, 0)", fontWeight: "400" }}>Asset</span></p>
</td>
<td style={{ borderWidth: "1pt", borderStyle: "solid", borderColor: "rgb(0, 0, 0)", padding: "5pt", overflow: "hidden", overflowWrap: "break-word" }}>
<p dir="ltr" style={{ lineHeight: "1.2", textAlign: "center", marginBottom: "0pt" }}><span style={{ fontSize: "11pt", fontFamily: "Arial", color: "rgb(0, 0, 0)", fontWeight: "400" }}>Asset Name</span></p>
</td>
</tr>
<tr style={{ height: "0pt" }}>
<td style={{ borderWidth: "1pt", borderStyle: "solid", borderColor: "rgb(0, 0, 0)", padding: "5pt", overflow: "hidden", overflowWrap: "break-word" }}>
<p dir="ltr" style={{ lineHeight: "1.2", textAlign: "center", marginBottom: "0pt" }}><span style={{ fontSize: "11pt", fontFamily: "Arial", color: "rgb(0, 0, 0)", fontWeight: "400" }}>Department</span></p>
</td>
<td style={{ borderWidth: "1pt", borderStyle: "solid", borderColor: "rgb(0, 0, 0)", padding: "5pt", overflow: "hidden", overflowWrap: "break-word" }}>
<p dir="ltr" style={{ lineHeight: "1.2", textAlign: "center", marginBottom: "0pt" }}><span style={{ fontSize: "11pt", fontFamily: "Arial", color: "rgb(0, 0, 0)", fontWeight: "400" }}>Department Name</span></p>
</td>
</tr>
<tr style={{ height: "0pt" }}>
<td style={{ borderWidth: "1pt", borderStyle: "solid", borderColor: "rgb(0, 0, 0)", padding: "5pt", overflow: "hidden", overflowWrap: "break-word" }}>
<p dir="ltr" style={{ lineHeight: "1.2", textAlign: "center", marginBottom: "0pt" }}><span style={{ fontSize: "11pt", fontFamily: "Arial", color: "rgb(0, 0, 0)", fontWeight: "400" }}>Service Item</span></p>
</td>
<td style={{ borderWidth: "1pt", borderStyle: "solid", borderColor: "rgb(0, 0, 0)", padding: "5pt", overflow: "hidden", overflowWrap: "break-word" }}>
<p dir="ltr" style={{ lineHeight: "1.2", textAlign: "center", marginBottom: "0pt" }}><span style={{ fontSize: "11pt", fontFamily: "Arial", color: "rgb(0, 0, 0)", fontWeight: "400" }}>Item Name</span></p>
</td>
</tr>
<tr style={{ height: "0pt" }}>
<td style={{ borderWidth: "1pt", borderStyle: "solid", borderColor: "rgb(0, 0, 0)", padding: "5pt", overflow: "hidden", overflowWrap: "break-word" }}>
<p dir="ltr" style={{ lineHeight: "1.2", textAlign: "center", marginBottom: "0pt" }}><span style={{ fontSize: "11pt", fontFamily: "Arial", color: "rgb(0, 0, 0)", fontWeight: "400" }}>Location</span></p>
</td>
<td style={{ borderWidth: "1pt", borderStyle: "solid", borderColor: "rgb(0, 0, 0)", padding: "5pt", overflow: "hidden", overflowWrap: "break-word" }}>
<p dir="ltr" style={{ lineHeight: "1.2", textAlign: "center", marginBottom: "0pt" }}><span style={{ fontSize: "11pt", fontFamily: "Arial", color: "rgb(0, 0, 0)", fontWeight: "400" }}>Location Name</span></p>
</td>
</tr>
</tbody>
</table></div>

## 객체 레코드 내보내기

<p data-identifyelement="562" dir="ltr" style={{ lineHeight: "1.38", marginBottom: "0pt" }}><span data-identifyelement="563" style={{ fontSize: "11pt", fontFamily: "Arial", color: "rgb(0, 0, 0)", fontWeight: "700" }}>Exporting Object Records</span></p>

<p data-identifyelement="566"><span data-identifyelement="567" style={{ fontSize: "11pt", fontFamily: "Arial", color: "rgb(0, 0, 0)", fontWeight: "400" }}>To export the object records in a custom object, click on </span><span data-identifyelement="568" style={{ fontSize: "11pt", fontFamily: "Arial", color: "rgb(0, 0, 0)", fontWeight: "700" }}>Export </span><span data-identifyelement="569" style={{ fontSize: "11pt", fontFamily: "Arial", color: "rgb(0, 0, 0)", fontWeight: "400" }}>to receive the exported records by email.</span></p>

## 실무 활용 예시

## 문제 해결

### 자주 발생하는 문제

#### 문제: 가져오기 중 일부 레코드가 실패함
**원인**: 룩업 필드의 참조 데이터가 존재하지 않음
**해결**: 
1. 실패한 레코드 목록을 확인
2. 참조되는 에이전트, 그룹, 자산 등이 실제로 존재하는지 검증
3. 올바른 매칭 필드 값(이메일, 이름 등)으로 수정 후 재시도

#### 문제: CSV 파일 업로드 시 형식 오류 발생
**원인**: 헤더 행 누락 또는 Record ID 컬럼 부재
**해결**:
1. CSV 파일 첫 번째 행에 필드명 헤더 추가
2. Record ID 전용 컬럼 생성 (신규는 빈 값, 업데이트는 기존 ID)
3. UTF-8 인코딩으로 저장

:::warning 데이터 무결성 주의
가져오기 전에 반드시 테스트 환경에서 검증하고, 중요한 데이터는 백업을 수행하세요.
:::

:::tip 효율적인 데이터 관리
- 정기적인 Export를 통한 백업 수행
- 표준 CSV 템플릿 사용으로 일관성 유지
- 단계적 Import로 오류 최소화
:::

:::success 가져오기/내보내기 완료
커스텀 객체 데이터가 성공적으로 처리되었습니다. 이제 효율적인 대량 데이터 관리가 가능합니다.
:::