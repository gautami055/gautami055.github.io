import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# App title
st.title("📊 Simple Data Dashboard")

# Sidebar
st.sidebar.header("Controls")
num_points = st.sidebar.slider("Number of data points", 10, 100, 50)
chart_type = st.sidebar.selectbox("Chart Type", ["Line", "Bar", "Scatter"])

# Main content
st.header("Welcome to My Streamlit App!")
st.write("This is a simple example of a Streamlit application.")

# Generate sample data
@st.cache_data
def generate_data(n):
    dates = pd.date_range('2024-01-01', periods=n, freq='D')
    values = np.cumsum(np.random.randn(n)) + 100
    return pd.DataFrame({'Date': dates, 'Value': values})

# Create and display data
df = generate_data(num_points)

st.subheader("Sample Data")
st.write(f"Showing {len(df)} data points:")

# Display chart based on selection
if chart_type == "Line":
    fig = px.line(df, x='Date', y='Value', title='Time Series Data')
elif chart_type == "Bar":
    fig = px.bar(df.tail(10), x='Date', y='Value', title='Last 10 Days')
else:  # Scatter
    fig = px.scatter(df, x='Date', y='Value', title='Scatter Plot')

st.plotly_chart(fig, use_container_width=True)

# Display raw data
if st.checkbox("Show raw data"):
    st.subheader("Raw Data")
    st.dataframe(df)

# User input
st.subheader("User Input")
user_name = st.text_input("Enter your name:")
if user_name:
    st.write(f"Hello, {user_name}! 👋")

# Metrics
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Average Value", f"{df['Value'].mean():.2f}")
with col2:
    st.metric("Max Value", f"{df['Value'].max():.2f}")
with col3:
    st.metric("Min Value", f"{df['Value'].min():.2f}")

# Footer
st.markdown("---")
st.markdown("Built with ❤️ using Streamlit")