#loop manipulation
#break
for i in "adwait":
    if i=="w":
        break
    else:
        print(i)

i=1
while i<=20:
    if i==10:
        break
    else:
        print(i)

#continue
for i in "adwait":
    if i=="w":
        continue
    else:
        print(i)

i=1
while i<=20:
    if i==10:
        continue
    else:
        print(i)

#pass
for i in "adwait":
    if i=="w":
        pass
    else:
        print(i)

i=1
while i<=20:
    if i==10:
        pass
    else:
        print(i)

#for with else loop
for i in "adwait":
    if i=="w":
        break
    else:
        print(i)
else:
    print("This has break")

for i in "adwait":
    if i=="w":
        pass
    else:
        print(i)
else:
    print("This has pass")


for i in "adwait":
    if i=="w":
        continue
    else:
        print(i)
else:
    print("This has continue")

#while with else loop
i=1
while i<=20:
    if i==10:
        break
    else:
        print(i)
else:
    print("This has break")

i=1
while i<=20:
    if i==10:
        continue
    else:
        print(i)
else:
    print("This has continue")

i=1
while i<=20:
    if i==10:
        pass
    else:
        print(i)
else:
    print("This has pass")

