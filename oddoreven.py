
def oddoreven(a):
    if a==0:
        print('the number Zero is neither even nor odd')
    elif a<0:
        print('u should consider entering a positive number')
    elif a%4==0:
        print('the number is even and is a multiple of four')
    elif a%2==0:
        print('the number is even')
    else:
        print('the number is odd')
print('Enter a number to check if it is odd or even')
a=int(input())
oddoreven(a)

def twonumbers(b,c):
    if b%c==0:
        print('first number is divisible by second number')
    else:
        print('bad luck!,first number is not divisible by second number')

def quest():
    print('Do you still want to continue in this program? If yes,enter Y, else N')
    d=str(input())
    if d!='Y' and 'N':
        print('enter a proper value')
        quest()
    elif d=='Y':
        print('enter two numbers')
        try:
            b=int(input())
            c=int(input())
            twonumbers(b,c)
        except:
            print('Error. Next time try entering the value one by one')
            quest()
    else:
        exit()
quest()
