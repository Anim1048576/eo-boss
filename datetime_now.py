from datetime import datetime, timezone

def main():
    now_utc = datetime.now(timezone.utc)
    # 2026-02-06T10:39:03.000000+00:00 형태
    print(now_utc.isoformat(timespec="microseconds"))

if __name__ == "__main__":
    main()
