
def read_file(filename):
	lines = []
	#utf-8-sig會把原記事本最前面的\ufeff編碼去掉
	with open(filename, 'r', encoding='utf-8-sig') as f:  
		for line in f:
			lines.append(line.strip()) #去掉\n
	return lines

def convert(lines):
	danny_word_count = 0
	danny_sticker_count = 0
	danny_image_count = 0
	garbo_word_count = 0
	garbo_sticker_count = 0
	garbo_image_count = 0
	for line in lines:
		s = line.split(' ') #用空白鍵分割
		time = s[0]
		name = s[1]
		if name == 'Danny':
			if s[2] == '貼圖':
				danny_sticker_count += 1
			elif s[2] == '圖片':
				danny_image_count += 1
			else: 
				for m in s[2:]:
					danny_word_count += len(m)
		elif name == 'Garbo':
			if s[2] == '貼圖':
				garbo_sticker_count += 1
			elif s[2] == '圖片':
				garbo_image_count += 1
			else: 
				for m in s[2:]: 
					garbo_word_count += len(m)

	print('Danny說了', danny_word_count, '個字')
	print( '傳了', danny_sticker_count, '個貼圖', '和', danny_image_count, '張圖片')
	print('Garbo說了', garbo_word_count, '個字')
	print( '傳了', garbo_sticker_count, '個貼圖', '和', danny_image_count, '張圖片')


def write_file(filename, lines):
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n')

def main():
	lines = read_file('line_input.txt')
	lines = convert(lines)
	#write_file('output.txt', lines)

main()

