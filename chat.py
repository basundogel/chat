
def read_file(filename):
	chat = []
	with open(filename, 'r', encoding = 'utf-8-sig') as f: # 讀取中文時,使用utf-8
		for line in f:
			chat.append(line.strip())
	return chat

def convert(chat):
	new = []
	person = None  # None
	for line in chat:
		if line == 'Allen':
			person = 'Allen'
			continue
		elif line == 'Tom':
			person = 'Tom'
			continue
		if person:  # 如果person有值的話
			new.append(person + ': ' + line)
	return new

def write_file(filename, chat):
	with open(filename, 'w') as f:
		for line in chat:
			f.write(line + '\n')

				
		
def main():
	chat = read_file('input.txt')
	chat = convert(chat)
	write_file('blank.txt', chat)



	# print(chat)
	# print(new)	







if __name__ == '__main__':
	main()