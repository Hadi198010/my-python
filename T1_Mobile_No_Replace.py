import re

# متن تستی ثابت برای اجرای CI/CD
text = "My number is 09121234567 and my office number is 09351234567."

# الگو برای شناسایی شماره موبایل‌های 11 رقمی با شروع 09
pattern = r"09\d{9}"

# جایگزینی شماره‌ها با مقدار ثابت
replaced = re.sub(pattern, "09xxxxxxxxx", text)

print("Modified text:", replaced)

