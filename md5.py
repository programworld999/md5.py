import hashlib 
import sys


def encode(inp):
	result = hashlib.md5(inp.encode())
	return result.hexdigest()

if __name__ == "__main__":
	opr=sys.argv[1]
	if(opr == "e"):
		str2hash = input("Input: ");
		print("Encoded: "+str(encode(str2hash)))
	elif(opr == "d"):
		print("decode: ")
	else:
		print("Invalid Argument '"+str(opr)+"'")


