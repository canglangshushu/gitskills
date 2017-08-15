import zipfile ,os
print(os.getcwd())#获取当前目录
os.chdir(r"E:\pyzip")#更改当前路径
#print(os.getcwd())
#E:\pyzip
zipFile = zipfile.ZipFile(os.path.join(os.getcwd(),'wrs2_asc_desc.zip'))
for file in zipFile.namelist():
    zipFile.extract(file,r'E:\pyzip')
	print（file+"解压完成"）
zipFile.close()