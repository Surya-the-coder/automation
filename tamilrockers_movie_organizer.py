import os
import re

root = "/Users/surya/Movies"#input("Enter the path to be organized : ")
os.chdir(root)
myfiles=os.listdir(root)
print("FILES : ")
for file in os.listdir(root):
	if os.path.isfile(file) and not file.startswith("."):
	 	print(file)
conf = input("All files listed \nDo you want to separate the abouve files (y/n) : ")
if conf == "y" or conf == "Y" or conf == "yes" or conf == "YES":
	pass
else:
	print("Aborted")
	exit()

ext = []
for file in myfiles:
	if not os.path.isdir(file) and not file.startswith("."):
		
		ex = file.split(".")
		ext = ex[-1]

		file1 = file.replace(" ","_")
		temp = file1
		try:
			matchObj = re.match(r'(www.)(TamilRockers)(.[a-z][a-z])(_-_)',temp,re.M|re.I)
			prefix = matchObj.group()
			temp = temp.replace(prefix,"")
			matchObj = re.search(r'([)])(.*)',temp,re.M|re.I)
			suffix = matchObj.group()
			temp = temp.replace(suffix,")")
			temp = temp.strip()
			#print("temp : "+temp)
		except:
			pass

		dst_fold = root+os.sep+temp

		if os.path.exists(dst_fold):
			pass
		else:
			os.mkdir(dst_fold)
	
		newfile = temp+"."+ext
		src = root+os.sep+newfile
		dst = dst_fold+os.sep+newfile

		#print("\n\n\n")
		#print(file+"\n"+newfile+"\n"+src+"\n"+dst)
		os.rename(file,newfile)
		os.replace(src,dst)



