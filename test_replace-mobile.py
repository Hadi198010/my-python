import re

def test_mobile_replace():
    text = "My number is 09121234567 and my office number is 09351234567."
    pattern = r"09\d{9}"
    replaced = re.sub(pattern, "09xxxxxxxxx", text)
    assert replaced == "My number is 09xxxxxxxxx and my office number is 09xxxxxxxxx"

