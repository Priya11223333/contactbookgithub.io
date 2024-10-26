contact={}
def display_contact():
    print("name \t\t phone number \t\t email \t\t address \t\t")
    for key in contact:
        print("{} \t\t {} \t\t {} \t\t {}".format(key,contact.get(key)))
while True:
    print("/n ***welcome to contact book***")
    print("1.ADD A new cntact")
    print("2.Search contact")
    print("3.view a contact")
    print("4.update a contact")
    print("5.delete a contact")
    print("6.exit")
    
    choice=("ENTER YOUR CHOICE:--")
    if choice==1:
        name=input("ENTER YOUR CONTACT NAME:-")
        phone_no=input("ENTER YOUR PHONE NUMBER:-")
        email=input("ENTER YOUR EMAIL_ID:-")
        address=input("ENTER YOUR ADDRESS:-")
        contact[name]=phone_no
        contact[email]=address
    elif choice==2:
        search_name=input("enter the contact name:")
        if search_name in contact:
            print(search_name,"'s contact number is",contact[search_name])
        else:
            print("name is not found in contact book")
    elif choice==3:
        if not contact:
            print("empty contact book")
        else:
            display_contact()
    elif choice==4:
        update_contact=input("enter the contact to be updated")
        if update_contact in contact:
            phone=input("enter mobile number contact[update_contact]=phone_no")
            print("contact updated")
            display_contact()
        else:
            print("name is not found in contact book")        
    elif choice==5:
        del_contact=input("enter the conact to be get deleted")
        if del_contact in contact:
            confirm=input("DO YOU WANT TO DELETE THIS CONTACT:Y/N ?")
            if confirm=='y' or confirm=='Y':
                contact.pop(del_contact)
                display_contact()
            else:
                print("name is not found in the contact book")
    else:
        print("error in your choice please check once")
        
