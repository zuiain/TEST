#python one.py
print("hello")

def func():
	print("func() in one.py")

print("Top level in one.py")

if __name__ == "__main__":
	#RUN THE SCRIPTS
	print("one.py is being run directly !")
else:
	print("one.py has been imported !")