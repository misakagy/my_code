import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

class zhiLianSpider(object):
    url = 'https://sou.zhaopin.com/?'
    def __init__(self, jl, kw, startpage, endpage):
        self.jl = jl
        self.kw = kw
        self.startpage = startpage
        self.endpage = endpage
    def handle_request(self, page):     
        pass
    
    def run(self):
        pass


def main():
    pass

if __name__ == '__main__':
    main()