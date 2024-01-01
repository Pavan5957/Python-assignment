with open("fruit.txt","w") as fruit_data:
   fruit_data.write("mango")

with open("fruit.txt", "r") as data:
    print(data.readline())
    

