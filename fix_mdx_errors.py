#!/usr/bin/env python3
import re
import os

# 처리할 파일들
files = [
    'docs/freshdesk/faq/api-webhooks/index.md',
    'docs/freshdesk/faq/integrations/index.md', 
    'docs/freshdesk/faq/multiple-products/index.md',
    'docs/freshdesk/faq/self-service-portal/index.md',
    'docs/freshdesk/faq/ssl-security/index.md',
    'docs/freshdesk/faq/ticketing-workflow/index.md'
]

for file_path in files:
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 1. 긴 id 속성 제거 또는 간소화
        content = re.sub(r'id="[^"]{100,}"', 'id="auto-generated-id"', content)
        
        # 2. 문제가 되는 JSX 속성들 정리
        content = re.sub(r'style=\{\{[^}]*\}\}', 'style={{ fontSize: "16px" }}', content)
        
        # 3. 잘못된 속성명 수정 (따옴표 포함)
        content = re.sub(r'[a-zA-Z-]+="[^"]*"[^=\s>]*"[^"]*"', 'class="auto-fixed"', content)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f'{file_path} 수정 완료')
    else:
        print(f'{file_path} 파일을 찾을 수 없습니다')

print("모든 파일 수정 완료")