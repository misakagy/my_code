import urllib.request
import urllib.parse

url = 'http://www.baidu.com/s?'

word = input(" Input search word !!\n")

data = {#'ie':'utf-8', 
        'wd':word}

query_str = urllib.parse.urlencode(data)

url += query_str
print(url)
response = urllib.request.urlopen(url)

filename = word + '.html'
with open(filename, 'wb') as fp:
    fp.write(response.read())