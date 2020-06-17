alphabet=input('name:').lower()
alphabets={
    "a":"apple",
    "b":"boy",
    "c":"cat",
    "d":"dog"
}
output=""
for i in alphabet:
    output+=alphabets.get(i,"!")+" "
print(output)
#missed emoji converter