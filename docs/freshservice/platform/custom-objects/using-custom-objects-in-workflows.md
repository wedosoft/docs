---
sidebar_position: 2
---

# 워크플로에서 커스텀 객체 활용하기

워크플로가 복잡해지고 조직의 데이터가 증가하면 하드코딩된 값으로 워크플로를 생성하는 것은 관리와 업데이트를 어렵게 만듭니다. Reader Node를 통해 커스텀 객체와 표준 객체의 값을 동적으로 참조하여 워크플로에서 사용할 수 있습니다.

:::info 워크플로 자동화
Reader Node는 워크플로 설정과 유지보수를 간소화하여 많은 관리 작업을 절약해줍니다.
:::

## Reader Node 소개

<div align="center">
  <img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50004949349/original/jBOBTtTWUEvskDivTlXJZbTvtA0mNb3Xfg.png?1646830515" width="298" height="318" alt="Reader Node" style={{border: '1px solid #ddd', borderRadius: '4px'}} />
</div>

## Reader Node 사용 방법

[커스텀 객체를 생성](creating-custom-objects.md)한 후, 워크플로 자동화에서 Reader Node를 통해 저장된 데이터를 기반으로 작업을 수행할 수 있습니다.

Reader Node는 다음 4개 섹션으로 구성됩니다:

- **Read from**: 읽어올 표준 또는 커스텀 Freshservice 객체 지정
- **Filters**: 커스텀 객체 필드를 필터링하고 레코드를 읽을 조건 생성
- **Sort By**: 여러 레코드가 조건에 맞는 경우 정렬 순서 설정
- **Preview results**: 필터 조건에 맞는 결과 미리보기

### Read From

표준 또는 커스텀 Freshservice 객체를 지정합니다.

<div align="center">
  <img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50004949343/original/-l9zHnmAtseYPPug0Vb1ai6l5oBBc9yg2Q.png?1646830513" width="320" height="254" alt="Read From" style={{border: '1px solid #ddd', borderRadius: '4px'}} />
</div>

### Filters

커스텀 객체 필드를 필터링하고 레코드를 읽을 조건을 생성합니다.

<div align="center">
  <img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50004949346/original/4EbSz65KmMxKWH4BN0k_t4WiVX_IDJpHbw.png?1646830514" width="334" height="277" alt="Filters" style={{border: '1px solid #ddd', borderRadius: '4px'}} />
</div>

### Sort By

조건에 맞는 레코드가 여러 개인 경우 Reader Node는 첫 번째 레코드만 반환합니다. Sort By 옵션으로 레코드를 정렬하여 올바른 첫 번째 레코드가 선택되도록 합니다.

<div align="center">
  <img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50004949344/original/pnriWtwGS7jJHB2mTQYdP5dWVb4Js4lKmg.png?1646830513" width="314" height="294" alt="Sort By" style={{border: '1px solid #ddd', borderRadius: '4px'}} />
</div>

### Preview Results

필터 섹션에서 지정한 조건에 맞는 Reader 결과를 보여줍니다. 동적 변수/플레이스홀더를 값으로 대체하여 Reader가 반환하는 결과를 확인할 수 있습니다.

:::note
Preview Results는 플레이스홀더에서는 작동하지 않습니다.
:::

<div align="center">
  <img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50004949345/original/aK_eOhhf3auMmga3VhxZqzMt4Psm_2khAQ.png?1646830513" width="347" height="323" alt="Preview Results" style={{border: '1px solid #ddd', borderRadius: '4px'}} />
</div>

## 한국 기업 사용 사례

### 사례 1: 지역별 티켓 라우팅 (삼성전자)

삼성전자처럼 전국에 지사가 있는 기업에서 지역에 따라 다른 지원팀으로 티켓을 라우팅하는 예시입니다.

| 지역 | 티켓 카테고리 | 담당 그룹 |
|------|--------------|-----------|
| 서울 | 하드웨어 | 서울지원팀 |
| 수원 | 소프트웨어 | 수원지원팀 |
| 부산 | 네트워크 | 부산지원팀 |
| 대구 | 하드웨어 | 대구지원팀 |

#### 워크플로 설정

1. **커스텀 객체 생성**: 요청자 위치를 기반으로 에이전트 그룹을 매핑하는 커스텀 객체 생성

2. **워크플로 생성**: 
   - Admin → 자동화 및 생산성 → 자동화 → 워크플로 자동화로 이동
   - 이벤트 블록에서 **티켓이 생성됨** 선택

:::info 다중 워크스페이스 환경
계정에 워크스페이스가 여러 개인 경우:
- 글로벌 워크플로 수정: **Admin > 글로벌 설정 > 자동화 및 생산성 > 자동화 > 워크플로 자동화**
- 워크스페이스 수준 워크플로 수정: **Admin > 워크스페이스 설정 > {워크스페이스 이름} > 자동화 및 생산성 > 자동화 > 워크플로 자동화**
:::

3. **Reader Node 추가**: 커스텀 객체에서 정보를 읽기 위해 Reader Node를 드래그앤드롭

4. **필터 설정**: Filter By 옵션에서 객체 필드를 선택하여 레코드 선택 기준 설정

5. **조건 블록 추가**: Reader가 레코드를 반환했는지 확인하는 조건 블록 추가

6. **액션 노드 생성**: 커스텀 객체 테이블을 기반으로 Reader Node가 반환한 해당 에이전트 그룹으로 티켓을 라우팅

### 사례 2: 회의실 예약 승인 (LG그룹)

LG그룹처럼 대규모 오피스에서 선택된 회의실을 기반으로 해당 회의실 관리자에게 승인을 보내는 시나리오입니다.

#### 구현 단계

1. **회의실 커스텀 객체 생성**: 회의실과 각각의 관리자 정보를 저장

2. **서비스 요청 폼 설정**: 커스텀 객체에서 회의실 목록을 조회하도록 설정
   - 데이터 소스에서 **커스텀 객체** → **회의실** 선택

3. **워크플로 구성**:
   - 조건 블록에서 **티켓 필드 → 요청 항목 → 회의실** 서비스 항목 선택
   - Reader Node 삽입하여 회의실 커스텀 객체 정보 읽기
   - Record ID를 Filter By 옵션에서 선택하고 서비스 요청의 회의실 필드와 매핑

:::note 룩업 필드 매핑
자산이나 커스텀 객체와 같은 데이터 소스를 사용하는 룩업 필드에서 데이터를 필터링하고 액세스하려면 해당 룩업 필드에 대해 레코드 ID를 매핑하세요. 룩업 필드는 내부적으로 참조된 레코드의 ID를 저장하므로 두 데이터 유형이 일치합니다.
:::

4. **액션 블록 생성**: 회의실 Reader Node(R1)에서 관리자를 선택하여 해당 관리자에게 승인 전송

5. **확인 이메일**: 서비스 요청이 승인되거나 거부된 경우 요청자에게 확인 이메일 전송

### 사례 3: 현대자동차 자산 기반 변경 승인

현대자동차처럼 다양한 자산을 관리하는 기업에서 연결된 자산을 기반으로 변경 승인 또는 라우팅을 수행하는 예시입니다.

#### 워크플로 단계

1. **이벤트 블록**: **변경이 생성됨** 선택

2. **조건 블록**: 변경에 연결된 자산이 있는지 확인

3. **Reader Node**: 연결된 자산 정보를 읽기 위해 Reader Node 추가

4. **알림 액션**: 자산을 관리하는 해당 그룹에 알림

5. **승인 액션**: 해당 자산 관리자 또는 CAB 그룹에 승인 전송

## Reader Node 출력 활용

각 워크플로의 Reader Node는 **R1**, **R2**와 같은 고유 식별자를 가집니다. Reader Node의 출력은 단일 레코드이며, 값은 **<Reader ID>.<객체 필드>** 형태로 참조됩니다.

**예시**: `R1.위치`, `R2.관리자`

:::warning 중요 사항
Reader 출력을 가져와서 액션에서 중첩 필드를 할당할 때, 여러 하위 카테고리가 있어도 커스텀 객체의 첫 번째 하위 카테고리만 할당할 수 있습니다.
:::

## 베스트 프랙티스

### 한국 기업 환경에서의 활용 팁

1. **조직 구조 반영**: 한국 기업의 계층적 조직 구조를 커스텀 객체에 반영하여 적절한 승인자 설정

2. **지역별 특성 고려**: 전국 지사가 있는 경우 지역별 특성과 업무 시간을 고려한 라우팅 설정

3. **다국어 지원**: 글로벌 기업의 경우 한국어와 영어를 모두 지원하는 필드 설정

4. **규정 준수**: 한국의 개인정보보호법 등 관련 규정을 준수하는 데이터 처리 워크플로 구성

## 문제 해결

### 일반적인 문제와 해결책

**Q: Reader Node가 빈 값을 반환합니다**
A: 조건 블록을 추가하여 Reader가 레코드를 반환했는지 확인하고, 빈 값으로 인한 워크플로 중단을 방지하세요.

**Q: 여러 레코드가 조건에 맞는 경우**
A: Sort By 옵션을 사용하여 적절한 레코드가 첫 번째로 선택되도록 정렬 기준을 설정하세요.

**Q: 커스텀 객체 룩업이 작동하지 않습니다**
A: Record ID를 Filter By 옵션에서 사용하고 해당 룩업 필드와 매핑했는지 확인하세요.

## 관련 문서

- [커스텀 객체 생성하기](creating-custom-objects.md)
- [커스텀 객체 룩업](lookups-to-custom-objects.md)
- [커스텀 객체 가져오기/내보내기](importing-and-exporting-custom-objects.md)