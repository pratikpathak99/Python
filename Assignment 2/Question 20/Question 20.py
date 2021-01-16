#Write a demo program for file read & write and file handling methods like seek, tell,writeline, readline.

f = open('name.txt', 'w')
f.write("Well glad to know that.")
f.close()
f = open('name.txt', 'r')
print(f.readline())

f.seek(5)   
print(f.tell())
print(f.readline())
print(f.tell())
f.close()
