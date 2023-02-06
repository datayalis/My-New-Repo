import streamlit as st
import pandas as pd
import plotly_express as px

import streamlit as st

st.header('Final Web Application')
st.header('Created using [_python_] virtual environments :sunglasses:')

df=pd.read_csv('vehicles_us.csv')
df['manufacturer']=df['model'].apply(lambda x:
x.split()[0])

# create a text header above the dataframe
st.header('Data viewer') 
# display the dataframe with streamlit
st.dataframe(df)

#vehicle types by manuf, to see distrib of veh types
st.header('Vehicle types by manufacturer')
# create a plotly histogram figure
fig = px.histogram(df, x='manufacturer', color='type')
# display the figure with streamlit
st.write(fig)

st.header('Price Range of Vehicles Per Type')
#creating a scatterplot
fig2 = px.scatter(df, x='type', y='price')
#displaying the scatterplot
st.write(fig2)

#histogram of cond vs model yr
st.header('Histogram of `manufacturer` vs `cylinders`')
fig = px.histogram(df, x='manufacturer', color='cylinders')
st.write(fig)

#histogram of odometer
st.header('Histogram of `color`')
fig = px.histogram(df, x='paint_color', color='manufacturer')
st.write(fig)

#compare price distrib btwn manuf
st.header('Compare days listed between manufacturers')
# get a list of car manufacturers
manufac_list = sorted(df['manufacturer'].unique())
# get user's inputs from a dropdown menu
manufacturer_1 = st.selectbox(
                              label='Select manufacturer 1', # title of the select box
                              options=manufac_list, # options listed in the select box
                              index=manufac_list.index('chevrolet') # default pre-selected option
                              )
# repeat for the second dropdown menu
manufacturer_2 = st.selectbox(
                              label='Select manufacturer 2',
                              options=manufac_list, 
                              index=manufac_list.index('hyundai')
                              )
# filter the dataframe 
mask_filter = (df['manufacturer'] == manufacturer_1) | (df['manufacturer'] == manufacturer_2)
df_filtered = df[mask_filter]

# add a checkbox if a user wants to normalize the histogram
normalize = st.checkbox('Normalize histogram', value=False)
if normalize:
    histnorm = 'percent'
else:
    histnorm = None

# create a plotly histogram figure
fig = px.histogram(df_filtered,
                      x='days_listed',
                      nbins=30,
                      color='manufacturer',
                      histnorm=histnorm,
                      barmode='overlay')
# display the figure with streamlit
st.write(fig)
