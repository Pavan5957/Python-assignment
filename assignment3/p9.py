with open("input2.txt", "r") as input:
    lines = input.readlines()
    lines = [line.strip() for line in lines]

with open("output2.txt", "w") as output:
    for i in range(len(lines)-1,-1,-1):
        output.write(f"{lines[i]}\n")
