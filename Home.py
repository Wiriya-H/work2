import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

st.header("Wiriya")
st.image("./pic/profile.jpg") 
st.balloons()

html_8 = """
<div style="background-color:#6BD5DA;padding:15px;border-radius:15px 15px 15px 15px;border-style:'solid';border-color:black">
<center><h5>การทำนายข้อมูลดอกไม้</h5></center>
</div>
<div>
<h1>Hello</h1>
</div>
"""

st.markdown(html_8, unsafe_allow_html=True)
st.markdown("")

dt=pd.read_excel("./data/NewData.xlsx")

st.write(dt.head(10))

dt1 = dt['L-CORE'].sum()
dt2 = dt['L-SURF'].sum()
dt3 = dt['L-O2'].sum()
dt4 = dt['L-BP'].sum()

dx = [dt1, dt2, dt3, dt4]
dx2 = pd.DataFrame(dx, index=["d1", "d2", "d3", "d4"])

if st.button("แสดงการจินตทัศน์ข้อมูล"):
   st.write(dt.head(10))
   st.bar_chart(dx2)
   st.button("ไม่แสดงข้อมูล")
else:
    st.write("ไม่แสดงข้อมูล")

html_8 = """
<div style="background-color:#FF5733;padding:15px;border-radius:15px 15px 15px 15px;border-style:'solid';border-color:black">
<center><h5>ส่วนของการทำนายข้อมูล</h5></center>
</div>
"""

st.markdown(html_8, unsafe_allow_html=True)
st.markdown("")

pt_len=st.slider("กรุณาเลือกข้อมูล L-CORE")
pt_wd=st.slider("กรุณาเลือกข้อมูล L-SURF")
sp_len=st.number_input("กรุณาเลือกข้อมูล L-O2")
sp_wd=st.number_input("กรุณาเลือกข้อมูล L-BP")

if st.button("ทำนายผล"):
   st.markdown("ใส่โมเดล")
   st.button("ไม่แสดงข้อมูล")
else:
    st.write("ไม่แสดงข้อมูล")