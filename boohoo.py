import requests
import json
import time
import pandas as pd 
from bs4 import BeautifulSoup as bs
from requests import Session 
s = Session()
s.headers['user-agent']='Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0'
url='https://www.boohoo.com/mens/new-in?start=40&sz=40'
r=s.get(url)
soup=bs(r.text,'html.parser')
product=soup.find_all('div','b-product_tile-container')
new_list=[]
def list_page():
    for item in range(len(product)):
        #name =item.find('h3').text.strip()
    # price=item.find('div','b-product_tile-price').find('span',"b-price-item").text.strip()
        name=product[item].find('h3').text.strip()   
        #price='£'+info['price'](it not run bcause info(json.loads) file is define in the downline)
        icon= 'https:'+product[item].find('img','b-product_tile_swatches-swatch_image').get('src')
        image='https:'+product[item].find('img','null').get('src')
        pro_link='https://www.boohoo.com'+product[item].find('h3').find('a').get('href')
        info=json.loads(product[item].find('h3').find('a').get('data-analytics'))
        #name=info['name']
        price='£'+info['price']
        cat=info['category']
        cat1=info['category1']
        #saleprice=info['salePrice']
        #brand=info['brand']
        colour=info['dimension65']
        itemid=info['itemId']
        id=info['id']
        shirt_cate =info['dimension62']

        detail=s.get(pro_link)
        soup_detail=bs(detail.text,'html.parser')
        D_price=soup_detail.find('span','b-price-item').text.strip()
        D_Name=soup_detail.find('span','b-price-item').text.strip()
        D_colour=soup_detail.find('span','b-variation_label-value').text.strip()  
        D_size=[i.text for i in soup_detail.find_all('span','b-variation_swatch-value_text')]
        #D_Size=soup_detail.find('span','b-variation_swatch-value_text').text
        D_product_detail=soup_detail.find('div','b-product_details-content').text.strip()
        D_product_message=soup_detail.find('p','b-product_details-additional_message').text.strip()
        D_delivery=soup_detail.find('div','b-product_delivery-description').text
        D_return_portal_link=soup_detail.find('div','b-product_shipping-returns_content').find('b').find('a').get('href')
        D_return_content=soup_detail.find('div','b-product_shipping-returns_content').text.strip()
        print(D_price)
        print(D_size)


        #print(name)
        data = {
            # 'landingURL':r.url,
            'id':id,
            'item_rank':item,
            'Name':name,
            'icon':icon,
            'pro_link':pro_link,
            'colour':colour,
                'shirt_cate':shirt_cate,
            'category':cat,
            'category1':cat1,
            'price':price,
            'itemId':itemid,
            'image':image,
            'info':info
                    }
        print(data)
        new_list.append(data)
list_page()
    #df = pd.DataFrame(new_list)
    #df.to_excel('boohoolist.xlsx',index=False)    



























#soup.find('div','b-product_tile-price').find('span',"b-price-item").text.strip()
#name print
#for i in soup.find_all('h3'):
#    name = i.text.strip()
#     
## one json file in soup (data-analysis)
#soup.find('div','b-product_tile-container').find('h3').find('a').get('data-analytics')
#infomation=json.loads(soup.find('div','b-product_tile-container').find('h3').find('a').get('data-analytics'))
