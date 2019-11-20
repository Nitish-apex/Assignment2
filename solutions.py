
#NITISH VELU
#PES1UG19CS551



import pandas as pd
df=pd.read_excel('empl.xlsx')

x=input("\npress Enter to view stats:\n")
#1.From the employee dataset provided print first and last five rows
print("first 5 rows:\n")
print(df.head(5))

x=input("\npress Enter to view stats:\n")
print("last 5 rows:\n")
print(df.tail(5))

x=input("\npress Enter to view stats:\n")
#2.Find person who joined after 2000
print("people who joined after 2000:")
for index,row in df.iterrows():
    if row["Year of Joining"]>2000:
        print(row["First Name"])
        

x=input("\npress Enter to view stats:\n")
#3.Find person who is drawing salary more than 1 lakh
print("people drawing salary more than 1 lakh:")
for index,row in df.iterrows():
    if row["Salary"]>100000:
        print(row["First Name"])
    


#4.Find person who are from mid east region
x=input("\npress Enter to view stats:\n")
print("no one from mideast in case the question meant midwest")
print("THE PEOPLE OF MIDWEST\n")
for index,row in df.iterrows():
    if row["Region"]=="Midwest":
        print("\t",row["First Name"])

x=input("\npress Enter to view stats:\n")
#5.Print employee details with his name ,email id, date of joining and his salary
print("employee details with his name ,email id, date of joining and his salary")

print(df[["Name Prefix","First Name","E Mail","Date of Joining","Salary"]])


#6.Sort employee name according to his salary
x=input("\npress Enter to view stats:\n")
# iterating through the sorted dataframe
print("employees sorted based on their salary")
for index,row in df.sort_values(["Salary","First Name"]).iterrows():
    print(row["First Name"])


#7.Sort employee name according to his age
x=input("\npress Enter to view stats:\n")
# iterating through the sorted dataframe
print("employees sorted based on their age")
for index,row in df.sort_values(["Age in Yrs.","First Name"]).iterrows():
    print(row["First Name"])


#8.Print female and male employee details separetely
x=input("\npress Enter to view stats:\n")
#male employee details
print("male employees:")
print(df.loc[df.Gender =="M"])
x=input("\npress Enter to view stats:\n")
#female employee details
print("female employees:")
print(df.loc[df.Gender=="F"])


