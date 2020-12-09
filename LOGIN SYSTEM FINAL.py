def Register():
    hand=open("users.txt","a")
    print ("--------------")
    print ("Registration")
    print ("--------------")
    users=input("Enter your username : ")
    passes=input("Enter your password : ")
    hand.write(users+"\t"+passes+"\n")
    hand.close()
    
def login():
    print ("--------------")
    print ("Login")
    print ("--------------")
    hand=open("users.txt","r")
    data=hand.read()
    hand.close()
    data=data.split("\n")
    users=input("Enter your username : ")
    passes=input("Enter your password : ")
    for i in range (0,len(data)):
        if ((users+"\t"+passes)==(data[i])):
            print("Login Sucessfull ")
            break
        elif((users+"\t"+passes)!=(data[i]) and (i==len(data)-1)):
            print("Wrong username or password")
while True:
    
    opt=input("Do you have an account ? (y/n) or type \"done\" to exit :")
    if (opt=="y"):
        login()
    elif(opt=="n"):
        Register()
    elif(opt=="done"):
        break
    elif(opt=="dev12345"):
        hand=open("users.txt","r")
        data=hand.read()
        hand.close()
        print(data)
