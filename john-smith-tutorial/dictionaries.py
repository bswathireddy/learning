#details should be entered in curly braces
#variable name can be used only once NO duplivate variable names(unique key names)
#can use any of the data types(int,string float etc)
#.get
#adding new key values later
customer={
    "name" : "swathi",
    "age" : 24,
    "mail ID": "swathi@gmail.com",
    "is_verified" : True
}
customer["name"]="Swathi"
print(customer.get("dateofbirth"))


