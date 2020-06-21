def palindrome():
    
    '''
largest palindrome of 3 digit product
    '''
    pal=[]
    for x in range(100,999):
        for i in range(100,999):
            num=str(i*x)
            if len(num)==6:
                if num[0]==num[-1]and num[1]==num[-2]and num[2] == num[-3]:
                    pal.append(i*x)
    return max(pal)
print(palindrome())

