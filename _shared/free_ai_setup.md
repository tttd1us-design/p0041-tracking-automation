# 10조 스튜디오 — 무료 AI 연결 체계 (확정 2026-10-03)

수석 결정문: `_docs/DECISIONS_2026-10-03.md`

## 핵심: hermes proxy

Nous Portal OAuth 구독을 **로컬 OpenAI 호환 API**로 변환한다.
API 키가 없어 놀던 모든 도구가 여기 붙는다. **추가비용 0원.**

```
http://127.0.0.1:8645/v1     (bearer 토큰은 아무 값이나 가능)
```

가동: `hermes proxy start --provider nous` (백그라운드 상시 실행)

검증: `curl http://127.0.0.1:8645/v1/chat/completions` → `"cost":0, "source":"free_path"` 확인

## 연결 완료 (실동작 검증)

| 도구 | 연결 방법 | 검증 결과 |
|---|---|---|
| **llm** | `~/AppData/Roaming/io.datasette.llm/extra-openai-models.yaml` | ✅ `llm -m 10jo "질문"` |
| **aider** | `~/.aider.conf.yml` | ✅ `aider` (모델 자동 지정) |
| **OpenCode** | `~/.config/opencode/opencode.json` | ✅ `opencode run "질문"` |
| **Hermes 본체** | 폴백 체인 | ✅ 무료 모델 3종 |
| **안티그래비티** | `_tools/antigravity_bridge.py` | ✅ 별도 경로 (Gemini) |

## 무료 모델 목록 (Nous Portal, cost=0 실측)

| 모델 | 컨텍스트 | 용도 |
|---|---|---|
| `meituan/longcat-2.5-preview:free` | 1,048,576 | **주력** — 긴 문서 분석 |
| `stepfun/step-3.7-flash:free` | 262,144 | 빠른 응답 |
| `poolside/laguna-s-2.1:free` | 262,144 | 코드 특화 |
| `inclusionai/ling-3.1-flash` | 262,144 | 범용 |
| `inclusionai/ling-3.0-flash-sante:free` | 262,144 | 범용 |
| `poolside/laguna-xs-2.1:free` | 262,144 | 경량 |

## 도구별 별칭 (llm)

- `10jo` — LongCat 2.5 (주력)
- `10jo-fast` — Step 3.7 Flash
- `10jo-code` — Laguna S 2.1
- `10jo-long` — Ling 3.1 Flash

## 불가 확정 (재검토 방지)

| 제안 | 판정 | 이유 |
|---|---|---|
| Qwen 2.5-Coder 32B 로컬 | ❌ 불가 | GPU VRAM 6GB (필요: 18~20GB) |
| Modal / Daytona 서버리스 | ❌ 불가 | 유료 (회사 규칙 4절) |
| Cursor | ❌ 제외 | GUI 전용 + headless 버그 |
| Grok API | ❌ 제외 | 유료 ($2~6/1M) |

## 주의

- 프록시가 꺼져 있으면 위 도구들이 모두 실패한다. 게이트웨이 재시작 시 `hermes proxy start`를 다시 실행한다.
- 안티그래비티는 별개 경로다 — Antigravity 앱이 실행 중이어야 한다.
