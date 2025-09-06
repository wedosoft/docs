import { themes as prismThemes } from 'prism-react-renderer';
import type { Config } from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';

// This runs in Node.js - Don't use client-side code here (browser APIs, JSX...)

const config: Config = {
  title: 'WedoSoft Documentation',
  tagline: '고객 지원을 위한 기술 문서 포털',
  favicon: 'img/favicon.ico',

  // Set the production url of your site here
  url: 'https://docs.wedosoft.net',
  // Set the /<baseUrl>/ pathname under which your site is served
  // For GitHub pages deployment, it is often '/<projectName>/'
  baseUrl: '/',

  // GitHub pages deployment config.
  // If you aren't using GitHub pages, you don't need these.
  organizationName: 'wedosoft', // Usually your GitHub org/user name.
  projectName: 'docs', // Usually your repo name.

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
          // WedoSoft documentation repository
        },
        blog: {
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
      },
      items: [
        {
          type: 'docSidebar',
          sidebarId: 'tutorialSidebar',
          position: 'left',
          label: 'Freshservice 가이드',
        },
        { to: '/blog', label: '블로그', position: 'left' },
      ],
    },
    footer: {
      style: 'dark',
      links: [
        {
          title: '문서',
          items: [
            {
              label: 'Freshservice 시작하기',
              to: '/docs/intro',
            },
            {
              label: '사용자 관리',
              to: '/docs/freshworks/freshservice/getting-started-with-freshservice/user-management/understanding-agents',
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
              label: 'WedoSoft 홈페이지',
              href: 'https://wedosoft.net',
            },
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} WedoSoft. All rights reserved.`,
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
