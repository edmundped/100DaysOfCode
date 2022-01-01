"""Adding all even numbers from 1 to 100"""
result = 0
for i in range(1,101):
    if i % 2 == 0:
        result += i

print(result)

"""FizzBuzz game - print number, but print fizz if it's divissible by 3, buzz if by 5. and FizzBuzz if divisible by 3 and 5"""

for i in range(1, 101):
    if i % 3 == 0:
        if i % 5 == 0:
            print("FizzBuzz")
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)