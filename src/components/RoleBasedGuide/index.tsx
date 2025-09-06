import React from 'react';
import Link from '@docusaurus/Link';
import './styles.css';

interface RoleAction {
    label: string;
    link: string;
    icon: string;
    type: 'primary' | 'secondary';
}

interface Role {
    icon: string;
    title: string;
    description: string;
    tasks: string[];
    actions: RoleAction[];
    cardType: 'end-user' | 'admin' | 'sys-admin';
}

const roles: Role[] = [
    {
        icon: '👤',
        title: '최종 사용자',
        description: '헬프데스크 이용자, 일반 직원',
        tasks: [
            'IT 지원 요청 (티켓 생성)',
            '셀프 서비스 포털 이용',
            '비밀번호 재설정',
            '장비 요청 및 반납'
        ],
        actions: [
            {
                label: '📋 티켓 생성 가이드',
                link: '/freshworks/freshservice/getting-started/user-management/understanding-agents',
                icon: '📋',
                type: 'primary'
            },
            {
                label: '🌐 포털 이용 방법',
                link: '/freshworks/freshservice/getting-started/self-service-portal-introduction/portal-access-login',
                icon: '🌐',
                type: 'secondary'
            }
        ],
        cardType: 'end-user'
    },
    {
        icon: '👩‍💼',
        title: '부서 관리자',
        description: '팀 리더, 부서장, 프로젝트 매니저',
        tasks: [
            '팀원 계정 관리',
            '승인 워크플로우 관리',
            '성과 리포트 확인',
            '프로젝트 진행 상황 추적'
        ],
        actions: [
            {
                label: '👥 사용자 그룹 관리',
                link: '/freshworks/freshservice/getting-started/user-management/create-manage-requester-groups',
                icon: '👥',
                type: 'primary'
            },
            {
                label: '🔐 권한 설정',
                link: '/freshworks/freshservice/getting-started/user-management/setting-agent-roles-permissions',
                icon: '🔐',
                type: 'secondary'
            }
        ],
        cardType: 'admin'
    },
    {
        icon: '🔧',
        title: '시스템 관리자',
        description: 'IT 관리자, 시스템 엔지니어',
        tasks: [
            '시스템 초기 설정',
            '통합 및 API 구성',
            '보안 정책 관리',
            '자동화 워크플로우 구축'
        ],
        actions: [
            {
                label: '⚙️ 시스템 설정',
                link: '/freshworks/freshservice/getting-started/setting-up-freshservice/freshservice-onboarding-flow',
                icon: '⚙️',
                type: 'primary'
            },
            {
                label: '📧 메일박스 구성',
                link: '/freshworks/freshservice/getting-started/setting-up-freshservice/setting-up-custom-mailbox',
                icon: '📧',
                type: 'secondary'
            }
        ],
        cardType: 'sys-admin'
    }
];

function RoleCard({ role }: { role: Role }) {
    return (
        <div className={`role-card ${role.cardType}`}>
            <div className="role-header">
                <span className="role-icon">{role.icon}</span>
                <h3>{role.title}</h3>
                <p>{role.description}</p>
            </div>
            <div className="role-content">
                <h4>🎯 주요 업무</h4>
                <ul>
                    {role.tasks.map((task, index) => (
                        <li key={index}>{task}</li>
                    ))}
                </ul>
                <div className="role-actions">
                    {role.actions.map((action, index) => (
                        <Link
                            key={index}
                            to={action.link}
                            className={`role-btn ${action.type}`}
                        >
                            {action.label}
                        </Link>
                    ))}
                </div>
            </div>
        </div>
    );
}

export default function RoleBasedGuide() {
    return (
        <div className="role-based-grid">
            {roles.map((role, index) => (
                <RoleCard key={index} role={role} />
            ))}
        </div>
    );
}
