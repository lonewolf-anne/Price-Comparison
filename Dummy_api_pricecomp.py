from fastapi import FastAPI
from pydantic import BaseModel
import json
import math
import requests
class priceData(BaseModel):
    shop:str
    items:str
    price:float

app= FastAPI()
@app.get("/intro")
def intro():
    return{"message":"Welcome to the comparison app."}

shops={}

#if shop in shops=False: instaed of this , use
@app.post("/user_data")
def user_data(data:priceData):
    if data.shop not in shops:
        shops[data.shop]={}
        shops[data.shop][data.items]=data.price#This tells python that go inside shops to the key shop, 
        #then go into the subdictionary iitem and there add the valeu or price
    return{'message':'Data added succesfully',
           'shop':shops
           }
#   shops.append(shop) .You can't use append for dictionaries so use


#This is the comparison logic.1st we have to find if the shop is part of our dictionares


@app.get("/user_comp")
def user_comp(item:str):
    lowest_price=float('inf')
    best_shop=None
    for shop,items in shops.items():
        if item in items:   
            price=items[item]  
            if price<lowest_price :
                lowest_price=price
                best_shop=shop
                if best_shop:
                   return({"shop":best_shop ,"price":price}) 
    
   
results=[]
@app.get('/get_data')
def get_data():
    responce=requests.get("https://fakestoreapi.com/products")
    data=responce.json()
    for item in data[:5]:
        results.append({'title':item['title'],
                        
                    'price':item['price']})
        return{'product':results} 
        
        