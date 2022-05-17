def fun1():
    yield "Karan Ghodake"
    yield "Official"
    yield "Bhose(K)"
    yield "Pandharpur"
    yield "Solapur"
    yield "Maharashtra"
    yield "India"

#Main Program
res=fun1()
print(next(res),end="  ")
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))