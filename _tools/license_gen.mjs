#!/usr/bin/env node
/**
 * Merge10 — 관리자용 라이선스 키 생성 도구 (로컬 전용)
 *
 * 사용법:
 *   node _tools/license_gen.mjs lifetime
 *   node _tools/license_gen.mjs day
 *   node _tools/license_gen.mjs trial 30      (30일)
 *
 * 개인키는 `_tools/.merge10_private.pem` 에 있고 git에 올리지 않는다.
 * 이 파일이 새면 누구나 유효한 라이선스를 만들 수 있다.
 *
 * 결제 연동 전까지는 수동 발급용이다.
 * 결제(Stripe/Gumroad) 연동 시 이 스크립트를 웹훅 서버에서 호출하게 된다.
 */
import crypto from "node:crypto";
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const here = path.dirname(fileURLToPath(import.meta.url));
const KEY_PATH = path.join(here, ".merge10_private.pem");

function b64url(buf) {
  return Buffer.from(buf).toString("base64").replace(/\+/g, "-").replace(/\//g, "_").replace(/=+$/, "");
}

function ensureKey() {
  if (fs.existsSync(KEY_PATH)) {
    return crypto.createPrivateKey(fs.readFileSync(KEY_PATH, "utf8"));
  }
  const { privateKey } = crypto.generateKeyPairSync("ec", { namedCurve: "P-256" });
  const pem = privateKey.export({ type: "pkcs8", format: "pem" });
  fs.writeFileSync(KEY_PATH, pem, { mode: 0o600 });
  console.error(`[새 개인키 생성] ${KEY_PATH}`);
  console.error("⚠ 이 파일은 절대 git에 올리지 마세요. .gitignore에 포함되어 있습니다.");
  return crypto.createPrivateKey(pem);
}

function makeSerial() {
  return crypto.randomBytes(6).toString("hex").toUpperCase();
}

function main() {
  const [tier = "lifetime", daysArg] = process.argv.slice(2);
  if (!["trial", "day", "lifetime"].includes(tier)) {
    console.error("사용법: node license_gen.mjs <trial|day|lifetime> [일수]");
    process.exit(1);
  }

  const privateKey = ensureKey();
  const now = new Date();
  const payload = {
    tier,
    issued: now.toISOString(),
    serial: makeSerial(),
  };

  if (tier === "trial") {
    const days = Number(daysArg ?? 14);
    const exp = new Date(now.getTime() + days * 24 * 60 * 60 * 1000);
    payload.expires = exp.toISOString();
  } else if (tier === "day") {
    const exp = new Date(now.getTime() + 24 * 60 * 60 * 1000);
    payload.expires = exp.toISOString();
  }
  // lifetime → expires 없음

  const payloadB64 = b64url(Buffer.from(JSON.stringify(payload), "utf8"));
  const sig = crypto.sign("sha256", Buffer.from(payloadB64, "utf8"), {
    key: privateKey,
    dsaEncoding: "ieee-p1363",
  });
  const token = `${payloadB64}.${b64url(sig)}`;

  console.log("─".repeat(70));
  console.log(`종류: ${tier}${payload.expires ? ` / 만료: ${payload.expires}` : " / 무기한"}`);
  console.log(`일련번호: ${payload.serial}`);
  console.log("─".repeat(70));
  console.log(token);
  console.log("─".repeat(70));
}

main();
