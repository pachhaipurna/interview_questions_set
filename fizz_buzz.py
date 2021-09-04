total_input =int(input('Enter input no::'))


for fizzbuzz in range(2, total_input):

    if fizzbuzz %3 == 0 and fizzbuzz %5 == 0:
        print('Fizzbuzz',fizzbuzz)
        continue

    elif fizzbuzz % 3 ==0:
        print('Fizz',fizzbuzz)
        continue
    
    elif fizzbuzz % 5 ==0:   
        print('BUzz', fizzbuzz)
        continue
    
   

