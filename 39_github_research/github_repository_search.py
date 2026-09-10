import requests
from requests.exceptions import ConnectionError, HTTPError, RequestException, Timeout


def search_github_repositories():
    keyword = input("Enter repository keyword: ").strip()
    if not keyword:
        print("No keyword provided.")
        return

    # GitHub Search API configuration
    url = "https://api.github.com/search/repositories"
    params = {"q": keyword, "per_page": 10}
    headers = {"Accept": "application/vnd.github.v3+json"}

    try:
        # requests.get() with timeout parameter
        response = requests.get(url, params=params, headers=headers, timeout=10)

        # raise_for_status() handles API status code errors (4xx, 5xx)
        response.raise_for_status()

        # JSON response handling
        data = response.json()

    # Exception handling for specific requests errors
    except Timeout:
        print("Error: The request timed out. Please try again.")
        return
    except ConnectionError:
        print("Error: Could not connect to GitHub. Check your internet connection.")
        return
    except HTTPError as http_err:
        print(f"HTTP Error occurred: {http_err} (Status Code: {response.status_code})")
        return
    except RequestException as req_err:
        print(f"An unexpected API error occurred: {req_err}")
        return

    items = data.get("items", [])

    print("\n===== GITHUB REPOSITORY SEARCH =====")
    print(f"\nEnter repository keyword: {keyword}\n")
    print("===== RESULTS =====\n")

    if not items:
        print("No repositories found.")
        return

    most_starred_repo = None
    max_stars = -1

    # Loops with enumerate() to list results
    for index, repo in enumerate(items, start=1):
        name = repo.get("name", "N/A")
        owner = repo.get("owner", {}).get("login", "N/A")
        stars = repo.get("stargazers_count", 0)
        language = repo.get("language") or "N/A"
        html_url = repo.get("html_url", "N/A")

        print(f"{index}. Repository: {name}")
        print(f"   Owner:      {owner}")
        print(f"   Stars:      {stars}")
        print(f"   Language:   {language}")
        print(f"   URL:        {html_url}\n")

        # Track the most starred repository for summary
        if stars > max_stars:
            max_stars = stars
            most_starred_repo = name

    # Summary section matching the output challenge requirement
    print("===== SUMMARY =====\n")
    print(f"Total repositories found: {len(items)}")
    print(f"Most starred repository:  {most_starred_repo}")
    print(f"Stars:                    {max_stars}")


if __name__ == "__main__":
    search_github_repositories()