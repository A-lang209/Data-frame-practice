import pandas as pd
df = pd.read_csv('words.csv', index_col='Word')
df.head()

##### How many elements does this dataframe have?
df.info() #Result = 172821 

##### What is the value of the word `microspectrophotometries`?
#df.loc["microspectrophotometries"]
df.loc["microspectrophotometries", "Value"] #Result = 317

##### What is the highest possible value of a word?
df["Value"].max() #Result = 172821.000000
#df.max()
#df.describe()

##### Which of the following words have a Char Count of `15`?
df.loc[[
    "pinfish",
    "microbrew",
    "superheterodyne",
    "enfold",
    "glowing"
], "Value"] #Result = superheterodyne

##### What is the highest possible length of a word?
df.describe() #Result = 28

##### What is the word with the value of `319`?
#df.sort_values(by=["Value"], ascending=False)
df.loc[df["Value"]==319] #Result = reinstitutionalizations

##### What is the most common value?
#df["Value"].describe()
#df["Value"].mode()
df["Value"].value_counts() #Result = 93

##### What is the shortest word with value `274`?
df.loc[df["Value"] == 274].sort_values(by="Char Count") #Result = overprotectivenesses

##### Create a column `Ratio` which represents the 'Value Ratio' of a word
df["Ratio"] = df["Value"]/df["Char Count"]
df.head()

##### What is the maximum value of `Ratio`?
df["Ratio"].max() #Result = 22.5

##### What word is the one with the highest `Ratio`?
df.sort_values(by="Ratio", ascending=False) #Result = xu
#df.loc[df["Ratio"]==df["Ratio"].max()]

##### How many words have a `Ratio` of `10`?
#df["Ratio"].value_counts()
#df.loc[df["Ratio"]==10].shape
df.query("Ratio == 10").shape #Result = 2604

##### What is the maximum `Value` of all the words with a `Ratio` of `10`?
#df.query("Ratio == 10").sort_values(by="Value", ascending=False).head()
df.loc[df["Ratio"]==10, "Value"].max() #Result = 240

##### Of those words with a `Value` of `260`, what is the lowest `Char Count` found?
df.query("Value == 260").sort_values(by="Char Count", ascending=True) #Result = 17

##### Based on the previous task, what word is it?
#Result = hydroxytryptamine






