from datetime import datetime, timezone

def main():
    now_utc = datetime.now(timezone.utc)
    print(now_utc.isoformat(timespec="microseconds"))

if __name__ == "__main__":
    main()
