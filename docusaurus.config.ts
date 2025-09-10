import { themes as prismThemes } from 'prism-react-renderer';
import type { Config } from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';

// This runs in Node.js - Don't use client-side code here (browser APIs, JSX...)

const config: Config = {
  title: '위두소프트 기술 문서 포털',
  tagline: 'IT 서비스 관리 솔루션을 위한 종합 가이드',
  favicon: 'img/favicon.ico',

  // Set the production url of your site here
  url: 'https://wedosoft.github.io',
  // Set the /<baseUrl>/ pathname under which your site is served
  // For GitHub pages deployment, it is often '/<projectName>/'
  baseUrl: '/docs2',

  // GitHub pages deployment config.
  // If you aren't using GitHub pages, you don't need these.
  organizationName: 'wedosoft', // Usually your GitHub org/user name.
  projectName: 'docs2', // Usually your repo name.

  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',

  // Even if you don't use internationalization, you can use this field to set
  // useful metadata like html lang. For example, if your site is Chinese, you
  // may want to replace "en" with "zh-Hans".
  i18n: {
    defaultLocale: 'ko',
    locales: ['ko', 'en'],
  },

  presets: [
    [
      'classic',
      {
        docs: {
          sidebarPath: './sidebars.ts',
          routeBasePath: '/', // Remove /docs from URL
          // WedoSoft documentation repository
        },
        blog: {
          routeBasePath: '/blog', // Explicitly set blog route
          showReadingTime: true,
          feedOptions: {
            type: ['rss', 'atom'],
            xslt: true,
          },
          // WedoSoft blog posts
          // Useful options to enforce blogging best practices
          onInlineTags: 'warn',
          onInlineAuthors: 'warn',
          onUntruncatedBlogPosts: 'warn',
        },
        theme: {
          customCss: './src/css/custom.css',
        },
      } satisfies Preset.Options,
    ],
  ],

  themeConfig: {
    // Replace with your project's social card
    image: 'img/docusaurus-social-card.jpg',
    navbar: {
      logo: {
        alt: 'WedoSoft Logo',
        src: 'img/logo-light.svg',
        srcDark: 'img/logo-dark.svg',
        href: '/intro',
      },
      items: [],
    },
    footer: {
      style: 'dark',
      links: [
        {
          title: '문서',
          items: [
            {
              label: 'Freshservice 시작하기',
              to: '/intro',
            },
            {
              label: '사용자 관리',
              to: '/freshworks/freshservice/getting-started/user-management/understanding-agents',
            },
          ],
        },
        {
          title: '커뮤니티',
          items: [
            {
              label: '고객 지원',
              href: 'https://wedosoft.net/support',
            },
            {
              label: '문의하기',
              href: 'https://wedosoft.net/contact',
            },
          ],
        },
        {
          title: '더보기',
          items: [
            {
              label: '블로그',
              to: '/blog',
            },
            {
              label: '홈페이지',
              href: 'https://www.wedosoft.net',
            },
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} We Do Soft Inc. All rights reserved.`,
    },
    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
    },
    algolia: {
      appId: '9T6ZL67IBN',
      apiKey: '351e7b8eb39c3dd129d2ff2440d01d81',
      indexName: 'docs',
      contextualSearch: true,
      searchParameters: {},
    },
  } satisfies Preset.ThemeConfig,
};

export default config;
