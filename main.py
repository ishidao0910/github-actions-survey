import datetime

if __name__ == '__main__':
	dt_now = datetime.datetime.now()
	add_txt = '<br>' + str(dt_now)
	print(dt_now)

	file_path = "README.md" 
	with open(file_path, "r") as file:
		txt = file.read()
		txt = txt + add_txt

	with open(file_path, 'w') as file:
		file.write(txt)
