import React from 'react';
import Link from '@docusaurus/Link';
import './styles.css';

interface CTACard {
    icon: string;
    title: string;
    description: string;
    link?: string;
    type: 'primary' | 'secondary';
    disabled?: boolean;
    badge?: string;
}

const ctaCards: CTACard[] = [
    {
        icon: '🎧',
        title: 'Freshservice 시작하기',
        description: 'IT 서비스 관리의 모든 것',
        link: '/freshworks/freshservice/getting-started/user-management/understanding-agents',
        type: 'primary'
    },
    {
        icon: '📋',
        title: 'Monday.com 둘러보기',
        description: '프로젝트 관리 & 팀 협업',
        type: 'secondary',
        disabled: true,
        badge: '준비중'
    }
];

function CTACard({ card }: { card: CTACard }) {
    const cardContent = (
        <div className={`cta-card ${card.type} ${card.disabled ? 'disabled' : ''}`}>
            {card.badge && <span className="cta-badge">{card.badge}</span>}
            <span className="cta-icon">{card.icon}</span>
            <h3>{card.title}</h3>
            <p>{card.description}</p>
            {!card.disabled && <span className="cta-arrow">→</span>}
        </div>
    );

    return card.link && !card.disabled ? (
        <Link to={card.link} style={{ textDecoration: 'none', color: 'inherit' }}>
            {cardContent}
        </Link>
    ) : (
        cardContent
    );
}

export default function FinalCTA() {
    return (
        <div className="cta-final">
            <h2>🎯 지금 바로 시작하세요!</h2>
            <div className="final-cta-grid">
                {ctaCards.map((card, index) => (
                    <CTACard key={index} card={card} />
                ))}
            </div>
        </div>
    );
}
