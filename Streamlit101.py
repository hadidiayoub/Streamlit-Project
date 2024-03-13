import streamlit as st
import pandas as pd


st.title("This is a title")
st.header("This is a header")
st.subheader("This is a subheader")
st.text("This is a text")
st.write("Hello World")
st.markdown("this is a **bold** *Markdown*")
st.markdown("[link to google](https://www.google.com)")
# https://www.markdownguide.org/cheat-sheet/

df = pd.DataFrame({"Column 1": [1, 2, 3, 4, 5, 6, 7], "Column 2": [10, 20, 30, 40, 50, 60, 70]})
st.table(df)


col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")

x = st.text_input("Favourite movie")
st.checkbox("checkbox", value="True")


st.write(f"Your favorite movie is: {x}")
is_clicked = st.button("click Me")
if is_clicked == True :
    st.write("hello world") 

import numpy as np

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