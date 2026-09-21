import requests
from pathlib import Path

SOURCE_URL = "https://pstream.ir/playlist.m3u8"
OUTPUT_FILE = Path(__file__).resolve().parent / "webplaylist.m3u8"

def main():
    print(f"Fetching: {SOURCE_URL}")

    response = requests.get(
        SOURCE_URL,
        timeout=30,
        headers={
            "User-Agent": "Mozilla/5.0"
        }
    )
    response.raise_for_status()

    content = response.content

    if not content:
        raise RuntimeError("Downloaded playlist is empty.")

    OUTPUT_FILE.write_bytes(content)

    print(f"Saved: {OUTPUT_FILE}")
    print(f"Size: {len(content)} bytes")


if __name__ == "__main__":
    main()
