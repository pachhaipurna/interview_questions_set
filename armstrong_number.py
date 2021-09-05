#Python number to check if number is armstrong or not 

def check_armstrong_number(num):

    sum = 0
    temp = num

    while temp > 0:
         digit = temp % 10
         sum += digit**3
         temp//= 10

    if sum == num:
        print(num, 'Is armstrong number')
    else:
        print(num, 'Is not armstrong number')

input_val = int(input('Enter any number'))
check_armstrong_number(input_val)