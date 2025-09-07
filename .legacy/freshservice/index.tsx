import type { ReactNode } from 'react';
import clsx from 'clsx';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';
import HomepageFeatures from '@site/src/components/HomepageFeatures';
import Heading from '@theme/Heading';

import styles from './index.module.css';

function HomepageHeader() {
  const { siteConfig } = useDocusaurusContext();
  return (
    <header className={clsx('hero hero--primary', styles.heroBanner)}>
      <div className="container">
        <Heading as="h1" className="hero__title">
          위두소프트 기술 문서 포털
        </Heading>
        <p className="hero__subtitle">Freshworks와 Monday.com으로 더 나은 비즈니스를</p>
        <div className={styles.buttons}>
          <Link
            className="button button--secondary button--lg"
            to="/intro">
            📚 시작하기 가이드
          </Link>
          <Link
            className="button button--primary button--lg"
            to="/freshworks/freshservice/getting-started/user-management/understanding-agents"
            style={{ marginLeft: '1rem' }}>
            🎧 Freshworks 둘러보기
          </Link>
        </div>
        <div className={styles.buttons} style={{ marginTop: '1rem' }}>
          <Link
            className="button button--outline button--lg"
            to="#"
            style={{ opacity: 0.7, cursor: 'not-allowed' }}>
            📋 Monday.com 준비중
          </Link>
        </div>
      </div>
    </header>
  );
}

export default function Home(): ReactNode {
  const { siteConfig } = useDocusaurusContext();
  return (
    <Layout
      title="위두소프트 기술 문서 포털"
      description="Freshworks, Monday.com 등 IT 서비스 관리 솔루션의 설정, 사용법, 문제해결 가이드">
      <HomepageHeader />
      <main>
        <HomepageFeatures />
      </main>
    </Layout>
  );
}
