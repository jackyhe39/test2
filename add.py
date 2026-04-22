# create a function that adds two numbers together and returns the result
def add(a, b):
    return a + b
# test the functionprint(add(2, 3))  # should print 5
print(add(10, 10))  # should print 0
print(add(20, 20))  # should print 0
print(add(1.5, 2.5))  # should print 4.0

# create the main function to test the add function
def main():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = add(num1, num2)
    print(f"The sum of {num1} and {num2} is {result}")

# create a simple test file with name aaa.txt only for testing purposes and store it in the repository once GitHub actiion run completed
with open("aaa.txt", "w") as f:
    f.write("This is a test file for GitHub Actions.")
# run the main function
if __name__ == "__main__":
    main()           