import time

file1 = open("/root/ApkalessTool/Test.txt", "r")

file2 = file1.readlines()
for i in file2:
    print(i)
    time.sleep(0.1)