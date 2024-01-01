try:
    with open("input.txt", "r") as input:
        lines = input.readlines()
        lines = [line.strip() for line in lines]


    with open("output.txt", "w") as output:
        for i in range(1,len(lines)+1):
            output.write(f"{i} : {lines[i-1]}\n")
        print("numbers added ")
except FileNotFoundError:
    print("file not found")




