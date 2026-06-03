############ write file ########
file = open("demo.txt","w")
file.write("hello ankita")


##### read file#######
file = open("demo.txt","r")
res = file.read()
print(res)
file.close()

##### append file ######
file = open("demo.txt","a")
file.write("\n rajarampuri")
