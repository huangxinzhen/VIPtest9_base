#-*-coding:utf-8-*-
import requests

# urlstr = 'https://www.wanandroid.com/'
# r = requests.get(urlstr)
# # print(r.text)
# print(r.status_code)
# # print(r.content)
# print(r.headers)
# print('#########')
# print(r.cookies)
# print('###########')
# print(r.url)
# print('##########')
# print(r.ok)
# print(r.__reduce__())


# urlstr = 'https://www.baidu.com/'
# r = requests.get(urlstr)
# r.encoding = r.apparent_encoding
# # print(r.text)
# # print(r.encoding)
# # print(r.apparent_encoding)
# # print('###')
# # print(r.content)
# print(r.raw)

"""
post


json在线解析网址：https://www.json.cn/
                https://www.bejson.com/
"""

"""
json报文解析：
r = requests.post(url=urlstr,data=datas)
print(r.status_code)
print(r.json())
#响应结果为res_result
res_result = r.json()
#r2 = 


返回json报文，第一层直接获取，第二层需取第一层后再获取第一层




"""


"""

"""
import requests
urlstr1 = 'urlstr1'
urlstr = 'urlstr'
datas = {'username':'zhuxiaodong','password':'test01'}
#访问登陆后的接口，用session方式访问
s = requests.session()
r = s.post(url=urlstr1)










