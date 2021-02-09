#Get user email address
email = input("What is your email address: ").strip()

#Slice out user name

user = email[:email.index("@")]

#Slice out domain name
domain = email[email.index("@") + 1:]

#Format message
output = "Your user name is {0} and your damin is {1}".format(user, domain)
#Display formatted output
print(output)

