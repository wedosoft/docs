import type { ReactNode } from 'react';
import clsx from 'clsx';
import Heading from '@theme/Heading';
import styles from './styles.module.css';

type FeatureItem = {
  title: string;
  Svg: React.ComponentType<React.ComponentProps<'svg'>>;
  description: ReactNode;
};

const FeatureList: FeatureItem[] = [
  {
    title: '🎧 Freshworks 제품군',
    Svg: require('@site/static/img/undraw_docusaurus_mountain.svg').default,
    description: (
      <>
        <strong>클라우드 기반 비즈니스 플랫폼</strong><br />
        🔧 <strong>Freshservice</strong> - IT 서비스 관리 (ITSM)<br />
        💬 <strong>Freshdesk</strong> - 고객 지원 관리<br />
        💼 <strong>Freshsales</strong> - 영업 & CRM 관리<br />
        <em>통합된 워크플로우로 효율적인 업무 환경 구축</em>
      </>
    ),
  },
  {
    title: '� Monday.com 제품군',
    Svg: require('@site/static/img/undraw_docusaurus_tree.svg').default,
    description: (
      <>
        <strong>비주얼 프로젝트 관리 플랫폼</strong><br />
        📊 <strong>Work Management</strong> - 프로젝트 & 팀 협업<br />
        🏢 <strong>monday CRM</strong> - 영업 파이프라인<br />
        👥 <strong>monday Dev</strong> - 개발 워크플로우<br />
        <em>직관적인 인터페이스로 팀 생산성 극대화</em>
      </>
    ),
  },
  {
    title: '📚 실무 중심 가이드',
    Svg: require('@site/static/img/undraw_docusaurus_react.svg').default,
    description: (
      <>
        <strong>단계별 설정부터 고급 활용까지</strong><br />
        🎯 역할별 맞춤 가이드 (사용자/관리자/시스템관리자)<br />
        💡 실제 업무 시나리오 기반 설명<br />
        🔍 빠른 검색과 카테고리별 탐색<br />
        <em>한국어/영어 다국어 지원으로 누구나 쉽게</em>
      </>
    ),
  },
];

function Feature({ title, Svg, description }: FeatureItem) {
  return (
    <div className={clsx('col col--4')}>
      <div className="text--center">
        <Svg className={styles.featureSvg} role="img" />
      </div>
      <div className="text--center padding-horiz--md">
        <Heading as="h3">{title}</Heading>
        <p>{description}</p>
      </div>
    </div>
  );
}

export default function HomepageFeatures(): ReactNode {
  return (
    <section className={styles.features}>
      <div className="container">
        <div className="row">
          {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}
