import requests
import json

ctg = 'OL7'
#rect = '127.0261466,37.4658277,127.0702340,37.5242554'
#rect = ['127.05,37.50,127.06,37.51','127.06,37.50,127.07,37.51','127.05,37.51,127.06,37.52','127.06,37.51,127.07,37.52']

rad = ['&y=37.514322572335935&x=127.06283102249932&radius=20000',
       '&y=37.51&x=127.06&radius=20000',
       '&y=37.50&x=127.05&radius=20000',
       '&y=37.51&x=127.05&radius=20000',
       '&y=37.51&x=127.07&radius=20000',
       '&y=37.50&x=127.07&radius=20000',
       '&y=37.50&x=127.06&radius=20000',
       '&y=37.50&x=127.08&radius=20000',


       ]


#url = "https://dapi.kakao.com/v2/local/search/category.json?category_group_code="+ ctg + "&rect=" + rect + '&page=' + page


payload = ""
access_token = "41cfe2db04d2f5d4ec715c5952dc407a"


headers = {'Content-Type' : "application/x-www-form-urlencoded", 'Cache-Control': "no-cache",}
headers.update({'Authorization' : "KakaoAK " + access_token})

f = open(ctg + '.txt', 'w')

for radv in rad:
       
    for pv in range (1,10):
        url = "https://dapi.kakao.com/v2/local/search/category.json?category_group_code="+ ctg + str(radv) + '&page=' + str(pv)
        response = requests.request("GET", url ,data=payload, headers=headers)
        lst = json.loads(response.text)['documents']

        for item in lst:
            print(item['id'])
            f.write(item['id'] + '\n')

f.close()
