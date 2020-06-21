def sum_of_3_and_5():
    '''
function to find the sum of all the multiples of 3 or 5 below 1000
    '''
    count=0
    for i in range(1,1000):
        if i%3 is 0 or i%5 is 0:
            count=count+i
    return count
a=sum_of_3_and_5()
print(a)
