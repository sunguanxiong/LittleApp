import shutil
import os

pic_path = '/home/sgx/groundtrue'

for folder in os.listdir(pic_path):
	pic_in_this = os.listdir(os.path.join(pic_path, folder))
	for f_p in pic_in_this:
		if os.path.isdir(os.path.join(pic_path, folder, f_p)):
			#shutil.copytree(os.path.join(pic_path, folder, f_p), os.path.join(pic_path, f_p))
			shutil.rmtree(os.path.join(pic_path, folder, f_p), True)
			print os.path.join(pic_path, folder, f_p) + 'removed!!!'
			
