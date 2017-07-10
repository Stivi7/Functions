
# ex no.1

def right_justify():                
    s = "monty"
    print(" " * 65, s)



right_justify()


# ex no.2

def do_twice(f, x):
    f(x)
    f(x)

def print_twice(x):        # print twice function.
    print(x)        
    print(x)
   

def print_spam(x):
    print('spam')

def do_four(f, x):
    do_twice(f, x)
    do_twice(f, x)

do_twice(print_twice, 'spam')
do_four(print_twice, 'spam')
