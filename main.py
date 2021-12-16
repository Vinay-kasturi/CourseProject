import pandas
import matplotlib.pyplot as plt
import numpy as np
fig, ax = plt.subplots()
df = pandas.read_excel("AircraftEventsDetail151221.xlsx")

#Dataframe characteristics used for cleaning data
#print(df.info())
#print(df.shape)
#print(df.isna().sum())

#Dataframe cleaning
cleaned_df=df[['Event Type','Aircraft Type','New Operator','New Manager','New Owner','New Engine Type','New Operator Country','Delivery Date']]
#print(cleaned_df.shape)
print(cleaned_df.info())
print(cleaned_df)

#Dataframe indexing and slicing
cleaned_indexed_df = cleaned_df.set_index("Event Type")
cleaned_indexed_df = cleaned_indexed_df.drop(["Finance","Lease End/Expiry","Deferred From","Sale & Lease-back","Transfer","Lease Start","Orders","Conversions (Non Freight)","Merger","LoI to Order","Cancellation","Deferral (Announced)","On Option","LoI to Option"])

#Dataframe sorting
Cleaned_sorted_df = cleaned_indexed_df.sort_values("Delivery Date")
print(cleaned_indexed_df.info())

#Analysing the Aircraft model type - A321 or A320 type
X=Cleaned_sorted_df["Aircraft Type"].tolist()
A = ["A320","A321"]
N = [0,0]

for i in X:
   if i == A[0]:
       N[0] = N[0]+1
   else:
    N[1] = N[1]+1
print(N[0])
print(N[1])

#ax.bar(A,N)

#Analysing the Engine type - PW1100 or LEAP type
X1=Cleaned_sorted_df["New Engine Type"].tolist()
E = ["LEAP","PW1000G","Unannounced"]
N1 = [0,0,0]

for i in X1:
   if i == E[0]:
       N1[0] = N1[0]+1
   elif i == E[1]:
       N1[1] = N1[1]+1
   else:
    N1[2] = N1[2]+1
print(N1[0])
print(N1[1])
print(N1[2])
ax.bar(E,N1)
plt.show()