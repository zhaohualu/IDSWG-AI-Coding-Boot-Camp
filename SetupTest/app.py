# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
import numpy as np
st.title("My First Streamlit App")
st.write("Welcome to Streamlit!")
# Generate random data
data = pd.DataFrame(np.random.randn(10, 2), columns=['Column A', 'Column B'])
st.line_chart(data)

