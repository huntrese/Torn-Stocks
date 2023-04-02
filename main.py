import requests, time, pywhatkit as kit
from datetime import datetime, timedelta
site="https://tornsy.com/api/stocks"

def stockCheker():
    r = requests.get(site)
    data= r.json()
    for i in data["data"]:
        if i["stock"]=='SYM':
            price=float(i["price"])
            print("SYM",price)
            if price>=602:
                kit.sendwhatmsg_instantly("+44 7393 357630",f"SYM price is: {price} go buy shit ",5)



C=True
while C:
    stockCheker()
    x=datetime.today()
    y = x.replace(second=20) + timedelta(minutes=1)
    delta_t=y-x

    secs=delta_t.total_seconds()
    print("$",secs)
    t = time.sleep(secs)
    
    


