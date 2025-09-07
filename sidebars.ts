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
              ],
            },
            {
              type: 'category',
              label: '🎫 IT 서비스 관리',
              collapsed: true,
              items: [
                'freshworks/freshservice/it-service-management/saas-workflows',
              ],
            },
            {
              type: 'category',
              label: '🏢 워크스페이스 관리',
              collapsed: true,
              items: [
                'freshworks/freshservice/workspace-management/workspace-views',
              ],
            },
            {
              type: 'category',
              label: '🔐 보안 & 정책',
              collapsed: true,
              items: [
                'freshworks/freshservice/security-and-policies/spam-and-trash',
              ],
            },
          ],
        },
      ],
    },
  ],
};

export default sidebars;
