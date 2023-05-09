import requests


url='https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r=requests.get(url,headers=headers)
print(r.status_code)
response_dict=r.json()
print(response_dict.keys())


print(f"Total Repo-{response_dict['total_count']}")
repo_dic=response_dict['items']
print(f"total repo item{len(repo_dic)}")

repo_dic = repo_dic[0]
print(f"\nKeys: {len(repo_dic)}")
# for key in sorted(repo_dic.keys()):
#     print(key)


