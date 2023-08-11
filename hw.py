# Path: hw.py
print("hello world")

def add(a, b):
    return a + b

def EvenorOdd(a):
    if a % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
def isPrime(a):
    if a == 1:
        return False
    else:
        for i in range(2, a):
            if a % i == 0:
                return False
        return True


if __name__ == "__main__":
    print("hello world")
    print(add(1, 2))
    print(isPrime(10))

