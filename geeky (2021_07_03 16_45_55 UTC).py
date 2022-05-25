#Under this sction, we are creating a dictionary of I.T terms and their meanings
#Creating the dictionary
geek={"HTTP":"Short for Hypertext Transfer Protocol, is a service that controls the tranmission of data over the internet",
      "Server":"As it's name denotes, it is usually a powerful computing device that sits at the center of a computer network and provide services to the clients or workstations"
    }
choice=None
while choice!="5":
    print(
        """
        Geekie Translator
        1. Look up a term
        2. Add a term
        3. Redefine or update a term
        4. Delete a term
        5. Quit Geekie
        """
    )
    choice=input("Choice: ")
    print()
    #Exiting with choice 5
    if choice=="5":
        print("Exiting Geekie...")
    #Getting a definition of term with choice 1
    elif choice=="1":
        term=input("What term do you want Geekie to translate?: ")
        if term in geek:
            definition=geek[term]
            print("The term ", term, "means: ",definition)
        else:
            print("\n The term", term,"cannot be found in the dictionary.")
    #Adding a Key-Value pair
    elif choice=="2":
        term=input("What term do you want to add to the dictionary?: ")
        if term in geek:
            print("The term ", term,"already exist")
        else:
            definition=input("What's the definition of the term?: ")
            geek[term]=definition
            print(term," has been added to the dictionary successfully")
    #Redefining or updating an existing term
    elif choice=="3":
        term=input("Which term do you want to update it's definition?: ")
        if term in term:
            definition=input("Enter the new definition.")
            geek[term]=definition
            print(term, " has been redefined")
        else:
            print("The term doesn't exists. Try adding it.")
    #Deleting a term
    elif choice=="4":
        term=input("Enter the term you want to delete.")
        if term in geek:
            del geek[term]
            print("The term ",term, "has been removed from the dictionary")
        else:
            print("Operation failed! ",term," doesn't exist in the dictionary")
    else:
        print("Invalid Choice")