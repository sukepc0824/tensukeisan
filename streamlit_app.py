import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px

subjects = ['Japanese', 'Math', 'English', 'Science', 'Social']

subjects_labels = ['国語', '数学', '英語', '理科', '社会']
scores = []

def main():
    st.title('成績分析')
    subjects = st.columns(5)

    for i, subject in enumerate(subjects):
        with subject:
            score = st.number_input(
                f'{subjects_labels[i]}', min_value=0, max_value=100, value=0, on_change=draw())
            scores.append(score)


def draw():
    data_flame = pd.DataFrame({
        '教科': subjects,
        '点数': scores
    })

    col1,col2,col3 =  st.columns(3)
    with col1:
        st.metric(label="平均点",value=np.average(data_flame['点数'].tolist()))
    with col2:
        st.metric(label="最高点",value=np.amax(data_flame['点数'].tolist()))
    with col3:
        st.metric(label="最低点",value=np.amin(data_flame['点数'].tolist()))

    fig = px.bar(data_flame, x='教科', y='点数', barmode='group')
    st.plotly_chart(fig)

    fig = px.line_polar(data_flame, r='点数', theta='教科',line_close=True)
    st.plotly_chart(fig)

main()
