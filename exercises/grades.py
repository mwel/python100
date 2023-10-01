# grading program

# scores dict

scores = {
    "Max" : 92,
    "Marine" : 100,
    "Alex" : 86,
    "Tom" : 72,
    "Dennis" : 54,
    "Kevin" : 1,
    "Charlotte" : 65,
    "Peter" : 47
}

grades = {}

for key in scores:
    if scores[key] > 91:
        grades[key] = "Outstanding"
    elif scores[key] > 80:
        grades[key] = "Exceeds Expectations"
    elif scores[key] > 70:
        grades[key] = "Acceptable"
    else:
        grades[key] = "Fail"
    
for key in grades:
    print (f"Student: {key} >> {grades[key]}.")
