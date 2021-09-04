#Check no is prime or not 

def check_prime_no(num):
    flag =False

    if num < 0:
        print('PLease input positive no only')
    
    elif num ==1:
        print('PLease add more than 1')
    
    else:    
        if num >1:
            for i in range(2, num):
                if num % i ==0:
                    flag =True
                    break

    if flag:
        print('This is not prime no')
    else:
        print('This is prime no')

input_val = (int(input('Enter any number')))

check_prime_no(input_val)

