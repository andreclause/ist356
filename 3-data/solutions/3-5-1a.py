import streamlit as st  # type: ignore
import pandas as pd

# Streamlit is a third-party module; its implementation is provided by the
# installed Streamlit package rather than by a local class in this file.

exams = pd.read_csv('https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/exam-scores/exam-scores.csv')



st.dataframe(exams)
st.write(list(exams.columns))

st.title("Group by examples")
group1 = exams.groupby(by=['Letter_Grade']).agg({'Letter_Grade': 'count'})
group1 = group1.rename(columns={'Letter_Grade': 'Student_Count'})

st.dataframe(group1)

# group by section and exam version and average the scores
# here are the column names: "Class_Section"
group2 = (
    exams.groupby(by=['Class_Section', 'Exam_Version'])
    .agg({'Student_Score': 'mean', 'Percentage': 'count'})
    .rename(columns={'Student_Score': 'Average_Score', 'Percentage': 'Student_Count'})
)

st.dataframe(group2)

st.title("Pivot Table Examples")

pivot1 = exams.pivot_table(
    index='Class_Section',
    columns='Exam_Version',
    values='Student_Score',
    aggfunc='count',
    fill_value=0,
).reset_index()

st.dataframe(pivot1)

st.title("Melt Example")

melt1 = pivot1.melt(id_vars=['Class_Section'], 
                    var_name='Exam_Version',
                    value_name='Student_Count')

st.dataframe(melt1)