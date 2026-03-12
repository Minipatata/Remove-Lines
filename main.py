# Write a Python program to remove lines of a file starting with prefix 
# - Coding and store the contents in a new file.
f=open("demo.txt","r")
f1=open("demo1.txt","w")
for i in f:
    if "Coding" in i:
        f1.write(i)