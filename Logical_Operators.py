#Logical Operators
#and to get output both should be true
has_high_incom = True
has_good_credit = True
if has_high_incom and has_good_credit:
    print("\nFor AND : ")
    print("Eligible for loan")
#or to get output anyone should be true
has_high_incom = False
has_good_credit = True
if has_high_incom or has_good_credit:
    print("\nFor OR : ")
    print("Eligible for loan")
#NOT to get output anyone should be true
has_good_credit = True
has_criminal_record = False
if has_good_credit and not has_criminal_record:
    print("\nFor NOT : ")
    print("Eligible for loan")