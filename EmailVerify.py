import re,email,is_disposable_email,socket,whois,builtwith

from email_validator import validate_email, EmailNotValidError

def domainIP(email):
    domain = email.split("@")[1]
    try:
        ip_address = socket.gethostbyname(domain)
        print(f"IP address for domain {domain}: {ip_address}")
    except socket.gaierror:
        print(f"Domain name {domain} not found")

def domainAddress(res):
    res = res.split('@')[1]
    print(res)

def checkemail(s):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    if re.match(pattern,s):
        print("Valid Email")
    else:
        print("Invalid Email")

def disposableEmail(email):
    result = is_disposable_email.check(email)
    if(result==True):
        print("Disposable Email")
    else:
        print("Non Disposable Email")

def emailValidate(email):
    try:
        emailinfo = validate_email(email, check_deliverability=True)
        email = emailinfo.normalized
        print("Deliverable Email")
    except EmailNotValidError as e:
        print("Not Deliverable Email")
        print(str(e))

def domaininfo(email):
    domain = email.split('@')[1]

    url = 'https://' + domain


    technologies = builtwith.builtwith(url)
    print('Technologies used in this domain:')
    for key, value in technologies:
        print(key, ':', value)


email=input("Enter the email:")

checkemail(email)

domainAddress(email)

disposableEmail(email)

emailValidate(email)

domainIP(email)