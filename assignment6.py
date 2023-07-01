def ds(roll_no, name):
    list = [roll_no, name]
    tuple = (roll_no, name)
    set = {roll_no, name}
    dict = {'Roll No': roll_no, 'Name': name}
    
    print("Initial values:")
    print("List:", list)
    print("Tuple:", tuple)
    print("Set:", set)
    print("Dictionary:", dict)
    
    new_roll_no = input("Enter new roll number: ")
    new_name = input("Enter new name: ")
    
    list[0] = new_roll_no
    list[1] = new_name
    
    tuple = (new_roll_no, new_name)
    
    set.remove(roll_no)
    set.add(new_roll_no)
    set.remove(name)
    set.add(new_name)
    
    dict['Roll No'] = new_roll_no
    dict['Name'] = new_name
    
    print("Updated values:")
    print("List:", list)
    print("Tuple:", tuple)
    print("Set:", set)
    print("Dictionary:", dict)

    del list
    del tuple
    del set
    del dict
    
    print("Data structures deleted.")

ds('123', 'Adwait')
