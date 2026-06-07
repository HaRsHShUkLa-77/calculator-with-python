a=int(input('enter your 1st number: ' ))
b=int(input('enter your 2nd number: ' ))
c=input('add operation: ')

if c=='/':
    try:
        print(a/b)
    except Exception as e:
        print('sorry an error occured', e)
        print('please enter a valid natural number')
    else:
        pass
    finally:
        pass
elif c=='+':
    print(a+b)
elif c=='-':
    print(a-b)
elif c=='*':
    print(a*b)
elif c=='//':
    print(a//b)
elif c=='%':
    print(a%b)
else:
    print('enter a valid operation')

