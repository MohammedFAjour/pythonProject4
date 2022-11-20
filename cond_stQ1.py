print("******Hello User********")
name = input("Enter Your Name :")

if name.isdigit() or name == "":
    print("Error Input.")

age= input("Enter Your Age : ")
if age.isalpha() or age == "":
    print("Error Input.")

address=input("Enter Your address: ")
if address.isdigit() or address == "":
    print("Error Input.")

print("Hello Mr/Ms :{",name ,"} Age: {",age,"} address: {",address,"}")