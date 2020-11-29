import urllib.request
import urllib

def clear_web_page(s):
	fl = False
	ind1 = 1
	ind2 = 1
	while (ind1 >= 0) and (ind2 >= 0):
		ind1 = s.find('<')
		ind2 = s.find('>')
		if ind1 > 0:
			s = s[0:ind1] + s[ind2+1:]
		elif ind1 == 0:
			s = s[ind2+1:]
	return s



strin = input()
url_name = 'http://sklonenie-slova.ru/' + strin


link = urllib.request.urlopen(url_name)
a_ed = []
a_mn = []

for line in link.readlines():
	s = str(line.decode('utf-8'))
	index1 = s.find('<th>Слово</th>')
	if  index1 > 0:
		index2 = s.find('</tr></tbody>', index1)
		subs = s[index1 : index2]
		subs = subs.strip()
		subs = subs.replace(' ', '')
		a = list(subs.split('<td>'))
		for i in range(3, len(a), 3):
			ind = a[i].find('<')
			a_ed.append(a[i][:ind])

	index1 = s.find('<h3 class="panel-title">Множественное число</h3>')
	if  index1 > 0:
		index2 = s.find('</tr></tbody>', index1)
		subs = s[index1 : index2]
		subs = subs.strip()
		subs = subs.replace(' ', '')
		a = list(subs.split('<td>'))
		for i in range(3, len(a), 3):
			ind = a[i].find('<')
			a_mn.append(a[i][:ind])
link.close()
ls = a_ed[0]
asd = ls
asd.encode('utf8')
asd = urllib.parse.quote(asd)

strin2 = 'http://gramota.ru/slovari/dic/?word=' + asd + '&all=x'
link2 = urllib.request.urlopen(strin2)
isFound = False
newstr = ''
for line in link2.readlines():
	s = str(line.decode('windows-1251'))
	if not isFound:
		ind = s.find('<h2><a href="http://www.gramota.ru/slovari/info/bts/">Большой толковый словарь</a></h2>')
		if ind > 0:
			isFound = True
	else:
		ind = s.find('<div style="padding-left:50px">')
		if ind > 0: text_mean = s[37:]
		break
print(clear_web_page(text_mean))

