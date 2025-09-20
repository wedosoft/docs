# 📁 워크스페이스 조직화 지침

> **목적**: 문서 파편화 방지 및 일관된 작업 환경 구축

## 🎯 핵심 원칙

### 1. 단일 진실 원천 (Single Source of Truth)
- **documents/**: 모든 프로젝트 관리 문서의 유일한 위치
- **scripts/**: 모든 작업용 스크립트의 유일한 위치
- **.github/instructions/**: 모든 작업 지침의 유일한 위치

### 2. 파편화 방지 (Anti-Fragmentation)
- 중복 문서 생성 금지
- 임시 파일은 즉시 정리
- 비슷한 내용은 기존 문서에 통합

### 3. 신규자 친화 (Newcomer-Friendly)
- 특정 폴더만 읽어도 전체 현황 파악 가능
- 명확한 읽기 순서 제공
- 즉시 실행 가능한 가이드 제공

---

## 📂 필수 폴더 구조

### 📄 **documents/ (프로젝트 문서)**
```
documents/
├── README.md                    # 📚 필수 읽기 - 폴더 가이드
├── project-status.md           # 📊 실시간 현황 (최우선)
├── freshservice-masterplan.md  # 📋 전체 계획
├── work-guidelines.md          # 📝 작업 표준
├── csv-conversion-guide.md     # 📄 변환 가이드
└── mdx-troubleshooting.md      # 🚨 문제해결
```

### 🛠️ **scripts/ (작업 스크립트)**
```
scripts/
├── mdx_fixer.py               # MDX 호환성 자동 수정
├── auto_converter.py          # CSV → Markdown 변환
├── extract_*.py               # 데이터 추출 도구
└── (새로운 스크립트들...)
```

### 📋 **.github/instructions/ (작업 지침)**
```
.github/instructions/
├── workspace-organization.md   # 이 문서
├── markdown-rewriting.instructions.md
├── mdx-compatibility-guide.md
└── (기타 기술 지침들...)
```

---

## ⚠️ 작업 시 필수 규칙

### ✅ **문서 생성 시 반드시 해야 할 것**

1. **위치 확인**: 올바른 폴더에 생성하는가?
   - 프로젝트 관리 → `documents/`
   - 스크립트 → `scripts/`
   - 작업 지침 → `.github/instructions/`

2. **중복 검사**: 비슷한 문서가 이미 있는가?
   - 있으면 기존 문서 업데이트
   - 없으면 새로 생성

3. **README 업데이트**: 새 문서 추가 시
   - `documents/README.md` 업데이트
   - 읽기 순서에 추가

4. **명명 규칙**: 
   - 명확하고 설명적인 파일명
   - 케밥 케이스 사용 (`kebab-case.md`)
   - 버전/날짜 포함 금지

### ❌ **절대 하지 말아야 할 것**

1. **파편화된 문서 생성**
   - "완료", "최종", "FINAL" 등 버전 문서
   - 임시 문서를 그대로 방치
   - 비슷한 내용의 여러 문서

2. **잘못된 위치에 파일 생성**
   - 루트 디렉토리에 임시 파일
   - docs/ 폴더에 관리 문서
   - 무작위 위치에 스크립트

3. **README 업데이트 누락**
   - 새 문서 추가 후 README 미업데이트
   - 읽기 순서 미반영

---

## 🔄 작업 워크플로우

### 새로운 작업 시작 시

1. **현황 파악** (필수 순서)
   ```bash
   # 1. documents 폴더로 이동
   cd documents/
   
   # 2. README 읽기 (전체 가이드)
   cat README.md
   
   # 3. 현재 상태 확인
   cat project-status.md
   
   # 4. 작업 지침 확인
   cat work-guidelines.md
   ```

2. **작업 계획 수립**
   - 기존 문서에 추가할 내용인가?
   - 새로운 문서가 필요한가?
   - 스크립트 개발이 필요한가?

3. **작업 실행**
   - 적절한 폴더에서 작업
   - 명명 규칙 준수
   - 즉시 테스트

4. **정리 및 문서화**
   - README 업데이트
   - 프로젝트 상태 갱신
   - 임시 파일 정리

### 문서 작성 시

```bash
# 올바른 예시
documents/new-feature-guide.md     ✅
scripts/data-processor.py          ✅
.github/instructions/api-guide.md  ✅

# 잘못된 예시
new-document-final-v2.md          ❌
temp_script.py                    ❌
docs/project-notes.md             ❌
```

### 스크립트 개발 시

```bash
# 위치
scripts/

# 명명 규칙
feature_processor.py              ✅
data_converter.py                 ✅
quality_validator.py              ✅

# 금지
temp.py                           ❌
script1.py                        ❌
test_final.py                     ❌
```

---

## 📊 품질 관리

### 주간 정리 체크리스트

- [ ] **중복 문서 제거**: 비슷한 내용 통합
- [ ] **임시 파일 정리**: temp, test, final 등 제거
- [ ] **README 업데이트**: 새로운 내용 반영
- [ ] **파일명 정규화**: 규칙에 맞지 않는 이름 수정
- [ ] **링크 검증**: 모든 문서 간 링크 확인

### 월간 구조 검토

- [ ] **폴더 구조 최적화**: 불필요한 중첩 제거
- [ ] **문서 분류 재검토**: 적절한 위치에 있는가?
- [ ] **작업 지침 업데이트**: 새로운 패턴 반영
- [ ] **성과 측정**: 파편화 감소 효과 확인

---

## 🚀 신규 작업자 온보딩

### 첫 30분 필수 과정

1. **documents/README.md** (5분)
   - 전체 폴더 구조 이해
   - 읽기 순서 파악

2. **documents/project-status.md** (10분)
   - 현재 진행 상황
   - 완료된 작업 확인

3. **documents/work-guidelines.md** (10분)
   - 작업 표준 및 규칙
   - 품질 기준 이해

4. **이 문서** (5분)
   - 파일 생성 규칙
   - 금지 사항 숙지

### 즉시 실행 가능한 첫 작업

```bash
# 1. 환경 확인
ls documents/
ls scripts/
ls .github/instructions/

# 2. 현재 상태 파악
cat documents/project-status.md

# 3. 간단한 테스트
python scripts/mdx_fixer.py --help
```

---

## 📋 체크리스트 템플릿

### 새 문서 생성 시

- [ ] 적절한 폴더에 생성 (`documents/`, `scripts/`, `.github/instructions/`)
- [ ] 기존 중복 문서 확인 및 통합 검토
- [ ] 명확하고 설명적인 파일명 사용
- [ ] 케밥 케이스 명명 규칙 준수
- [ ] README 업데이트 (해당하는 경우)
- [ ] 링크 및 참조 확인
- [ ] 임시 파일 정리

### 작업 완료 시

- [ ] 모든 생성된 파일이 올바른 위치에 있음
- [ ] README 파일들이 최신 상태로 업데이트됨
- [ ] 임시 파일 및 중복 파일 정리됨
- [ ] 프로젝트 상태 문서 갱신됨
- [ ] 다음 작업자가 즉시 이해할 수 있는 상태

---

> **💡 핵심 메시지**: "새로운 작업자가 documents/ 폴더만 보고 30분 내에 전체 현황을 파악하고 즉시 기여할 수 있어야 한다"
