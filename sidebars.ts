import type { SidebarsConfig } from '@docusaurus/plugin-content-docs';

// This runs in Node.js - Don't use client-side code here (browser APIs, JSX...)

/**
 * Creating a sidebar enables you to:
 - create an ordered group of docs
 - render a sidebar for each doc of that group
 - provide next/previous navigation

 The sidebars can be generated from the filesystem, or explicitly defined here.

 Create as many sidebars as you want.
 */
const sidebars: SidebarsConfig = {
  // Main documentation sidebar with product-focused structure
  tutorialSidebar: [
    'intro',

    // === FRESHWORKS 제품군 ===
    {
      type: 'category',
      label: '🎧 Freshworks',
      collapsed: false,
      items: [
        // Freshservice - IT 서비스 관리
        {
          type: 'category',
          label: '🔧 Freshservice (ITSM)',
          link: {
            type: 'doc',
            id: 'freshworks/freshservice/freshworks-freshservice-index',
          },
          collapsed: false,
          items: [
            // 시작하기 (Getting started with Freshservice - 115개 문서)
            {
              type: 'category',
              label: '📚 시작하기',
              collapsed: false,
              items: [
                // User Management 폴더 (20개 문서)
                {
                  type: 'category',
                  label: '👥 사용자 관리',
                  collapsed: false,
                  items: [
                    'freshworks/freshservice/getting-started-with-freshservice/user-management/understanding-agents',
                    'freshworks/freshservice/getting-started-with-freshservice/user-management/setting-agent-roles-permissions',
                    'freshworks/freshservice/getting-started-with-freshservice/user-management/managing-requesters',
                    'freshworks/freshservice/getting-started-with-freshservice/user-management/importing-requesters-csv',
                    'freshworks/freshservice/getting-started-with-freshservice/user-management/finding-agent-user-id',
                    'freshworks/freshservice/getting-started-with-freshservice/user-management/adding-custom-fields-users',
                    'freshworks/freshservice/getting-started-with-freshservice/user-management/csv-import-guidelines',
                    'freshworks/freshservice/getting-started-with-freshservice/user-management/merging-requesters',
                    'freshworks/freshservice/getting-started-with-freshservice/user-management/password-policy-setup',
                    'freshworks/freshservice/getting-started-with-freshservice/user-management/changing-requester-password',
                    'freshworks/freshservice/getting-started-with-freshservice/user-management/adding-custom-fields-departments',
                    'freshworks/freshservice/getting-started-with-freshservice/user-management/exporting-agent-information',
                    'freshworks/freshservice/getting-started-with-freshservice/user-management/importing-agent-information',
                    'freshworks/freshservice/getting-started-with-freshservice/user-management/automatically-associating-contacts-companies',
                    'freshworks/freshservice/getting-started-with-freshservice/user-management/add-members-observers-agent-groups',
                    'freshworks/freshservice/getting-started-with-freshservice/user-management/create-manage-agent-groups',
                    'freshworks/freshservice/getting-started-with-freshservice/user-management/create-manage-requester-groups',
                    'freshworks/freshservice/getting-started-with-freshservice/user-management/managing-requesters-freshservice',
                    'freshworks/freshservice/getting-started-with-freshservice/user-management/importing-departments-companies-csv',
                    'freshworks/freshservice/getting-started-with-freshservice/user-management/merging-users-advanced-scenarios',
                    // ✅ User Management 폴더 완성! (20개 문서 복구됨!)
                  ],
                },
                // 향후 추가: form-fields, fresh-themes, setting-up-freshservice 등 다른 폴더들
                'freshworks/freshservice/getting-started/config-sets',
                'freshworks/freshservice/getting-started/importing-assets',
              ],
            },

            // IT 서비스 관리 (Support Guide: IT Service Management - 187개 문서) 
            {
              type: 'category',
              label: '🎫 IT 서비스 관리',
              collapsed: true,
              items: [
                'freshworks/freshservice/it-service-management/freshworks-freshservice-it-service-management-saas-workflows',
                // 향후 추가: getting-started-with-tickets, ticket-actions, change-management 등
              ],
            },

            // IT 자산 관리 (Support Guide: IT Asset Management - 95개 문서)
            // {
            //   type: 'category',
            //   label: '💻 IT 자산 관리',
            //   collapsed: true,
            //   items: [
            //     // 향후 추가: get-started-with-assets, discovery-probe, saas-management 등
            //   ],
            // },

            // 워크스페이스 & ESM (Enterprise Service Management - 69개 문서)
            {
              type: 'category',
              label: '🏢 워크스페이스 관리',
              collapsed: true,
              items: [
                'freshworks/freshservice/workspace-management/freshworks-freshservice-workspace-management-workspace-views',
                // 향후 추가: workspaces, employee-onboarding, access-controls 등
              ],
            },

            // IT 운영 관리 (IT Operations Management - 95개 문서)
            // {
            //   type: 'category',
            //   label: '🔧 IT 운영 관리',
            //   collapsed: true,
            //   items: [
            //     // 향후 추가: monitoring-tools-integration, alert-management 등
            //   ],
            // },

            // 플랫폼 & 자동화 (Platform - 101개 문서)
            // {
            //   type: 'category',
            //   label: '🤖 플랫폼 & 자동화',
            //   collapsed: true,
            //   items: [
            //     // 향후 추가: analytics, workflow-automator, custom-objects 등
            //   ],
            // },

            // 앱 & 통합 (How to Setup Apps and Integrations - 87개 문서)
            // {
            //   type: 'category',
            //   label: '🔌 앱 & 통합',
            //   collapsed: true,
            //   items: [
            //     // 향후 추가: extending-freshservice-with-integrations, connector-apps 등
            //   ],
            // },

            // 보안 & 정책 (Security and Policies + Policies and Data Protection - 62개 문서)
            {
              type: 'category',
              label: '🔐 보안 & 정책',
              collapsed: true,
              items: [
                'freshworks/freshservice/security-and-policies/freshworks-freshservice-security-and-policies-spam-and-trash',
                // 향후 추가: sso, security, remote-authentication 등
              ],
            },

            // 프로젝트 관리 (Project & Workload Management - 47개 문서)
            // {
            //   type: 'category',
            //   label: '📋 프로젝트 관리',
            //   collapsed: true,
            //   items: [
            //     // 향후 추가: new-gen-project-management, workload-management 등
            //   ],
            // },

            // 사용자 가이드 (User Guide - Admin/Agent/End User - 62개 문서)
            // {
            //   type: 'category',
            //   label: '👥 사용자 가이드',
            //   collapsed: true,
            //   items: [
            //     // 향후 추가: admin-settings, agent-guide, end-user-guide 등
            //   ],
            // },

            // FAQ & 지원 (Freshservice FAQs - 508개 문서)
            // {
            //   type: 'category',
            //   label: '❓ FAQ & 지원',
            //   collapsed: true,
            //   items: [
            //     // 향후 추가: 자주 묻는 질문들 (가장 많은 문서 수)
            //   ],
            // },
          ],
        },

        // Freshdesk - 고객 지원
        // {
        //   type: 'category',
        //   label: '💬 Freshdesk (고객 지원)',
        //   collapsed: true,
        //   items: [
        //     // 향후 추가 예정
        //   ],
        // },

        // Freshsales - 영업 관리
        // {
        //   type: 'category',
        //   label: '💼 Freshsales (영업 관리)',
        //   collapsed: true,
        //   items: [
        //     // 향후 추가 예정
        //   ],
        // },
      ],
    },

    // === MONDAY.COM 제품군 ===
    // {
    //   type: 'category',
    //   label: '📋 Monday.com',
    //   collapsed: true,
    //   items: [
    //     // 향후 추가 예정
    //   ],
    // },

    // === 튜토리얼 (기존 유지) ===
    {
      type: 'category',
      label: '📖 Docusaurus 튜토리얼',
      collapsed: true,
      items: [
        {
          type: 'category',
          label: 'Tutorial - Basics',
          items: ['tutorial-basics/create-a-page', 'tutorial-basics/create-a-document', 'tutorial-basics/create-a-blog-post', 'tutorial-basics/markdown-features', 'tutorial-basics/deploy-your-site', 'tutorial-basics/congratulations'],
        },
        {
          type: 'category',
          label: 'Tutorial - Extras',
          items: ['tutorial-extras/manage-docs-versions', 'tutorial-extras/translate-your-site'],
        },
      ],
    },
  ],
};

export default sidebars;
