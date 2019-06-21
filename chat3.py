
chat = []
with open('3.txt', 'r', encoding = 'utf-8-sig') as f:
	for line in f:
		chat.append(line.strip())

for line in chat:
	m = line.split(' ')
	time = m[0][:5]
	name = m[0][5:]
	print('time:', time, ', name:', name)


