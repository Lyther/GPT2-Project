import os
import sys
import json

dir_name = ""
file_name = ""

def main():
	files = [file for file in os.listdir(dir_name) if os.path.isfile(dir_name + '/' + file)]
	result = ""
	for file in files:
		with open(dir_name + '/' + file, 'rb') as reader:
			lines = reader.read().decode('utf-8', errors='ignore')
			lines = lines.replace('\n', '')
			result += lines
	with open('train.json', 'w', encoding='utf-8') as writer:
		json.dump((result,), writer)

if __name__ == "__main__":
	if len(sys.argv) == 2 and os.path.isdir(sys.argv[1]):
		dir_name = sys.argv[1]
		main()
	else:
		dir_name = input("Please input the directory name: ")
		main()