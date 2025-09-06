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
    title: '🔧 Freshservice (ITSM)',
    Svg: require('@site/static/img/undraw_docusaurus_mountain.svg').default,
    description: (
      <>
        IT 서비스 관리를 위한 종합 솔루션입니다.
        티켓 관리, 사용자 관리, 자산 관리, 워크플로우 자동화 등
        IT 운영에 필요한 모든 기능을 제공합니다.
      </>
    ),
  },
  {
    title: '👥 사용자 중심 가이드',
    Svg: require('@site/static/img/undraw_docusaurus_tree.svg').default,
    description: (
      <>
        신입 상담원부터 관리자까지, 실무에서 바로 활용할 수 있는
        단계별 가이드를 제공합니다. 예시 중심의 설명으로
        누구나 쉽게 따라할 수 있습니다.
      </>
    ),
  },
  {
    title: '🌐 다국어 지원',
    Svg: require('@site/static/img/undraw_docusaurus_react.svg').default,
    description: (
      <>
        한국어와 영어를 지원하며, 지속적으로 업데이트되는
        최신 기능 정보와 문제해결 방법을 제공합니다.
        실시간 검색과 카테고리별 탐색이 가능합니다.
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
