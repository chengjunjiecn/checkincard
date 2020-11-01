 
import requests
from flask import json
import ssl
ssl._create_default_https_context = ssl._create_unverified_context 

#嘉翊体温
headers = {
"Cookie": "healthLastLoginTime=$2a$10$oc4/xYa/ueLLzFF7vtOKreIu.8JLlIHk3qmVqCMVhOpUIS40bJcby; route=98c04df13eac867f3aae90f6b18dd5a4; healthLoginName1=%E7%A8%8B%E5%98%89%E7%BF%8A1582462176866; JSESSIONID=6B73764EC5D8C82CD98184331D2A0648"
};


url = "https://health.tripaway.cn/healthCard/add"
data = {"type":"new","isTouched":"无","isHealth":"健康","healthDesc":"","isFamilyHealth":"健康","familyHealth":"","signName":"吴晓蓉","signDate":"2020年11月01日","cardTemp":"36.5"}
res = requests.post(url=url,json=data,headers = headers)
print(res.text)


url = "https://health.tripaway.cn/tempRecord/add"
data = {"remark":"健康，无以下状况,","temp":"36.5","recordTimeStr":"2020-11-01 22:55","field1":"腋温"}
res = requests.post(url=url,json=data,headers = headers)
print(res.text)


#嘉和体温
headers = {
"Cookie": "route=98c04df13eac867f3aae90f6b18dd5a4; healthLoginName1=%E7%A8%8B%E5%98%89%E5%92%8C1598599192206; healthLastLoginTime=$2a$10$A.d4XD2g4i5tDX3EHuEOduloJnsYiOMQ/VCHyxUMCM66r2H8bqEnm; JSESSIONID=8BB663ED7EFFB204FB534474C1F0F870"
};
url = "https://health.tripaway.cn/healthCard/add"
data = {"type":"new","isTouched":"无","isHealth":"健康","healthDesc":"","isFamilyHealth":"健康","familyHealth":"","signName":"吴晓蓉","signDate":"2020年11月01日","cardTemp":"36.5"}
res = requests.post(url=url,json=data,headers = headers)
print(res.text)


url = "https://health.tripaway.cn/tempRecord/add"
data = {"remark":"健康，无以下状况,","temp":"36.5","recordTimeStr":"2020-11-01 22:55","field1":"腋温"}
res = requests.post(url=url,json=data,headers = headers)
print(res.text)
