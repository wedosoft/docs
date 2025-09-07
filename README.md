# Website

This webs# 📚 Freshservice 문서 포털

> **목적**: CSV 데이터를 기반으로 Freshservice 기술문서를 Docusaurus 기반 웹사이트로 자동 변환

이 웹사이트는 [Docusaurus](https://docusaurus.io/)를 사용하여 구축된 현대적인 정적 웹사이트입니다.

## 🎯 프로젝트 개요

- **총 문서 수**: 1,557개 (CSV 데이터 기준)
- **현재 상태**: 1단계 완료 (74개 문서 v3.0 템플릿 적용)
- **다음 단계**: CSV → Markdown 자동 변환 시스템 구축

## 🚀 빠른 시작

### 설치

```bash
npm install
```

### 로컬 개발

```bash
npm start
```

개발 서버가 시작되고 브라우저 창이 열립니다. 대부분의 변경사항은 서버 재시작 없이 실시간으로 반영됩니다.

### 빌드

```bash
npm run build
```

## 📁 프로젝트 구조

```
├── 📄 documents/               # 프로젝트 관리 문서 (필독!)
│   ├── README.md              # 📚 documents 폴더 가이드
│   ├── project-status.md      # 📊 실시간 프로젝트 현황
│   ├── freshservice-masterplan.md # 📋 전체 마스터플랜
│   ├── work-guidelines.md     # 📝 작업 지침 및 표준
│   ├── csv-conversion-guide.md # 📄 CSV 변환 가이드
│   └── mdx-troubleshooting.md # 🚨 MDX 문제해결
├── 📖 docs/                   # 사용자 문서 (Docusaurus)
│   └── freshworks/freshservice/ # Freshservice 문서 (74개 완료)
├── 🛠️ scripts/                # 작업용 스크립트
│   └── mdx_fixer.py          # MDX 호환성 자동 처리
├── 📊 raw_data/               # 원본 CSV 데이터 (5개 파일, 1,557개 문서)
├── 🎨 src/                    # 사이트 소스 코드
└── 🔧 .github/                # 작업 지침 및 템플릿
```

## 👋 신규 작업자 가이드

### 1️⃣ 필수 읽기 순서
```
1. documents/README.md           - 전체 가이드 
2. documents/project-status.md   - 현재 진행 현황
3. documents/work-guidelines.md  - 작업 규칙
```

### 2️⃣ 상황별 참조
```
- documents/freshservice-masterplan.md - 전체 계획
- documents/csv-conversion-guide.md    - 2단계 작업 가이드  
- documents/mdx-troubleshooting.md     - 문제해결
```

## 🔧 주요 도구 및 스크립트

### MDX 호환성 자동 처리
```bash
# 전체 폴더 처리
python3 scripts/mdx_fixer.py docs/freshworks/freshservice/

# 특정 폴더 처리  
python3 scripts/mdx_fixer.py docs/freshworks/freshservice/user-management/

# 단일 파일 처리
python3 scripts/mdx_fixer.py docs/path/to/file.md
```

### 개발 및 테스트
```bash
# 개발 서버 시작
npm start

# 빌드 테스트
npm run build

# MDX 호환성 검사
python3 scripts/mdx_fixer.py docs/
```ilt using [Docusaurus](https://docusaurus.io/), a modern static website generator.

## 🚀 Quick Start

### Installation

```bash
$ yarn
```

### Local Development

```bash
$ yarn start
```

This command starts a local development server and opens up a browser window. Most changes are reflected live without having to restart the server.

## � 프로젝트 구조

```
├── docs/                    # 사용자 문서 (Docusaurus)
├── scripts/                 # 모든 작업용 스크립트
├── documents/               # 프로젝트 관리 문서
├── raw_data/               # 원본 CSV 데이터
└── src/                    # 사이트 소스 코드
```

## �📝 Freshservice 문서 작업

### MDX 호환성 자동 처리
새로운 CSV 문서를 추가하거나 MDX 오류가 발생할 때:

```bash
# 전체 처리
python3 scripts/mdx_fixer.py docs/freshworks/freshservice/

# 특정 폴더 처리  
python3 scripts/mdx_fixer.py docs/freshworks/freshservice/getting-started/

# 단일 파일 처리
python3 scripts/mdx_fixer.py docs/path/to/file.md
```

### 주요 스크립트들
- `scripts/mdx_fixer.py` - MDX 호환성 자동 처리
- `scripts/auto_converter.py` - CSV → Markdown 변환
- `scripts/extract_*.py` - 데이터 추출 도구

### 작업 가이드
- [프로젝트 파일 관리 지침](documents/project-file-management-guidelines.md)
- [MDX 호환성 가이드](.github/instructions/mdx-compatibility-guide.md)

## 📈 현재 진행 현황

### ✅ 1단계 완료 (2024년 12월)
- **템플릿 표준화**: 74개 문서 v3.0 템플릿 적용 완료
- **MDX 호환성**: 한글 중괄호 이스케이프 문제 해결
- **문서 품질**: 일관된 형식 및 구조 확립

### 🔄 2단계 준비 중 (2024년 12월 말 ~ 2025년 1월)
- **CSV 분석**: 5개 파일, 1,557개 문서 스키마 파악
- **자동 변환**: Python 기반 대량 변환 시스템 개발
- **품질 검증**: 자동화된 검증 및 테스트 체계 구축

## 🎯 성과 지표

- **완료율**: 4.8% (74/1,557 문서)
- **품질**: 100% 빌드 성공률
- **표준화**: v3.0 템플릿 완전 적용
- **호환성**: MDX 오류 0건

## 🚨 문제해결

### MDX 빌드 오류 시
```bash
# 자동 수정
python3 scripts/mdx_fixer.py problematic-file.md

# 전체 검사
npm run build
```

### 일반적인 오류들
- **한글 중괄브**: `{텍스트}` → `&#123;텍스트&#125;`
- **Style 속성**: `style="color: red"` → `style={{ color: 'red' }}`
- **Freshservice 플레이스홀더**: `{{ticket.id}}` → `` `{{ticket.id}}` ``

## 🏗️ 빌드 & 배포

### 프로덕션 빌드

```bash
npm run build
```

정적 콘텐츠가 `build` 디렉토리에 생성되며 정적 호스팅 서비스에서 제공할 수 있습니다.

### 배포

SSH 사용:

```bash
USE_SSH=true npm run deploy
```

SSH 미사용:

```bash
GIT_USER=<GitHub 사용자명> npm run deploy
```

GitHub Pages 호스팅을 사용하는 경우, 이 명령어로 웹사이트를 빌드하고 `gh-pages` 브랜치에 푸시할 수 있습니다.

---

> **💡 중요**: 신규 작업자는 반드시 `documents/` 폴더의 README부터 읽어주세요!
