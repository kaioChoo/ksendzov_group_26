# STRING

string = 'Ilya'
print('1) STRING //', string)
print(type(string))

# INT

int = 2022
print('2) INT //', int)
print(type(int))

# FLOAT

a1 = 17.43
b1 = 13.90
c1 = a1 + b1
print('3) FLOAT //', c1)
print(type(a1))

# BYTES

bytes2 = b'''Pyataev,
Ilya,
Sergeevich'''
print('4) BYTES // ', bytes)
print(type(bytes2))

# LIST

listtest = 'KSENDZOV'
listtest = list(listtest)
print('5) LIST //', listtest)
print(type(listtest))

# TUPLE

a = (1, 2.2, 'hello', 'world')
print('6) TUPLE //', a)
print(type(a))

# SET

settest = set(['A', 'B', 'B', 'C'])
print('7) SET // ', set(settest))
print(type(settest))

# FROZENSET

frozensettest = frozenset({'Ilya', 'Ilya', 'Sergeevich', 'Pyataev'})
print('8) FROZENSET //', frozenset(frozensettest))
print(type(frozensettest))

# DICT

dicttest = {'Country': 'Russia', 'City': 'SPb', 'Age': 24}
print('9) DICT //', dicttest)
print(type(dicttest))

# STEP 10

print('10) В консоле после каждый переменной есть название переменной')

# STEP 11

a2 = 'сканте'
b2 = 'нировал'
print('11) Скантенировать две переменные стринг:',a2+b2)

# STEP 12

a3 = 'Мой день рождения'
b3 = 7
c3 = 'апреля'
print('12) Переменные int, str в одну строку:', a3, ',' , b3 , ',' , c3)
# STEP 13

a4 = 'Десять'
b4 = 15
c4 = '=25'
print('13) Переменные str, int в одну строку используя +:'+a4+'+'+str(b4)+c4)
