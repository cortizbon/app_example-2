import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

X = np.random.normal(0, 1, 1000)
Y = np.random.normal(10, 1, 1000)

st.title("Aplicación en clase")


         
fig, ax = plt.subplots(1, 2, sharex=True)

ax[0].hist(X, bins=50)
ax[1].hist(Y, bins=50)
