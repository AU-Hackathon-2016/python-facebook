import requests
import json

token1='CAACEdEose0cBANyYaDK0dTlYUOd7ou7vYigOwlZAMEUmopmTep0xiQSVOffFNuPMVsIxOyhxxOPjrZCYddNDNT0IbcvlZC32SG31wV0Lsl3FVOKlmL1BGDQEsAPIqxBbYhPNZB7kzMFy8BkmeoezSxPGrytefT2sWQ6vUJFtT36JEtnBQ2hIqUZBnlGFWxHvLe086qKN0XQZDZD'

def pictureByID(userID):
    r = requests.get('https://graph.facebook.com/v2.3/'+userID+'?fields=picture&access_token='+token1)
    pic=r.json()
    picURL=pic['picture']['data']['url']
    return picURL

def searchByID(userID):
    r = requests.get('https://graph.facebook.com/v2.3/'+userID+'?access_token='+token1)
    user=r.json()
    user['picture']=pictureByID(userID)
    return user

def searchByName(name,limit):
    userList=[]
    r = requests.get('https://graph.facebook.com/v2.3/search?q='+name+'&type=user&limit='+str(limit)+'&access_token='+token1)
    idList=r.json()
#     print idList
    data=idList['data']
    for content in data:
        userID=content['id']
        userList.append(searchByID(userID))
    return userList

print searchByName('Zhitao Gong',5)
