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
labels = []
repo_links = []
for repo_dict in repo_dicts:
    repo_names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    label = f"{owner}<br />{description}"
    labels.append(label)

    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)

data = [{
    'type': 'bar',
    'x': repo_links,
    'y': stars,
    'hovertext': labels,
    'marker': {
        'color': 'rgb(60, 100, 150)',
        'line': {
            'width': 1.5,
            'color': 'rgb(25, 25, 25)'
        }
    },
    'opacity': 0.6
}]

my_layout = {
    'title': "Most-Starred Python Projects on GitHub",
    'titlefont': {
        'size': 28
    },
    'xaxis': {
        'title': 'Repo',
        'titlefont': {
            'size': 15
        },
        'tickfont': {
            'size': 15
        }
    },
    'yaxis': {
        'title': 'Stars',
        'titlefont': {
            'size': 15
        },
        'tickfont': {
            'size': 15
        }
    }
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename="python_repos.html")
