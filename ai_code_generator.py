import os
import requests
import time

# ইউজার রিকোয়েস্ট পড়ুন
with open("user_request.txt", "r") as f:
    user_request = f.read()

# DeepSeek API কনফিগারেশন
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
    # API কল
    response = requests.post(API_URL, headers=headers, json=data)
    
    # ডিবাগিং ইনফো
    print(f"Status Code: {response.status_code}")
    print(f"Response Text: {response.text}")
    
    if response.status_code == 200:
        response_data = response.json()
        if "choices" in response_data:
            generated_code = response_data["choices"][0]["message"]["content"]
        else:
            generated_code = f"# Error: Unexpected API response format\n{response.text}"
    else:
        generated_code = f"# Error: API request failed with status {response.status_code}\n{response.text}"

except Exception as e:
    generated_code = f"# Error: {str(e)}"

# কোড সেভ করুন
with open("generated_code.py", "w") as f:
    f.write(generated_code)

# বিলম্ব যোগ করুন (রেট লিমিট এড়াতে)
time.sleep(5)
