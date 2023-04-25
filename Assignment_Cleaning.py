
import pandas as pd
from datetime import datetime
import statistics as stats
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime


df= pd.read_csv("databreaches650.csv")

df['Domain'] = df['Domain'].astype('str')
df['Domain'] = df['Domain'].str.lower()
print(df['Domain'])
# print(df.info()) 


#--------Checking null values------------------------------#

# df_null= df[df.isnull().any(axis=1)]
# print(df_null.info())
 
nan_cols = [i for i in df.columns if df[i].isnull().any()] #-----26 null values

# print(nan_cols)

#--------dropping null values------------------------------#

df = df.dropna()
# print(df.info())

#------Formatting1----converting object to datetime format--#


df['BreachDate'] = pd.to_datetime(df['BreachDate'], infer_datetime_format=True)
df['AddedDate'] = pd.to_datetime(df['AddedDate'], infer_datetime_format=True)
df['ModifiedDate'] = pd.to_datetime(df['ModifiedDate'], infer_datetime_format=True)

# print(df.info())

#--------Finding reported days----------------------------#

df['ReportedDays'] = (df['AddedDate'] - df['BreachDate']).dt.days

# print(df.ReportedDays)

# print(df.info())

#------Finding 5 largest/lowest reported days--------------#

b = df.nlargest(n=5, columns=['ReportedDays'])
c = df.nsmallest(n=5, columns=['ReportedDays'])

# print(b)
# print(c)


#------Finding descriptive statistics for reporteddays-----#

x_bar = stats.mean(df.ReportedDays)
median= stats.median(df.ReportedDays)

#-------Extracting year from the date field----------------#

df['Reported_year'] = df['AddedDate'].dt.year
df['Breach_year'] = df['BreachDate'].dt.year

# print(df.Reported_year)
# print(df.Breach_year)

#----One-hot encoding for two selected categorical columns---# confirm with team!!!!!

df = pd.get_dummies(df, columns = ['IsVerified', 'IsSensitive', 'IsFabricated', 'IsRetired', 'IsSpamList', 'IsMalware'])
# df['IsVerified_False'].astype(int)
# df['IsVerified_True'].astype(int)
# df['IsSensitive_False'].astype(int)
# df['IsSensitive_True'].astype(int)
# df['IsFabricated_False'].astype(int)
# df['IsFabricated_True'].astype(int)
# df['IsRetired_False'].astype(int)
# df['IsRetired_True'].astype(int)
# df['IsSpamList_False'].astype(int)
# df['IsSpamList_True'].astype(int)
# df['IsMalware_False'].astype(int)
# df['IsMalware_True'].astype(int)
# print(df.info())

# print(one_hot_encoded_data)

#-----binary encoding-----------------------#

# df.IsFabricated[df.IsFabricated == 'TRUE'] = 1
# df.IsFabricated[df.IsFabricated == 'FALSE'] = 0

# df.IsSensitive[df.IsSensitive == 'TRUE'] = 1
# df.IsSensitive[df.IsSensitive == 'FALSE'] = 0

# df.loc[df['IsVerified'] == "FALSE",
#             'IsVerified'] = 0

# df.loc[df['IsVerified'] == "TRUE",
#             'IsVerified'] = 1

# df['IsVerified'] = (df['IsVerified'] == 1).astype(int)

# df.loc[df['IsSensitive'] == "FALSE",
#             'IsSensitive'] = 0

# df.loc[df['IsSensitive'] == "TRUE",
#             'IsSensitive'] = 1

# df['IsSensitive'] = (df['IsSensitive'] == 1).astype(int)

# print(df.IsFabricated)


#---------Grouping the data classes---------------#



#---------Dropping unwanted attributes------------#

df = df.drop(['Name', 'Title', 'BreachDate',
                      'ModifiedDate', 'AddedDate' ,'LogoPath'], axis=1)

print(df.info())

# df.to_csv(
#       r'C:\Masters\Sem 3\S123 PRT564 DATA ANALYTICS AND VISUALISATION\Assignment\codes\Master.CSV', index=False)

#Visualizing the past trends!!

#-------------Line graph of number of pawned count per year---------------#

sample = df.groupby(['Breach_year'], as_index=False)['PwnCount'].sum()
lines = sample.plot.line(x='Breach_year', y='PwnCount')

#--------------Stacked Bar chart for verified breaches every year----------#

df.groupby(['Breach_year', 'IsVerified']).size().unstack().plot(kind='bar', stacked=True,
            color=['steelblue','lightblue'], title='Verified breaches every year?')


#--------------Stacked sensitive breaches every year-------------------#

df.groupby(['Breach_year', 'IsSensitive']).size().unstack().plot(kind='bar', stacked=True,
            color=['darkblue','lightblue'], title='Sensitive data breached every year?')


#--------------Line graph to show to dayes taken to report breaches every year------#

sample = df.groupby(['Breach_year'], as_index=False)['ReportedDays'].sum()
lines = sample.plot.line(x='Breach_year', y='ReportedDays')


#---Multiple line graph of sensitive vs non sensitive data breached every incident per year----#

fig, ax = plt.subplots(figsize=(15,7))

df.groupby(['Breach_year', 'IsSensitive']).count()['Title'].unstack().plot(ax=ax)
plt.title("Sensitive vs non sensitive data breached through the years")
plt.ylable("Reported Days")


#------------------Pie chart to show percentage of sensitive data stolen---------#

colors = ['lightblue', 'blue']

explode = (0.1,0.1)

df.groupby(['IsSensitive']).sum().plot(kind='pie', y='PwnCount', title = "Percentage of Sensitive data stolen" ,explode=explode, colors=colors, autopct='%1.0f%%')



# df.to_csv(
#     r'C:\Masters\Sem 3\S123 PRT564 DATA ANALYTICS AND VISUALISATION\Assignment\codes\clean.CSV', index=False)

# print(df.info())


