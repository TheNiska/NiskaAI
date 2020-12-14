import rus_words

def findObj(b):
	obj = -1
	file = open('rus_words.py', 'r')
	for line in file:
		i_pos = -1
		i_pos = line.find('class')
		if i_pos != -1:
			ii_pos = line.find('(', i_pos)
			obj_str = 'rus_words.' + line[i_pos+5:ii_pos]
			temp_obj = eval(obj_str)

			if temp_obj.word_type == 'noun':
				if rus_words.find_Wrd_inArr(b,temp_obj.sklon_ed):
					return temp_obj
				if rus_words.find_Wrd_inArr(b,temp_obj.sklon_mn):
					return temp_obj

			elif temp_obj.word_type == 'numeral':
				if rus_words.find_Wrd_inArr(b,temp_obj.sklon_kolich):
					return temp_obj
	file.close()
	return obj


text = input()
text = text.lower()
text_array = list(text.split())
for i in range(len(text_array)):
	if text_array[i] == 'это':
		set_obj = findObj(text_array[i+1])
		elem_obj = findObj(text_array[i-1])
		if (set_obj != -1) and (elem_obj != -1):
			print(set_obj.isIt(elem_obj.)
		else:
			print('Обнаружены неизвестные слова, ответ невозможен')
