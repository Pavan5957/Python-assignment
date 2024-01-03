try:
    with open("example.txt",'r') as f:
        data = f.read()

        print(data)

except FileNotFoundError:
    print("file does not found")

except PermissionError:
    print("you dont have permission to access this file")

except Exception as e:
    print(f"An unexpected error occured: {e}")




