def find_Wrd_inArr(word, arr):
    ans = False
    for i in range(len(arr)):
        if arr[i] == word:
            ans = True
            return ans
    return ans

def isStrNum(s):
    s = s.replace(',','.')
    try:
        x = int(s)
        return True
    except ValueError:
        try:
            x = float(s)
            return True
        except ValueError:
            pass
    return False

textNum = {'один':1, 'два':2, 'три':3, 'четыре':4, 'пять':5, 'шесть':6, 'семь':7, 'восемь':8, 'девять':9,
           'десять':10, 'одиннадцать':11, 'двенадцать':12, 'тринадцать':13, 'четырнадцать':14, 'пятнадцать':15, 
           'шестнадцать':16, 'семнадцать':17, 'восемнадцать':18, 'девятнадцать':19, 'двадцать':20, 'тридцать':30,
           'сорок':40, 'пятьдесят':50, 'шестьдесят':60, 'семьдесят':70, 'восемьдесят':80, 'девяносто':90,
            'сто':100, 'двести':200, 'триста':300, 'четыреста':400, 'пятьсот':3, 'шестьсот':600, 'семьсот':700, 
            'восемьсот':800, 'девятьсот':900, 'тысяча':1000}

class Slovo():
    word = None
    word_type = None
    isObject = False
    isSet = False
    isDefinedSet = False
    def isIt():
        pass


class Число(Slovo):
    word = 'число'
    word_type = 'noun' # какая это часть речи
    isSet = True
    def isIt(x):
        pass

    root = 'числ' # корень слова
    sklon_ed = ['число', 'числа', 'числу', 'число', 'числом', 'числе']
    sklon_mn = ['числа', 'чисел', 'числам', 'числа', 'числами', 'числах']

    def isIt(s):
        s = list(s.split())
        if len(s) == 1:
            if isStrNum(s[0]):
                return (True, float(s))
            else:
                x = textNum.get(s[0])
                if x != None: return (True, x)
                else: return (False, 0)
        else:
            sum = 0
            for i in range(len(s)):
                sum += Число.isIt(s[i])[1]
            return (True,sum)

    def comparison(wordClass, wordText):
        if (wordClass.word_type == 'numeral') and (find_Wrd_inArr(wordText, wordClass.sklon_kolich)):
            return ('Да')
        else:
            return ('Нет')

class Два(Slovo):
    word = 'два'
    word_type = 'numeral'
    number = 2
    root = 'дв'
    sklon_kolich = ['два', 'двух', 'двум', 'два', 'двумя', 'двух']

class Цифра(Slovo):
    word = 'цифра'
    word_type = 'noun'
    isSet = True
    isDefinedSet = True
    setW = {i for i in range(10)}
    sklon_kolich = ['два', 'двух', 'двум', 'два', 'двумя', 'двух']

s = input()
print(Число.isIt(s))