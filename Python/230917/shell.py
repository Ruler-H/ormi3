import os

while True:
	userInput = input('>')
	if userInput == 'pwd':
		print('현재 위치 출력')
		# print('/'.join(__file__.split('\\')[:-1]))
		print(os.getcwd())
	elif userInput == 'dir' or userInput == 'ls':
		print('현재 폴더에 폴더와 파일명 출력')
		print(os.listdir(os.getcwd()))
	elif userInput == 'exit':
		print('안녕히가세요.')
		break