# 02_product_spec — 기획팀

## 역할
승인된 불편(P-번호)을 해법으로 바꾸고 개발팀이 바로 만들 수 있는 spec.md를 작성한다.

## 폴더 구조

```
02_product_spec/
├── business/
│   ├── plan/           # 사업 계획서
│   ├── financial/      # 재무 계획
│   └── marketing/      # 마케팅 전략
├── organization/
│   ├── roles/          # 조직 구조, 역할 정의
│   └── processes/      # 업무 프로세스
├── specs/
│   ├── approved/       # 승인된 명세서
│   ├── draft/          # 작성 중인 명세서
│   └── archive/        # 보관용 명세서
└── templates/          # 문서 템플릿
```

## 작업 절차

1. **불편 선정:** `01_pain_mining/data/processed/painpoints.json`에서 승인된 아이템 확인
2. **해법 도출:** 불편을 해결할 소프트웨어 솔루션 설계
3. **명세서 작성:** `specs/draft/spec.md` 작성
4. **승인 요청:** 대표님에게 승인 요청
5. **승인 완료:** `specs/approved/`로 이동

## 스킬
`10jo-product-spec` 스킬을 참고한다.
