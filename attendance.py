employees=["Denzell","Kaamilah","Arielle","Tariq","Alyyah","Seinfuddin"]
attendence=["Denzell","Kaamilah","Alyyah","Seinfuddin"]

numberOfEmployees=6

if "Denzell" in employees:
    print "Denzell is promoted"
    #This is a comment
elif "Denzell" not in employees:
    print "Denzell is fired"
##############################################
if "Kaamilah" in employees:
    print "Kaamilah is promoted"

elif "Kaamilah" not in employees:
    print "Kaamilah is promoted"
##############################################
if "Arielle" in employees:
    print "Arielle is promoted"

elif "Arielle" not in employees:
    print "Arielle is promoted"

print ("\n")

for person in employees:
    if person in employees and person in attendence:
        print person," is promoted"
    elif person in employees and person not in attendence:
        print person," is fired"

print("\n")

for person in employees:
    if person in employees and person in attendence:
        print person," is promoted"
    else:
        print person," is fired"
