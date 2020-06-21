def sum_even_fibonacci():
    '''
find sum of even value in fibonacci series upto 4m
    '''
    a=0
    b=1
    c=0
    count=0
    while(c<4000000):
        c=a+b
        a=b
        b=c
        if c%2==0:
            count=count+c
    return count    

a=sum_even_fibonacci()
print(a)
