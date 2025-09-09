# 🎯 FAQ 크로스 폴더 전략 (올바른 디렉토리 구조)

## 📁 **올바른 디렉토리 구조**

```
docs/freshworks/freshservice/freshservice-faqs/
├── api-and-webhooks/
│   └── index.md (API FAQ 16개)
├── automations-and-triggers/
│   └── index.md (자동화 FAQ 59개)
├── agents-and-groups/
│   └── index.md (상담원 FAQ 32개)
├── asset-management/
│   └── index.md (자산 관리 FAQ 45개)
├── business-hours-and-slas/
│   └── index.md (업무 시간 FAQ 10개)
├── changes/
│   └── index.md (변경 관리 FAQ 51개)
├── email/
│   └── index.md (이메일 FAQ 22개)
├── ... (총 28개 폴더)
└── reports/
    └── index.md (리포트 FAQ 38개)
```

## 🚀 **크로스 폴더 배치 전략**

### **1단계: 텍스트 전용 문서 배치 (329개 - 1-2일)**

#### **100% 텍스트 폴더들 (즉시 완료)**
```bash
# 이 폴더들은 모든 FAQ가 텍스트만
docs/freshworks/freshservice/freshservice-faqs/
├── pricing-faq/index.md (2개 완성)
├── gamification-and-arcade/index.md (5개 완성)
├── sandbox/index.md (13개 완성)
├── orchestration/index.md (1개 완성)
└── affliate-marketing/index.md (1개 완성)

# 총 22개 FAQ 즉시 완성
```

#### **90%+ 텍스트 폴더들 (빠른 처리)**
```bash
# 이 폴더들은 대부분 텍스트 + 소수 복합 요소
docs/freshworks/freshservice/freshservice-faqs/
├── business-hours-and-slas/index.md (9개 텍스트 먼저)
├── problem/index.md (23개 텍스트 먼저)
├── email/index.md (19개 텍스트 먼저)
├── feedback-widget/index.md (11개 텍스트 먼저)
└── api-and-webhooks/index.md (13개 텍스트 먼저)

# 총 75개 텍스트 FAQ 먼저 완성
```

### **2단계: 복합 요소 문서 배치 (179개 - 2-4주)**

#### **복합 요소가 많은 폴더들**
```bash
# 이미지/테이블이 많은 폴더들은 수동 처리
docs/freshworks/freshservice/freshservice-faqs/
├── automations-and-triggers/index.md (42개 복합 요소)
├── changes/index.md (19개 복합 요소)
├── asset-management/index.md (18개 복합 요소)
├── reports/index.md (14개 복합 요소)
└── service-catalog/index.md (15개 복합 요소)
```

## 🎯 **작업 순서**

### **Phase 1: 크로스 폴더 텍스트 배치**
```bash
# 1일차: 가장 쉬운 폴더들부터
1. 모든 폴더에서 텍스트만 문서 추출 (329개)
2. 자동 번역 + 아코디언 형태 변환
3. 각 폴더에 index.md 생성

# 결과: 28개 폴더 모두에 기본 FAQ 완성
```

### **Phase 2: 폴더별 순차 완성**
```bash
# 텍스트 100% 폴더부터 완전 완성
1. pricing-faq/ (2개) ✅ 완성
2. gamification-and-arcade/ (5개) ✅ 완성
3. sandbox/ (13개) ✅ 완성
...

# 그 다음 90%+ 폴더들
1. business-hours-and-slas/ (1개 복합 요소 추가)
2. problem/ (3개 복합 요소 추가)
...
```

### **Phase 3: 원본 순서 재배치**
```bash
# 각 폴더에서 원본 position 순서로 재정렬
for folder in /docs/freshworks/freshservice/freshservice-faqs/*/
do
    reorder_by_original_position $folder
done
```

## 📋 **Sidebars 구성**

```typescript
// sidebars.ts
const sidebars = {
  tutorialSidebar: [
    {
      type: 'category',
      label: 'Freshservice FAQs',
      items: [
        'freshworks/freshservice/freshservice-faqs/api-and-webhooks/index',
        'freshworks/freshservice/freshservice-faqs/automations-and-triggers/index',
        'freshworks/freshservice/freshservice-faqs/agents-and-groups/index',
        // ... 28개 폴더
      ],
    },
  ],
};
```

## 🎯 **예상 성과**

### **1주일 후**
- ✅ 28개 FAQ 폴더 모두 기본 완성
- ✅ 329개 텍스트 FAQ 완전 서비스 가능
- ✅ 사용자가 모든 주제에서 기본 답변 확인 가능

### **1개월 후**  
- ✅ 508개 FAQ 완전 완성
- ✅ 이미지/테이블/코드까지 완벽 복원
- ✅ 원본 순서대로 최적화된 사용자 경험

이 구조가 **가장 체계적이고 확장 가능한** 방식입니다! 🚀
