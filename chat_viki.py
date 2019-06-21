
def read_file(filename):
	chat = []
	with open(filename, 'r', encoding = 'utf-8-sig') as f: # 讀取中文時,使用utf-8
		for line in f:                                     # -sig:去除"\ufeff"  
			chat.append(line.strip())
	return chat

def count(chat):
	allen_word_count = 0
	viki_word_count = 0
	allen_sticker_count = 0
	viki_sticker_count = 0
	a_pic_count = 0
	v_pic_count = 0
	for line in chat:
		s = line.split(' ') # split的結果是清單
		time = s[0]
		name = s[1]
		if name == 'Allen':
			if s[2] == '貼圖':
				allen_sticker_count += 1
			elif s[2] == '圖片':
				a_pic_count += 1
			else:
				for m in s[2:]:
					allen_word_count += len(m)

		elif name == 'Viki':
			if s[2] == '貼圖':
				viki_sticker_count += 1
			elif s[2] == '圖片':
				v_pic_count += 1
			else:
				for m in s[2:]:
					viki_word_count += len(m)
	print('Allen說了', allen_word_count, '個字, used', allen_sticker_count, 'stickers', a_pic_count, 'pictures')
	print('Viki說了', viki_word_count, '個字, used', viki_sticker_count, 'stickers', v_pic_count, 'pictures')

def write_file(filename, chat):
	with open(filename, 'w') as f:
		for line in chat:
			f.write(line + '\n')

def main():
	chat = read_file('-LINE-Viki.txt')
	count(chat)
	# write_file('blank.txt', chat)
	

if __name__ == '__main__':
	main()





