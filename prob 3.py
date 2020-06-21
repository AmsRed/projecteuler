
def prime_no(num):
    '''
    '''
    for i in range(2,num):
        if num%i!=0:
            return True
        else:
            return False



l=[]
def factor(num):
    ''' '''
    for i in range(2,num):
        if num%i==0:
            l.append(i)
    return l

def prime_factor(num):
    '''
finding largest prime factor
    '''
    a=0
    for i in range(2,num+1):
        if num%i==0:
            a=1
            for j in range(2,(i//2+1)):
                if i%j==0:
                    a=0
                    break
            if a==1:
                print(i)
                
                

num=600851475143
a=prime_no(num)
c=prime_factor(num)
print(c)

