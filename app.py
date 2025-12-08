def greet(name: str):
    return f"hi - {name}"

def add(a: int, b: int):
    return a + b

def mul(a: int, b: int):
    return a * b

def popsa(a: int, b: int):
    return a / b
if __name__ == "__main__":
    print(greet("Stas"))
    print("2 + 3 =", add(2, 3))
    print("2 * 5 =", mul(2, 5))
    print("6 / 3 =", popsa(6, 3))
        
