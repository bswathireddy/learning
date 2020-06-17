#convert numbers to words
#phone:1234
#one two three four
phone_number=int(input('phone:'))
i=0
digits={
    "0":"zero",
    "1":"one",
    "2":"two",
    "3":"three",
    "4":"four",
    "5":"five",
    "6":"six",
    "7":"seven",
    "8":"eight",
    "9":"nine"
}
output = ""
for i in str(phone_number):
    output=output + digits.get(i)+" "
print(output)