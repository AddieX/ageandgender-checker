gender = str(input("enter your gender (Male/Female): ".lower().strip()))
age = int(input("enter your age most be above (18+): "))

if age >= 18 and (gender == "male" or gender == "female"):
    if gender == "male":
        print("Welcome sir enter you information down below")

        first_name = str(input("1st name: "))
        last_name = str(input("2nd name: "))

        print(
            f"Welcome, Mr {first_name.capitalize()} {last_name.capitalize()} you can enter the room"
        )
        print(
            "Your full inforamtions:\n",
            {
                "First Name": first_name,
                "Last Name": last_name,
                "Gender": gender,
                "Age": age,
            },
        )
    elif gender == "female":
        print("Welcome miss enter you information down below")

        first_name = str(input("1st name: "))
        last_name = str(input("2nd name: "))

        print(
            f"Welcome, Miss {first_name.capitalize()} {last_name.capitalize()} you can enter the room"
        )
        print(
            "Your full inforamtions:\n",
            {
                "First Name": first_name.capitalize(),
                "Last Name": last_name.capitalize(),
                "Gender": gender.capitalize(),
                "Age": str(age).capitalize(),
            },
        )
    else:
        print("Invalid can't enter!")
else:
    print("You'r too young cant enter this room!")
