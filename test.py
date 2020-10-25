res = requests.post(url=url,json=data,headers = headers)


url = "https://health.tripaway.cn/login"

username=health_%E7%A8%8B%E5%98%89%E7%BF%8A%40%26a123456%40%26%40%26%40%26%40%26

res = requests.post(url=url,json=data,headers = headers)
print(res.text)
headers = {
"Content-Type": "application/json",
"Origin": "https://health.tripaway.cn",
"Sec-Fetch-Site": "same-origin",
"Sec-Fetch-Mode": "cors",
"Sec-Fetch-Dest": "empty",
"Referer": "https://health.tripaway.cn/html/health/temp-record-parent.html?ver=1.0.32",
"Accept-Encoding": "gzip, deflate, br",
"Accept-Language": "zh-CN,zh;q=0.9",
"Cookie": "route=26fe6cc8d720507b1d09e68194f40f9c; healthLoginName1=%E7%A8%8B%E5%98%89%E7%BF%8A1582462176866; healthLastLoginTime=$2a$10$oc4/xYa/ueLLzFF7vtOKreIu.8JLlIHk3qmVqCMVhOpUIS40bJcby; JSESSIONID=8C9603EA3B9B51443F41C5579F096321"


};
