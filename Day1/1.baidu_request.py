import requests

url = 'http://www.baidu.com'
# 第三步  根据url获取 HTML信息

# 调用类似于浏览器的函数，返回html
response = requests.get(url)

# print(response)
#
# # 返回的html信息字符串类型叫做  response.text
#
# # 返回的html信息二进制类型叫做  response.content
#
# print(response.text)
#
# # 上面的内容会遇到乱码的问题， response.encoding
#
# response.encoding = 'utf-8'
#
# print(response.text)
#
#
# # 返回的html信息二进制（bytes）类叫做 response.content
#
# print(response.content)


# 第五步  保存到文件系统

with open('baidu.html', 'wb') as f:
    f.write(response.content)