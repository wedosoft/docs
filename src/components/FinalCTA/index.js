"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.default = FinalCTA;
var react_1 = require("react");
var Link_1 = require("@docusaurus/Link");
require("./styles.css");
var ctaCards = [
    {
        icon: '🎧',
        title: 'Freshservice 시작하기',
        description: 'IT 서비스 관리의 모든 것',
        link: '/freshservice/getting-started/user-management/understanding-agents',
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
function CTACard(_a) {
    var card = _a.card;
    var cardContent = (<div className={"cta-card ".concat(card.type, " ").concat(card.disabled ? 'disabled' : '')}>
            {card.badge && <span className="cta-badge">{card.badge}</span>}
            <span className="cta-icon">{card.icon}</span>
            <h3>{card.title}</h3>
            <p>{card.description}</p>
            {!card.disabled && <span className="cta-arrow">→</span>}
        </div>);
    return card.link && !card.disabled ? (<Link_1.default to={card.link} style={{ textDecoration: 'none', color: 'inherit' }}>
            {cardContent}
        </Link_1.default>) : (cardContent);
}
function FinalCTA() {
    return (<div className="cta-final">
            <h2>🎯 지금 바로 시작하세요!</h2>
            <div className="final-cta-grid">
                {ctaCards.map(function (card, index) { return (<CTACard key={index} card={card}/>); })}
            </div>
        </div>);
}
