import os
# print(os.getcwd())
# print(os.listdir())

basedir = os.getcwd()
subdir_list = []
for item in os.listdir(basedir):
	fullpath = os.path.join(basedir,item)
	#rint(fullpath)
	if os.path.isdir(fullpath):
		subdir_list.append(fullpath)
		#print(subdir_list)
	else:
		#print																																																																																																																																																										(fullpath)

print(subdir_list)



# import os

# def file_list(dir):
#     basedir = dir
#     subdir_list = []
#     for item in os.listdir(dir):
#         fullpath = os.path.join(basedir,item)
#         if os.path.isdir(fullpath):
#             subdir_list.append(fullpath)
#         else:
#             print (fullpath)

#     for d in subdir_list:
#         file_list(d)

# file_list(os.getcwd())
