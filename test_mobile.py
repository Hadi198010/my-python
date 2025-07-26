import re

def mask_mobile_numbers(text):
    return re.sub(r"09\d{9}", "09xxxxxxxxx", text)

def test_single_mobile():
    assert mask_mobile_numbers("My number is 09123456789") == "My number is 09xxxxxxxxx"

def test_multiple_mobiles():
    assert mask_mobile_numbers("Call 09123456789 or 09351234567") == "Call 09xxxxxxxxx or 09xxxxxxxxx"

def test_no_mobile():
    assert mask_mobile_numbers("No phone here") == "No phone here"

