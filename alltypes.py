import os

audio_formats = [".aa",".aac",".aax",".act",".aiff",".amr",".ape",".au",".awb",".dct",".dss",".dvf",".flac",".gsm",".iklax",".ivs",".m4a",".m4b",".m4p",".mmf",".mp3",".mpc",".msv",".nmf",".nsf",".ogg",".oga",".mogg",".opus",".ra",".rm",".raw",".sln",".tta",".voc",".vox",".wav",".wma",".wv",".webm",".8svx"]

root = input("Enter the path to be organized : ")
os.chdir(root)
myfiles=os.listdir(root)

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
		temp = file.split(".")
		ext = temp[-1]
		dst_fold = root+os.sep+ext

		if os.path.exists(dst_fold):
			pass
		else:
			os.system("mkdir %s"%dst_fold)
	
		dst = root+os.sep+ext+os.sep+file
		file = root+os.sep+file
		os.replace(file,dst)