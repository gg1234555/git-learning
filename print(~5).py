# 1
print("Задание 1:")
print("A", "B", "C")
print('a b xor')
for a in range(0,2):
    for b in range(0,2):
        if a == b or b == a:
            xor = 0
        else:
            xor = 1
        print(a, b, xor)
print()

# 2
print("Задание 2:")
print("A", "B")
print("C")
f = 'zxcfckulrlly'
print(f[:3])
print(f[-4:])
print(f[7:10])
print(f[1::2])
print(f[::-1][4:7])
print(f[7:9]+f[6]+f[2]+f[4])
print()

# 3
print("Задание 3:")
print("A", "B")
print("C")
s = input()
result = ' '.join(s.split())
print(result)
print()

# 4
print("Задание 4:")
print("A", "B")
print("C")
def T_pas(password):
    if " " in password:
        return False
    if len(password) <8 or len(password) > 20:
        return False
    if sum(1 for i in password if i in "!@#$%^&*()-=_=") < 2:
        return False
    if sum(1 for i in password if i in "ZXCVBNMASDFGHJKLQWERTYUIOP") < 3:
        return False
    return True
password = input("Введите пароль: ")
result = T_pas(password)
if result == True:
    print("Пароль надежный.")
elif result == False:
    print("Пароль ненадежный.")

print()

# 5
print("Задание 5:")
print("A")
def custom_append(element, append_to=None):
    if append_to is None:
        append_to = []
    append_to.append(element)
    return append_to


print(custom_append(1, [1, 2]))     
print(custom_append(1))             
print(custom_append(1, [1, 2, 0]))  
print(custom_append(2))             
print("C"  "A")
print('Создано: 3. Осталось: 2 , т. к. a потерял ссылку на список при del a и при deд c[0], при del b толко переменная b потеряла ссылку на список но в с осталась ссылка на этот список.')
class MyInt(int):
    def __new__(cls, number: str | float | int = 0):
        if isinstance(number, str):
            number = float(number)
        return super().__new__(cls, int(number))


random_numbers: list[str] = ["9.11", "6.66", "3.1415926", "2.718281828459045"]
list_float = [float(x) for x in random_numbers]
print("list[float]:", list_float)
list_int = [int(float(x)) for x in random_numbers]  
print("list[int]:", list_int)
list_myint = [MyInt(x) for x in random_numbers]
print("list[MyInt]:", list_myint)
list_of_lists = [[float(x), float(x) * 2] for x in random_numbers]
print("list[list[float, float]]:", list_of_lists)
print()
