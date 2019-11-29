import urllib.request

url = 'http://www.baidu.com'

response = urllib.request.urlopen(url)

#print(dict(response.getheaders()))

with open('baid.html', 'wb') as fp:
    fp.write(response.read())

image_url = 'https://ss0.bdstatic.com/94oJfD_bAAcT8t7mm9GUKT-xh_/timg?image&quality=100&size=b4000_4000&sec=1567441978&di=516a44b4bde4b612f4271be5194d66d1&src=http://pic33.nipic.com/20130924/9822353_015119969000_2.jpg'
image = urllib.request.urlopen(image_url)
with open('image.jpg', 'wb') as fp:
    fp.write(image.read())

urllib.request.urlretrieve(image_url, 'woman.jpg')