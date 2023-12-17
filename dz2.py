1
num1=int(input("Введіть першу цифру: "))
num2=int(input("Введіть другу цифру: "))
num3=int(input("Введіть третю цифру: "))


result=num1*100+num2*10+num3
print("Відповідь", result)
2
number=int(input("Введіть чотиризначне число: "))
num1=number//1000 
num2=(number//100)%10 
num3=(number//10) % 10
num4=number%10
result=num1*num2*num3*num4
print(result)
3
meters=int(input("Введіть кількість метрів: "))
centimeters=meters*100
decimeters=meters*10
millimeters=meters*1000
miles=meters/1609.34
print(centimeters)
print(decimeters)
print(millimeters)
print(miles)
4
osnova=int(input("Введіть розмір основи : "))
visota=int(input("Введіть розмір висоти : "))
ploscha=0.5*osnova*visota
print("Площа трикутника:",ploscha)
5
number=(input("Введіть число: "))
print(number[::-1])