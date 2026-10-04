"""GPU 모니터링 — 판단 2 이행.

RTX 3060 사용률·VRAM 사용량을 기록하고, 과부하 시 경고.
"""
import subprocess
import json
import pathlib
from datetime import datetime

LOG_DIR = pathlib.Path('D:/10jo_Studio/_shared/monitoring')
LOG_DIR.mkdir(parents=True, exist_ok=True)

def get_gpu_stats():
    """nvidia-smi로 GPU 상태를 조회."""
    try:
        r = subprocess.run(
            ['nvidia-smi', '--query-gpu=utilization.gpu,memory.used,memory.total,temperature.gpu',
             '--format=csv,noheader,nounits'],
            capture_output=True, text=True, timeout=10
        )
        if r.returncode == 0:
            parts = r.stdout.strip().split(',')
            return {
                'util': int(parts[0].strip()),
                'mem_used': int(parts[1].strip()),
                'mem_total': int(parts[2].strip()),
                'temp': int(parts[3].strip())
            }
    except Exception:
        pass
    return None

def main():
    stats = get_gpu_stats()
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    if stats:
        log_file = LOG_DIR / 'gpu_log.jsonl'
        with open(log_file, 'a', encoding='utf-8') as f:
            f.write(json.dumps({'time': now, **stats}, ensure_ascii=False) + '\n')
        
        # 과부하 경고 (사용률 90% 이상 또는 VRAM 90% 이상)
        if stats['util'] >= 90 or stats['mem_used'] >= stats['mem_total'] * 0.9:
            print(f"⚠️ GPU 과부하 경고: 사용률 {stats['util']}%, VRAM {stats['mem_used']}/{stats['mem_total']} MiB")
        else:
            print(f"✓ GPU 정상: 사용률 {stats['util']}%, VRAM {stats['mem_used']}/{stats['mem_total']} MiB, 온도 {stats['temp']}°C")
    else:
        print("✗ GPU 정보 조회 실패")

if __name__ == '__main__':
    main()
