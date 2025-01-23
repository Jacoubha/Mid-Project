
import pandas as pd
import streamlit as st
from sklearn.impute import KNNImputer
import plotly.express as px
from datasist.structdata import detect_outliers

st.set_page_config(
    layout='wide',
    page_title='Youtube',
    page_icon= '🪙'
)


# read needed csv files
df         = pd.read_csv("Global YouTube Statistics_2.csv",encoding="utf-8",encoding_errors="ignore")
df_normal  = pd.read_csv("Global YouTube Statistics Normal.csv",encoding="utf-8",encoding_errors="ignore")
df_outlier = pd.read_csv("Global YouTube Statistics Outlier.csv",encoding="utf-8",encoding_errors="ignore")

st.title("Youtube Statistics Data")

tabs=st.tabs(['Total' , "Normal" ,"Extraordinary", "Conclusion"])




with tabs[0]:
    # header
    st.header("Youtube map")
    # making dataframe for country counts
    country_counts = df['country'].value_counts().reset_index()
    # making world map figure 
    fig=px.choropleth(country_counts, locations="country",color="count", hover_name="country",
                  locationmode='country names',labels={'count': 'Value Count'})
    st.plotly_chart(fig,use_container_width=True)
    
    # header
    st.header("Youtube Channels count")
    count = df.groupby('channel_type')["youtuber"].count()
    # draw figure 
    fig=px.bar(count,color_discrete_sequence=px.colors.qualitative.Vivid)
    # Persent figure 
    st.plotly_chart(fig,use_container_width=True)
    
    # header
    st.header("Top 100 Youtube Channels")
    # top 100 channels in views 
    top_100= df[df['video_views_rank'] <= 100 ]['channel_type']
    fig=px.histogram(top_100 ,y = 'channel_type' )
    # Persent figure 
    st.plotly_chart(fig,use_container_width=True)
    
    # header
    st.header("Categorical")
    # top 100 channels in views 
    cat= px.sunburst(df,path=['category', 'channel_type'])
    # Persent figure 
    st.plotly_chart(cat,use_container_width=True)
    



with tabs[1]:
    # header
    st.header("Subscribers vs Video Views ")
    # draw figure 
    fig=px.scatter(df_normal, x='subscribers',y="video_views" ,color_discrete_sequence=px.colors.qualitative.Bold_r,)
    # Persent figure 
    st.plotly_chart(fig,use_container_width=True,)
    
    # header
    st.header("Percentage OF Genere")
    # draw figure 
    fig=px.pie(df_normal,names='channel_type' ,color_discrete_sequence=px.colors.qualitative.Bold_r)
    # Persent figure 
    st.plotly_chart(fig,use_container_width=True)

    # header
    st.header("Count of Genere")
    # sum of youtube channels according to money made 
    count = df_normal.groupby('channel_type')["youtuber"].count()
    # bar fighure 
    fig=px.line(count,color_discrete_sequence=px.colors.qualitative.Vivid)
    # Persent figure 
    st.plotly_chart(fig,use_container_width=True)

    
    # header
    st.header("Total Money Making")
    # sum of youtube channels according to money made 
    count = df_normal.groupby('channel_type')["estimate_money"].sum()
    # bar fighure 
    fig=px.bar(count,color_discrete_sequence=px.colors.qualitative.Dark2)
    # Persent figure 
    st.plotly_chart(fig,use_container_width=True)
    
    # header
    st.header("Money paid To genere for 1000 Views")    
    # making dataframe with channel_type and corresponding video_views mean 
    genere = (df_normal.groupby('channel_type')["money_per_1000_views"].mean())
    genere = genere.drop(['Nonprofit','Autos',"Sports",'News'],axis=0).reset_index()
    #draw figure
    fig=px.funnel(genere,x='channel_type',y='money_per_1000_views',color_discrete_sequence=px.colors.qualitative.Bold)
    # Persent figure 
    st.plotly_chart(fig,use_container_width=True)


with tabs[2]: 
    # header
    st.header("Subscribers vs Video Views ")
    # draw figure 
    fig=px.scatter(df_outlier, x='subscribers',y="video_views" ,color_discrete_sequence=px.colors.qualitative.Bold_r)
    # Persent figure 
    st.plotly_chart(fig,use_container_width=True)
    
    # header
    st.header("Percentage OF Genere")
    # draw figure 
    fig=px.pie(df_outlier,names='channel_type' ,color_discrete_sequence=px.colors.qualitative.Bold_r)
    # Persent figure 
    st.plotly_chart(fig,use_container_width=True)

    # header
    st.header("Count of Genere")
    # sum of youtube channels according to money made 
    count = df_outlier.groupby('channel_type')["youtuber"].count()
    # bar fighure 
    fig=px.bar(count,color_discrete_sequence=px.colors.qualitative.Vivid)
    # Persent figure 
    st.plotly_chart(fig,use_container_width=True)
    
    # header
    st.header("Total Money Making")
    # sum of youtube channels according to money made 
    count = df_outlier.groupby('channel_type')["estimate_money"].sum()
    # bar fighure 
    fig=px.bar(count,color_discrete_sequence=px.colors.qualitative.Dark2)
    # Persent figure 
    st.plotly_chart(fig,use_container_width=True)
    
    # header
    st.header("Money paid To genere for 1000 Views")        
    # making dataframe with channel_type and corresponding video_views mean 
    genere = (df_outlier.groupby('channel_type')["money_per_1000_views"].mean())
    genere = genere.drop(['Nonprofit','Autos',"Sports",'News'],axis=0).reset_index()
    #draw figure
    fig=px.funnel(genere,x='channel_type',y='money_per_1000_views',color_discrete_sequence=px.colors.qualitative.Bold)
    # Persent figure 
    st.plotly_chart(fig,use_container_width=True)
    

with tabs[3]:
    # header
    st.header("Conclusion")    
    # page content 
    col1, col2, col3 = st.columns([5,5,5])
    
    with col1:
        st.subheader("Normal Youtube Channels")
        st.caption(
            """
            1. Entertainment has higher number of channels 
            2. Music has the higher number of views
            3. Most payed genere is Tech followed by film for 1000 Views
            """
        )

    
    with col2:
        st.subheader("general")
        st.caption(
            """
            1. Number of uploads dosn't effect Views
            2. Entertainment and Music is the most Popluer Genere in Youtube
            3. Increse in number of subscribers dose increase views

            """
        )

    with col3:
        st.subheader("Extraordinary Youtube Channels")
        st.caption(
            """
            1. Entertainment has higher number of channels 
            2. Entertainment has the higher number of views
            3. Most payed genere is Education for 1000 Views
            4. Exsseive No.OF video Uploads limit number of views
            """
        )
    

        

