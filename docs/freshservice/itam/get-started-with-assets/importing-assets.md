---
sidebar_position: 4
---

# 자산 가져오기 (Importing Assets)

대량의 자산 데이터를 Freshservice로 효율적으로 가져오는 방법을 안내합니다. CSV 파일을 사용하여 한 번에 여러 자산을 시스템에 등록할 수 있습니다.

## 가져오기 준비사항

### CSV 파일 형식
- UTF-8 인코딩 사용
- 첫 번째 행에 컬럼 헤더 포함
- 필수 필드 포함 확인

### 필수 필드
- **Name**: 자산 이름
- **Asset Type**: 자산 유형
- **Asset Tag**: 자산 태그 (선택사항)

### 권장 필드
- **Used By**: 사용자 이메일
- **Location**: 위치 정보
- **Department**: 부서명
- **Asset State**: 자산 상태

## 가져오기 단계

1. **Admin > Asset Management > Import Assets**로 이동
2. 자산 유형 선택
3. CSV 파일 업로드
4. 필드 매핑 확인
5. 가져오기 실행

## 주의사항

- 중복 자산 태그 확인
- 사용자 이메일 정확성 검증
- 위치 정보 일관성 유지
- 대량 가져오기 시 단계적 진행 권장

## 오류 해결

### 일반적인 오류
- **Invalid email format**: 사용자 이메일 형식 오류
- **Asset tag already exists**: 중복 자산 태그
- **Invalid asset type**: 존재하지 않는 자산 유형

### 해결 방법
- CSV 파일 형식 재확인
- 중복 데이터 제거
- 필수 필드 완성도 검토