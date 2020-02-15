try:
    loop_val = True
    user_dob = ""
    user_age = 0
    user_full_name = ""
    user_country = ""
    user_state = ""
    user_is_active = ""

    while loop_val:
        try:
            user_dob = input("Enter Date of Birth: ")

            user_age = int(input("Enter age: "))

            user_full_name = input("Enter Full Name:")

            user_country = input("Enter Country:")

            user_state = input("Enter State:")

            user_is_active = input("Active or Not Active in Software Development:")

            loop_val = False
        except Exception as qust:
            loop_val = True
            print(qust)
            print("Please answer all questions.")
            pass
        pass

        user_info = {"DOB": user_dob, "Fullname": user_full_name, "Country": user_country, "State": user_state, "Active/NotActive": user_is_active}

        users_experience = input("How many years of experience do you have developing software?\n[1] Less than 1 year experience.\n"
                                    "[2] 1-3 years of experience.\n[3] 3-8 years of experience.\n[4]"
                                    "8+ years of experience.\n")
                                    
        if int(users_experience) == 1:
            print("Expect between $40,000 and $60,000 for your level of experience.")
        elif int(users_experience) == 2:
            print("Expect between $60,000 and $80,000 for your level of experience.")
        elif int(users_experience) == 3:
            print("Expect between $80,000 and $120,000 for your level of experience.")
        elif int(users_experience) == 4:
            print("Expect at least $130,000 for your level of experience.")
        else:
            print("Sorry, invalid option selected.")
        user_coding_languages = input("Which Coding Languages do you know? (Seperate each language by commas)\n")
        print("Before split():" + user_coding_languages)
        user_coding_languages = user_coding_languages.split(",")

        print("After split():" + str(user_coding_languages))

        if len(user_coding_languages) < 3:
           print("Learn more Coding Languages & deduct $10k from expected salary.")
        elif len(user_coding_languages) == 3:
           print("Great! We can add a minimum of $5k to your annual salary.")
        elif len(user_coding_languages) >= 5:
           print("With your proficiency with multiple Coding Languages, we can negotiate a $15k bump in your annual salary.")
        elif len(user_coding_languages) == 4:
           print("Perfect! You are a model candidate for the position, we can negotiate a $10k bump in you annual salary after quarterly reviews ")
        
        if input("Do you want to enter another another candidate? ").upper == "Y":
           loop_val = True
        else:
           print(user_info)
           loop_val = False
           pass
except Exception as inst:
    loop_val = True
    print("Program halted with exception " + inst)
    pass
