from fastapi import FastAPI, Query
import requests

app = FastAPI()

# তোমার ভ্যালিড API Key গুলোর লিস্ট (তুমি চাইলে এখানে ক্লায়েন্টদের নাম বা প্যাকেজ অনুযায়ী Key বসাতে পারো)
VALID_API_KEYS = {
    "NEXA_KEY_2026": "Team Nexa Admin",
    "SKETVIA_PREMIUM": "Developer Sketvia Client",
    "NANO_TEST_KEY": "Team Nano Trial"
}

@app.get("/")
def read_root():
    return {"message": "API is Running Secured!"}

# URL এর শেষে ?key=API_KEY দিতে হবে
@app.get("/check-uid/{uid}")
def check_uid(uid: str, key: str = Query(None)):
    
    # API Key চেক করার লজিক
    if not key or key not in VALID_API_KEYS:
        return {
            "error": True,
            "message": "Invalid or missing API Key. Access Denied."
        }
        
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
        
        if data.get("error") is False and "data" in data and "username" in data["data"]:
            username = data["data"]["username"]
        else:
            username = "Not Found"

        return {
            "uid": uid,
            "username": username,
            "authorized_by": VALID_API_KEYS[key] # কোন ক্লায়েন্ট/প্যাকেজ ব্যবহার করছে সেটা দেখাবে
        }
        
    except Exception:
        return {
            "uid": uid,
            "username": "Error"
        }
