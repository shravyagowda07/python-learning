import requests

print("===== GITHUB USER FINDER =====")
def get_github_user_info():
    #takes a github username from the user
    username = input("Enter Github username: ").strip()

    if not username:
        print("User name cannot be empty.")
        return
    
#Sends a request to the Github API
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)

#check whether user exists
    if response.status_code == 200:
        data = response.json()

# Displays
        print("\n---- Github User Profile ----")
        print(f"Name: {data.get('name') or 'N/A'}")
        print(f"Username: {data.get('login')}")
        print(f"Public Repositories: {data.get('public_repos')}")
        print(f"Followers: {data.get('followers')}")
        print(f"Following: {data.get('following')}")

    elif response.status_code == 404:
        print(f"\nUser {'username'} does not exists.")
    else:
        print("\nFailed to retrive data (Status code: {response.status_code})")

if __name__ == "__main__":
    get_github_user_info()