while True:
    try:
        age=int(input("Enter your age for  permanent driving license:"))
        if age<18:
            raise Exception
        else:
            print("Your are elegible for  permanent license")
            break
    except Exception:
        print("You are not elegible for  permanent driving license")
