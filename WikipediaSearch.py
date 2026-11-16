#54th github project --> Wikipedia Search
print('----------Wikipedia Search----------')
import requests


def main():
    print("WIKIPEDIA SEARCH")

    query = input("Search for: ").strip()
    if not query:
        print("No search term given.")
        return

    url = "https://api.wikimedia.org/core/v1/wikipedia/en/search/page"
    headers = {
        "User-Agent": "MyWikipediaSearch/1.0 (your@email.com)"
    }
    params = {
        "q": query,
        "limit": 5,
    }

    try:
        response = requests.get(url, headers=headers, params=params, timeout=5)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return

    data = response.json()
    pages = data.get("pages", [])

    if not pages:
        print("No results found.")
        return

    print(f"\nTop {len(pages)} results:\n")
    for i, page in enumerate(pages, 1):
        title = page.get("title", "No title")
        description = page.get("description") or "No description available."
        key = page.get("key", "")
        article_url = f"https://en.wikipedia.org/wiki/{key}"

        print(f"{i}. {title}")
        print(f"   {description}")
        print(f"   {article_url}\n")

main()