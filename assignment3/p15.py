try:
    with open("example.txt",'r') as file:
        data = file.read()
        print(data)

except FileNotFoundError:
    print("file not found")

finally:
    file.close()
