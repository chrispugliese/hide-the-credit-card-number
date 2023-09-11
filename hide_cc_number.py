#need to allow credit card input from user
    ##credit_card_number = input("enter credit card number")


#print(credit_card_number)
#def hide_cc_number():
credit_card_number = input("Enter credit card number: ")
while len(credit_card_number) != 16:
    print("Not a valid credit card number!: ")
    credit_card_number = input("Enter credit card number: ")
else:
    print(credit_card_number)




#class credit_card:
#    def __init__(self, number):
#        self.number = number  