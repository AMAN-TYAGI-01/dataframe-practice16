# row addition

# import pandas as pd
# stu = {
#     'name': ['saad', 'akhil', 'narendra', 'ashi'],
#     'cls': [12, 11, 10, 9],
#     'res': ['pass', 'fail', 'pass', 'fail']
# }
# df = pd.DataFrame(stu, index=[1, 2, 3, 4])
# print(df)
# stu1 = {
#     'name': ['ayush', 'karan'],
#     'cls': [6, 3],
#     'res': ['pass', 'fail']
# }
# df1 = pd.DataFrame(stu1, index=[5, 6])
# df = pd.concat([df, df1])
# print(df)


# row deletion
# import pandas as pd
# df=pd.DataFrame([12,23,45,56,33],
# index=[1,2,3,4,5],columns=['number'])
# print(df)
# df=df.drop(2)
# print(df)

# rows & columns
#  rename
# import pandas as pd
# df=pd.DataFrame([12,44],index=[1,2],columns=['num'])
# print(df)
# # rename code
# df=df.rename(columns={'num':'number'},index={1:"one",2:'two'})
# print(df)


# indexing selecting and slicing data

# import pandas as pd

# data = {
#     "name": ["Akhil", "Karan", "Saad", "Ayush"],
#     "marks": [80, 75, 90, 85],
#     "city": ["Bhopal", "Indore", "Sehore", "Bhopal"]
# }

# df = pd.DataFrame(data, index=[101, 102, 103, 104])
# print(df)
# Ek row select karna
# print(df.loc[102])
# Ek row ka particular column select karna
# print(df.loc[102, "name"])
# Multiple rows select karna
# print(df.loc[101:103])
# Multiple rows aur ek column select karna
# print(df.loc[101:103, "name"])
# Multiple rows aur multiple columns select karna
# print(df.loc[101:103, ["name", "marks"]])


# iloc[] ka full form hai Integer Location. Iska use row aur column ki numerical position ke basis par data select karne ke liye hota hai.
import pandas as pd

data = {
    "name": ["Akhil", "Karan", "Saad", "Ayush"],
    "marks": [80, 75, 90, 85],
    "city": ["Bhopal", "Indore", "Sehore", "Bhopal"]
}

df = pd.DataFrame(data, index=[101, 102, 103, 104])
# Pehli row select karna
# print(df.iloc[0])
# Pehli row ka pehla column
# print(df.iloc[0, 0])
# Doosri row ka marks
# print(df.iloc[1, 1])
# Pehli teen rows select karna
# print(df.iloc[0:3])

# Pehli teen rows aur pehle do columns
print(df.iloc[0:3, 0:2])
