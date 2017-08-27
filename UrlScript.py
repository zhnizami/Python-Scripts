import re
import urllib.request
url="http://www.google.com/finance?q="
def getInput():
    try:
        global url
        stock=input("Please enter your stock company name:")
        url=url+stock
        data=urllib.request.urlopen(url).read()
        data1=data.decode("utf-8")
        m=re.search('meta itemprop="price"',data1)
        start= m.start()
        end=start+50
        data3=data1[start:end]
        m=re.search('content="',data3)
        start=m.end()
        data4=data3[start:]
        m=re.search("/>",data4)
        start=0
        end=m.end()-4
        DATA=data4[start:end]
        print("___________________________________________________")
        print("Stock Rate of "+stock +":  "+DATA)
    except:
        print("No such stock company found!")

getInput()
