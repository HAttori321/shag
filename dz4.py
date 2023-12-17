# number=int(input("Enter number week(1-7):"))
# if number==1:
#     print("Monday")
# if number==2:
#     print("Tuesday")
# if number==3:
#     print("Wednesday")
# if number==4:
#     print("Thursday")
# if number==5:
#     print("Friday")
# if number==6:
#     print("Saturday")
# if number==7:
#     print("Sunday")
# else:
#     print("Please write number 1 to 7")


#2
# number=int(input("Введіть номер місяця (1-12): "))
# if number==1:
#     print("січень")
# elif number==2:
#     print("лютий")
# elif number==3:
#     print("березень")
# elif number==4:
#     print("квітень")
# elif number==5:
#     print("травень")
# elif number==6:
#     print("червень")
# elif number==7:
#     print("липень")
# elif number==8:
#     print("серпень")
# elif number==9:
#     print("вересень")
# elif number==10:
#     print("жовтень")
# elif number==11:
#     print("листопад")
# elif number==12:
#     print("грудень")
# else:
#     print("Введіть число від 1 до 12.")


# 3
# number=int(input("Enter number: "))
# if number>0:
#     print("Number is positive")
# elif number<0:
#     print("Number is negative")
# else:
#     print("Number is equal to zero")


number1=int(input("Введіть перше число: "))
number2=int(input("Введіть друге число: "))
if number1==number2:
    print("Числа рівні")
else:
    print("Числа не рівні. Їх порядок зростання:")
    if number1<number2:
        print(number1, number2)
    else:
        print(number2, number1)
