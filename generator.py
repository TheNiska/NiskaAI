import math
import random
import rus_words

def getNumWord(num):
	wrd = rus_words.numText.get(num)
	if wrd == None:
		wr1 = (num // 10) * 10
		wr1 = rus_words.numText.get(wr1)
		wr2 = num % 10
		wr2 = rus_words.numText.get(wr2)
		wrd = str(wr1) + ' ' + str(wr2)
	return wrd




f = open('adding.txt', 'w')

for i in range(300):
	x = random.randrange(50)
	y = random.randrange(50)
	z = y + x
	x_txt = getNumWord(x)
	y_txt = getNumWord(y)
	z_txt = getNumWord(z)
	string = x_txt + ' плюс ' + y_txt + ' = ' + z_txt
	f.write(string +'\n')
f.close()
	