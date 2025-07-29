class BANK:
    def __init__(self):
        self.widhraw = ""
        self.pin = ""
        self.menu()
        if self.input == "1":
            self.changepin()
            
        elif self.input == "3":
            self.setpin()
        self.menu()
        

    
    def menu(self):
        print(""" press 1 for change pin
                  press 2 for enter name
                  press 3 for enter pin
""")
        self.input = input("Enter the number you wnat to perform")
        
    def changepin(self):
        self.oldpin = input("write your oldpin")
        if self.pin == self.oldpin:
            value = input("write your new pin")

            self.pin = value
        else:
            print("first set your pin")
        

    def setpin(self):
        if self.pin == "":
            self.pins = input("enterpin")
            self.pin = self.pins
            
            print("pin setted")
        else:
            "You already have a pin"
        

bank = BANK()       
