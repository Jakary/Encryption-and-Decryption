def Encrypt(filename,key):
    file = open(filename,"rb")
    data = file.read()
    file.close()

    data = bytearray(data)
    for index, value in enumerate(data):
        data[index]= value ^ key 

    file = open("oo" +  filename,"wb")
    file.write(data)
    file.close()

def Decrypt(filename, key):
    file = open(filename,"rb")
    data = file.read()
    file.close()

    data = bytearray(data)
    for index, value in enumerate (data):
        data[index] = value ^ key

    file = open(filename,"wb")
    file.write(data)
    file.close()
        
    
choice = ""
while choice !="3":
    print("Select and an option")
    print("1.Encrypt a file")
    print("2.Decrypt a file")
    print("3.Quit")

    choice = input()
    if choice == "1" or choice == "2":
        key = int(input("Enter a key as a number\n"))
        filename = input("Enter file name:\n")
    if choice == "1":
        Encrypt(filename, key)
    if choice == "2":
        Decrypt(filename, key)
Encrypt(filename,key)
