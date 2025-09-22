import type { SidebarsConfig } from '@docusaurus/plugin-content-docs';

const sidebars: SidebarsConfig = {
  tutorialSidebar: [
    // 시작하기 페이지를 맨 위에 배치
    'intro',

    // Freshservice - IT 서비스 관리
    {
      type: 'category',
      label: '🔧 Freshservice (ITSM)',
      collapsed: false,
      items: [
        {
          type: 'category',
          label: '🧪 PoC 가이드',
          collapsed: true,
          items: [
            'freshservice/poc-guides/comprehensive-poc-guide',
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
                'freshservice/getting-started/user-management/understanding-agents',
                'freshservice/getting-started/user-management/setting-agent-roles-permissions',
                'freshservice/getting-started/user-management/managing-requesters',
                'freshservice/getting-started/user-management/importing-requesters-csv',
                'freshservice/getting-started/user-management/finding-agent-user-id',
                'freshservice/getting-started/user-management/adding-custom-fields-users',
                'freshservice/getting-started/user-management/csv-import-guidelines',
                'freshservice/getting-started/user-management/merging-requesters',
                'freshservice/getting-started/user-management/password-policy-setup',
                'freshservice/getting-started/user-management/changing-requester-password',
                'freshservice/getting-started/user-management/adding-custom-fields-departments',
                'freshservice/getting-started/user-management/exporting-agent-information',
                'freshservice/getting-started/user-management/importing-agent-information',
                'freshservice/getting-started/user-management/automatically-associating-contacts-companies',
                'freshservice/getting-started/user-management/add-members-observers-agent-groups',
                'freshservice/getting-started/user-management/create-manage-agent-groups',
                'freshservice/getting-started/user-management/create-manage-requester-groups',
                'freshservice/getting-started/user-management/managing-requesters-freshservice',
                'freshservice/getting-started/user-management/importing-departments-companies-csv',
                'freshservice/getting-started/user-management/merging-users-advanced-scenarios',
              ],
            },
            {
              type: 'category',
              label: '🌐 셀프 서비스 포털',
              collapsed: true,
              items: [
                'freshservice/getting-started/self-service-portal-introduction/service-desk-branding',
                'freshservice/getting-started/self-service-portal-introduction/vanity-url-setup',
                'freshservice/getting-started/self-service-portal-introduction/portal-access-login',
                'freshservice/getting-started/self-service-portal-introduction/custom-ssl-certificate',
                'freshservice/getting-started/self-service-portal-introduction/chatbot-conversational-portal',
              ],
            },
            {
              type: 'category',
              label: '⚙️ 시스템 설정',
              collapsed: true,
              items: [
                'freshservice/getting-started/setting-up-freshservice/freshservice-onboarding-flow',
                'freshservice/getting-started/setting-up-freshservice/freshservice-system-requirements',
                'freshservice/getting-started/setting-up-freshservice/setting-up-custom-mailbox',
                'freshservice/getting-started/setting-up-freshservice/managing-agents-freshservice',
                'freshservice/getting-started/setting-up-freshservice/scanning-discovering-assets-network',
                'freshservice/getting-started/setting-up-freshservice/time-zones-supported',
                'freshservice/getting-started/setting-up-freshservice/languages-supported',
                'freshservice/getting-started/setting-up-freshservice/managing-service-catalog',
                'freshservice/getting-started/setting-up-freshservice/managing-sla-policy',
              ],
            },
            {
              type: 'category',
              label: '📝 폼 및 템플릿',
              collapsed: true,
              items: [
                'freshservice/getting-started/form-fields-and-form-templates/understanding-different-types-ticket-fields',
                'freshservice/getting-started/form-fields-and-form-templates/setting-up-form-fields-tickets-problems-changes-releases',
                'freshservice/getting-started/form-fields-and-form-templates/creating-custom-fields-ticket-problem-change-release-task-form',
                'freshservice/getting-started/form-fields-and-form-templates/understanding-dependent-fields',
                'freshservice/getting-started/form-fields-and-form-templates/using-dependent-fields-tickets-problems-changes-releases',
                'freshservice/getting-started/form-fields-and-form-templates/setting-up-dropdown-fields',
                'freshservice/getting-started/form-fields-and-form-templates/setting-up-multi-select-dropdown',
                'freshservice/getting-started/form-fields-and-form-templates/setting-up-rich-text-sections-content-fields',
                'freshservice/getting-started/form-fields-and-form-templates/dynamic-sections',
                'freshservice/getting-started/form-fields-and-form-templates/archive-delete-custom-ticket-field',
                'freshservice/getting-started/form-fields-and-form-templates/creating-ticket-change-template',
                'freshservice/getting-started/form-fields-and-form-templates/create-no-code-dynamic-forms-business-rules',
                'freshservice/getting-started/form-fields-and-form-templates/create-no-code-dynamic-change-forms-business-rules',
                'freshservice/getting-started/form-fields-and-form-templates/business-rules-usecases',
                'freshservice/getting-started/form-fields-and-form-templates/business-rules-troubleshooting-guide',
                'freshservice/getting-started/form-fields-and-form-templates/customizing-service-desk-statuses',
              ],
            },
          ],
        },
        {
          type: 'category',
          label: '👨‍💼 관리자 가이드',
          collapsed: true,
          items: [
            {
              type: 'category',
              label: '⚙️ 관리자 설정',
              collapsed: true,
              items: [
                'freshservice/user-guide-admin/admin-settings/index',
                'freshservice/user-guide-admin/admin-settings/general-settings',
                'freshservice/user-guide-admin/admin-settings/user-management',
                'freshservice/user-guide-admin/admin-settings/service-desk-productivity',
                'freshservice/user-guide-admin/admin-settings/reorganization-renaming-admin',
                'freshservice/user-guide-admin/admin-settings/asset-management',
                'freshservice/user-guide-admin/admin-settings/export-service-desk-data',
              ],
            },
            {
              type: 'category',
              label: '🎯 시작하기',
              collapsed: true,
              items: [
                'freshservice/user-guide-admin/getting-started/index',
              ],
            },
            {
              type: 'category',
              label: '📊 CMDB',
              collapsed: true,
              items: [
                'freshservice/user-guide-admin/cmdb/index',
              ],
            },
            {
              type: 'category',
              label: '🚀 릴리스 관리',
              collapsed: true,
              items: [
                'freshservice/user-guide-admin/release-management/index',
              ],
            },
            {
              type: 'category',
              label: '💡 솔루션 (지식 베이스)',
              collapsed: true,
              items: [
                'freshservice/user-guide-admin/solutions/index',
              ],
            },
            {
              type: 'category',
              label: '🔄 변경 관리',
              collapsed: true,
              items: [
                'freshservice/user-guide-admin/change-management/index',
              ],
            },
            {
              type: 'category',
              label: '📋 인시던트 관리',
              collapsed: true,
              items: [
                'freshservice/user-guide-admin/incident-management/index',
              ],
            },
            {
              type: 'category',
              label: '🔍 문제 관리',
              collapsed: true,
              items: [
                'freshservice/user-guide-admin/problem-management/index',
              ],
            },
            {
              type: 'category',
              label: '📈 보고서',
              collapsed: true,
              items: [
                'freshservice/user-guide-admin/reports/index',
              ],
            },
          ],
        },
        {
          type: 'category',
          label: '📘 IT 서비스 관리 지원 가이드',
          collapsed: true,
          items: [
            {
              type: 'category',
              label: '📋 인시던트 관리',
              collapsed: true,
              items: [
                'freshservice/itsm/incident-management/understanding-sla-policies',
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
              id: 'freshservice/faqs/agents-and-groups/index',
              label: '에이전트 및 그룹',
            },
            {
              type: 'doc',
              id: 'freshservice/faqs/analytics-faqs/index',
              label: '분석 및 리포트',
            },
            {
              type: 'doc',
              id: 'freshservice/faqs/announcements/index',
              label: '공지사항',
            },
            {
              type: 'doc',
              id: 'freshservice/faqs/api-webhooks/index',
              label: 'API & Webhooks',
            },
            {
              type: 'doc',
              id: 'freshservice/faqs/asset-management/index',
              label: '자산 관리',
            },
            {
              type: 'doc',
              id: 'freshservice/faqs/automations-triggers/index',
              label: '자동화 및 트리거',
            },
            {
              type: 'doc',
              id: 'freshservice/faqs/business-hours-slas/index',
              label: '업무 시간 및 SLA',
            },
            {
              type: 'doc',
              id: 'freshservice/faqs/changes/index',
              label: '변경 관리',
            },
            {
              type: 'doc',
              id: 'freshservice/faqs/email/index',
              label: '이메일',
            },
            {
              type: 'doc',
              id: 'freshservice/faqs/email-notifications/index',
              label: '이메일 알림',
            },
            {
              type: 'doc',
              id: 'freshservice/faqs/feedback-widget/index',
              label: '피드백 위젯',
            },
            {
              type: 'doc',
              id: 'freshservice/faqs/incidents-service-requests/index',
              label: '인시던트 및 서비스 요청',
            },
            {
              type: 'doc',
              id: 'freshservice/faqs/new-gen-project-mgmt/index',
              label: 'New-Gen 프로젝트 관리',
            },
            {
              type: 'doc',
              id: 'freshservice/faqs/orchestration/index',
              label: '오케스트레이션',
            },
            {
              type: 'doc',
              id: 'freshservice/faqs/pricing-faq/index',
              label: '가격 정책',
            },
            {
              type: 'doc',
              id: 'freshservice/faqs/priority-matrix/index',
              label: '우선순위 매트릭스',
            },
            {
              type: 'doc',
              id: 'freshservice/faqs/problems/index',
              label: '문제 관리',
            },
            {
              type: 'doc',
              id: 'freshservice/faqs/release/index',
              label: '릴리스 관리',
            },
            {
              type: 'doc',
              id: 'freshservice/faqs/reports/index',
              label: '보고서',
            },
            {
              type: 'doc',
              id: 'freshservice/faqs/sandbox/index',
              label: '샌드박스',
            },
            {
              type: 'doc',
              id: 'freshservice/faqs/service-catalog/index',
              label: '서비스 카탈로그',
            },
            {
              type: 'doc',
              id: 'freshservice/faqs/service-desk-faq/index',
              label: '서비스 데스크 FAQ',
            },
            {
              type: 'doc',
              id: 'freshservice/faqs/sso/index',
              label: 'SSO 및 인증',
            },
            {
              type: 'doc',
              id: 'freshservice/faqs/tasks/index',
              label: '작업 관리',
            },
            {
              type: 'doc',
              id: 'freshservice/faqs/ticketing-workflow/index',
              label: '티켓팅 워크플로우',
            },
            {
              type: 'doc',
              id: 'freshservice/faqs/workspaces/index',
              label: '워크스페이스',
            },
          ],
        },
        {
          type: 'category',
          label: '🔧 플랫폼',
          collapsed: true,
          items: [
            'freshservice/platform/platform-components-overview',
            'freshservice/platform/platform-integration-guide',
            'freshservice/platform/platform-troubleshooting-guide',
            {
              type: 'category',
              label: '📊 분석 및 리포팅',
              collapsed: true,
              items: [
                {
                  type: 'category',
                  label: '📈 Analytics',
                  collapsed: true,
                  items: [
                    'freshservice/platform/analytics/understanding-the-service-desk-at-a-glance-report',
                    'freshservice/platform/analytics/analytics-data-warehouse-and-etl-processes',
                    'freshservice/platform/analytics/common-reports-using-analytics',
                    'freshservice/platform/analytics/comparing-multiple-metrics-in-a-widget',
                    'freshservice/platform/analytics/custom-metrics-and-custom-attributes',
                    'freshservice/platform/analytics/exporting-data-from-analytics-to-power-bi',
                    'freshservice/platform/analytics/exporting-data-from-analytics-to-tableau',
                    'freshservice/platform/analytics/gain-visibility-into-service-operations-with-generative-ai-powered-freddy-insights',
                    'freshservice/platform/analytics/generate-intuitive-reports-using-analytics-pro',
                    'freshservice/platform/analytics/how-is-the-row-count-in-the-underlying-data-more-than-total-metrics-count-on-the-report-chart',
                    'freshservice/platform/analytics/incremental-data-exports-in-freshservice',
                    'freshservice/platform/analytics/reporting-on-approval-metrics-in-analytics',
                    'freshservice/platform/analytics/setting-up-time-sheet-reports',
                    'freshservice/platform/analytics/understanding-sorting-behaviour-in-freshservice-analytics',
                    'freshservice/platform/analytics/why-are-field-values-not-loading-in-analytics-filters',
                  ],
                },
                {
                  type: 'category',
                  label: '📋 Reporting',
                  collapsed: true,
                  items: [
                    'freshservice/platform/reporting/asset-reports',
                    'freshservice/platform/reporting/change-reports',
                    'freshservice/platform/reporting/the-advanced-reporting-suite',
                    'freshservice/platform/reporting/the-enterprise-reporting-suite',
                    'freshservice/platform/reporting/understanding-the-helpdesk-at-a-glance-report',
                  ],
                },
              ],
            },
            {
              type: 'category',
              label: '🛠️ 자동화 및 워크플로우',
              collapsed: true,
              items: [
                {
                  type: 'category',
                  label: '⚡ Workflow Automator',
                  collapsed: true,
                  items: [
                    'freshservice/platform/workflow-automator/advanced-workflow-trigger-configuration',
                    'freshservice/platform/workflow-automator/auto-assigning-tickets-to-agents-in-a-group-round-robin',
                    'freshservice/platform/workflow-automator/expression-builder-node-troubleshooting-guide',
                    'freshservice/platform/workflow-automator/fix-for-custom-objects-behavior-in-workflow-automator',
                    'freshservice/platform/workflow-automator/introduction-to-scheduled-workflows',
                    'freshservice/platform/workflow-automator/json-parser-node',
                    'freshservice/platform/workflow-automator/operators-in-expression-builder-node',
                    'freshservice/platform/workflow-automator/powerful-placeholders-with-liquid-filters',
                    'freshservice/platform/workflow-automator/reader-node',
                    'freshservice/platform/workflow-automator/sample-usecase-invoke-webrequest-node-to-fetch-ticket-details-and-perform-actions-based-on-it',
                    'freshservice/platform/workflow-automator/scheduled-workflows-for-software-applications-and-users',
                    'freshservice/platform/workflow-automator/web-request-node',
                  ],
                },
              ],
            },
            {
              type: 'category',
              label: '🎯 사용자 정의 객체',
              collapsed: true,
              items: [
                'freshservice/platform/custom-objects/creating-custom-objects',
                'freshservice/platform/custom-objects/importing-and-exporting-custom-objects',
                'freshservice/platform/custom-objects/using-custom-objects-in-workflows',
              ],
            },
            {
              type: 'category',
              label: '🏢 Freshworks Organization',
              collapsed: true,
              items: [
                'freshservice/platform/freshworks-organization/introducing-freshworks-organization',
                'freshservice/platform/freshworks-organization/migrating-freshservice-sso-to-freshworks-organization',
                'freshservice/platform/freshworks-organization/setting-up-sso-policies-in-freshworks-organization',
                'freshservice/platform/freshworks-organization/upgrading-multi-account-configurations-to-freshworks-organization',
                'freshservice/platform/freshworks-organization/upgrading-msp-mode-accounts-to-freshworks-organization',
              ],
            },
            {
              type: 'category',
              label: '🔐 보안 및 인증',
              collapsed: true,
              items: [
                'freshservice/platform/credential-store/centralized-credential-store',
              ],
            },
            {
              type: 'category',
              label: '💼 구독 관리',
              collapsed: true,
              items: [
                'freshservice/platform/managing-freshservice-subscription/how-to-manage-a-freshservice-subscription-during-trial',
                'freshservice/platform/managing-freshservice-subscription/faqs',
              ],
            },
            {
              type: 'category',
              label: '🔄 API 및 마이그레이션',
              collapsed: true,
              items: [
                'freshservice/platform/api-v1-deprecation/deprecating-v1-apis-for-freshservice',
              ],
            },
          ],
        },
      ],
    },
  ],
};

export default sidebars;
