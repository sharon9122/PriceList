import requests
import json
from utilities.configurations import *
from utilities.resources import *

# Constructing the URL
url = getConfig()['API']['endpoint']+'/'+GitRepo.owner+'/'+GitRepo.repo+'/contents/'+GitRepo.path+'?ref='+GitRepo.branch
print(url)
r = requests.get(url,
      headers={
        'accept': 'application/vnd.github.v3.raw',
      }
    )
print(r.status_code)
assert (r.status_code == 200)
finalJson = json.loads(r.content)
# Counter for getting the count of items with price = 17.99
price_count = 0
#Iterating through the list items of json file data
for i in finalJson:
    for key in i.keys():
        if key =='price':
            if(i[key] == 17.99):
                price_count += 1
            if(i[key] > 20.00):
                # Printing the item price and name with price greater than 20.00
                print(i['name'])
                print(i['price'])
print(price_count)