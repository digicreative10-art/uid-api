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
        
        # সাময়িকভাবে আমরা পুরো ডাটাটা প্রিন্ট করছি দেখার জন্য
        return {
            "uid": uid,
            "raw_data": data
        }
        
    except Exception as e:
        return {
            "uid": uid,
            "error": str(e)
        }
