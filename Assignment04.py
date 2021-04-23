import mysql.connector
from faker import Faker
import pandas as pd
import datetime

#c.execute("create TABLE Mortgage(OwnerID int primary key auto_increment, DownPayment int, InterestRate float,Years int,"
                    #"FOREIGN KEY Mortgage(OwnerID) references Owner(OwnerID))")
#c.execute("Drop Table Mortgage")

# csv_file = open("./SampleMortgage.csv","w")
# writer = csv.writer(csv_file)
# for x in range(0,10):
#    writer.writerow([myGenerator.random_int(),myGenerator.random_int(),myGenerator.random_int()])
#
# with open('./sampleMortgage.csv',"w",newline='') as file:
#    writer = csv.writer(file)
#    writer.writerow(myGenerator.random_int())

db=mysql.connector.connect(host="34.94.182.22",user="furlong@chapman.edu",passwd="FooBar!@#$",database="furlong_db")
c=db.cursor()
myGenerator = Faker('en_US')


#Owner
df = pd.DataFrame()
OwnerID = []
DOB = []
Sex = []
Occupation = []
IncomeYear = []
MaritalStatus = []
Children = []

# Options for the string variable
my_gender_list = ['Male','Female','Other']
my_marital_list = ['Married','Divorced','Single']

# Adding fake information
for i in range(20):
    OwnerID.append(i)
    i+=1
    DOB.append(myGenerator.date_of_birth(tzinfo=None, minimum_age=25, maximum_age=70))
    Sex.append(myGenerator.word(ext_word_list=my_gender_list))
    Occupation.append(myGenerator.job())
    IncomeYear.append(myGenerator.random_int(min=1, max=9999))
    MaritalStatus.append(myGenerator.word(ext_word_list=my_marital_list))
    Children.append(myGenerator.random_int(min=1, max=5))

# Creating Column
df["OwnerID"] = OwnerID
df["DOB"] = DOB
df["Sex"] = Sex
df["Occupation"] = Occupation
df["IncomeYear"] = IncomeYear
df["MaritalStatus"] = MaritalStatus
df["Children"] = Children
#print(df)
#df.to_csv("FakerMortgage.csv",index=False, header=["OwnerID", "DownPayment", "InterestRate", "Years"])

# Inserting into SQL
for i, row in df.iterrows():
    sql = "INSERT INTO Owner VALUES (%s,%s,%s,%s,%s,%s,%s)"
    c.execute(sql, tuple(row))
    print("Record inserted")
    db.commit()

c.execute('SELECT * from Owner')
data = pd.DataFrame(c.fetchall())
print(data)


#Mortgage
df1 = pd.DataFrame()
OwnerID = []
DownPayment = []
InterestRate = []
Years = []
# Adding fake information
for i in range(20):
    OwnerID.append(i)
    i+=1
    DownPayment.append(myGenerator.random_int(min=1000,max=9000))
    InterestRate.append(myGenerator.random_int(min=1.0, max=30.0))
    Years.append(myGenerator.random_int(min=1, max=30))

df1["OwnerID"] = OwnerID
df1["DownPayment"] = DownPayment
df1["InterestRate"] = InterestRate
df1["Years"] = Years
#print(df1)
#df.to_csv("FakerMortgage.csv",index=False, header=["OwnerID", "DownPayment", "InterestRate", "Years"])

# Inserting into SQL
for i, row in df1.iterrows():
    sql = "INSERT INTO Mortgage VALUES (%s,%s,%s,%s)"
    c.execute(sql, tuple(row))
    print("Record inserted")
    db.commit()

c.execute('SELECT * from Mortgage')
data = pd.DataFrame(c.fetchall())
print(data)

#House
df2 = pd.DataFrame()
OwnerID = []
Address = []
Value = []
numBed = []
numBath = []
Size = []
Pool = []
Garage = []
OtherAmenities = []

# List for text options
my_gender_list = ['Male','Female','Other']
my_marital_list = ['Married','Divorced','Single']
my_pool_list = ['Yes','No']
my_garage_list = ['Yes','No']
my_OtherAmenities = ['Barbeque','Gym']

#Inserting fake information
for i in range(20):
    OwnerID.append(i)
    i+=1
    Address.append(myGenerator.address())
    Value.append(myGenerator.random_int(min=1, max=9999))
    numBed.append(myGenerator.random_int(min=1, max=9))
    numBath.append(myGenerator.random_int(min=1, max=9))
    Size.append(myGenerator.random_int(min=1, max=9999))
    Pool.append(myGenerator.word(ext_word_list=my_pool_list))
    Garage.append(myGenerator.word(ext_word_list=my_garage_list))
    OtherAmenities.append(myGenerator.word(ext_word_list=my_OtherAmenities))

# Turning into column
df2["OwnerID"] = OwnerID
df2["Address"] = Address
df2["Value"] = Value
df2["numBed"] = numBed
df2["numBath"] = numBath
df2["Size"] = Size
df2["Pool"] = Pool
df2["Garage"] = Garage
df2["OtherAmenities"] = OtherAmenities

#print(df2)
#df.to_csv("FakerMortgage.csv",index=False, header=["OwnerID", "DownPayment", "InterestRate", "Years"])

for i, row in df2.iterrows():
    sql = "INSERT INTO House VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    c.execute(sql, tuple(row))
    print("Record inserted")
    db.commit()

c.execute('SELECT * from House')
data = pd.DataFrame(c.fetchall())
print(data)


#Neighbourhood
df3 = pd.DataFrame()
OwnerID = []
Groceries = []
Church = []
EduLower = []
EduHigher = []
Retail = []
Entertainment = []

# Adding fake information
for i in range(20):
    OwnerID.append(i)
    i+=1
    Groceries.append(myGenerator.random_int(min=1,max=9))
    Church.append(myGenerator.random_int(min=1, max=9))
    EduLower.append(myGenerator.random_int(min=1, max=9))
    EduHigher.append(myGenerator.random_int(min=1, max=9))
    Retail.append(myGenerator.random_int(min=1, max=9))
    Entertainment.append(myGenerator.random_int(min=1, max=9))

# Creating columns
df3["OwnerID"] = OwnerID
df3["Groceries"] = Groceries
df3["Church"] = Church
df3["EduLower"] = EduLower
df3["EduHigher"] = EduHigher
df3["Retail"] = Retail
df3["Entertainment"] = Entertainment

#print(df3)
#df.to_csv("FakerMortgage.csv",index=False, header=["OwnerID", "DownPayment", "InterestRate", "Years"])

#inserting into sql
for i, row in df3.iterrows():
    sql = "INSERT INTO Neighbourhood VALUES (%s,%s,%s,%s,%s,%s,%s)"
    c.execute(sql, tuple(row))
    print("Record inserted")
    db.commit()

c.execute('SELECT * from Neighbourhood')
data = pd.DataFrame(c.fetchall())
print(data)

#Utilities
df4 = pd.DataFrame()
OwnerID = []
Internet = []
Water = []
Electricity = []
Gas = []
Waste= []

#creating fake data
for i in range(20):
    OwnerID.append(i)
    i+=1
    Internet.append(myGenerator.random_int(min=1,max=100))
    Water.append(myGenerator.random_int(min=1, max=100))
    Electricity.append(myGenerator.random_int(min=1, max=100))
    Gas.append(myGenerator.random_int(min=1, max=100))
    Waste.append(myGenerator.random_int(min=1, max=100))

df4["OwnerID"] = OwnerID
df4["Internet"] = Internet
df4["Water"] = Water
df4["Electricity"] = Electricity
df4["Gas"] = Gas
df4["Waste"] = Waste


print(df4)
#df.to_csv("FakerMortgage.csv",index=False, header=["OwnerID", "DownPayment", "InterestRate", "Years"])

#inserting into sql
for i, row in df4.iterrows():
    sql = "INSERT INTO Utilities VALUES (%s,%s,%s,%s,%s,%s)"
    c.execute(sql, tuple(row))
    print("Record inserted")
    db.commit()

c.execute('SELECT * from Utilities')
data = pd.DataFrame(c.fetchall())
print(data)