##file= open("new.txt","x")
with open("new.txt", "w") as f:
    f.write("Hello Python")
f = open("new.txt","r")
content=f.read()
print(content)
f.close()

with open("new.txt") as f:
    for line in f:
        print(line)
with open("new.txt", "a") as f :
    f.write("\nNew Line Added")

lines = ["One\n", "Two\n", "Three\n"]
with open("new.txt", "w") as file:
    file.writelines(lines)    

with open("new.txt","r") as f:
    for lines in f:
        print(lines)