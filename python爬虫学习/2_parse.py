import urllib.parse

url = 'http://www.baidu.com/index.html?name=二狗&passwd=123456'

ret = urllib.parse.quote(url)
print(ret)
ret = urllib.parse.unquote(ret)
print(ret)

date = {'name':'gongyi', 'age':'22', 'company':'hikvision'}
ret = urllib.parse.urlencode(date)
print(ret)
