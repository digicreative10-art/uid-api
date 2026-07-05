from fastapi import FastAPI, HTTPException
import requests

app = FastAPI()

@app.get("/")
def read_root():
    return {
        "status": "success", 
        "message": "UID to Name API is Live!"
    }

# তোমার Vercel API লিংক GET মেথডেই কাজ করবে
@app.get("/check-uid/{uid}")
def check_uid(uid: str):
    if len(uid) < 5:
        raise HTTPException(status_code=400, detail="Invalid UID format")
    
    try:
        # mbtopupbazar-এর API URL
        url = 'https://apis.mbtopupbazar.com/api/game-id-checker'
        
        # তোমার বের করা হেডার্স
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

        # এখানে 'playerid' এর জায়গায় তোমার লিংকের {uid} টা ডায়নামিক করে দিলাম
        json_data = {
            'playerid': uid,
        }

        # mbtopupbazar-এ POST রিকোয়েস্ট পাঠানো হচ্ছে
        response = requests.post(url, headers=headers, json=json_data)
        
        # রেসপন্স ডাটা JSON ফরম্যাটে বের করা
        data = response.json()
        
        # যেহেতু আমরা জানি না mbtopupbazar তাদের JSON-এ নামের ফিল্ডটার কী নাম দিয়েছে (যেমন- name, nickname নাকি account_name), 
        # তাই পুরো ডাটাটাই 'provider_response' এর ভেতর রিটার্ন করে দিচ্ছি। 
        return {
            "status": 200,
            "uid": uid,
            "provider_response": data
        }
        
    except Exception as e:
        return {
            "status": 500,
            "error": "Failed to fetch name from target server",
            "details": str(e)
        }
