# Imported Libraries
import pickle
import streamlit as st
import numpy as np


st.title("Gymnastics Final Score App")

with open("model.pkl", "rb") as f:
    lr_model = pickle.load(f)

sl = st.number_input("Floor Exercice")
sw = st.number_input("Pomel Horse")
pl = st.number_input("Romen Rings")
pw = st.number_input("Vaulting Table")
sl = st.number_input("Parellel Bar")
sw = st.number_input("High Bar")

if st.button("Final Score"):
    pred = lr_model.predict(np.array([[sl, sw, pl, pw, sl, sw]]))
    st.write("The Final Score is :", pred[0])

# pip install streamlit numpy scikit-learn
# python -m streamlit run main.py
