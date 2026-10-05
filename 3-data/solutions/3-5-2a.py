import streamlit as st # pyright: ignore[reportMissingImports]
import pandas as pd


exams = pd. read_svhttps://raw.githubusercontent.com/maudge/datasets/refs/heads/master/exam

st. title("Exam Scores Pivot Table Example")

row = st. selectbox "Select Row", options=list (exams. columns))
col = st. selectbox "Select Column", options=list(exams. columns))
measure = st.selectbox "Select Measure"
, options=list(exams. columns))
aggregate = st.selectbox "Select Aggregate", options=["mean", "sum", "count" 1)

pivot1 = exams.pivot_table index-row, columns=col,
values=measure, aggfunc=aggregate)

st. dataframe(pivot1)