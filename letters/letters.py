import numpy as np
import math

letters_by_code = {
    '0 0 0 -1' : 'а',
    '0 0 0 0'  : 'б',
    '0 0 0 1'  : 'в',
    '0 0 -1 -1': 'г',
    '0 0 -1 0' : 'д',
    '0 0 -1 1' : 'е',
    '0 0 1 -1' : 'ё',
    '0 0 1 0'  : 'ж',
    '0 0 1 1' : 'з',
    '0 -1 -1 -1'  : 'и',
    '0 -1 -1 0'  : 'й',
    '0 -1 -1 1': 'к',
    '0 -1 0 -1' : 'л',
    '0 -1 0 0' : 'м',
    '0 -1 0 1' : 'н',
    '0 -1 1 -1'  : 'о',  
    '0 -1 1 0' : 'п',
    '0 -1 1 1' : 'р',
    '0 1 -1 -1' : 'с',
    '0 1 -1 0'  : 'т',
    '0 1 -1 1' : 'у',
    '0 1 0 -1'  : 'ф',
    '0 1 0 0'  : 'х',
    '0 1 0 1': 'ц',
    '0 1 1 -1' : 'ч',
    '0 1 1 0' : 'ш',
    '0 1 1 1' : 'щ',
    '-1 -1 -1 -1'  : 'ъ',
    '-1 -1 -1 0'  : 'ы',
    '-1 -1 -1 1'  : 'ь',
    '-1 -1 0 -1': 'э',
    '-1 -1 0 0' : 'ю',
    '-1 -1 0 1' : 'я'
}

num_by_letters = {value: key for key, value in letters_by_code.items()}



def random_init():
    np.random.seed(1)
    w1 = np.random.randn(32, 4)
    b1 = np.random.randn(32, 1)
    w2 = np.random.randn(4, 32)
    b2 = np.random.randn(4, 1)

    return w1, b1, w2, b2


def propagate(w1, b1, w2, b2, X, Y):
    m = X.shape[1]
    z1 = np.dot(w1, X) + b1
    a1 = np.tanh(z1)

    a2 = np.dot(w2, a1) + b2
    cost = (1/m) * np.sum(np.abs(a2 - Y))

    dz2 = a2 - Y
    dw2 = (1/m) * np.dot(dz2, a1.T)
    db2 = (1/m) * np.sum(dz2)

    dz1 = np.dot(w2.T, dz2)
    dw1 = (1/m) * np.dot(dz1, X.T)
    db1 = (1/m) * np.sum(dz1)

    return cost, dw1, db1, dw2, db2


def optimize(w1, b1, w2, b2, X, Y, num_iterations, learning_rate):
    for i in range(num_iterations):
        cost, dw1, db1, dw2, db2  = propagate(w1, b1, w2, b2, X, Y)
        w1 = w1 - learning_rate  * dw1
        b1 = b1 - learning_rate * db1
        w2 = w2 - learning_rate * dw2
        b2 = b2 - learning_rate * db2
        print(cost)
    return w1, b1, w2, b2

def predict(w1, b1, w2, b2, X):
    m = X.shape[1]

    z1 = np.dot(w1, X) + b1
    a1 = np.tanh(z1)

    a2 = np.dot(w2, a1) + b2
    
    return a2

def model_letters(ch, train_again=False):
    if train_again:
        w1, b1, w2, b2 = random_init()
        w1, b1, w2, b2 = optimize(w1, b1, w2, b2, x, y, 400000, 0.04)
        np.savetxt('C:\\Users\\Dente\\PycharmProjects\\NiskaAI\\letters\\letter_recognizer_w1.txt', w1)
        np.savetxt('C:\\Users\\Dente\\PycharmProjects\\NiskaAI\\letters\\letter_recognizer_b1.txt', b1)
        np.savetxt('C:\\Users\\Dente\\PycharmProjects\\NiskaAI\\letters\\letter_recognizer_w2.txt', w2)
        np.savetxt('C:\\Users\\Dente\\PycharmProjects\\NiskaAI\\letters\\letter_recognizer_b2.txt', b2)
    else:
        w1 = np.loadtxt('C:\\Users\\Dente\\PycharmProjects\\NiskaAI\\letters\\letter_recognizer_w1.txt')

        b1 = np.loadtxt('C:\\Users\\Dente\\PycharmProjects\\NiskaAI\\letters\\letter_recognizer_b1.txt')
        b1 = b1.reshape(b1.shape[0], 1)

        w2 = np.loadtxt('C:\\Users\\Dente\\PycharmProjects\\NiskaAI\\letters\\letter_recognizer_w2.txt')

        b2 = np.loadtxt('C:\\Users\\Dente\\PycharmProjects\\NiskaAI\\letters\\letter_recognizer_b2.txt')
        b2 = b2.reshape(b2.shape[0], 1)

    ch = ch.lower()
    code = num_by_letters[ch]
    lst = list(map(int, code.split()))
    ch_code = np.array(lst).reshape(4,1)

    output = predict(w1, b1, w2, b2, ch_code)

    return output

if __name__ == '__main__':

    i = 0
    for key in num_by_letters:
        lst = list(map(int, num_by_letters[key].split()))
        if i == 0:
            x = np.array(lst).reshape(4,1)
        else:
            tmp = np.array(lst).reshape(4,1)
            x = np.column_stack((x,tmp))
        i += 1
    y = x

    train_again = False
    print('Тренировать модель снова: ')
    t = input().lower()
    if (t == 'y') or (t == 'да') or (t == 'yes'):
        train_again = True


    while  True:
        print("Введите букву: ")
        b = input()

        ans = model_letters(b, train_again)
        print(ans)
        answer = np.squeeze(ans).T # скармливаем этот код нашей сети
        code = np.around(answer)
        code = code.astype(int)
        print(code)
        str_answer = str(code).strip('[')
        str_answer = str_answer.strip(']').strip().replace('  ', ' ') # получаем ответ как строку из буквы
        try:
            print(letters_by_code[str_answer])
        except KeyError:
            print('Незнаю что за буква')
        train_again = False