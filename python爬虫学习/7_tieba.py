import urllib.request
import urllib.parse
import os

org_url = 'http://tieba.baidu.com/f?ie=utf-8'

name = 'python'
start_page = 1
end_page = 5

if not os.path.exists(name):
    os.mkdir(name)

for page in range(start_page, end_page + 1):
    data = {
        'kw' : name,
        'pn' : (page - 1) * 50,
    }
    data = urllib.parse.urlencode(data)
    url = org_url + '&' + data
    header = { 
                'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
                'Connection' : 'keep-alive',
                'Accept' : '*/*',
                'X-Requested-With' : 'XMLHttpRequest',
                #'Sec-Fetch-Mode' : 'cors',
                'Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8',
                'Sec-Fetch-Site' : 'same-origin',
                'Accept-Language' : 'zh-CN,zh;q=0.9',
    }
    request = urllib.request.Request(url=url, headers=header)
    print('第%s页开始下载' % page)
    response = urllib.request.urlopen(request)
    file_name = name + '/' + name + str(page) + '.html'
    with open(file_name, 'wb') as fp :
        fp.write(response.read()) 






