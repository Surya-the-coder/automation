import os
paths = []
root = input("Enter the path containing files to be separated: ")
paths = os.listdir(root)

for p in paths:print(p)

conf = input("All files listed \nDo you want to separate the above files (y/n) : ")

if conf == "y" or conf == "Y" or conf == "yes" or conf == "YES":
	pass
else:
	print("Aborted")
	exit()

if os.path.exists("./Images"):
	pass
else:
	os.mkdir("Images")

if os.path.exists("./Videos"):
	pass
else:
	os.mkdir("Videos")


print("Separating Images and Videos...")

for p in paths:
	
	if ".jpg" in p:

		if os.path.exists("./Images/jpg"):
			pass
		else:
			os.system("mkdir Images/jpg")
		
		dst = "Images/jpg/%s"%p
		os.replace(p,dst)
	
	elif ".png" in p:
		if os.path.exists("./Images/png"):
			pass
		else:
			os.system("mkdir Images/png")

		dst = "Images/png/%s"%p
		os.replace(p,dst)
	
	elif ".mp4" in p:
		if os.path.exists("./Videos/mp4"):
			pass
		else:
			os.system("mkdir Videos/mp4")

		dst = "Videos/mp4/%s"%p
		os.replace(p,dst)

	elif ".3gp" in p:
		if os.path.exists("./Videos/3gp"):
			pass
		else:
			os.system("mkdir Videos/3gp")

		dst = "Videos/3gp/%s"%p
		os.replace(p,dst)

print("Separation Successfull")