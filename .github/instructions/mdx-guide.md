# Freshservice 문서 MDX 호환성 가이드

> **목적**: CSV에서 변환된 Freshservice 문서가 Docusaurus에서 오류 없이 빌드되도록 하는 가이드

## 🚨 주요 문제와 해결책

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

## 📋 작업 워크플로우

### 새로운 CSV 문서 추가 시:
1. CSV에서 Markdown 변환 실행
2. `python3 mdx_fixer.py` 실행
3. `npm start` 실행하여 오류 확인
4. 오류가 없으면 완료! 🎉

### 기존 문서 수정 시:
- 수동으로 위의 패턴들을 확인하거나
- `mdx_fixer.py` 실행하여 자동 처리

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
