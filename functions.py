def square(x):
    return x ** 2

y = square(3) # może tez być y = square(x=3)
print(y)

def power(exponent, base):
    return base ** exponent

print(power(2, 3))
print(power(exponent=2, base=3))
print(power(2, base=3))
