import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import altair as alt



df=pd.read_csv('Book3.csv')

col_names=['ISO Code','Countries and areas','Continent','Year','School age population (thousands)','% urban', '% pre-primary', '% primary','% secondary', 'NATIONAL Basic water service','NATIONAL Limited water service', 'NATIONAL No water service',
           'URBAN Basic water service','URBAN Limited water service', 'URBAN No water service',
          'RURAL Basic water service','RURAL Limited water service', 'RURAL No water service',
          'PRE-PRIMARY Basic water service','PRE-PRIMARY Limited water service', 'PRE-PRIMARY No water service',
          'PRIMARY Basic water service','PRIMARY Limited water service', 'PRIMARY No water service',
          'SECONDARY Basic water service','SECONDARY Limited water service', 'SECONDARY No water service',
          'NATIONAL Basic sanitation service','NATIONAL Limited sanitation service', 'NATIONAL No sanitation service',
          'URBAN Basic sanitation service','URBAN Limited sanitation service', 'URBAN No sanitation service',
          'RURAL Basic sanitation service','RURAL Limited sanitation service', 'RURAL No sanitation service',
          'PRE-PRIMARY Basic sanitation service','PRE-PRIMARY Limited sanitation service', 'PRE-PRIMARY No sanitation service',
          'PRIMARY Basic sanitation service','PRIMARY Limited sanitation service', 'PRIMARY No sanitation service',
          'SECONDARY Basic sanitation service','SECONDARY Limited sanitation service', 'SECONDARY No sanitation service',
          'NATIONAL Basic hygine service','NATIONAL Limited hygine service', 'NATIONAL No hygine service',
          'URBAN Basic hygine service','URBAN Limited hygine service', 'URBAN No hygine service',
          'RURAL Basic hygine service','RURAL Limited hygine service', 'RURAL No hygine service',
          'PRE-PRIMARY Basic hygine service','PRE-PRIMARY Limited hygine service', 'PRE-PRIMARY No hygine service',
          'PRIMARY Basic hygine service','PRIMARY Limited hygine service', 'PRIMARY No hygine service',
          'SECONDARY Basic hygine service','SECONDARY Limited hygine service', 'SECONDARY No hygine service']

df_temp = pd.read_csv('Book3.csv',index_col=0,names=col_names)

df_temp = df_temp.fillna(0) # to fill the NAN values as 0

df_temp["% urban"] = df_temp ["% urban"].astype(int)
df_temp["Year"] = df_temp ["Year"].astype(int)
df_temp["School age population (thousands)"] = df_temp ["School age population (thousands)"].astype(int)
df_temp["% pre-primary"] = df_temp ["% pre-primary"].astype(int)
df_temp["% primary"] = df_temp ["% primary"].astype(int)
df_temp["% secondary"] = df_temp ["% secondary"].astype(int)
@st.cache
def load_data():
    df_temp = pd.read_csv('Book3.csv',index_col=0,names=col_names)
    return df_temp

df_temp = load_data()

st.title('Clean Water')

if st.sidebar.checkbox('Show Dataframe'):
    st.write(df_temp)

if st.sidebar.checkbox('Bar Graph of % Pre-primary to Countries/Areas'):
    c = alt.Chart(df_temp).mark_bar().encode(
        x='Countries and areas', y='% pre-primary')
    st.altair_chart(c)

if st.sidebar.checkbox('Bar Graph of % Primary to Countries/Areas'):
    c = alt.Chart(df_temp).mark_bar().encode(
        x='Countries and areas', y='% primary')
    st.altair_chart(c)

if st.sidebar.checkbox('Bar Graph of % Secondary to Countries/Areas'):
    c = alt.Chart(df_temp).mark_bar().encode(
        x='Countries and areas', y='% secondary')
    st.altair_chart(c)

if st.sidebar.checkbox('Bar Graph of % Urban to Countries/Areas'):
    c = alt.Chart(df_temp).mark_bar().encode(
        x='Countries and areas', y='% urban')
    st.altair_chart(c)

if st.sidebar.checkbox('Mean of each continent'):
    g = df_temp.groupby("Continent")['% primary'].mean()
    st.write(g)

if st.sidebar.checkbox('Mean Continent by % Primary'):
    g = df_temp.groupby("Continent")['% primary'].mean()
    c = st.bar_chart(g)

#if st.sidebar.checkbox('Bottom 20 Countries/Areas'):
   # l = df_temp.groupby("Continent")['% primary'].min()
