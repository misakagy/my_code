import urllib.request
import urllib.parse

url = 'http://www.baidu.com/s?ie=utf-8&wd=ip'

header = { 
            'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
            'Connection' : 'keep-alive',
            'Accept' : '*/*',
            'X-Requested-With' : 'XMLHttpRequest',
            'Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8',
            'Sec-Fetch-Site' : 'same-origin',
            'Accept-Language' : 'zh-CN,zh;q=0.9',
}

handler = urllib.request.ProxyHandler({'http':'118.78.196.54:8118'})

opener = urllib.request.build_opener(handler)

request = urllib.request.Request(url, headers=header)

response = opener.open(request)

with open('ip.html', 'wb') as fp:
    fp.write(response.read())





