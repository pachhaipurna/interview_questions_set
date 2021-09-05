
#code wars
# You are going to be given a word. Your job is to return the middle character of the word. If the word's length is odd, return the middle character. If the word's length is even, return the middle 2 characters.

def get_middle(s):
    #your code here
    str_len = len(s)
    if str_len % 2 > 0:
        print(s[int(str_len / 2)])
        return (s[int(str_len / 2)])
    
    if str_len % 2 == 0:
        print(s[int(str_len/2 - 1):int(str_len / 2 + 1)])
        return s[int(str_len/2 - 1):int(str_len / 2 + 1)]
    
    else:
        return s
input_val = str(input('Enter any string'))
get_middle(input_val)
