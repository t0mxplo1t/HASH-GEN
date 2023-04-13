import argon2

from time import sleep
from argon2 import PasswordHasher

def banner():
	print("""\033[32m
██╗  ██╗ █████╗ ███████╗██╗  ██╗     ██████╗ ███████╗███╗   ██╗
██║  ██║██╔══██╗██╔════╝██║  ██║    ██╔════╝ ██╔════╝████╗  ██║
███████║███████║███████╗███████║    ██║  ███╗█████╗  ██╔██╗ ██║
██╔══██║██╔══██║╚════██║██╔══██║    ██║   ██║██╔══╝  ██║╚██╗██║
██║  ██║██║  ██║███████║██║  ██║    ╚██████╔╝███████╗██║ ╚████║
╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝     ╚═════╝ ╚══════╝╚═╝  ╚═══╝\033[0m
\033[30;42mHash Generator | Written using Python\033[0m\n""")
banner()

x = PasswordHasher()
plain_text = input("\033[1;32mEnter text : \033[0m")
result = x.hash(plain_text)
print("\033[1;32mHash :\033[0m",result)

try:
	print("\n\033[1;32mThe Hash is valid?\033[0m")
	sleep(1)
	x.verify(result,plain_text)
	print("\033[30;42mValid\033[0m")

except:
	sleep(1)
	print("\033[30;mInvalid\033[0m")
