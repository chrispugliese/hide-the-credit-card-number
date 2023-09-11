#private_credit_card_number = credit_card_number.replace( str(num), str(num+1), '*')

K = '*'

credit_card_number = input("Enter credit card number: ")
while len(credit_card_number) != 16 or (not credit_card_number.isdigit()):
    print("Not a valid credit card number! ")
    credit_card_number = input("Try again: ")
else:
    for i in credit_card_number:
        if i.isdigit():
            credit_card_number = credit_card_number.replace(i, K)

    print(credit_card_number)


#need to allow credit card input from user
    ##credit_card_number = input("enter credit card number")
#print(credit_card_number)
#def hide_cc_number():
#class credit_card:
#    def __init__(self, number):
#        self.number = number  
#private_credit_card_number = credit_card_number.replace( [0,11], "*")
# replace function?

