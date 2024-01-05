import requests

from plotly.graph_objs import Bar
from plotly import offline

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {
    'Accept': 'application/vnd.github.v3+json'
}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

response_dict = r.json()

# basic info
print(f"Total repo: {response_dict['total_count']}")
repo_dicts = response_dict['items']

repo_names = []
stars = []
for repo_dict in repo_dicts:
    repo_names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

data = [{
    'type': 'bar',
    'x': repo_names,
    'y': stars
}]

my_layout = {
    'title': "'Most-Starred Python Projects on GitHub",
    'xaxis': {'title': 'Repo'},
    'yaxis': {'title': 'Stars'}
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename="python_repos.html")
