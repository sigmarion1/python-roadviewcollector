import requests
import json

ctg = 'PM9'
#rect = '127.0261466,37.4658277,127.0702340,37.5242554'
#rect = ['127.05,37.50,127.06,37.51','127.06,37.50,127.07,37.51','127.05,37.51,127.06,37.52','127.06,37.51,127.07,37.52']

rect = ['127.0,37.5,127.1,37.6',
        '127.1.37.5,127.2,37.6',
        '127.0.37.6,127.1.37.7',
        '127.1.37.6,127.2,37.7',
        '127.1.37.7,127.2.37.8',
        '127.2.37.6,127.3,37.7',
        '127.2,37.7,127.3,37.8']

#url = "https://dapi.kakao.com/v2/local/search/category.json?category_group_code="+ ctg + "&rect=" + rect + '&page=' + page


payload = ""
access_token = "41cfe2db04d2f5d4ec715c5952dc407a"


headers = {'Content-Type' : "application/x-www-form-urlencoded", 'Cache-Control': "no-cache",}
headers.update({'Authorization' : "KakaoAK " + access_token})

f = open(ctg + '.txt', 'w')

for rv in rect:
    for pv in range (1,15):
        url = "https://dapi.kakao.com/v2/local/search/category.json?category_group_code="+ ctg + "&rect=" + str(rv) + '&page=' + str(pv)
    
        response = requests.request("GET", url ,data=payload, headers=headers)
        lst = json.loads(response.text)['documents']

        for item in lst:
            print(item['id'])
            f.write(item['id'] + '\n')

f.close()
