import datetime
import json
import re
import time

import requests
from lxml import etree

from ctrip_config import data, config, city, code, data2
from Check_in import Ck_in
from Check_out import Ck_out
from Mongodb import Mongodb


class Ctrip(object):

    def __init__(self):
        self.headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Content-Length': '518',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Host': 'hotels.ctrip.com',
            'Origin': 'https://hotels.ctrip.com',
            'referer': 'https://hotels.ctrip.com/',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'
        }

        self.data = data
        self.data['SSH_CheckIn'] = time.strftime('%Y-%m-%d')
        self.data['checkIn'] = ck_in
        self.data['checkOut'] = ck_out
        self.data['cityId'] = config[hotel_city]['cityId']
        self.data['cityPY'] = config[hotel_city]['cityPY']
        self.data['RoomGuestCount'] = room, people, '0'
        self.data.update(data)
        self.url = 'http://hotels.ctrip.com/hotel/{}{}'.format(config[hotel_city]['cityPY'], config[hotel_city]['cityId'])
        self.hotel_link = 'https://hotels.ctrip.com/Domestic/Tool/AjaxHotelList.aspx'  # 酒店列表链接 POST

    # 根据条件抓取网页源码
    def get_html(self):
        response = requests.post(url=self.url, data=self.data, headers=self.headers)
        if response.status_code == 200:
            return response.text
        else:
            print(response.status_code)

    # 抓取酒店名称，链接，图片链接
    def get_hotel(self, html):

        tree = etree.HTML(html)
        price = tree.xpath('//span[@class="J_price_lowList"]/text()')

        form_data = data2
        form_data['cityName'] = hotel_city
        form_data['StartTime'] = ck_in
        form_data['DepTime'] = ck_out
        form_data['checkIn'] = ck_in
        form_data['checkOut'] = ck_out
        form_data['RoomGuestCount'] = room, people, '0'
        form_data['cityId'] = config[hotel_city]['cityId']
        form_data['cityPY'] = config[hotel_city]['cityPY']
        form_data['cityCode'] = code[hotel_city]
        cityLat = re.findall('name="cityLat" value="(.*?)"', html, re.S)
        if cityLat:
            form_data['cityLat'] = cityLat[0]
        else:
            print('cityLat is False')
        cityLng = re.findall('name="cityLng" value="(.*?)"', html, re.S)
        if cityLng:
            form_data['cityLng'] = cityLng[0]
        else:
            print('cityLng is False')
        AllHotelIds = re.findall('name="AllHotelIds" value="(.*?)"', html, re.S)
        if AllHotelIds:
            form_data['AllHotelIds'] = AllHotelIds[0].replace(',', '%2C')
        else:
            print('AllHotelIds is False')
        ubt_price_key = re.findall('name="ubt_price_key" value="(.*?)"', html, re.S)
        if ubt_price_key:
            form_data['ubt_price_key'] = ubt_price_key[0]
        else:
            print('ubt_price_key is False')
        traceAdContextId = re.findall('name="traceAdContextId" value="(.*?)"', html, re.S)
        if traceAdContextId:
            form_data['traceAdContextId'] = traceAdContextId[0]
        else:
            print('traceAdContextId is False')
        pyramidHotels = re.findall('name="pyramidHotels" value="(.*?)"', html, re.S)
        if pyramidHotels:
            form_data['pyramidHotels'] = pyramidHotels[0]
        else:
            print('pyramidHotels is False')
        hotelIds = re.findall('hotelIds : \'(.*?)\'', html, re.S)
        if hotelIds:
            form_data['hotelIds'] = hotelIds[0]
        else:
            print('hotelIds is False')
        form_data.update(data2)
        response = requests.post(self.hotel_link, data=form_data)
        if response.status_code == 200:
            hotelPosition = json.loads(response.text)
            links = hotelPosition['hotelPositionJSON']
            for i, link in enumerate(links):
                hotel = {}
                hotel['id'] = link['id']
                hotel['name'] = link['name']
                url = link['url'].split('#')
                hotel['url'] = 'https://hotels.ctrip.com' + url[
                    0] + '&checkIn={check_in}&checkOut={check_out}#'.format(check_in=ck_in, check_out=ck_out) + url[1]
                hotel['img'] = 'https:' + link['img']
                hotel['stardesc'] = link['stardesc']  # 类型--高档型
                hotel['shortName'] = link['shortName']  # 酒店名字
                hotel['address'] = link['address']  # 地址
                hotel['score'] = link['score']  # 评分
                hotel['dpscore'] = link['dpscore']  # 100%用户推荐
                hotel['dpcount'] = link['dpcount']  # 多少客户点评
                hotel['price'] = price[i]
                yield hotel
        else:
            print('hotelPositionJSON is False')

    def parse_content(self, hotel_link):
        response = requests.get(hotel_link['url'])
        tree = etree.HTML(response.text)
        intro = tree.xpath('//*[@id="ctl00_MainContentPlaceHolder_hotelDetailInfo_lbDesc"]/text()')
        if intro:  # 酒店简介
            hotel_link['intro'] = intro[0].replace('\u3000', '')
        else:
            hotel_link['intro'] = ''
        return hotel_link

    def save_to_mongo(self, hk):
        mongo = Mongodb()
        mongo.save_mongo(hk)

    def run(self):
        html = self.get_html()
        for hotel_link in self.get_hotel(html):
            hk = self.parse_content(hotel_link)
            self.save_to_mongo(hk)


if __name__ == '__main__':

    hotel_city = input('请输入城市：')
    if hotel_city in city:
        hotel_city = hotel_city
    else:
        hotel_city = '上海'
    ck_in = Ck_in()
    check = input('入住时间：xxxx-xx-xx')  # 2019-03-26
    ck_in = ck_in.check_in(check)
    ck_out = Ck_out()
    check2 = input('离店时间：xxxx-xx-xx')  # 2019-03-26
    ck_out = ck_out.check_out(check2)

    room = input('入住房间数：1~')
    people = input('入住人数:1~')
    ctrip = Ctrip()
    ctrip.run()



