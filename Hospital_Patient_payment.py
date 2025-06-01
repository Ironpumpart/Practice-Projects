''' A simple program for patients to pay their medical bills.
Features:
1. An option to view patient profile.
2. After seeing treatment cost, patients can proceed to make payment
3. Select insurance (if on any) and insurance type. Details of the insurance benefits will be displayed
4. Select payment method for both patients with insurance and those without.
5. Payment is confirmed
6. Select if patient would perform another task
7. If no, program ends. 

written by: David Nnaji on 5/22/2025'''



import sys

def patient_info():
    # A funtion to retrieve patient data and treatment cost
    print('---------------------')
    print(f'Name:  {name}')
    print(f'Age:  {age}')
    print(f'Diagnosis:  {diagnosis}')
    print(f'Treatment:  ${cost:.2f}')
    print('---------------------')

def is_insurance():
    is_running = True
    # A function to check if patient has insurance
    while is_running:
        print('---------------------')
        print('Do you have insurance?')
        print('---------------------')
        print('1. YES')
        print('2. NO')
        print('3. Exit')
        choice = input('Input a number: ')
        if choice == '1':
            insurance_type()
            is_running = False
        elif choice == '2':
            print('---------------------')
            print(f'Full payment: ${cost:.2f}')
            print('---------------------')
            if_no_insurance()
            is_running = False
        elif choice == '3':
            is_running = False
        else:
            print('---------------------')
            print('Invalid Number!!')
            print('---------------------')
            


values = []
def insurance_type():
    # A function to determine the type of insurance the patient has
    is_running = True
    while is_running:
        print('---------------------')
        print('What is your Insurance plan?')
        print('---------------------')
        print('1. Platinum')
        print('2. Gold(individual)')
        print('3. Gold(family)')
        print('4. Silver')
        print('5. Exit')
        choice = input('Input a number: ')
        if choice == '1':
            print('---------------------')
            print('You are eligible for a full discount')
            values.append(1.0)
            insurance_value()
            is_running = False
        elif choice == '2':
            print('---------------------')
            print('You are eligible for 70% discount')
            values.append(0.70)
            insurance_value()
            is_running = False
        elif choice == '3':
            print('---------------------')
            print('You are eligible for half discount')
            values.append(0.50)
            insurance_value()
            is_running = False
        elif choice == '4':
            print('---------------------')
            print('You are eligible for 25% discount')
            values.append(0.25)
            insurance_value()
            is_running = False
        elif choice == '5':
                is_running = False
        else:
                print('---------------------')
                print('Invalid Number!!')
                print('---------------------')


def insurance_value():
    global final_payment
    discount = cost * values[0]
    final_payment = cost - discount
    # A function to check the value of the insurance type
    print('---------------------')
    print(f'Payment before discount: {cost:.2f}')
    print(f'Discounted amount: {discount:.2f}')
    print(f'Payment after discount: {final_payment:.2f}')
    # Move to push to select_payment()
    print('---------------------')
    print(f'Do you want to proceed to pay {final_payment:.2f}?')
    print('---------------------')
    print('1. YES')
    print('2. NO')
    choice = input('Input Number: ')
    is_running = True
    while is_running:
        if choice == '1':   
            select_payment()
            is_running = False
        elif choice == '2':
            is_running = False
        else:
            print('Invalid Entry!')
            return 0

def if_no_insurance():
     # A function to select payment for patients without insurance
     print('---------------------')
     print(f'Proceed to pay: {cost}')
     print('---------------------')
     print('1. YES')
     print('2. NO')
     choice = input('Input Number: ')
     is_running = True
     while is_running:
        if choice == '1':
            no_insurance_select_payment()
            is_running = False
        elif choice == '2':
             is_running = False
        else:
             print('---------------------')
             print('Invalid Entry')
             print('---------------------')
             return 0

def no_insurance_invoice():
     # A function to generate an invoice for patients without insurance
    print('---------------------')
    print('INVOICE')
    print('---------------------')
    print('Invoice ID')
    print(f'Name: {name}')
    print(f'Amount: {cost:.2f}')
    print('Invoice number: 1234567')     
            
   
def no_insurance_select_payment():
    # A function to select between payment types for patients without insurance  
    # choose your preferred payment method
    print('---------------------')
    print(f'How would you like to pay: {cost}')
    print('---------------------')
    print('1. Cash')
    print('2. Card')
    print('3. Bank Transfer')
    print('4. Exit')
    choice = input('Input a number: ')
    is_running = True
    while is_running:
        if choice == '1':
            no_insurance_invoice()
            is_running = False
            back_to_start()
        elif choice == '2':
            print('Input card')
            print('---------------------')
            validate_pin()
            is_running = False
            back_to_start()
        elif choice == '3':
            print('---------------------')
            print('Bank: Fidelity Bank PLC')
            print('Account no: 87654321')
            print('---------------------')
            is_running = False
            back_to_start()
        elif choice == '4':
             is_running = False
        else:
            print('---------------------')
            print('Invalid Number!!')
            print('---------------------')
            return 0   




def invoice():
            # A function to generate a payment invoice  
            print('---------------------')
            print('INVOICE')
            print('---------------------')
            print('Patient ID: 098')
            print(f'Name: {name}')
            print(f'Amount: {final_payment:.2f}')
            print('Invoice number: 1234567')

            

def validate_pin():   
            # A function to check validity of inputted pin
            user_pin = input('Enter Pin: ')
            if user_pin == pin:
                print('---------------------')
                print('Payment Successful!')
                print('---------------------')
            else:
                print('Incorrect Pin!')

def select_payment():
    # A function to select between payment types   
    # choose your preferred payment method
    print('---------------------')
    print(f'How would you like to pay: {final_payment}')
    print('---------------------')
    print('1. Cash')
    print('2. Card')
    print('3. Bank Transfer')
    print('4. Exit')
    choice = input('Input a number: ')
    is_running = True
    while is_running:
        if choice == '1':
            invoice()
            is_running = False
            back_to_start()
        elif choice == '2':
            print('---------------------')
            print('Input card')
            print('---------------------')
            validate_pin()
            is_running = False
            back_to_start()
        elif choice == '3':
            print('---------------------')
            print('Bank: Fidelity Bank PLC')
            print('Account no: 87654321')
            print('---------------------')
            is_running = False
            back_to_start()
        elif choice == '4':
             is_running = False
        else:
            print('---------------------')
            print('Invalid Number!!')
            print('---------------------')
            return 0    

def finish():
     print('---------------------')
     print('A & B Hospitals')
     print('Thank you, Have a nice day')
     print('---------------------') 

def back_to_start():
    print('---------------------')
    print('Do you want to perform another action?')
    print('---------------------')
    print('1. YES')
    print('2. NO')
    choice = input('Input Number: ')
    is_running = True
    while is_running:
        if choice == '1':
            is_running = False
        elif choice == '2':
            finish()
            is_running = False
            sys.exit()
        else:
            print('---------------------')
            print('Invalid Number!')
            print('---------------------')
            return 0 
    
def main():
    global cost
    global name
    global age
    global diagnosis
    global pin                        
    # test variables 
    cost = 100
    name = 'Mark'
    age = 31
    diagnosis = 'Malaria'
    pin = '1234'

    is_running = True

    while is_running:
            print('---------------------')
            print('Welcome to A & B Hospitals')
            print(f'Hello {name}')
            print('---------------------')
            print('Would you like to: ')
            print('1. View profile')
            print('2. Make payment')
            print('3. Exit')
            print('---------------------')

            choice = input('Enter your choice: ')
        
            if choice == '1':
                patient_info()
            elif choice == '2':
                is_insurance()
            elif choice == '3':
                is_running = False
            else:
                print('---------------------')
                print('Invalid Number!!') 
    print('---------------------')
    print('A & B Hospitals')
    print('Thank you, Have a nice day')
    print('---------------------')


if __name__ == '__main__':
     main()
