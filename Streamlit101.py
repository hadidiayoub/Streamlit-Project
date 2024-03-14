import streamlit as st
import pandas as pd
import numpy as np
import time as ts
from datetime import time

st.title("This is a title")
st.header("This is a header")
st.subheader("This is a subheader")
st.text("This is a text")
st.write("Hello World")
st.markdown("this is a **bold** *Markdown*")
st.markdown("[link to google](https://www.google.com)")
# https://www.markdownguide.org/cheat-sheet/
st.divider()



df = pd.DataFrame({"Column 1": [1, 2, 3, 4, 5, 6, 7], "Column 2": [10, 20, 30, 40, 50, 60, 70]})
st.table(df)
st.divider()


col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")
st.divider()



#this is an input
x = st.text_input("Your name")
st.write(f"Your name is: {x}")
st.divider()




#this is checkbox with some js interactivity
def change():
    print(st.session_state.checker)
state = st.checkbox("checkbox", value="True",on_change=change,key='checker')
if state ==True and x:
    st.write("Hello",x)
st.divider()



#this is radio button
radio_btn = st.radio("What's your favorite movie genre",options=("Comedy", "Drama", "Documentary"))
 #print(radio_btn)
st.divider()



#this is a button with a function
def btn_click():
    print("Button clicked")
btn=st.button("Click Me!", on_click=btn_click)

if btn == True :
    st.write("hello world") 
st.divider()


#selectbox and select boxes
select=st.selectbox("What is your favourite car ?", options=("Audi","BMW","Mercedes"))
#print(select)

multi_select=st.multiselect("What is your favourite Tech brand?",options=("Microsoft","Apple","Amazon","Oracle"))
st.write(multi_select)

st.divider()


#This is a file uploader
image = st.file_uploader("Please upload an Image", type=["png","jpg"])
if image is not None:
    st.image(image) #diplay an image
    #st.video(video) #display a video

st.divider()

#those are different inputs
st.slider("This is a slider", min_value=50, max_value=150, value=70)
x = st.text_input("Your name", max_chars=11)
y = st.text_area("short description")
date=st.date_input("Your Birthday")
time=st.time_input("set your time zone")
st.divider()

#function for progress bar on time
'''
def converter(value):
    m,s,mm=value.split(":")
    t_s=int(m)*60+int(mm)/1000
    return t_s

val=st.time_input("set Timer", value=time(0,0,0))
if str(val) == "00:00:00":
    st.write("Please sent timer")
else:
    sec=converter(str(val))
    print(sec)
    bar=st.progress(0)
    per=sec/100
    for i in range(10):
        bar.progress((i+1)*10)
        ts.sleep(per)
'''

#this is a User Registration form
st.markdown("<h1>User Registration</h1>",unsafe_allow_html=True)
with st.form("Form 2", clear_on_submit=True):
    col1,col2=st.columns(2)
    f_name=col1.text_input("First Name")
    l_name=col2.text_input("Last Name")
    st.text_input("Email Address")
    st.text_input("Password")
    st.text_input("Confirm Password")
    day,month,year=st.columns(3)
    day.text_input("Day")
    month.text_input("Month")
    year.text_input("Year")
    s_state=st.form_submit_button("Register")
    if s_state:
        if f_name == "" and l_name=="":
            st.warning("Please Fill above fields")
        else:
            st.success("Submitted Successfully")




st.divider()
dataframe = np.random.randn(10, 20)
st.dataframe(dataframe)

st.write("*Streamlit* is **really** ***cool***.")

st.markdown('''
    :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
    :gray[pretty] :rainbow[colors].''')

st.title("AYOUB HADIDI")
st.header("THIS IS HEADEAR")
st.code("a=1234",language="python", line_numbers=True)
st.divider()
st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')

