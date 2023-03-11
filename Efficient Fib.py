#recurssion - calling a function to itself
def fib_simple(n):
    if n<0:
        print("Enter a valid number")
    elif n==1 :
        return(1)
    elif n==2:
        return(1) 
    elif n>2
        result= fib_simple(n-1)+ fib_simple(n-2)
        return(result)     