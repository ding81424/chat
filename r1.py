
def read_file(filename):
	lines = []
	#utf-8-sig會把原記事本最前面的\ufeff編碼去掉
	with open(filename, 'r', encoding='utf-8-sig') as f:  
		for line in f:
			lines.append(line.strip()) #去掉\n
	return lines

def convert(lines):
	new = []
	person = None
	for line in lines:
		if line == 'Allen':
			person = 'Allen'
			continue
		elif line == 'Tom':
			person = 'Tom'
			continue
		if person:   #處理當第一行不是人名時
		    new.append(person + ': ' + line) 		
	return new

def write_file(filename, lines):
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n')


def main():
	lines = read_file('input.txt')
	lines = convert(lines)
	write_file('output.txt', lines)

main()

