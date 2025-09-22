# Freshservice 문서 MDX 호환성 가이드

> **목적**: CSV에서 변환된 Freshservice 문서가 Docusaurus에서 오류 없이 빌드되도록 하는 가이드

## � MDX 호환성 강제 검증 시스템

### 📋 번역 전 HTML/MDX 호환성 선체크
- [ ] **HTML 태그 스캔**: 원본에 포함된 모든 HTML 태그를 식별했는가?
- [ ] **중괄호 패턴 확인**: `{변수명}`, `{product.name}` 등 모든 중괄호 패턴을 확인했는가?
- [ ] **Self-closing 태그 점검**: `<img>`, `<br>`, `<hr>` 태그가 있는지 확인했는가?
- [ ] **Style 속성 확인**: HTML style 속성이 포함된 요소가 있는지 확인했는가?

### 🔄 번역 중 실시간 MDX 검증
- [ ] **태그 변환 즉시 확인**: HTML 태그를 MDX 호환 형태로 즉시 변환했는가?
- [ ] **중괄호 이스케이프 확인**: 각 중괄호를 발견할 때마다 즉시 처리했는가?
- [ ] **코드 블록 언어 지정**: 모든 코드 블록에 언어 힌트를 지정했는가?

### ✅ 번역 후 MDX 호환성 후체크
- [ ] **자동 처리 스크립트 실행**: `python3 scripts/fix_inline_styles.py` 등 실행했는가?
- [ ] **빌드 테스트**: `npm run build` 명령어로 오류 없음을 확인했는가?
- [ ] **브라우저 확인**: `npm start`로 실제 렌더링 상태를 확인했는가?

## �🚨 주요 문제와 해결책

### 1. **Freshservice Placeholder 오류**
```
❌ 오류: {ticket.id} is not defined
✅ 해결: `{ticket.id}` (백틱으로 감싸서 인라인 코드로 처리)
```

### 2. **한글 중괄호 오류**  
```
❌ 오류: {워크스페이스명} is not defined
✅ 해결: &#123;워크스페이스명&#125; (HTML 엔티티로 이스케이프)
```

### 3. **HTML Style 속성 오류**
```
❌ 오류: style="color: red" (HTML 문법)
✅ 해결: style={{color: 'red'}} (JSX 문법)
```

### 4. **문서 제목 서식 불일치**
```
❌ 다른 서식: <div class="subtitle">설명</div>
✅ 정상 서식: :::info 문서 목적\n설명\n:::
```

## 🛠️ 자동 처리 방법

### 방법 1: 전체 자동 처리 (권장)
```bash
cd /Users/alan/GitHub/docs
python3 mdx_fixer.py docs/freshworks/freshservice/
```

### 방법 2: 특정 폴더만 처리
```bash
python3 mdx_fixer.py docs/freshworks/freshservice/getting-started/user-management/
```

## 📋 작업 워크플로우 (강제 단계별 진행)

### PHASE 1: 번역 시작 전 (필수 선체크)
```bash
# 1. 원본 HTML 구조 분석
grep -n "<.*>" 원본파일.md | head -20
grep -n "{.*}" 원본파일.md | head -10

# 2. 백업 생성 (필수)
cp 원본파일.md 원본파일.backup.md
```

### PHASE 2: 번역 진행 중 (실시간 검증)
```bash
# 각 섹션 번역 후 즉시 MDX 검증
python3 scripts/fix_inline_styles.py 번역중파일.md
python3 scripts/fix_escaped_br_tags.py 번역중파일.md
```

### PHASE 3: 번역 완료 후 (최종 검증)
```bash
# 1. 전체 MDX 호환성 자동 처리
python3 scripts/fix_inline_styles.py docs/freshservice/target-directory/
python3 scripts/fix_escaped_br_tags.py docs/freshservice/target-directory/
python3 scripts/fix_escaped_html_imgs.py docs/freshservice/target-directory/

# 2. 빌드 테스트 (필수)
npm run build
# ⚠️ 145초 동안 절대 취소하지 말고 완료까지 대기

# 3. 개발 서버 확인 (권장)
npm start
# 브라우저에서 번역된 페이지 직접 확인
```

### 🚫 강제 중단 조건
**다음 상황 시 즉시 작업 중단하고 처음부터 재시작:**
- 선체크 없이 번역 시작한 경우
- 실시간 MDX 검증 없이 다음 섹션으로 진행한 경우  
- `npm run build` 실패 시 원인 해결 없이 진행하려는 경우

## 📋 작업 워크플로우

### 새로운 CSV 문서 추가 시 (강제 순서):
1. **PHASE 1 선체크**: 원본 HTML/중괄호 구조 분석 완료
2. **백업 생성**: 원본 파일 백업 생성 
3. **CSV에서 Markdown 변환 실행**
4. **PHASE 2 실시간 검증**: 각 섹션별 MDX 검증
5. **python3 scripts/mdx_fixer.py 실행**
6. **PHASE 3 최종 검증**: `npm run build` 성공 확인
7. **완료 조건**: 오류가 없으면 완료! 🎉

### 기존 문서 수정 시 (강제 순서):
1. **PHASE 1 선체크**: 기존 파일 HTML 구조 분석
2. **수동 수정 또는 mdx_fixer.py 실행하여 자동 처리**  
3. **PHASE 3 최종 검증**: 빌드 테스트 통과 확인

## 🔍 수동 확인이 필요한 경우

자동 스크립트가 놓칠 수 있는 패턴들:

1. **복잡한 JSX 구조**
2. **중첩된 중괄호** 
3. **특수한 Freshservice placeholder**

이런 경우 브라우저 개발자 도구에서 오류 메시지를 확인하고 수동 수정 필요.

## 📁 파일 위치

- `mdx_fixer.py`: 메인 자동 처리 스크립트
- `fix_braces.py`: 중괄호만 처리하는 구 스크립트 (삭제 가능)
- `brace_fix_helper.py`: 헬퍼 스크립트 (삭제 가능)

## ⚠️ 주의사항

1. **백업**: 대량 처리 전 Git commit 권장
2. **테스트**: 처리 후 반드시 `npm start`로 빌드 확인
3. **검토**: 중요한 문서는 수동 검토 권장

## 🆘 문제 해결

### "ReferenceError: XXX is not defined" 오류 시:
1. `mdx_fixer.py` 실행
2. 여전히 오류 시 해당 파일에서 `{XXX}` 패턴 찾아서 수동 수정

### "Could not parse expression with acorn" 오류 시:
1. 복잡한 중괄호 구조가 있는지 확인
2. 수동으로 이스케이프 처리 또는 백틱 처리

---

> **💡 팁**: 문제가 생기면 `mdx_fixer.py`를 먼저 실행해보세요. 대부분의 MDX 호환성 문제가 자동으로 해결됩니다!
