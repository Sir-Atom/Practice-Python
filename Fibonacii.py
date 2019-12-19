def fib():
    print('how many Fibonnaci numbers you want to generate?')
    a=int(input())
    b=0
    c=0
    d=1
    for i in range(0,a):
        b=b+c
        c=d
        d=b
        print(d)
fib()
