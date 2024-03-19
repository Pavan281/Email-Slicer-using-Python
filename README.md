# Email-Slicer-using-Python
This code will separate the username and the domain used in the given or provided Mail ID. This is the beginners project. 

# Code :- 
def main():
	print(" Welcome to the Email Slicer ")
	print("")
	
	email_input = input(" Input your Email Address : ")
	
	(username, domain) = email_input.split("0")
	(domain, extension) = domain.split(".")

	print("Username : ", username)
	print("Domain : ", domain)
	print("Extension : ", extension)

while True:
	main()
