import type { SidebarsConfig } from '@docusaurus/plugin-content-docs';

const sidebars: SidebarsConfig = {
  tutorialSidebar: [
    // 시작하기 페이지를 맨 위에 배치
    'intro',

    // Freshworks 제품군
    {
      type: 'category',
      label: '🎧 Freshworks',
      collapsed: false,
      items: [
        // Freshservice - IT 서비스 관리
        {
          type: 'category',
          label: '🔧 Freshservice (ITSM)',
          collapsed: false,
          items: [
            {
              type: 'category',
              label: '🚀 PoC 가이드',
              collapsed: true,
              items: [
                'freshworks/freshservice/poc-guides/comprehensive-poc-guide',
              ],
            },
            {
              type: 'category',
              label: '📚시작하기',
              collapsed: true,
              items: [
                {
                  type: 'category',
                  label: '👥 사용자 관리',
                  collapsed: true,
                  items: [
                    'freshworks/freshservice/getting-started/user-management/understanding-agents',
                    'freshworks/freshservice/getting-started/user-management/setting-agent-roles-permissions',
                    'freshworks/freshservice/getting-started/user-management/managing-requesters',
                    'freshworks/freshservice/getting-started/user-management/importing-requesters-csv',
                    'freshworks/freshservice/getting-started/user-management/finding-agent-user-id',
                    'freshworks/freshservice/getting-started/user-management/adding-custom-fields-users',
                    'freshworks/freshservice/getting-started/user-management/csv-import-guidelines',
                    'freshworks/freshservice/getting-started/user-management/merging-requesters',
                    'freshworks/freshservice/getting-started/user-management/password-policy-setup',
                    'freshworks/freshservice/getting-started/user-management/changing-requester-password',
                    'freshworks/freshservice/getting-started/user-management/adding-custom-fields-departments',
                    'freshworks/freshservice/getting-started/user-management/exporting-agent-information',
                    'freshworks/freshservice/getting-started/user-management/importing-agent-information',
                    'freshworks/freshservice/getting-started/user-management/automatically-associating-contacts-companies',
                    'freshworks/freshservice/getting-started/user-management/add-members-observers-agent-groups',
                    'freshworks/freshservice/getting-started/user-management/create-manage-agent-groups',
                    'freshworks/freshservice/getting-started/user-management/create-manage-requester-groups',
                    'freshworks/freshservice/getting-started/user-management/managing-requesters-freshservice',
                    'freshworks/freshservice/getting-started/user-management/importing-departments-companies-csv',
                    'freshworks/freshservice/getting-started/user-management/merging-users-advanced-scenarios',
                  ],
                },
                {
                  type: 'category',
                  label: '🌐 셀프 서비스 포털',
                  collapsed: true,
                  items: [
                    'freshworks/freshservice/getting-started/self-service-portal-introduction/service-desk-branding',
                    'freshworks/freshservice/getting-started/self-service-portal-introduction/vanity-url-setup',
                    'freshworks/freshservice/getting-started/self-service-portal-introduction/portal-access-login',
                    'freshworks/freshservice/getting-started/self-service-portal-introduction/custom-ssl-certificate',
                    'freshworks/freshservice/getting-started/self-service-portal-introduction/chatbot-conversational-portal',
                  ],
                },
                {
                  type: 'category',
                  label: '⚙️ 시스템 설정',
                  collapsed: true,
                  items: [
                    'freshworks/freshservice/getting-started/setting-up-freshservice/freshservice-onboarding-flow',
                    'freshworks/freshservice/getting-started/setting-up-freshservice/freshservice-system-requirements',
                    'freshworks/freshservice/getting-started/setting-up-freshservice/setting-up-custom-mailbox',
                    'freshworks/freshservice/getting-started/setting-up-freshservice/managing-agents-freshservice',
                    'freshworks/freshservice/getting-started/setting-up-freshservice/scanning-discovering-assets-network',
                    'freshworks/freshservice/getting-started/setting-up-freshservice/time-zones-supported',
                    'freshworks/freshservice/getting-started/setting-up-freshservice/languages-supported',
                    'freshworks/freshservice/getting-started/setting-up-freshservice/managing-service-catalog',
                    'freshworks/freshservice/getting-started/setting-up-freshservice/managing-sla-policy',
                  ],
                },
                {
                  type: 'category',
                  label: '📝 폼 및 템플릿',
                  collapsed: true,
                  items: [
                    'freshworks/freshservice/getting-started/form-fields-and-form-templates/understanding-different-types-ticket-fields',
                    'freshworks/freshservice/getting-started/form-fields-and-form-templates/setting-up-form-fields-tickets-problems-changes-releases',
                    'freshworks/freshservice/getting-started/form-fields-and-form-templates/creating-custom-fields-ticket-problem-change-release-task-form',
                    'freshworks/freshservice/getting-started/form-fields-and-form-templates/understanding-dependent-fields',
                    'freshworks/freshservice/getting-started/form-fields-and-form-templates/using-dependent-fields-tickets-problems-changes-releases',
                    'freshworks/freshservice/getting-started/form-fields-and-form-templates/setting-up-dropdown-fields',
                    'freshworks/freshservice/getting-started/form-fields-and-form-templates/setting-up-multi-select-dropdown',
                    'freshworks/freshservice/getting-started/form-fields-and-form-templates/setting-up-rich-text-sections-content-fields',
                    'freshworks/freshservice/getting-started/form-fields-and-form-templates/dynamic-sections',
                    'freshworks/freshservice/getting-started/form-fields-and-form-templates/archive-delete-custom-ticket-field',
                    'freshworks/freshservice/getting-started/form-fields-and-form-templates/creating-ticket-change-template',
                    'freshworks/freshservice/getting-started/form-fields-and-form-templates/create-no-code-dynamic-forms-business-rules',
                    'freshworks/freshservice/getting-started/form-fields-and-form-templates/create-no-code-dynamic-change-forms-business-rules',
                    'freshworks/freshservice/getting-started/form-fields-and-form-templates/business-rules-usecases',
                    'freshworks/freshservice/getting-started/form-fields-and-form-templates/business-rules-troubleshooting-guide',
                    'freshworks/freshservice/getting-started/form-fields-and-form-templates/customizing-service-desk-statuses',
                  ],
                },
              ],
            },
            {
              type: 'category',
              label: '❓ FAQ',
              collapsed: true,
              items: [
                {
                  type: 'doc',
                  id: 'freshworks/freshservice/faqs/agents-and-groups/index',
                  label: '에이전트 및 그룹',
                },
                {
                  type: 'doc',
                  id: 'freshworks/freshservice/faqs/analytics-faqs/index',
                  label: '분석 및 리포트',
                },
                {
                  type: 'doc',
                  id: 'freshworks/freshservice/faqs/announcements/index',
                  label: '공지사항',
                },
                {
                  type: 'doc',
                  id: 'freshworks/freshservice/faqs/api-webhooks/index',
                  label: 'API & Webhooks',
                },
                {
                  type: 'doc',
                  id: 'freshworks/freshservice/faqs/asset-management/index',
                  label: '자산 관리',
                },
                {
                  type: 'doc',
                  id: 'freshworks/freshservice/faqs/automations-triggers/index',
                  label: '자동화 및 트리거',
                },
                {
                  type: 'doc',
                  id: 'freshworks/freshservice/faqs/business-hours-slas/index',
                  label: '업무 시간 및 SLA',
                },
                {
                  type: 'doc',
                  id: 'freshworks/freshservice/faqs/changes/index',
                  label: '변경 관리',
                },
                {
                  type: 'doc',
                  id: 'freshworks/freshservice/faqs/email/index',
                  label: '이메일',
                },
                {
                  type: 'doc',
                  id: 'freshworks/freshservice/faqs/email-notifications/index',
                  label: '이메일 알림',
                },
                {
                  type: 'doc',
                  id: 'freshworks/freshservice/faqs/feedback-widget/index',
                  label: '피드백 위젯',
                },
                {
                  type: 'doc',
                  id: 'freshworks/freshservice/faqs/incidents-service-requests/index',
                  label: '인시던트 및 서비스 요청',
                },
                {
                  type: 'doc',
                  id: 'freshworks/freshservice/faqs/new-gen-project-mgmt/index',
                  label: '신세대 프로젝트 관리',
                },
                {
                  type: 'doc',
                  id: 'freshworks/freshservice/faqs/orchestration/index',
                  label: '오케스트레이션',
                },
                {
                  type: 'doc',
                  id: 'freshworks/freshservice/faqs/pricing-faq/index',
                  label: '가격 정책',
                },
                {
                  type: 'doc',
                  id: 'freshworks/freshservice/faqs/priority-matrix/index',
                  label: '우선순위 매트릭스',
                },
                {
                  type: 'doc',
                  id: 'freshworks/freshservice/faqs/problems/index',
                  label: '문제 관리',
                },
                {
                  type: 'doc',
                  id: 'freshworks/freshservice/faqs/release/index',
                  label: '릴리스 관리',
                },
                {
                  type: 'doc',
                  id: 'freshworks/freshservice/faqs/reports/index',
                  label: '보고서',
                },
                {
                  type: 'doc',
                  id: 'freshworks/freshservice/faqs/sandbox/index',
                  label: '샌드박스',
                },
                {
                  type: 'doc',
                  id: 'freshworks/freshservice/faqs/service-catalog/index',
                  label: '서비스 카탈로그',
                },
                {
                  type: 'doc',
                  id: 'freshworks/freshservice/faqs/service-desk-faq/index',
                  label: '서비스 데스크 FAQ',
                },
                {
                  type: 'doc',
                  id: 'freshworks/freshservice/faqs/sso/index',
                  label: 'SSO 및 인증',
                },
                {
                  type: 'doc',
                  id: 'freshworks/freshservice/faqs/tasks/index',
                  label: '작업 관리',
                },
                {
                  type: 'doc',
                  id: 'freshworks/freshservice/faqs/ticketing-workflow/index',
                  label: '티켓팅 워크플로우',
                },
                {
                  type: 'doc',
                  id: 'freshworks/freshservice/faqs/workspaces/index',
                  label: '워크스페이스',
                },
              ],
            },
          ],
        },
      ],
    },
  ],
};

export default sidebars;
