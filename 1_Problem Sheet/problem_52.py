# Extract username from a given email. 
# Eg if the email is nitish24singh@gmail.com then the username should be nitish24singh
def extract_username(email):
    username = email.split('@')[0]
    return username

# Extract domain name from a given email.
# Eg if the email is nitish24singh@gmail.com then the domain name should be gmail
def extract_domain(email):
    domain = email.split('@')[1]
    return domain

# Take user input
email = input("Enter your email: ")

# Extract and print username and domain
print("Username:", extract_username(email))
print("Domain:", extract_domain(email))

