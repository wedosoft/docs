"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.default = ProductShowcase;
var react_1 = require("react");
var Link_1 = require("@docusaurus/Link");
require("./styles.css");
var freshworksProducts = [
    {
        icon: '🔧',
        name: 'Freshservice',
        description: 'IT 서비스 관리 (ITSM)',
        features: ['헬프데스크 티켓 관리', 'IT 자산 및 인벤토리', '사용자 권한 관리', 'SLA 및 워크플로우'],
        status: 'available',
        link: '/freshservice/getting-started/user-management/understanding-agents'
    },
    {
        icon: '💬',
        name: 'Freshdesk',
        description: '고객 지원 관리',
        features: ['멀티채널 고객 지원', '티켓 자동 분류', '지식베이스 관리', '고객 만족도 조사'],
        status: 'coming-soon'
    },
    {
        icon: '💼',
        name: 'Freshsales',
        description: '영업 및 CRM 관리',
        features: ['리드 및 거래 추적', '영업 파이프라인', '이메일 자동화', '성과 분석 리포트'],
        status: 'coming-soon'
    }
];
var mondayProducts = [
    {
        icon: '📊',
        name: 'Work Management',
        description: '프로젝트 & 작업 관리',
        features: ['칸반 & 간트 차트', '팀 협업 도구', '자동화 워크플로우', '시간 추적 & 리포팅'],
        status: 'coming-soon'
    },
    {
        icon: '🏢',
        name: 'monday CRM',
        description: '영업 파이프라인 관리',
        features: ['거래 및 연락처 관리', '영업 활동 추적', '성과 대시보드', '이메일 통합'],
        status: 'coming-soon'
    },
    {
        icon: '👥',
        name: 'monday Dev',
        description: '개발팀 워크플로우',
        features: ['스프린트 계획', '버그 & 이슈 추적', '코드 리뷰 관리', '배포 파이프라인'],
        status: 'coming-soon'
    }
];
function StatusBadge(_a) {
    var status = _a.status;
    return (<span className={"status-badge ".concat(status)}>
            {status === 'available' ? '이용 가능' : '준비중'}
        </span>);
}
function SubProductCard(_a) {
    var product = _a.product;
    var CardContent = (<div className={"sub-product-card ".concat(product.status)}>
            <div className="sub-product-header">
                <span className="sub-product-icon">{product.icon}</span>
                <h4>{product.name}</h4>
                <StatusBadge status={product.status}/>
            </div>
            <p><strong>{product.description}</strong></p>
            <ul>
                {product.features.map(function (feature, index) { return (<li key={index}>{feature}</li>); })}
            </ul>
            {product.status === 'available' && product.link && (<div className="quick-actions">
                    <Link_1.default to={product.link} className="action-link primary">
                        📖 바로 시작하기
                    </Link_1.default>
                </div>)}
        </div>);
    return product.link ? (<Link_1.default to={product.link} style={{ textDecoration: 'none', color: 'inherit' }}>
            {CardContent}
        </Link_1.default>) : CardContent;
}
function ProductGroup(_a) {
    var title = _a.title, subtitle = _a.subtitle, type = _a.type, products = _a.products;
    return (<div className={"product-main-card ".concat(type, "-card")}>
            <h3>{title}</h3>
            <p>{subtitle}</p>
            <div className="product-grid-internal">
                {products.map(function (product, index) { return (<SubProductCard key={index} product={product}/>); })}
            </div>
        </div>);
}
function ProductShowcase() {
    return (<div className="product-showcase">
            <ProductGroup title="🎧 Freshworks 제품군" subtitle="올인원 비즈니스 소프트웨어 플랫폼" type="freshworks" products={freshworksProducts}/>
            <ProductGroup title="📋 Monday.com 제품군" subtitle="비주얼 프로젝트 관리 & 팀 협업 플랫폼" type="monday" products={mondayProducts}/>
        </div>);
}
