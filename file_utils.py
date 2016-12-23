import os

def get_all_files(path):
  #return all files' name in certain folder.
	result = []
	for name in os.listdir(path):
		if os.path.isfile(os.path.join(path, name)):
			result.append(name)
	return result
