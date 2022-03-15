from asyncio.windows_events import NULL
import pymongo
import click
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["admin"]
coll=mydb["CMDOperation"]
################################################### @author-- SAURABH KUMAR #######################################################

choices={"0":"Exit","1":"Insert","2":"Find","3":"Delete","4":"Update Data","5":"Show Datas"}
# print(choices)

print("==============================================")
print("[0]. Exit")
print("[1]. Insert Document")
print("[2]. Find Document")
print("[3]. Delete Document")
print("[4]. Update Document")
print("[5]. Show Documents")
print("==============================================")
print("Kindly Enter Any Number [0] or [1] or [2] or [3] or [4] or [5] based on the Requirement")

choice_input=str((input("Please Enter Your Choice here..\n")))

if choice_input=="0":
    print("Exit")
    click.confirm("Please Press Any Button to Exit !!")

    ##################### Insert Document ###########################
elif choice_input=="1":
    print("Here, We are going to ask your user details like [Name] and [Company Name] and [Mobile No] and [Email I'd] and [Address] to insert the Document")

    new_name=str(input("Please Enter Your New Name\n"))
    new_company_name=str(input("Please Enter Your Company Name\n"))
    new_Mobile=str(input("Please Enter Your Mobile Number\n"))
    new_email=str(input("Please Enter Your New Email I'd\n"))
    new_address=str(input("Please Enter Your New Address\n"))

   

    insert_values_total={"name":new_name,"company name":new_company_name,"mobile":new_Mobile,"email":new_email,"address":new_address}
    insert_values_mobile={"mobile":new_Mobile}
    insert_values_email={"email":new_email}

   

    if coll.find_one(insert_values_mobile):
        print("Mobile Number already Exist in the databases, Please enter another mobile number")
    if coll.find_one(insert_values_email):
        print("Email I'd already Exist in the databases, Please enter another email i'd")
    if  new_name=="" or  new_company_name=="" or  new_Mobile=="" or  new_email=="" or  new_address=="":
        print("Any entry field can not be empty [ Required ]")
    else:   
        coll.insert_one(insert_values_total)
        print("Great :) Document has been inserted successfully :)")

    click.confirm("Please Press Any Button to Exit !!")
elif choice_input=="2":
    print("Find Details By Mobile No....")
    mobile_input=str(input("Please Enter Your Mobile No.\n"))
    value1={"mobile":mobile_input}

    res=coll.find(value1)
    for i in res:
        print(i)
        click.confirm("Please Press Any Button to Exit !!")

    ##################### Delete Document ###########################
elif choice_input=="3":
    print("Here, We shall ask your existing Mobile number for Delete the Documents")

    find_by_mobileNo_Input=str(input("Please Ente Your Existing Mobile No\n"))
    exist_mobile={"mobile":find_by_mobileNo_Input}
    if coll.find_one(exist_mobile):
        coll.delete_one(exist_mobile)
        print("Document has been deleted Successfully :)\n")

    else:
        print("Invalid, Mobile Number does not exist in the database")

    click.confirm("Please Press Any Button to Exit !!")
elif choice_input=="4":
    print("Update Seperate Document\n")
    print("==============================================")
    print("N. Name")
    print("E. Email")
    print("A. Address")
    print("M. Mobile")
    print("C. Company Name")
    print("==============================================")


    print("Please Enter Any Keys [N] or [E] or [A] or [M] or [C] based on the requirement")
    update_choices={"N":"Name","E":"Email","A":"Address","M":"Mobile","C":"Company Name"}
    print("\n")
    update_input=str(input(update_choices)).upper()

    ###################### Update Name #############################

    if update_input=="N":

        print("Please Update Name [ Here, We shall ask your existing name and new name for update]\n")

        find_by_mobileNo_Input=str(input("Please Ente Your Existing Mobile No\n"))
        exist_mobile={"mobile":find_by_mobileNo_Input}
        if coll.find_one(exist_mobile):
            old_name_input=str(input("Please Enter Your Existing Name\n"))
            old_name_myquery = {"name": old_name_input}

            if coll.find_one(old_name_myquery):
                update_name_input=str(input("Please Enter Your New Name ..\n"))
                newvalues_update =  {"$set":{ "name": update_name_input }}

                coll.update_one(old_name_myquery,newvalues_update)
                print("Name has been Updated Successfully..")
            else:
                print("Username not exist in the Database\n")
        else:
            print("Sorry, Mobile Number Not Found in the database")

        click.confirm("Please Press Any Button to Exit !!")

        ###################### Update Email #############################
    elif update_input=="E":
        print("Please Update Email [ Here, We shall ask your existing email and new email for update]\n")

        find_by_mobileNo_Input=str(input("Please Ente Your Existing Mobile No\n"))
        exist_mobile={"mobile":find_by_mobileNo_Input}

        if coll.find_one(exist_mobile):

            old_email_input=str(input("Please Enter Your Existing Email I'd\n"))

            old_email_myquery = {"email": old_email_input}
            if coll.find_one(old_email_myquery):
                update_email_input=str(input("Please Enter Your New Email I'd ..\n"))
                newvalues_update_email =  {"$set":{ "email": update_email_input }}
                coll.update_one(old_email_myquery,newvalues_update_email)
                print("Emaid I'd has been Updated Successfully..")
            else:
                print("Email I'd not Exist in the Database :( \n")                
        else:
            print("Invalid Mobile Number")

        click.confirm("Please Press Any Button to Exit !!")

        ###################### Update Address #############################
    elif update_input=="A":
        print("Please Update Address [ Here, We shall ask your existing address and new address for update]\n")

        find_by_mobileNo_Input=str(input("Please Ente Your Existing Mobile No\n"))
        exist_mobile={"mobile":find_by_mobileNo_Input}

        if coll.find_one(exist_mobile):
            old_address_input=str(input("Please Enter Your Existing Address\n"))
            old_address_myquery = {"address": old_address_input}

            if coll.find_one(old_address_myquery):

                update_address_input=str(input("Please Enter Your New Address ..\n"))
                newvalues_update_address =  {"$set":{ "address": update_address_input }}
                coll.update_one(old_address_myquery,newvalues_update_address)
                print("Address has been Updated Successfully..")
            else:
                print("Sorry, This address does not exist in the database :( \n")
        else:
            print("Sorry, Mobile Number Not Found in the database :( \n")

        click.confirm("Please Press Any Button to Exit !!")

        ###################### Update Mobile No. #############################
    elif update_input=="M":
        print("Please Update Mobile Number [ Here, We shall ask your existing mobile number and new mobile number for update]\n")

        find_by_mobileNo_Input=str(input("Please Ente Your Existing Mobile No\n"))
        exist_mobile={"mobile":find_by_mobileNo_Input}

        if coll.find_one(exist_mobile):
            old_mobile_input=str(input("Please Enter Your Existing Mobile Number\n"))
            old_mobile_myquery = {"mobile": old_mobile_input}

            if coll.find_one(old_mobile_myquery):

                update_mobile_input=str(input("Please Enter Your New Mobile Number ..\n"))
                newvalues_update_mobile =  {"$set":{ "mobile": update_mobile_input }}
                coll.update_one(old_mobile_myquery,newvalues_update_mobile)
                print("Mobile Number has been Updated Successfully..")
                
            else:
                print("Invalid, Mobile Number does not exist  :(")
        else:
            print("This Mobile Number does not exist in the database :(")
        click.confirm("Please Press Any Button to Exit !!")

        ###################### Company Name #############################

    elif update_input=="C":
        print("Please Update Company Name [ Here, We shall ask your existing Company Name and new Company Name for update]\n")

        find_by_mobileNo_Input=str(input("Please Ente Your Existing Mobile No\n"))
        exist_mobile={"mobile":find_by_mobileNo_Input}

        if coll.find_one(exist_mobile):
            old_companyname_input=str(input("Please Enter Your Existing Company Name\n"))
            old_companyname_myquery = {"company name": old_companyname_input}

            if coll.find_one(old_companyname_myquery):

                update_companyname_input=str(input("Please Enter Your New Company Name ..\n"))
                newvalues_update_companyname =  {"$set":{ "company name": update_companyname_input }}
                coll.update_one(old_companyname_myquery,newvalues_update_companyname)
                print("Company Name has been Updated Successfully..")
            else:
                print("Sorry, This Company Name does not exist in the database :(\n")
        else:
            print("Sorry, Mobile Number Not Found in the database :( \n")

        click.confirm("Please Press Any Button to Exit !!")
    else:
        print("Kindly choose correct key [N] or [E] or [A] or [M] or [C] to proceed !!")
        click.confirm("Please Press Any Button to Exit !!")


##################### Show Entire Documents ##############################################
elif choice_input=="5":
    print("Showing Entire Documents\n")

    print("Total Documents are: "+str(coll.count_documents({})))
    for i in coll.find({}):
        print(i)
    
    print("Find User details By Unique Mobile No....")
    mobile_input=str(input("Please Enter Your Existing Mobile No.\n"))
    value1={"mobile":mobile_input}

    res=coll.find(value1)
    if res:
        for i in res:
            print(i)
            click.confirm("Please Press Any Button to Exit !!")
    else:
        print("Invalid Mobile Number\n")

else:
    print("Invalid, Please Enter correct choice")

