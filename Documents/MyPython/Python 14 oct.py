# def fact(num):
#     result=1
#     while num>=1:
#         result=result*num
#         num=num-1
#     return result

# for i in range (1,5):
#     print("the factorial of",i,"is:",fact(i))


# def cal(a,b):
#     add=a+b
#     sub=a-b
#     mul=a*b
#     div=a/b
#     return add,sub,mul,div
# t=cal(50,10)
# print("the results are:")
# for i in t:
#     print(i)


# def even_odd(num):
#     if num%2==0:
#         print(num,"is even no.")
#     else:
#       print(num,"is odd no.")

# even_odd(5)
# even_odd(6)


# def greet(name,msg):
#     '''this function greets the person with the help of a msg'''
#     print("hello",name,msg)

# greet(name="jayeta",msg="gm")
# greet(msg="gm",name="jayeta")


# def marks(sub,mrks):
#     '''show marks along with sub'''
#     print("sub is %s and marks are %d" %(sub,mrks))

# marks('C',10)


# def greet(name="jayeta",msg="gm"):
#     '''this function greets the person with the help of a msg'''
#     print("hello",name,msg)

# greet()
# greet("devyani")
# greet("devyani","good morning")
# greet(name="jayeta",msg="gm")
# greet(msg="gm",name="jayeta")


def func1(*var_arg,arg1):
    print(arg1,end=" ")
    for i in var_arg:
        print(i,end=" ")
    print()
