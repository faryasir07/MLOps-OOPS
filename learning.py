class chatbook:
    #constructor : Already called when an object of the class is created
    def __init__(self):
        
        self.username=''
        self.password=''
        self.logged=False
        self.menu()
        
    def menu(self):
        user_input=input('''
                    Welcome to Chatbook !! How would you like to proceed ?
                         1. Press 1 to signup
                         2. Press 2 for signin
                         3. PRess 3 to write an Post 
                         4. Press 4 to message a friend
                         5. PRess any other key to exit ''')
        if user_input=="1":
            self.signup()
        elif user_input=='2':
            self.signin()
        elif user_input=="3":
            self.my_post()
        elif user_input=="4":
            self.sendmsg()
        elif user_input=="5":
            exit()
        
    def signup(self):   ## methods
        email=input("Enter you email here -->")
        pwd=input("ENter your password here --->")
        self.username=email
        self.password=pwd
        print("You have signed up Successfully !!!")
        print("\n")
        self.menu() 

    def signin(self):
        if self.username=="" and self.password=="":
            print("Please sign up first !!!")
        else:
            uname=input('ENter you email/username here -->')
            pwd=input('Enter your password here -->')
            if self.username==uname and self.password==pwd:
                print('You have singed up successfully')
                self.logged=True
            else:
                print("Please enter correct credentials !!!")
        print("\n")
        self.menu()

    def my_post(self):
        if self.logged==True:
            txt=input("ENter your message here -->")
            print(f"The following content has been posted --> {txt}")
        else:
            print("You need to signin first to post something ...")
        print("\n")
        self.menu()
    
    def sendmsg(self):
        if self.logged==True:
            txt = input("Enter your message here -> ")
            frnd = input("Whom to send the msg? -> ")
            print(f"Your message has been sent to {frnd}")
        else:
            print("You need to signin first to post something...")
        print("\n")
        self.menu()
    
user=chatbook()
# user.menu()