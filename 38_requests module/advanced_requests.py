import requests

print("==== GITHUB REPOSITORY FINDER ====")
def git_repository():
    # Takes the github username
    username = input("Enter Github username: ")

    #Send a request to the Github API
    url = f"https://api.github.com/users/{username}/repos"

    try:
        #Request Github API with a timeout
        response = requests.get(url, timeout=5)

        #Raise HTTPError
        response.raise_for_status()

        repos = response.json()

        print("\nRepositories:\n")
        if not repos:
            print("No public repositories found.")
            return

        for index, repo in enumerate(repos, start=1):
            name = repo.get("name")
            html_url = repo.get("html_url")
            print(f"{index}. {name}")
            print(f" URL:{html_url}\n")

    except requests.exception.Timeout:
        print('\nError: The request timed out. Please try again later.')
    except requests.exceptions.ConnectionError:
        print("\nError: A connection error occured. Check your internet connection.")
    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 404:
            print(f"\nError: User '{username}' not found.")
        else:
            print(f"\nHTTP error occured: {http_err}")
    except requests.exceptions.RequestException as err:
        print(f"\nAn error occured: {err}")

if __name__ == "__main__":
    git_repository()