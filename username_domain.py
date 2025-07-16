a=input('Enter an email please:') # Get email input from user
if '@' not in a: # Check if '@' is not present in the email
    print('Enter an email completely please. It should be involved domain part.') #Display error message if email is incomplete
    exit() # Exit the program if email is invalid
(username,domain)=a.split('@') #Split email into username and domain using '@' as separator
print('Username=',username) # print the username
print('Domain=',domain) # print the domain