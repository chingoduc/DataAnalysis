import urllib.request
from bs4 import BeautifulSoup

f = open('wunder-data.txt', 'wt')

for m in range(1, 13):
    for d in range(1, 32):
        if(m == 2 and d > 28):
            break
        elif(m in [4, 6, 9, 11] and d > 30):
            break

        url = "http://www.wunderground.com/history/airport/KBUF/2009/" + str(m) + '/' + str(d) + "/DailyHistory.html"
        page = urllib.request.urlopen(url)

        soup = BeautifulSoup(page)
        dayTemp = soup.find_all(attrs={"class":"nobr"})[5].span.string

        if len(str(m)) < 2:
            mStamp = '0' + str(m)
        else:
            msStamp = str(m)

        if len(str(d)) < 2:
            dStamp = '0' + str(d)
        else:
            dStamp = str(d)

        timestamp = '2009' + mStamp + dStamp

        print(timestamp + ': ' + dayTemp)
        f.write(timestamp + ',' + dayTemp + '\n')

f.close()
