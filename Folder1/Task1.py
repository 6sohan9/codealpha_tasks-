def fibonacci_generator(n):
    a,b=0,1
    fib_sequence = ['0']
    
    for i in range(0,n):
        c=a+b
        a=b
        b=c
        fib_sequence.append(a)
    print("["," ".join(map(str, fib_sequence)),"]")
    
fibonacci_generator(10)
#0 1 1 2 3 5
#0 1 2 3 4 5 