#This is fibonaccie series number program , ask multiple times in interview

def fibonacci_series(num):

    n1,n2 =0,1
    count = 0

    if num < 0:
        print('Please input positive number only')
    
    if num == 1:
        print('Fibonaccie series for ', num)
    
    else:

        while (count<num):
            print(n1)
            nth = n1 + n2
            n1 = n2
            n2 = nth
            count += 1
        
input_val = int(input('Enter number of terms'))

fibonacci_series(input_val)
