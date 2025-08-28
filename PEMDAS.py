medical_cause= input("Do you have a medical cause?")
attendence= int(input("Input your attendence."))
if medical_cause=="yes":
    print("You are allowed.")
else:
    if attendence>=75:
        print("You are allowed.")
    else:
        print("You are not allowed.")
 