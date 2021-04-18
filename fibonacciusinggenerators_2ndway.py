#fibonacci using generators; this function uses yield instead of return, hence it is generator
def fib(n):
    try:
        a=0
        b=1
        for i in range(int(n)):
            if i==0:
                yield a
            elif i==1:
                yield b
            else:
                c=a+b
                yield c
                a=b
                b=c
    except:
        print('Incorrect type error, Enter intergers only')


if __name__=='__main__':
    print("Welcome to Fibonacci series calculator, In the shell below enter the number up to which you want fibonacci series to be generated or enter 'quit' to exit:")
    while True:
        print('>>>',end='')
        n=input()
        if n=='quit':
            break
        else:
            for num in fib(n):
                print(num)