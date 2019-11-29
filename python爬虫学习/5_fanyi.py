import urllib.request
import urllib.parse

post_url = 'http://fanyi.baidu.com/v2transapi'

form_data = {
    'from' : 'en', 
    'to' : 'zh', 
    'query' : 'wolf',
    'transtype' : 'realtime', 
    'simple_mean_flag' : '3',
    'sign' : '275695.55262',
    'token' : '5060022639da2984ff224b80b19d1e6e',
}
form_data = urllib.parse.urlencode(form_data).encode()
print(form_data)
headers = { 
            'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
            'Connection' : 'keep-alive',
            #'Content-Length' : '126',
            'Accept' : '*/*',
            'Origin' : 'https://fanyi.baidu.com',
            'X-Requested-With' : 'XMLHttpRequest',
            'Sec-Fetch-Mode' : 'cors',
            'Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8',
            'Sec-Fetch-Site' : 'same-origin',
            'Referer' : 'https://fanyi.baidu.com/?aldtype=16047',
            #'Accept-Encoding' : 'gzip, deflate, br'
            'Accept-Language' : 'zh-CN,zh;q=0.9'
            #'Cookie' : 'BIDUPSID=701E7F18812F99DA03237CF8795622CD; PSTM=1529836833; MCITY=-%3A; BDUSS=owM3RVTXZMMVAwYXkwR2QzSlg2VG9qNH5GUUVqSmh1ZnM3aHRvSkg2Y2h-SnhjQVFBQUFBJCQAAAAAAAAAAAEAAACNWRcP1qrKttW-s6QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACFvdVwhb3Vcel; BAIDUID=117D145692E96770C822D5B290F7C2A9:FG=1; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; H_PS_PSSID=; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; APPGUIDE_8_0_0=1; delPer=0; PSINO=5; BDRCVFR[n9IS1zhFc9f]=mk3SLVN4HKm; locale=zh; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1567960275,1567962440; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1567962440; __yjsv5_shitong=1.0_7_c13f481a2e82ddb35c91485d7276415091ef_300_1567962440818_125.119.221.71_b5205f30; yjs_js_security_passport=9b7a3d0ae881b0c5e3345b3b7d70b969898a91d7_1567962441_js; to_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; from_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D'
}

request = urllib.request.Request(url = post_url, headers=headers)

response = urllib.request.urlopen(request, data = form_data)

print(response.read().decode())