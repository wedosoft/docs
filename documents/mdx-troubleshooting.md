# 🚨 MDX 문제해결 가이드

> **목적**: Docusaurus MDX 빌드 오류 및 호환성 문제 해결 방법

## ⚡ 긴급 상황 해결

### 빌드 실패 시 즉시 확인할 것
```bash
# 1. 빌드 로그 확인
npm run build

# 2. 개발 서버로 상세 오류 확인
npm start

# 3. 특정 파일 문제인지 확인
npm run build -- --locale en
```

---

## 🔧 자주 발생하는 오류와 해결법

### 1. 한글 중괄호 오류
**오류 메시지**
```
Error: Unexpected token (1:15)
  1 | {워크스페이스명}
    |               ^
```

**해결 방법**
```markdown
# Before (오류 발생)
{워크스페이스명}
{사용자명}
{티켓제목}

# After (정상 작동)
&#123;워크스페이스명&#125;
&#123;사용자명&#125;
&#123;티켓제목&#125;
```

**자동 수정 스크립트**
```python
# mdx_fixer.py 사용
python mdx_fixer.py target_file.md
```

### 2. Freshservice 자리표시자 오류
**오류 메시지**
```
Error: Expected corresponding JSX closing tag for <ticket>
```

**해결 방법**
```markdown
# Before (오류 발생)
{{ticket.id}}
{{user.name}}
{{company.domain}}

# After (정상 작동)
`{{ticket.id}}`
`{{user.name}}`
`{{company.domain}}`
```

### 3. Style 속성 오류
**오류 메시지**
```
Error: Style prop value must be an object
```

**해결 방법**
```markdown
# Before (오류 발생)
<span style="color: red; margin: 10px;">텍스트</span>
<div style="background-color: yellow;">내용</div>

# After (정상 작동)
<span style={{ color: 'red', margin: '10px' }}>텍스트</span>
<div style={{ backgroundColor: 'yellow' }}>내용</div>
```

**변환 규칙**
```javascript
// CSS 속성명 변환
margin-top    → marginTop
background-color → backgroundColor
font-size     → fontSize
border-radius → borderRadius

// 값 변환
10px    → '10px'
red     → 'red'
#ffffff → '#ffffff'
```

### 4. 잘못된 JSX 구조
**오류 메시지**
```
Error: Unexpected token <
Error: Expected corresponding JSX closing tag
```

**해결 방법**
```markdown
# Before (오류 발생)
<div class="highlight">
<span>내용</span>

# After (정상 작동)
<div className="highlight">
<span>내용</span>
</div>
```

---

## 🛠️ 자동화 도구 사용법

### mdx_fixer.py 스크립트
```bash
# 단일 파일 수정
python mdx_fixer.py file.md

# 폴더 전체 수정
python mdx_fixer.py folder_name/

# 백업과 함께 수정
python mdx_fixer.py file.md --backup
```

**스크립트 기능**
- ✅ 한글 중괄호 자동 이스케이프
- ✅ Freshservice 자리표시자 백틱 처리
- ✅ Style 속성 JSX 형식 변환
- ✅ HTML 주석 내용 보호
- ✅ 백업 파일 생성

### 검증 명령어
```bash
# MDX 문법 검사
npx @mdx-js/mdx file.md

# Docusaurus 빌드 테스트
npm run build

# 특정 로케일만 빌드
npm run build -- --locale en
```

---

## 🔍 오류 디버깅 방법

### 1. 오류 위치 특정
```bash
# 빌드 로그에서 오류 파일 찾기
npm run build 2>&1 | grep -E "Error|Failed"

# 특정 파일만 확인
npx @mdx-js/mdx docs/path/to/file.md
```

### 2. 문제 구간 격리
```markdown
<!-- 문제 구간을 주석으로 격리 -->
<!--
{문제가 되는 내용}
-->

<!-- 또는 임시로 백틱 처리 -->
`{문제가 되는 내용}`
```

### 3. 단계별 복원
```markdown
1. 가장 단순한 형태로 시작
2. 점진적으로 내용 추가
3. 각 단계마다 빌드 테스트
4. 오류 발생 지점 특정
```

---

## 📋 예방 체크리스트

### 문서 작성 시 필수 확인
- [ ] **중괄호 사용 금지** → 이스케이프 처리 또는 백틱 사용
- [ ] **Style 속성 검사** → JSX 형식 사용
- [ ] **HTML 태그 검증** → 올바른 열기/닫기
- [ ] **className 사용** → class 속성 금지
- [ ] **인용문 처리** → 특수문자 이스케이프

### 폴더 작업 완료 시
- [ ] **전체 빌드 테스트** → `npm run build`
- [ ] **개발 서버 확인** → `npm start`
- [ ] **링크 검증** → 모든 링크 작동 확인
- [ ] **이미지 표시 확인** → 모든 이미지 정상 로딩

---

## 🆘 긴급 상황 대응

### 빌드가 완전히 실패할 때
```bash
# 1. 최근 변경사항 확인
git diff HEAD~1

# 2. 문제 파일 임시 제거
mv problematic_file.md problematic_file.md.backup

# 3. 빌드 확인
npm run build

# 4. 문제 파일 개별 수정
# 5. 다시 추가
```

### 대량 오류 발생 시
```bash
# 1. mdx_fixer.py로 일괄 수정
python mdx_fixer.py docs/freshworks/freshservice/

# 2. 전체 빌드 테스트
npm run build

# 3. 개별 오류 수정
# 각 오류 메시지를 이 가이드와 대조하여 수정
```

---

## 📞 추가 지원

### 새로운 오류 패턴 발견 시
1. **오류 메시지 전체 복사**
2. **문제 파일 및 해당 라인 특정**
3. **이 문서에 새로운 케이스 추가**
4. **mdx_fixer.py 스크립트 업데이트**

### 참고 자료
- [MDX 공식 문서](https://mdxjs.com/)
- [Docusaurus MDX 가이드](https://docusaurus.io/docs/markdown-features/react)
- [React JSX 문법](https://reactjs.org/docs/introducing-jsx.html)

---

> **💡 핵심 원칙**: MDX는 Markdown + JSX입니다. HTML처럼 보이지만 React 컴포넌트로 변환되므로 JSX 문법 규칙을 따라야 합니다.
