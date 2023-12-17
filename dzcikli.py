#1
# start=int(input("Початкове число діапазону: "))
# end=int(input("Кінцеве число діапазону: "))
# print(f"Числа в діапазоні від {start} до {end}, які кратні 7:")
# for i in range(start,end+1):
#     if i%7==0:
#         print(i)


#2
# start=int(input("Початкове число діапазону: "))
# end=int(input("Кінцеве число діапазону: "))
# print(f"\nВсі числа в діапазоні від {start} до {end}:")
# for i in range(start,end+1):
#     print(i,end="")
# print(f"\n Всі числа від {start} до {end} в спадному порядку:")
# for i in range(end,start,-1):
#     print(i,end="")

# print(f" \n Числа від {start} до {end}, які кратні 7:")
# for i in range(start,end+1):
#     if i%7==0:
#         print(i,end="")

# count=sum(1 for i in range(start,end+1) if i%5==0)
# print(f"\n Кількість чисел, які кратні 5: {count}")
#3


start=int(input("Початкове число діапазону: "))
end=int(input("Кінцеве число діапазону: "))
print(f"Результат для чисел в діапазоні від {start} до {end}:")
for i in range(start,end+1):
    if i%3==0:
        print("Fizz")
    if i%5==0:
        print("Buzz")
    elif i%3==0 and i%5==0:
        print("Fizz Buzz")
    else:
        print(i)