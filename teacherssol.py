import streamlit as st
from nltk.sentiment import SentimentIntensityAnalyzer
import glob
import plotly.express as px

filepaths = sorted(glob.glob("diary/*txt"))

analyzer = SentimentIntensityAnalyzer()

negativity = []
positivity = []
for filepath in filepaths:
    with open(filepath) as file:
        content = file.read()
    scores = analyzer.polarity_scores(content)
    positivity.append(scores["pos"])
    negativity.append(scores["neg"])

dates = [name.strip(".txt").strip("diary").strip("[\]") for name in filepaths]
print(dates)

st.title("Diary Tone")
st.subheader("Positivity")
pos_figure = px.line(x=dates, y=positivity,
                     labels={"x": "Date", "y": "Positivity"})
st.plotly_chart(pos_figure)

st.subheader("Negativity")
neg_figure = px.line(x=dates, y=negativity,
                     labels={"x": "Dates", "y": "Negativity"})
st.plotly_chart(neg_figure)