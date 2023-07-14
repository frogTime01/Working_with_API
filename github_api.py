import requests
import json

user_name = "frogTime01"
url = f"https://api.github.com/users/{user_name}/repos"

repo_list = requests.get(url).json()
with open("repo.json", "w", encoding="utf8") as f:
    json.dump(repo_list, f)
print(*[item["name"] for item in repo_list])
