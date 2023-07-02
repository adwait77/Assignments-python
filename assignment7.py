
def update(rollno, name, class_name, file="data.txt"):
    try:
        f=open(file,"a")
        f.writelines([rollno +"\n" ,name + "\n" ,class_name +"\n"])
        print("Data added successfully")
        f=open(file,"r")
        data=f.readlines()
        for line in data:
            print(line)
       
    except IOError :
        print("Unable to open or write to the file")


update("15","Adwait","CO")