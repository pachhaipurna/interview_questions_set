#Reverse an array in ascinding order 

def reverse_array_ascending(input_arr):

    arr_len = len(input_arr)
    temp =0 

    for i in range(0, arr_len):
        for j in range(i+1,arr_len):
            if (input_arr[i]> input_arr[j]):
                temp = input_arr[i]
                input_arr[i] =input_arr[j]
                input_arr[j] = temp

                print(input_arr[i])

    print('Reversed array in ascending', input_arr)

input_arra_data = [23,56,6,78,8,26,18, 2, 8, 7, 1]

reverse_array_ascending(input_arra_data)
