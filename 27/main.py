import student
a = input("fayl nomi kiriting")
b = []

try:
    with open(a,  'r') as file:
        for line in file:
            ism, ball = line.strip().split(',')
            student.student(ism, ball, b)

except FileNotFoundError:
    print("fayl mavjud emas")            
except ValueError as e:
    print(e) 