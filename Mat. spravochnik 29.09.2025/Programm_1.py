import random;
def sl_b ():
    return random.randint(0,3);
operation=(12, 10, (sl_b),2, 1, (sl_b),4, 8, (sl_b))
l=len(operation)/3
def operation(a, b, vid):
    if vid==0:
        return (a+b)
    elif vid==1:
        return (a-b)
    elif vid==2:
        return (a*b)
    else:
        return (a/b)
def otvet(operation, l):
    l-=1

print()
#функция.append(Значение) - добавление в конец списка значения