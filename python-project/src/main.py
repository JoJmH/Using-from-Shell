import calculations

def main():
    print("Welcome to the Python Project!")

def subtract():
    print(f"Subtracting two numbers and the answer is:", calculations.subtract(5, 3))
    
def add():
    print(f"Adding two numbers and the answer is:", calculations.add(3, 5))

if __name__ == "__main__":
    main()
    subtract()
    add()