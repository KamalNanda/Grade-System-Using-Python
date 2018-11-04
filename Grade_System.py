records={"name":[],"English":[],"Maths":[],"Sciece":[],"History":[]}
n=int(input("Enter total number of students: "))

for i in range(1,n+1):
    
    for key in records:
        if key=="name":
            records[key].append(input(f"\nEnter {key} : "))
        else:
            records[key].append(int(input(f"Enter {key} : ")))
print("\n")           
def percentage( id ):
    sum=0
    for key in records:
            if key != "name":
                sum+=records[key][id]

    Percent=sum/4
    name=records["name"][id]
    print(f"Percentage of {name} is {Percent}")
for i in range(n):
    percentage(i)
print("\n")
for key in records:
    if key!="name":
        highest=max(records[key])
        idx=[i for i,x in enumerate(records[key]) if x ==(max(records[key]))]
        for i in idx:
            name=records["name"][i]
            print(f"Highest marks in {key} - {highest} \t  - \t Achieved by {name}")
