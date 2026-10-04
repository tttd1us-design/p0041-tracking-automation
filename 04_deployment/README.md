# 04_deployment — 배포 & 운영팀

## 역할
승인된 MVP를 무료 경로(임시 데모 URL, GitHub Pages)로 배포하고 결제 연동을 준비한다.

## 폴더 구조

```
04_deployment/
├── domains/            # 도메인 설정
├── ssl/                # SSL 인증서
├── cdn/                # CDN 설정
├── monitoring/         # 모니터링 설정
└── backups/
    ├── daily/          # 일간 백업
    ├── weekly/         # 주간 백업
    └── monthly/        # 월간 백업
```

## 작업 절차

1. **코드 확인:** `03_apps_dev/projects/`에서 완성된 코드 확인
2. **GitHub 푸시:** 코드 GitHub에 푸시
3. **배포:** Vercel/Netlify에 서버리스 배포
4. **도메인 연결:** 도메인 설정 및 SSL 인증서 발급
5. **모니터링:** 모니터링 도구 설정
6. **백업:** `backups/`에 정기 백업 실행

## 스킬
`10jo-deploy` 스킬을 참고한다.
