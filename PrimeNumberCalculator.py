#Program to find prime numbers till given number
def prime_nums(plimit):
    
    num_list=[]
    prime_list=[]

    for num in range(2,(plimit+1)):
        num_list.append(num)

    for i in range(0,(plimit-1)):
        count=0
        for k in range(1,num_list[i]):
            if (num_list[i]%k)==0:
                count+=1
        if count==1:
            prime_list.append(num_list[i])

    return prime_list




if __name__=='__main__':

    print("Welcome to prime number calculator shell, Enter the limit till which prime number is to be generated or type 'quit' to exit:")
    while True:
        print(">>>",end='')
        n=input()

        if n.lower() == 'quit':
            break

        elif not n.isdigit():
            print("Enter digits only!!!")

        elif int(n)<=0:
            print("Enter positive number only!!!")

        elif int(n)==1:
            print("1 is not a prime number")

        else:
            plimit=int(n)
            numbers=prime_nums(plimit)
            print(f"Prime numbers till {plimit}: {numbers}")