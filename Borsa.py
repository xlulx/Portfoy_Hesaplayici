from urllib.request import urlopen 
import json 

Dosya = open("Portföy.txt","a+")

portföy = ["THYAO", "ISCTR"]
fiyatlar = []

for hisse in portföy :
    url = f"https://bigpara.hurriyet.com.tr/api/v1/borsa/hisseyuzeysel/{hisse}"
    # store the response of URL 
    response = urlopen(url) 
    
    # storing the JSON response  
    # from url in data 
    data_json = json.loads(response.read()) 
    
    # print the json response 
    fiyatlar.append([data_json["data"]["hisseYuzeysel"]["sembol"] , data_json["data"]["hisseYuzeysel"]["alis"]])
    
print(fiyatlar)