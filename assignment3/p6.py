import re

def ectract_email(text):
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,3}\b'

    emails = re.findall(email_pattern, text)

    return emails

text = "lakmajepavan@gmail.com asjn adcdb adfb lakmajepavan2003@gmail.com"
result = ectract_email(text)
if result:
    for email in result:
        print(email)
else:
    print("no email address found")
