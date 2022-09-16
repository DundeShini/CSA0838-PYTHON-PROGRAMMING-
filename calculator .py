def add(X, N):
    return X + N
def subtract(x, N):
    return X- N
def multiply(x, N):
    return X * N
def divide(X, y):
    return X / N
def pow(X, N):
    return X**N

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.power")

while True:
    choice = input("Enter choice(1/2/3/4/5): ")
    if choice in ('1', '2', '3', '4'):
        X= float(input("X= "))
        N= float(input("N= "))

        if choice == '1':
            print(X, "+", N, "=", add(X, N))

        elif choice == '2':
            print(X, "-", N, "=", subtract(X, N))

        elif choice == '3':
            print(X, "*", N, "=", multiply(X, N))

        elif choice == '4':
            print(X, "/", N, "=", divide(X, N))
        elif choice == '5':
            print(X, "**", N, "=", pow(x, N))
        
        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    
    else:
        print("Invalid Input")
