import matplotlib.pyplot as plt
import math

numbers = list(range(-10, 10))
result = []

def prob1(x):
    return x**2 - 10

def prob2(x):
    return x**2 + x - 100

def prob3(x):
    return x**10 - x**8 + x**2 - 8

def prob4(x):
    return x**4 + x**3 + x**2 + x + 1

def prob5(x):
    if x != 0:
        return (x**2 + x + 10) / (2*x)
    else:
        return None 
    
def prob6(x):
    if x != 0:
        return math.sin(x) / (3*x)
    else:
        return None

def prob7(x):
    return x**3 + 2*x**2 - 10*x + 3

def prob8(x):
    if x != 0:
        return math.cos(x) / (5*x)
    else:
        return None

def prob9(x):
    if x != 0:
        return (x**3 / (2*x)) - 10*x
    else:
        return None

def prob10(x):
    return (x+2)*(x+3)*(x-4)

problems = [prob1, prob2, prob3, prob4, prob5, prob6, prob7, prob8, prob9, prob10]

ans = int(input("What problem do you want to graph? (1-10): "))

if 1 <= ans <= 10:
    for x in numbers:
        result.append(problems[ans - 1](x))
else:
    print("Oops! Input must be between 1 and 10.")

plt.plot(numbers, result, label=f'Problem {ans}')
plt.xlabel('Numbers')
plt.ylabel('Result')
plt.legend()
plt.show()