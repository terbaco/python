import requests

url= 'https://api.github.com/search/repositories?q=language:python&sort=starts'
http_proxy = "http://proxy.global.sonyericsson.net:8080/accelerated_pac_base.pac"
proxy_dict = {"http": http_proxy}
r = requests.get(url, proxies=proxy_dict)
print("status code:", r.status_code)

response_dict = r.json()
print(response_dict.keys())

print("Total repositories:", response_dict['total_count'])

repo_dicts=response_dict['items']
print("Repositories returened:", len(repo_dicts))

repo_dict = repo_dicts[0]
print("\nKeys:", len(repo_dict))
for key in sorted(repo_dict.keys()):
    print(key)