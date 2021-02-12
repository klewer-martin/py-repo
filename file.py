
fileName = "myfile.txt"

# Open or create "myfile.txt";
f = open(fileName, "w")

f.write("Hello world!")
f.close()

#open and read the file after the appending:
f = open(fileName, "r")
print(f.read())
