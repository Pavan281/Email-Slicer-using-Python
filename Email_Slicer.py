# Code for the Email Slicer:- 

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
