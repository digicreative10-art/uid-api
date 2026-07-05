from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "API is Running!"}

@app.get("/check-uid/{uid}")
def check_uid(uid: str):
    try:
        url = 'https://apis.mbtopupbazar.com/api/game-id-checker'
        
        headers = {
            'accept': 'application/json',
            'accept-language': 'en-US,en;q=0.9,bn;q=0.8',
            'content-type': 'application/json',
            'origin': 'https://mbtopupbazar.com',
            'priority': 'u=1, i',
            'referer': 'https://mbtopupbazar.com/',
            'sec-ch-ua': '"Not;A=Brand";v="8", "Chromium";v="150", "Google Chrome";v="150"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Linux; Android 15; Pixel 9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Mobile Safari/537.36',
        }

        json_data = {'playerid': uid}

        response = requests.post(url, headers=headers, json=json_data)
        data = response.json()
        
        # তোমার দেওয়া JSON রেসপন্স অনুযায়ী পারফেক্ট লজিক
        if data.get("error") is False and "data" in data and "username" in data["data"]:
            username = data["data"]["username"]
        else:
            username = "Not Found"

        # ঠিক তুমি যেভাবে চেয়েছো সেভাবে রিটার্ন করা হচ্ছে
        return {
            "uid": uid,
            "username": username
        }
        
    except Exception:
        return {
            "uid": uid,
            "username": "Error"
        }
