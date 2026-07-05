from fastapi import FastAPI, HTTPException
import requests

app = FastAPI()

# API ঠিকমতো লাইভ হয়েছে কিনা তা চেক করার জন্য
@app.get("/")
def read_root():
    return {
        "status": "success", 
        "message": "UID to Name API is Live on Vercel!"
    }

# মেইন UID চেকার এন্ডপয়েন্ট
@app.get("/check-uid/{uid}")
def check_uid(uid: str):
    # UID ভ্যালিডেশন (উদাহরণস্বরূপ: UID ৫ ক্যারেক্টারের কম হলে এরর দিবে)
    if len(uid) < 5:
        raise HTTPException(status_code=400, detail="Invalid UID format")
    
    try:
        # ---------------------------------------------------------
        # এখানে তোমার আসল API বা স্ক্র্যাপিং লজিক বসবে। 
        # উদাহরণ:
        # api_url = f"https://your-secret-provider.com/api?uid={uid}"
        # response = requests.get(api_url)
        # data = response.json()
        # ---------------------------------------------------------
        
        # আপাতত ডেমো রেসপন্স রিটার্ন করছি যেন তুমি লাইভ টেস্ট করতে পারো।
        # শেষের ৩টা ডিজিট নামের সাথে যুক্ত করে দিচ্ছি ডাইনামিক ফিল আনার জন্য।
        demo_name = "GamerBD_" + uid[-3:] 
        
        return {
            "status": 200,
            "uid": uid,
            "account_name": demo_name,
            "message": "Name fetched successfully"
        }
        
    except Exception as e:
        return {
            "status": 500,
            "error": "Failed to fetch name",
            "details": str(e)
        }