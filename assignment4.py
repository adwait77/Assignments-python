 #Demonstrate the use of loop manipulation statements.

#1)break
for i in "Adwait":
    if i=="w":
        break
    else:
        print(i)

i=1
while i<=10:
    if i==5:
        break
    else:
        print(i)
        i+=1

# 2)continue
for i in "Adwait":
    if i=="w":
        continue
    else:
        print(i)

i=1
while i<=10:
    if i==5:
        continue
    else:
        print(i)
        i+=1
# 3)pass
for i in "Adwait":
    if i=="w":
        pass
    else:
        print(i)

i=1
while i<=10:
    if i==5:
        pass
    else:
        print(i)
        i+=1
# 4)for with else loop
for i in "Adwait":
    if i=="w":
        break
    else:
        print(i)
else:
    print("This has break")

for i in "Adwait":
    if i=="w":
        pass
    else:
        print(i)
else:
    print("This has pass")


for i in "Adwait":
    if i=="w":
        continue
    else:
        print(i)
else:
    print("This has continue")

# 5)while with else loop
i=3
while i<=10:
    if i==5:
        break
    else:
        print(i)
        i+=1
else:
    print("This has break")

i=4
while i<=10:
    if i==5:
        continue
    else:
        print(i)
        i+=1
else:
    print("This has continue")

i=1
while i<=10:
    if i==5:
        pass
    else:
        print(i)
        i+=1
else:
    print("This has pass")

