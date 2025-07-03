import os

# ইউজারের রিকোয়েস্ট পড়ুন
with open("user_request.txt", "r") as f:
    user_request = f.read()

# এখানে আমরা একটি সাধারণ উদাহরণ দিচ্ছি। পরে AI API যোগ করবো
generated_code = f"""
# AI দ্বারা জেনারেট করা কোড (উদাহরণ)
print("Hello, World!")
# ইউজার রিকোয়েস্ট: {user_request}
"""

# কোড ফাইলে সেভ করুন
with open("generated_code.py", "w") as f:
    f.write(generated_code)
