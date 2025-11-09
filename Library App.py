from datetime import datetime, timedelta
student_name=input("What is the student's name? ")
book_name=input("What is the name of the book? ")
borrow_datestr=input("When was this book borrowed? (YYYY-MM-DD) ")
borrow_date=datetime.strptime(borrow_datestr,"%Y-%m-%d")
borrow_time=14
due_date=borrow_date+timedelta(days=borrow_time)
print("The student's name is:", student_name)
print("The book name is:",book_name)
print("The borrow date is:",borrow_date)
print("The due date is:",due_date)
return_datestr=input("When are you going to return the book or enter the date you returned it (if you have)? ") 
return_date=datetime.strptime(return_datestr,"%Y-%m-%d")
if return_date <= due_date:
    print("Returned on time, no fine will be administered")
else:
    late_days=(return_date-due_date)
    fine= late_days*10
    print("Returned late by", late_days, "days.")
    print("Your fine is", fine, "rupees")