import os
import requests

# ইউজারের রিকোয়েস্ট পড়ুন
with open("user_request.txt", "r") as f:
    user_request = f.read()

# DeepSeek API কল করুন (উদাহরণ)
API_KEY = os.getenv("API_KEY")  # GitHub Secrets থেকে লোড হবে
headers = {"Authorization": f"Bearer {API_KEY}"}
data = {
    "model": "deepseek-coder",
    "messages": [{"role": "user", "content": user_request}]
}

response = requests.post("https://api.deepseek.com/v1/chat/completions", headers=headers, json=data)
generated_code = response.json()["choices"][0]["message"]["content"]

# কোড ফাইলে সেভ করুন
with open("generated_code.py", "w") as f:
    f.write(generated_code)
