"""                       TASK 1

                  FIBONACCI GENERATOR

The Fibonacci series is a sequence where each number is
the sum of the two preceding numbers, defined by a
mathematical recurrence relationship."""
# 0 1 1 2 3 5 8 
# if the previous number a and b the next number c= a+b
def fibonacc_generator(n):
    a,b = 0,1
    fib_sequence = ['0']
    for i in range(1,n):
        c=a+b
        a=b
        b=c
        fib_sequence.append(a)
    print("["," ".join(map(str,fib_sequence)),"]")

fibonacc_generator(10)