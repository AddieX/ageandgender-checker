gender = str(input("enter your gender (Male/Female): ".lower().strip()))
age = int(input("enter your age most be above (18+): "))

if age >= 18 and (gender == "male" or gender == "female"):
    if gender == "male":
        print("Welcome sir enter you information down below")

        first_name = str(input("1st name: "))
        last_name = str(input("2nd name: "))

        print(
            f"Welcome, Mr {first_name.capitalize()} {last_name.capitalize()} you able to pass"
        )
        print(
            "Your full inforamtions:",
            {
                "First Name": first_name.capitalize(),
                "Last Name": last_name.capitalize(),
                "Gender": gender.capitalize(),
                "Age": age,
            },
        )
    elif gender == "female":
        print("Welcome miss enter you information down below")

        first_name = str(input("1st name: "))
        last_name = str(input("2nd name: "))

        print(
            f"Welcome, Miss {first_name.capitalize()} {last_name.capitalize()} you able to pass"
        )
        print(
            "Your full inforamtions:",
            {
                "First Name": first_name.capitalize(),
                "Last Name": last_name.capitalize(),
                "Gender": gender.capitalize(),
                "Age": age,
            },
        )
    else:
        print("Invalid can't enter!")
else:
    print("You'r too young can not be able to pass!")
