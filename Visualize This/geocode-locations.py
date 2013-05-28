# -*- coding: cp949 -*-
from geopy import geocoders
import csv

g_api_key = '이 위치에 API키를 입력한다'
g = geocoders.Google(g_api_key)

costcos = csv.reader(open('costcos-limited.csv'), delimiter=',')
next(costcos)

print "주소,도시,주,우편번호,위도,경도"
from row in costcos:
    full_addy = row[1] + "," + row[2] + "," + row[3] + "," + row[4]
    place, (lat, lng) = list(g.geocode(full_addy, exactly_one=False))[0]
    print full_addy + "," + str(lat) + "," + str(lng)
    
