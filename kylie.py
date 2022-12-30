import requests
import pandas as pd
from requests import Session
from bs4 import BeautifulSoup as bs

s=Session()
import requests

cookies = {
    'vuex-en-eu': '{%22product%22:{%22variantId%22:null}%2C%22user%22:{%22isModalOpen%22:false%2C%22customerProfile%22:{}}%2C%22notify%22:{%22isSiteEnabled%22:true%2C%22isFormCompleted%22:false%2C%22isNotifyModalOpen%22:false%2C%22user%22:{}%2C%22products%22:[]%2C%22pendingProduct%22:%22%22%2C%22buttonLabel%22:%22NOTIFY%20ME%22%2C%22successLabel%22:%22Notification%20successful!%22%2C%22currentProductName%22:%22%22%2C%22serviceData%22:{%22endpointUrl%22:%22p28q8w4y93.execute-api.eu-central-1.amazonaws.com/prod%22%2C%22apiKey%22:%220pZ2yOLMkgvy7iw87lCyBzgvbOKN1FKuzVsIS6q0%22}}}',
    'REGION': 'EU',
    'forterToken': 'c4ef525060584dda8ba34a4ae6e2785e_1671605385032__UDF43-mnf-anf_13ck',
    'OptanonConsent': 'isIABGlobal=false&datestamp=Wed+Dec+21+2022+12%3A20%3A12+GMT%2B0530+(India+Standard+Time)&version=202208.1.0&hosts=&consentId=9263b029-8ec2-4854-b978-05b88bc52f79&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&geolocation=IN%3BDL&AwaitingReconsent=false',
    'at_check': 'true',
    'mbox': 'PC#2f47ef0e8c4c4009942acd8ae6ab2275.31_0#1734779050|session#f0026e45e8ca4a1d9cfc0547a6f76c25#1671607274',
    'NoCookie': 'true',
    'OptanonAlertBoxClosed': '2022-12-20T11:04:13.227Z',
    '_attn_': 'eyJ1Ijoie1wiY29cIjoxNjcxNTM0MjUzMjUwLFwidW9cIjoxNjcxNTM0MjUzMjUwLFwibWFcIjoyMTkwMCxcImluXCI6ZmFsc2UsXCJ2YWxcIjpcImI5MzA1OWVlZDlmZjRhOGRhZjQ2ZGRhOWE4NzBlZGFhXCJ9In0=',
    'tpc_a': 'e65975fddf9f4c88a50bb5c6d49c2c22.1671534253.0dN.1671604190',
    '__attentive_id': 'b93059eed9ff4a8daf46dda9a870edaa',
    '__attentive_cco': '1671534253250',
    '__attentive_dv': '1',
    '_gcl_au': '1.1.297625122.1671534258',
    '_fbp': 'fb.1.1671534258746.874445305',
    '_ga': 'GA1.1.2020528193.1671534260',
    '_gid': 'GA1.2.1356831555.1671534260',
    'adobeujs-optin': '%7B%22aam%22%3Atrue%2C%22adcloud%22%3Atrue%2C%22aa%22%3Atrue%2C%22campaign%22%3Afalse%2C%22ecid%22%3Atrue%2C%22livefyre%22%3Afalse%2C%22target%22%3Afalse%2C%22mediaaa%22%3Afalse%7D',
    'AMCV_157D1990530FC26A0A490D4C%40AdobeOrg': '-1124106680%7CMCMID%7C14058605793425920423042194391505956394%7CMCAAMLH-1672208991%7C12%7CMCAAMB-1672208991%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1671611391s%7CNONE%7CMCAID%7CNONE%7CMCSYNCSOP%7C411-19354%7CvVersion%7C5.2.0%7CMCIDTS%7C19347',
    'AMCVS_157D1990530FC26A0A490D4C%40AdobeOrg': '1',
    's_ppvl': 'EU%253Akylie-cosmetics%253Ashop-all%2C78%2C78%2C35216%2C1536%2C439%2C1536%2C864%2C1.25%2CP',
    's_ppv': 'https%253A%2F%2Fkyliecosmetics.com%2Fen-eu%2Fkylie-cosmetics%2Fshop-all%2C100%2C100%2C439%2C1536%2C439%2C1536%2C864%2C1.25%2CP',
    's_visnum': '1671605413269',
    's_nr': '1671605413270-Repeat',
    's_cc': 'true',
    'QuantumMetricUserID': 'd587a0c91ae37a146cde93f58d5e3e6b',
    '_ga_HJXEVNV20J': 'GS1.1.1671604188.2.1.1671605382.0.0.0',
    's_sq': '%5B%5BB%5D%5D',
    'affinity': '"f6cbef914f408170"',
    'BVImplmain_site': '16784',
    '__attentive_pv': '3',
    '__attentive_ss_referrer': 'https://kyliecosmetics.com/en-eu',
    'gpv_e7': 'no%20value',
    's_visnum_s': 'Less%20than%201%20day',
    's_visit': '1',
    'QuantumMetricSessionID': 'f1ae9348ee930ee66713a0e45797614d',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Referer': 'https://kyliecosmetics.com/en-eu/kylie-cosmetics/shop-all',
    # 'Cookie': 'vuex-en-eu={%22product%22:{%22variantId%22:null}%2C%22user%22:{%22isModalOpen%22:false%2C%22customerProfile%22:{}}%2C%22notify%22:{%22isSiteEnabled%22:true%2C%22isFormCompleted%22:false%2C%22isNotifyModalOpen%22:false%2C%22user%22:{}%2C%22products%22:[]%2C%22pendingProduct%22:%22%22%2C%22buttonLabel%22:%22NOTIFY%20ME%22%2C%22successLabel%22:%22Notification%20successful!%22%2C%22currentProductName%22:%22%22%2C%22serviceData%22:{%22endpointUrl%22:%22p28q8w4y93.execute-api.eu-central-1.amazonaws.com/prod%22%2C%22apiKey%22:%220pZ2yOLMkgvy7iw87lCyBzgvbOKN1FKuzVsIS6q0%22}}}; REGION=EU; forterToken=c4ef525060584dda8ba34a4ae6e2785e_1671605385032__UDF43-mnf-anf_13ck; OptanonConsent=isIABGlobal=false&datestamp=Wed+Dec+21+2022+12%3A20%3A12+GMT%2B0530+(India+Standard+Time)&version=202208.1.0&hosts=&consentId=9263b029-8ec2-4854-b978-05b88bc52f79&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&geolocation=IN%3BDL&AwaitingReconsent=false; at_check=true; mbox=PC#2f47ef0e8c4c4009942acd8ae6ab2275.31_0#1734779050|session#f0026e45e8ca4a1d9cfc0547a6f76c25#1671607274; NoCookie=true; OptanonAlertBoxClosed=2022-12-20T11:04:13.227Z; _attn_=eyJ1Ijoie1wiY29cIjoxNjcxNTM0MjUzMjUwLFwidW9cIjoxNjcxNTM0MjUzMjUwLFwibWFcIjoyMTkwMCxcImluXCI6ZmFsc2UsXCJ2YWxcIjpcImI5MzA1OWVlZDlmZjRhOGRhZjQ2ZGRhOWE4NzBlZGFhXCJ9In0=; tpc_a=e65975fddf9f4c88a50bb5c6d49c2c22.1671534253.0dN.1671604190; __attentive_id=b93059eed9ff4a8daf46dda9a870edaa; __attentive_cco=1671534253250; __attentive_dv=1; _gcl_au=1.1.297625122.1671534258; _fbp=fb.1.1671534258746.874445305; _ga=GA1.1.2020528193.1671534260; _gid=GA1.2.1356831555.1671534260; adobeujs-optin=%7B%22aam%22%3Atrue%2C%22adcloud%22%3Atrue%2C%22aa%22%3Atrue%2C%22campaign%22%3Afalse%2C%22ecid%22%3Atrue%2C%22livefyre%22%3Afalse%2C%22target%22%3Afalse%2C%22mediaaa%22%3Afalse%7D; AMCV_157D1990530FC26A0A490D4C%40AdobeOrg=-1124106680%7CMCMID%7C14058605793425920423042194391505956394%7CMCAAMLH-1672208991%7C12%7CMCAAMB-1672208991%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1671611391s%7CNONE%7CMCAID%7CNONE%7CMCSYNCSOP%7C411-19354%7CvVersion%7C5.2.0%7CMCIDTS%7C19347; AMCVS_157D1990530FC26A0A490D4C%40AdobeOrg=1; s_ppvl=EU%253Akylie-cosmetics%253Ashop-all%2C78%2C78%2C35216%2C1536%2C439%2C1536%2C864%2C1.25%2CP; s_ppv=https%253A%2F%2Fkyliecosmetics.com%2Fen-eu%2Fkylie-cosmetics%2Fshop-all%2C100%2C100%2C439%2C1536%2C439%2C1536%2C864%2C1.25%2CP; s_visnum=1671605413269; s_nr=1671605413270-Repeat; s_cc=true; QuantumMetricUserID=d587a0c91ae37a146cde93f58d5e3e6b; _ga_HJXEVNV20J=GS1.1.1671604188.2.1.1671605382.0.0.0; s_sq=%5B%5BB%5D%5D; affinity="f6cbef914f408170"; BVImplmain_site=16784; __attentive_pv=3; __attentive_ss_referrer=https://kyliecosmetics.com/en-eu; gpv_e7=no%20value; s_visnum_s=Less%20than%201%20day; s_visit=1; QuantumMetricSessionID=f1ae9348ee930ee66713a0e45797614d',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

response = requests.get(
    'https://kyliecosmetics.com/content/kylie-beauty/countries/eu/en/kylie-cosmetics/shop-all/jcr:content/root/main_area/product_list_copy.list.json/0.json',
    cookies=cookies,
    headers=headers,
)
response
r=response.json()
r
#r.keys()
#r[0]
#r[0].keys()
#r[0]['right']
#r[0]['right']['brand']
##r[0]['right'].keys()
#r[0]['right']['name']
#r[0]['right']['bundleName']
#r[1]['right']['bundleName']
#r[1]['right'].keys()
#r[1]['right']['imageGallerySrc']
#r[0]['right']['imageGallerySrc']
#r[2]['right']['imageGallerySrc']
#len(r[2]['right'])
#len(r[1]['right'])
#len(r[0]['right'])
#len(r[3]['right'])
#r[0]['right'].keys()
#r[1]['right'].keys()
#r[5]['right'].keys()
#len(r[5]['right'])
#r['right'].keys()
#r[0]['right'].keys()
list=[]
for i in r:
    name=i.get('right').get('name')
    price=i.get('right').get('price')
    img=i.get('right').get('imageSrc')
    handle=i.get('right').get('handle')
    brand=i.get('right').get('brand')
    link=i.get('right').get('url')
    print(link)
    data={'name':name,
         'price':price,
         'img':img,
         'handle':handle,
         'brand':brand,
         'link':link
         }
    list.append(data)
    print(list)
df = pd.DataFrame(list)
df.to_excel('kylie.xlsx')
