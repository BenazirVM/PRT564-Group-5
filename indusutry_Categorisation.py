
import pandas as pd
from datetime import datetime
import statistics as stats
import numpy as np
import matplotlib.pyplot as plt

#------------merging two datasets-----------------------#

df1= pd.read_csv("Master.csv", encoding = 'unicode_escape')

df2= pd.read_csv("industry.csv", encoding = 'unicode_escape')

# print(df2.info())

df= pd.merge(df1, df2, on ='Domain')

df = df.drop_duplicates()

# print(df.info())

#-----------Categorising the industries--------------------#

pattern = 'Gaming|Game|games|gaming|Games|gambling|bettingÂ'

# a= (df['type'].str.contains(pattern))

df.loc[df["type"].str.contains(pattern),'Category'] = 1   #----1 for Gaming industry

pattern2 = 'entertainment|Celebrities|adult|Adult|art|Art|astrology|Entertainment|Sports|Anime|cinema|anime|Event|Literature|Magic|Manga|Media|Music|music|media|literature|Streaming|events|event'

df.loc[df["type"].str.contains(pattern2),'Category'] = 2   #----2 for Entertainement industry


pattern3 = 'banking|Banking|blockchain|Credit|Financial|cashback|e-commerce|block|budgeting|financial|trading|payment|payments|loan|wallet|payments'

df.loc[df["type"].str.contains(pattern3),'Category'] = 3   #----3 for Finance industry

pattern4 = 'Energy|Government|Law|law|legal|advocacy|Crowdfunding|charitable|Firearms|Aerospace|Community|Polls|Political|political|Wildlife|community'

df.loc[df["type"].str.contains(pattern4),'Category'] = 4   #----4 for Government industry

pattern5 = 'Health|health|healthcare|Healthcare|family'

df.loc[df["type"].str.contains(pattern5),'Category'] = 5   #----5 for Health industry

pattern6 = 'automotive|Automotive|Car|metals|Engineering|Manufacturing'

df.loc[df["type"].str.contains(pattern6),'Category'] = 6   #----6 for Manufacturing industry

pattern7 = 'estate|delivery|Beauty|Book|Cannabis|toys|Delivery|camping|E-commerce|devices|clothing|Fashion|Food|food|beauty|furnishing|supplies|appliances|ordering|retail|gifts|gore|skincare|auctions|collectibles|accessories|Retail'

df.loc[df["type"].str.contains(pattern7),'Category'] = 7   #----7 for Retail industry

pattern8 = 'Education|education|Childcare|Employment|outsourcing|job|recruitment|Productivity'

df.loc[df["type"].str.contains(pattern8),'Category'] = 8   #----8 for service industry

pattern9 = 'Market|marketing|marketplace|fitness|Fitness|services|cleaning|Interior|surveys|parenting|Parenting|People|search|contact|information|reviews|publishing|Traffic|Transportation|Travel|Matrimonial|Dating|messaing|communication|social|networking|dating|instant|messaging|messaging|advertising'

df.loc[df["type"].str.contains(pattern9),'Category'] = 9   #----9 for Marketing industry


pattern10 = 'Email|design|Design|Photography|file|sharing|technology|commenting|programming|Internet|email|business|Business|Blogging|Chat|Contact|media|PowerPoint|mobile|app|Mobile|app|Technology|technology|Web|cyber|Cybersecurity|intelligence|machine|learning|software|digital|photography|SEO|hosting|authentication|internet|monitoring|hacking|Torrents|sharing|telecommunication'

df.loc[df["type"].str.contains(pattern10),'Category'] = 10   #----10 for technology industry


# df= df.dropna()

df = df.drop(['Domain', 'type'], axis=1)



# df.to_csv(r'C:\Masters\Sem 3\S123 PRT564 DATA ANALYTICS AND VISUALISATION\Assignment\codes\final5.CSV', index=False)

# print(df.info())