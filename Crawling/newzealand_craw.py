import requests
import json 
import datetime
from db_connect import foreignbank_info


def nzd_craw(conn):

    now = datetime.datetime.now()

    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
        'apikey': 'l7xx93b1538ae6564c3fa170f899b645c605',
        'Connection': 'keep-alive',
        'Host': 'api.asb.co.nz',
        'Origin': 'https://www.asb.co.nz',
        'Referer': 'https://www.asb.co.nz/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'
    }

    req = requests.get('https://api.asb.co.nz/public/v1/exchange-rates', headers=headers) 

    # print(req.text) 이게 이미 위에서 json에서 딕셔너리 형태로 바뀐 form 이다.
    neo_result = json.loads(req.text)




    # type을 확인해주면 dict라고 뜨는데 json에서 dict형태로 바꾸는데 성공한 것임!
    # print(type(neo_result))
    # print(neo_result) 를 해주면 json에서 dict형태로 바뀐 데이터들이 줄줄 나온다. 

    # 이제 JPY랑 USD 의 정보를 가져오려면
    # for 문을 돌려야한다.. 한번 돌려보자..! 

    #def nation_cur_info(neo_result): 
    #    for i in neo_result:
    #        print(i)
    #11,18
    usd = (neo_result.get('value')[18].get('buysNotes'))
    jpy = (neo_result.get('value')[11].get('buysNotes'))
    
    usd = 1/float(usd)
    jpy = 1/float(jpy)
    
    foreignbank_info(conn, 'NZD', usd, jpy, now)