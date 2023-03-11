import requests
import json

url = "https://twitter154.p.rapidapi.com/user/tweets"

querystring = {"username":"joebiden","limit":"2","user_id":"939091","include_replies":"false"}

headers = {
	"X-RapidAPI-Key": "8cd4e9e876msh94390cd459bab51p19ccc9jsn5c5983825c97",
	"X-RapidAPI-Host": "twitter154.p.rapidapi.com"
}

#get from api
#response = requests.request("GET", url, headers=headers, params=querystring)
#response = json.loads(response.text)

#get from local
f = open('jbtweets.json')
response = json.load(f)

for result in response['results']: 
    print("**************new line **************************\n")
    print(result)

