import pandas as pd


df = pd.read_excel("onomata.xls")
new_df = pd.DataFrame()
Fname = []
Lname = []
for index, row in df.iterrows():
    # print(row["Ονόματα"])
    name = row["Ονόματα"].split()
    Fname.append(name[0])
    Lname.append(name[1])

new_df["Fname"] = Fname
new_df["Lname"] = Lname
new_df.to_excel("Names.xls")
