import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt
from PIL import Image
st.title("TATA IPL 2024 AUCTION ANALYSIS")
img= Image.open("C://Users//user//Downloads//iplauctionjpg-1701350288696.jpeg")
st.image(
    img,
    caption="All Sold and Unsold players analysis of TATA IPL 2024",
    width=400,
    channels="RGB"
)
st.audio("C://Users//user//Downloads//Ipl Theme 2024-(PagalSongs.Com.IN).mp3")
st.markdown("Welcome to all the Cricket Lovers!!This is our website where we have analyzed thoruoghly the IPL 2024 Auction and extracted useful insights")
st.write('_Sounds_ :blue[cool] :sunglasses:')
video_file = open('C://Users//user//Downloads//WhatsApp Video 2024-03-29 at 8.46.06 PM.mp4', 'rb')
video_bytes = video_file.read()
st.video(video_bytes)
video_file1=open('C://Users//user//Downloads//WhatsApp Video 2024-03-29 at 8.55.59 PM (1).mp4','rb')
video_bytes1 = video_file1.read()
st.video(video_bytes1)
st.header("IPL 2024 SOLD PLAYERS DATA")
buys = pd.read_csv('C://Users//user//OneDrive//Documents//IPLauction2024//IPL_PLAYERS.csv')
def convert_df(df):
    return df.to_csv().encode('utf-8')

csv = convert_df(buys)
st.download_button(
    label="Download data as CSV",
    data=csv,
    file_name='Players.csv',
    mime='text/csv',
)
#st.dataframe(buys)
#Modifying short names of some teams
buys.loc[buys['TEAM']=='SH','TEAM']='SRH'
buys['TEAM']=buys['TEAM'].replace('PK','PBKS')
buys['TEAM'].unique()
st.table(st.data_editor(
    buys,
    column_config={
        "price": st.column_config.NumberColumn(
            "Price (in USD)",
            help="The price of the product in USD",
            min_value=0,
            max_value=320000000,
            step=1,
            format="$%d",
        )
    },
    hide_index=True,
)
)
chart = alt.Chart(buys).mark_circle().encode(
    x='PLAYERS', y='TEAM', size='PRICE PAID', color='NATIONALITY', tooltip=['PLAYERS','TEAM','PRICE PAID','NATIONALITY'])

st.write(chart)
st.header("EDA of Sold Players")
st.markdown("Types of cricketers Sold: ")
st.write(buys['TYPE'].value_counts())
st.write('Number of players sold to different Teams :',buys['TEAM'].value_counts())
st.markdown("Number of Indian and Overseas cricketers Sold: ")
st.write(buys['NATIONALITY'].value_counts())
st.header("Distribution of the players count depending on the price paid to them")
st.bar_chart(y='PRICE PAID',data=buys)
#Nationality wise player count
plt.figure(figsize=(12,10))
buys['NATIONALITY'].value_counts().plot.pie(autopct="%1.1f%%")
st.title("Nationality wise Players sold")
img= Image.open("C://Users//user//nationality_pie.png")
st.image(img)
#Type wise classification of cricketers
plt.figure(figsize=(12,10))
buys['TYPE'].value_counts().plot.pie(autopct="%1.1f%%")
st.title("Type wise sold Cricketers")
img= Image.open("C://Users//user//type_pie.png")
st.image(img)
custom_colors = ['#FBFF42', 'DarkBlue', 'Black', 'Purple', 'SkyBlue', 'Blue', '#D2042D', 'LightPink', 'Red', '#FF9442']
plt.figure(figsize=(10, 6))
plt.title("Number of Buys by each team")
ax=sns.countplot(x='TEAM',data=buys,palette=custom_colors,edgecolor='black')
for p in ax.patches:
    ax.annotate(format(p.get_height(), '.0f'),
                    (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='center',
                   xytext=(0, 9),
                   textcoords='offset points')
plt.xlabel('Team')
plt.ylabel('Number of Buys')
st.title("Number of buys of each Team")
img= Image.open("C://Users//user//team_pie.png")
st.image(img)
st.header("Highlighting maximum price paid cricketer and overseas cricketers")
st.dataframe(buys[['NATIONALITY','PRICE PAID']].style.highlight_max())
max_price_per_team = buys.groupby('TEAM')['PRICE PAID'].max()
plt.figure(figsize=(10,6))
ax=max_price_per_team.plot(kind='bar',color=custom_colors,edgecolor='black')
for p in ax.patches:
    ax.annotate(format(p.get_height(), '.0f'),
                   (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='center',
                xytext=(0, 9),
                textcoords='offset points')

plt.title("Most Priced Buy of the Team")
plt.xlabel("Team")
plt.ylabel("Price Paid")
st.title("Most Priced buy of the Teams")
img= Image.open("C://Users//user//pricedbuy_bar.png")
st.image(img)
Money_spent_by_each_team=buys.groupby('TEAM')['PRICE PAID'].sum()
st.header("Total Money Spent by each team")
st.table(Money_spent_by_each_team.sort_values(ascending=False))
plt.figure(figsize=(10,6))
ax=Money_spent_by_each_team.plot(kind='bar',color=custom_colors,edgecolor='black')
for p in ax.patches:
    ax.annotate(format(p.get_height(), '.0f'),
                   (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='center',
                   xytext=(0, 9),
                   textcoords='offset points')

plt.title("Total Money Spent by the Team")
plt.xlabel("Team")
plt.ylabel("Total Money Spent")
st.title("Total Money Spent by the Teams")
img= Image.open("C://Users//user//totalmoney_bar.png")
st.image(img)
Highest_Paid_Foriegn_Player=buys[buys['NATIONALITY']=='Overseas'].loc[buys['PRICE PAID'].idxmax()]
st.write("The most expensive overseas player is :",Highest_Paid_Foriegn_Player)
img= Image.open("C://Users//user//Downloads//GJ2TGHYXUAAFZU-.jpg")
st.image(img,
         width=300)
Highest_Paid_Indian_Player=buys.loc[buys[buys['NATIONALITY']=='Indian']['PRICE PAID'].idxmax()]
st.write("The most expensive Indian player is :",Highest_Paid_Indian_Player)
img= Image.open("C://Users//user//Downloads//Harshal-Patel.png")
st.image(img,
         width=300)
Overseas=buys[buys['NATIONALITY']=='Overseas']
st.write("All the sold Overseas players this year :")
st.dataframe(Overseas.sort_values(by='PRICE PAID',ascending=False,ignore_index=True))
plt.figure(figsize=(10, 6))
plt.title("Overseas Classification")
ax=sns.countplot(x='TYPE',data=Overseas,edgecolor='black')
for p in ax.patches:
    ax.annotate(format(p.get_height(), '.0f'),
                   (p.get_x() + p.get_width() / 2., p.get_height()),
                   ha = 'center', va = 'center',
                   xytext = (0, 9),
                   textcoords = 'offset points')
st.title("Overseas players classification")
img= Image.open("C://Users//user//overseas_bar.png")
st.image(img)
Indians=buys[buys['NATIONALITY']=='Indian']
st.write("All the sold Indian players this year :")
st.dataframe(Indians.sort_values(by='PRICE PAID',ascending=False))
plt.figure(figsize=(10, 6))
plt.title("Indians Classification")
ax=sns.countplot(x='TYPE',data=Indians,edgecolor='black')
for p in ax.patches:
    ax.annotate(format(p.get_height(), '.0f'),
                   (p.get_x() + p.get_width() / 2., p.get_height()),
                   ha = 'center', va = 'center',
                   xytext = (0, 9),
                   textcoords = 'offset points')
st.title("Indian players classification")
img= Image.open("C://Users//user//indians_bar.png")
st.image(img)
Highest_Paid_WK=buys.loc[buys[buys['TYPE']=='Wicket-Keeper']['PRICE PAID'].idxmax()]
st.write("Highest Paid wicket-keeper is :",Highest_Paid_WK)
img= Image.open("C://Users//user//Downloads//kushagra_191_77187337_466030091003544_6256216625834057268_n_658199a052839.jpeg")
st.image(img,
         width=300)
Highest_Paid_Batter=buys.loc[buys[buys['TYPE']=='Batter']['PRICE PAID'].idxmax()]
st.write("Highest Paid batter is :",Highest_Paid_Batter)
img= Image.open("C://Users//user//Downloads//images.jpg")
st.image(img,
         width=300)
Highest_Paid_All=buys.loc[buys[buys['TYPE']=='All-Rounder']['PRICE PAID'].idxmax()]
st.write("Highest Paid all rounder is :",Highest_Paid_All)
img= Image.open("C://Users//user//Downloads//BB1kpPRN.jpg")
st.image(img,
         width=300)
Highest_Paid_Bowler=buys.loc[buys[buys['TYPE']=='Bowler']['PRICE PAID'].idxmax()]
st.write("Highest Paid bowler is :",Highest_Paid_Bowler)
img= Image.open("C://Users//user//Downloads//GJ2TGHYXUAAFZU-.jpg")
st.image(img,
         width=300)
st.write("List of all sold batters:")
bat=buys[buys['TYPE']=='Batter']
st.dataframe(bat)
plt.figure(figsize=(10, 6))
plt.title("Batters Classification")
ax=sns.countplot(x='NATIONALITY',data=bat,edgecolor='black')
for p in ax.patches:
    ax.annotate(format(p.get_height(), '.0f'),
                   (p.get_x() + p.get_width() / 2., p.get_height()),
                   ha = 'center', va = 'center',
                   xytext = (0, 9),
                   textcoords = 'offset points')
st.title("Batters Classification")
img= Image.open("C://Users//user//batters.png")
st.image(img)
st.write("List of all sold bowlers:")
bowl=buys[buys['TYPE']=='Bowler']
st.dataframe(bowl)
plt.figure(figsize=(10, 6))
plt.title("Bowlers Classification")
ax=sns.countplot(x='NATIONALITY',data=bowl,edgecolor='black')
for p in ax.patches:
    ax.annotate(format(p.get_height(), '.0f'),
                   (p.get_x() + p.get_width() / 2., p.get_height()),
                   ha = 'center', va = 'center',
                   xytext = (0, 9),
                   textcoords = 'offset points')
st.title("Bowlers Classification")
img= Image.open("C://Users//user//bowlers.png")
st.image(img)
st.write("List of all sold wicket-keepers:")
wk=buys[buys['TYPE']=='Wicket-Keeper']
st.dataframe(wk)
plt.figure(figsize=(10, 6))
plt.title("Keepers Classification")
ax=sns.countplot(x='NATIONALITY',data=wk,edgecolor='black')
for p in ax.patches:
    ax.annotate(format(p.get_height(), '.0f'),
                   (p.get_x() + p.get_width() / 2., p.get_height()),
                   ha = 'center', va = 'center',
                   xytext = (0, 9),
                   textcoords = 'offset points')
st.title("Keepers Classification")
img= Image.open("C://Users//user//keepers.png")
st.image(img)
st.write("List of all sold all rounders:")
AR=buys[buys['TYPE']=='All-Rounder']
st.dataframe(AR)
plt.figure(figsize=(10, 6))
plt.title("All-rounders Classification")
ax=sns.countplot(x='NATIONALITY',data=AR,edgecolor='black')
for p in ax.patches:
    ax.annotate(format(p.get_height(), '.0f'),
                   (p.get_x() + p.get_width() / 2., p.get_height()),
                   ha = 'center', va = 'center',
                   xytext = (0, 9),
                   textcoords = 'offset points')
st.title("All-rounders Classification")
img= Image.open("C://Users//user//AR.png")
st.image(img)
plt.figure(figsize=(10,6))
plt.title("Earnings Based on Nationality")
ax=buys.groupby('NATIONALITY')['PRICE PAID'].sum().plot(kind='bar',edgecolor='black')
for p in ax.patches:
    ax.annotate(format(p.get_height(), '.0f'),
                   (p.get_x() + p.get_width() / 2., p.get_height()),
                   ha = 'center', va = 'center',
                   xytext = (0, 9),
                   textcoords = 'offset points')
plt.xlabel("Nationality")
plt.ylabel("Overall Earnings")
st.title("Earnings Based on Nationality")
img= Image.open("C://Users//user//earning_ntn.png")
st.image(img)
st.title("EDA of Unsold Players")
unsold=pd.read_csv('C://Users//user//OneDrive//Documents//IPLauction2024//UNSOLD_PLAYERS.csv')
st.dataframe(unsold)
plt.figure(figsize=(10, 6))
plt.title("Unsold Players Base Price Classification")
ax=sns.countplot(x='BASE PRICE',data=unsold,edgecolor='black')
for p in ax.patches:
    ax.annotate(format(p.get_height(), '.0f'),
                   (p.get_x() + p.get_width() / 2., p.get_height()),
                   ha = 'center', va = 'center',
                   xytext = (0, 9),
                   textcoords = 'offset points')
st.title("Unsold Players Base Price Classification")
img= Image.open("C://Users//user//unsoldbp.png")
st.image(img)
plt.figure(figsize=(10, 6))
plt.title("Unsold Nationality Classification")
ax=sns.countplot(x='NATIONALITY',data=unsold,edgecolor='black')
for p in ax.patches:
    ax.annotate(format(p.get_height(), '.0f'),
                   (p.get_x() + p.get_width() / 2., p.get_height()),
                   ha = 'center', va = 'center',
                   xytext = (0, 9),
                   textcoords = 'offset points')
st.title("Unsold Nationality Classification")
img= Image.open("C://Users//user//unsoldn.png")
st.image(img)
plt.figure(figsize=(10, 6))
plt.title("Unsold Type Classification")
ax=sns.countplot(x='TYPE',data=unsold,edgecolor='black')
for p in ax.patches:
    ax.annotate(format(p.get_height(), '.0f'),
                   (p.get_x() + p.get_width() / 2., p.get_height()),
                   ha = 'center', va = 'center',
                   xytext = (0, 9),
                   textcoords = 'offset points')
st.title("Unsold Type Classification")
img= Image.open("C://Users//user//unsoldty.png")
st.image(img)
st.write("Unsold players whose base price is 20000000")
st.dataframe(unsold[unsold['BASE PRICE']==20000000])
unsold_bat=unsold[unsold['TYPE']=='Batter']
plt.title("Unsold Batter Classification")
ax=sns.countplot(x='NATIONALITY',data=unsold_bat,edgecolor='black')
for p in ax.patches:
    ax.annotate(format(p.get_height(), '.0f'),
                   (p.get_x() + p.get_width() / 2., p.get_height()),
                   ha = 'center', va = 'center',
                   xytext = (0, 9),
                   textcoords = 'offset points')
st.title("Unsold Batter Classification")
img= Image.open("C://Users//user//unsoldbat.png")
st.image(img)
unsold_bowler=unsold[unsold['TYPE']=='Bowler']
plt.title("Unsold Bowler Classification")
ax=sns.countplot(x='NATIONALITY',data=unsold_bowler,edgecolor='black')
for p in ax.patches:
    ax.annotate(format(p.get_height(), '.0f'),
                   (p.get_x() + p.get_width() / 2., p.get_height()),
                   ha = 'center', va = 'center',
                   xytext = (0, 9),
                   textcoords = 'offset points')
st.title("Unsold Bowler Classification")
img= Image.open("C://Users//user//unsoldbowl.png")
st.image(img)


