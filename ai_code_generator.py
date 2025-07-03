import os
import requests

# ১. ইউজারের রিকোয়েস্ট পড়ুন
with open("user_request.txt", "r") as f:
    user_request = f.read()

# ২. DeepSeek API কল করুন
API_KEY = os.getenv("API_KEY")
API_URL = "https://api.deepseek.com/v1/chat/completions"
headers = {"Authorization": f"Bearer {API_KEY}"}
data = {
    "model": "deepseek-coder",
    "messages": [{"role": "user", "content": user_request}],
    "temperature": 0.7
}

try:
    response = requests.post(API_URL, headers=headers, json=data)
    response.raise_for_status()  # এরর চেক করুন
    generated_code = response.json()["choices"][0]["message"]["content"]
except Exception as e:
    generated_code = f"# Error: {str(e)}\n# API Response: {response.text if 'response' in locals() else 'None'}"

# ৩. কোড ফাইলে সেভ করুন
with open("generated_code.py", "w") as f:
    f.write(generated_code)
