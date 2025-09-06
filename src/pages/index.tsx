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
          웨도소프트 기술 문서 포털
        </Heading>
        <p className="hero__subtitle">고객지원 및 IT 서비스 관리를 위한 종합 가이드</p>
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
            🔧 Freshservice 바로가기
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
      title="웨도소프트 기술 문서 포털"
      description="Freshworks, Monday.com 등 IT 서비스 관리 솔루션의 설정, 사용법, 문제해결 가이드">
      <HomepageHeader />
      <main>
        <HomepageFeatures />
      </main>
    </Layout>
  );
}
