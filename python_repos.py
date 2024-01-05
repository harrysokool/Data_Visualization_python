import requests

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {
    'Accept' : 'application/vnd.github.v3+json'
}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

response_dict = r.json()

# basic info
print(f"Total repo: {response_dict['total_count']}")
repo_dicts = response_dict['items']
print(f"Repo returned: {len(repo_dicts)}")

repo_dict = repo_dicts[0]
# print(f"\nKeys: {len(repo_dict)}")
# for key in sorted(repo_dict.keys()):
#     print(key)

print("\nSelected information about first repository:")
print(f"Name: {repo_dict['name']}")
print(f"Owner: {repo_dict['owner']['login']}")
print(f"Stars: {repo_dict['stargazers_count']}")
print(f"Repo: {repo_dict['html_url']}")
print(f"Created: {repo_dict['created_at']}")
print(f"Updated: {repo_dict['updated_at']}")
print(f"Description: {repo_dict['description']}")




