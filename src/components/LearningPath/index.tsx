import React from 'react';
import Link from '@docusaurus/Link';
import './styles.css';

interface LearningStep {
    step: string;
    title: string;
    description: string;
    link: string;
}

const learningSteps: LearningStep[] = [
    {
        step: '1️⃣',
        title: '기본 개념 이해',
        description: '에이전트와 요청자 이해하기',
        link: '/freshworks/freshservice/getting-started/user-management/understanding-agents'
    },
    {
        step: '2️⃣',
        title: '기초 설정 완료',
        description: '사용자 관리 시작하기',
        link: '/freshworks/freshservice/getting-started/user-management/managing-requesters-freshservice'
    },
    {
        step: '3️⃣',
        title: '고급 기능 활용',
        description: '에이전트 그룹 및 권한 관리',
        link: '/freshworks/freshservice/getting-started/user-management/create-manage-agent-groups'
    }
];

function LearningPathStep({ step }: { step: LearningStep }) {
    return (
        <Link to={step.link} className="learning-path" style={{ textDecoration: 'none' }}>
            <div className="path-step">{step.step}</div>
            <div className="path-content">
                <strong>{step.title}</strong><br />
                {step.description}
            </div>
        </Link>
    );
}

export default function LearningPath() {
    return (
        <div className="learning-path-container">
            <h3>🎯 추천 학습 경로</h3>
            {learningSteps.map((step, index) => (
                <LearningPathStep key={index} step={step} />
            ))}
        </div>
    );
}
