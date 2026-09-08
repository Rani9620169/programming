#15. take an email address and print username,domain,and eversed domain
email = input("Enter an email address: ")

username, domain = email.split('@')

reversed_domain = domain[: :-1]

print("Username:", username)
print("Domain:", domain)
print("Reversed Domain:", reversed)