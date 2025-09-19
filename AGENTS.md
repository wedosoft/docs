# Repository Guidelines

## Project Structure & Module Organization
사이트는 Docusaurus 3 기반이며 설정은 `docusaurus.config.ts`와 `sidebars.ts`에서 관리합니다. 문서는 `docs/{product}/{category}/{folder}/{article}` 4단계 구조를 따라야 하며, 슬러그 규칙은 `.github/instructions/unified-doc-template.md`를 참조하세요. 작업용 스크립트는 `scripts/`, 변환 가이드와 상태 보고서는 `documents/`, 원본 CSV는 `categories/`와 `raw_data/`, 커스텀 컴포넌트와 테마는 `src/`, 정적 에셋은 `static/`에 있습니다.

## Build, Test, and Development Commands
Node 18 이상에서 `npm install`로 의존성을 설치합니다. `npm start`는 라이브 미리보기 개발 서버를, `npm run build`는 프로덕션 번들을, `npm run serve`는 빌드 결과 검수를 제공합니다. `npm run clear`로 Docusaurus 캐시를 비우고, TypeScript 변경 시 `npm run typecheck`로 타입 검사를 실행하세요. 대량 변환 후에는 `python3 scripts/mdx_fixer.py docs/freshservice/...`로 HTML 조각을 정규화합니다.

## Content Style & Naming Conventions
Frontmatter는 `sidebar_position`만 유지하고 나머지는 제거합니다. 원본 HTML, 이미지, 테이블, 링크, 스타일은 반드시 보존하며 필요할 때만 한국어 설명을 덧붙입니다. 콜아웃은 `:::info`, `:::warning`, `:::tip`, `:::success`만 사용하고, 코드 블록에는 언어 힌트를 지정하세요. 파일명은 소문자-하이픈 슬러그(예: `auto-close-resolved-tickets-48hours.md`), 폴더도 3~4단어 이내 핵심 키워드로 정리합니다. MDX/TSX는 2칸 들여쓰기를 유지합니다.

## Testing & QA Workflow
변경 전후로 `npm run build`를 실행해 MDX 문법과 링크를 검증하고, TSX나 설정을 수정했다면 `npm run typecheck`를 병행합니다. 변환 문서는 `python3 scripts/mdx_fixer.py <target-dir>`로 통일성을 확보하고, 필요 시 `npm run serve` 또는 `npm start`에서 시각적 이상을 확인합니다. 빌드가 실패하면 캐시를 정리한 뒤 재시도하세요.

## Localization & Tone Guidelines
한국어 번역은 실무 중심으로 의역하고, 제품 고유 용어는 원문을 괄호로 병기합니다. 특정 기업 대신 "대기업", "제조업체"와 같은 일반 명사를 사용하고, 초보자에게 어려운 용어에는 짧은 설명을 추가합니다. 문서 하나만으로 작업이 끝나도록 단계와 예시를 구체적으로 작성하세요.

## Commit & Pull Request Guidelines
커밋 메시지는 명령형 한 문장으로 작성하고 필요 시 `docs:`·`build:` 접두어를 붙입니다. PR에는 요약, 영향받은 디렉터리, 실행한 검증 명령(`npm run build` 등), 시각적 변화 스크린샷 또는 dev 링크를 포함하세요. CSV 데이터나 참고 문서를 근거로 삼았다면 링크를 남기고, 리뷰어가 확인해야 할 질문은 PR 본문에 명시합니다.

## HTML/MDX Compatibility & Error Resolution
HTML 태그가 포함된 마크다운 파일을 MDX로 변환할 때 발생하는 호환성 문제를 해결하는 방법입니다.

### 자동화 도구 활용
- **Prettier**: `npm install -g prettier` 설치 후 `prettier --write --parser markdown *.md`로 마크다운 파일 자동 포맷팅
- **Markdownlint**: `npm install -g markdownlint-cli` 설치 후 `markdownlint --fix *.md`로 문법 오류 자동 수정
- **MDX Fixer**: 프로젝트 내 `python3 scripts/mdx_fixer.py <target-dir>`로 HTML 조각 정규화

### 일반적인 HTML 태그 오류 패턴
1. **Self-closing 태그 문제**: `<img>`, `<br>`, `<hr>` 등은 반드시 `<img />`, `<br />`, `<hr />`로 작성
2. **이중 슬래시 오류**: `//>`를 `/>`로 수정 (`sed -i '' 's|//></span>|/></span>|g' *.md`)
3. **unclosed 태그**: 모든 열린 태그는 반드시 닫혀야 함

### 빌드 오류 대응 절차
1. `npm run build` 실행하여 오류 확인
2. 오류 메시지에서 파일명과 줄 번호 확인
3. 해당 위치의 HTML 태그 구문 수정
4. 자동화 도구로 일괄 수정 후 재빌드
5. 캐시 문제 시 `npm run clear` 실행

## Employee Onboarding Project Status (2025.09.19 완료)

### 완료된 작업
✅ **폴더 구조 통합**: 중복된 3개 폴더를 `docs/freshservice/enterprise-service-management/employee-onboarding-and-offboarding/` 하나로 통합  
✅ **파일 정리**: 28개 중복 파일을 15개 핵심 파일로 정리 (재작성 12개 + 기존 핵심 3개)  
✅ **네비게이션 수정**: `sidebars.ts`에서 삭제된 13개 파일 참조 제거  
✅ **자동화 도구 도입**: Prettier, Markdownlint 설치 및 포맷팅 완료  

### 남은 작업 (후속 작업자 진행 필요)
🔧 **HTML 태그 호환성 수정**: 다음 5개 파일의 MDX 호환성 문제 해결 필요
- `configuring-offboarding-checklist.md` (line 35, column 267)
- `configuring-offboarding-form.md` (line 143, column 267)  
- `configuring-onboarding-form.md` (line 39, column 263)
- `creating-offboarding-tasks.md` (line 80, column 507)
- `creating-onboarding-tasks.md` (line 43, column 922)

### 수정 방법 가이드
```bash
# 작업 디렉터리로 이동
cd docs/freshservice/enterprise-service-management/employee-onboarding-and-offboarding

# 문제가 되는 HTML 태그 패턴 확인
grep -n "//>" *.md

# 자동 수정 실행
sed -i '' 's|" //>|" />|g' *.md
find . -name "*.md" -exec sed -i '' 's|<img \([^>]*\)>|<img \1 />|g' {} \;
find . -name "*.md" -exec sed -i '' 's|<br>|<br />|g' {} \;

# 빌드 테스트
npm run build
```

### 파일별 상세 현황
- **유지된 기존 파일**: `building-onboarding-kits.md`, `index.md`, `reports-onboarding-offboarding.md`
- **새로 작성된 파일**: 12개 (모든 주요 온보딩/오프보딩 기능 커버)
- **삭제된 중복 파일**: 13개 (내용 중복으로 통합됨)

## Reference Checklist
- `documents/project-status.md`와 `documents/work-guidelines.md`로 우선순위를 확인
- `.github/instructions/unified-doc-template.md`의 품질 체크리스트(실무 예시 2개 이상, Callout, 이미지 경로)를 준수
- Employee onboarding 프로젝트는 구조 정리 완료, HTML 태그 호환성만 수정하면 완전 완료
- 완료 후 `git status`로 변경 파일을 확인하고, 필요한 테스트 명령을 다시 기록하세요
