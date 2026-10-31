import requests
from pathlib import Path

SOURCES = [
    {
        "url": "https://pstream.ir/playlist.m3u8",
        "output": Path(__file__).resolve().parent / "webplaylist.m3u8",
    },
    {
        "url": "https://pstream.ir/playlist.m3u",
        "output": Path(__file__).resolve().parent / "webplaylist.m3u",
    },
]


def fetch_and_save(url: str, output_file: Path) -> None:
    print(f"Fetching: {url}")

    response = requests.get(
        url,
        timeout=30,
        headers={"User-Agent": "Mozilla/5.0"},
    )
    response.raise_for_status()

    content = response.content
    if not content:
        raise RuntimeError(f"Downloaded playlist is empty: {url}")

    output_file.write_bytes(content)

    print(f"Saved: {output_file}")
    print(f"Size: {len(content)} bytes")
    print("-" * 40)


def main():
    for source in SOURCES:
        fetch_and_save(source["url"], source["output"])


if __name__ == "__main__":
    main()
