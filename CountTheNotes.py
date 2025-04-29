m = int(input("Enter the ammount: "))

note1000 = m // 1000
print("1000 TAKA note: ", note1000)
m %= 1000
note500 = m // 500
print("500 TAKA note: ", note500)
m %= 500
note200 = m // 200
print("200 TAKA note: ", note200)
m %= 200
note100 = m // 100
print("100 TAKA note: ", note100)
m %= 100
note50 = m // 50
print("50 TAKA note: ", note50)
m %= 50
note20 = m // 20
print("20 TAKA note: ", note20)
m %= 20
note10 = m // 10
print("50 TAKA note: ", note50)
m %= 10
note5 = m // 5
print("5 TAKA note: ", note5)
m %= 5
note2 = m // 2
print("2 TAKA note: ", note2)
m %= 2

print("1 TAKA coin", m)
