# try: 
#     print(5/0) 
# except ZeroDivisionError: 
#     print("You can't divide by zero!")
    
    
print(f"Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ") 
    if first_number == 'q':
        print(f'Your have exited from program.')
        break 
    second_number = input("Second number: ") 
    if second_number == 'q':
        print(f'Your have exited from program.')
        break
    try:
        answer = int(first_number) / int(second_number) 
    except  ZeroDivisionError:
        print("You cannot divide by zero !")
    else:
        print(answer)