import os
import requests
import time

# ১. ইউজারের রিকোয়েস্ট পড়ুন
with open("user_request.txt", "r") as f:
    user_request = f.read()

# ২. DeepSeek API কনফিগারেশন
API_KEY = os.getenv("API_KEY")
API_URL = "https://api.deepseek.com/v1/chat/completions"
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}
data = {
    "model": "deepseek-chat",
    "messages": [{"role": "user", "content": user_request}],
    "temperature": 0.7
}

try:
    # ৩. API কল করুন
    response = requests.post(API_URL, headers=headers, json=data)
    print(f"API Status: {response.status_code}")
    print(f"API Response: {response.text}")  # ডিবাগিং
    
    if response.status_code == 200:
        response_data = response.json()
        generated_code = response_data["choices"][0]["message"]["content"]
    else:
        generated_code = f"# Error: API request failed\nStatus: {response.status_code}\nResponse: {response.text}"
        
except Exception as e:
    generated_code = f"# Error: {str(e)}"

# ৪. কোড ফাইলে সেভ করুন
with open("generated_code.py", "w") as f:
    f.write(generated_code)

# ৫. রেট লিমিট এড়াতে বিলম্ব করুন
time.sleep(5)
