import streamlit as st
import pandas as pd

st.title("This is my streamlit app")

st.header("This is a Header")
st.subheader("This is a Subheader")
st.text("This is simple text")

st.markdown("""
**Bold text**, *italic text*, ***bold and italic***

- Bullet point 1
- Bullet point 2

1. Numbered list
2. Second item

[Link text](https://example.com)

`inline code`
""")


st.write("Text, dataframes, objects, etc.")
st.write("Multiple", "arguments", 123)
st.write({"key": "value"})


st.code("""
def hello_world():
    print("Hello, Streamlit!")
    return True
""", language="python")

st.html("""
<div style="background: linear-gradient(to right, #ff6b6b, #4ecdc4); 
            padding: 20px; border-radius: 10px;">
    <h2>Custom HTML Content</h2>
</div>
""")

st.latex(r"\int_a^b f(x)dx = F(b) - F(a)")

st.caption("This is a caption - smaller, lighter text")

st.divider()

# Data Display

#DataFrame (Interactive)
import pandas as pd

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['NYC', 'London', 'Paris']
})

st.dataframe(df)
#use_container_width=True

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['NYC', 'London', 'Paris']
})

st.dataframe(df,use_container_width=True)

st.dataframe(
    df.style.highlight_max(axis=0, subset=['Age']),
    use_container_width=True
)

st.table(df)

st.metric(
    label="Temperature",
    value="70 °F",
    delta="1.2 °F",
    delta_color="normal"  # "normal", "inverse", "off"
)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Metric 1", "100", "+10%")

with col2:
    st.metric("Metric 2", "200", "-5%")

with col3:
    st.metric("Metric 3", "300", "+15%")


sample_json = {
    "name": "Streamlit",
    "version": "1.0",
    "features": ["interactive", "fast"]
}

st.json(sample_json)

edited_df = st.data_editor(
    df,
    num_rows="dynamic",  # "fixed" or "dynamic"
    use_container_width=True,
    hide_index=False
)


#Charts & Visualizations

import numpy as np


chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['A', 'B', 'C']
)

st.line_chart(chart_data)

st.area_chart(chart_data)

st.bar_chart(chart_data)

scatter_data = pd.DataFrame({
    'x': np.random.randn(100),
    'y': np.random.randn(100),
    'size': np.random.randint(10, 100, 100),
    'color': np.random.choice(['A', 'B', 'C'], 100)
})

st.scatter_chart(
    scatter_data,
    x='x',
    y='y',
    size='size',
    color='color'
)

map_data = pd.DataFrame({
    'lat': [37.76, 37.77, 37.78],
    'lon': [-122.4, -122.41, -122.42],
    'size': [100, 200, 150]
})

st.map(map_data, size='size')

import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.hist(np.random.randn(1000), bins=30)
ax.set_title("Histogram")

st.pyplot(fig)

import plotly.express as px
import plotly.graph_objects as go

# Simple Plotly Express
# df = pd.DataFrame({
#     'x': range(10),
#     'y': np.random.randn(10).cumsum()s
# })

# fig = px.line(df, x='x', y='y', title='Interactive Chart')
# st.plotly_chart(fig, use_container_width=True)

# # Plotly Graph Objects
# fig = go.Figure(data=[go.Bar(x=[1, 2, 3], y=[4, 5, 6])])
# st.plotly_chart(fig)


# Input Widgets

if st.button("Click Me!", type="primary"):  # type: "primary" or "secondary"
    st.write("Button clicked!")

if st.button("Click Me!", type="secondary"):  # type: "primary" or "secondary"
    st.write("Button clicked!")   

csv_data = "Name,Age\nAlice,25\nBob,30"

st.download_button(
    label="Download CSV",
    data=csv_data,
    file_name="data.csv",
    mime="text/csv"
)


st.link_button("Go to Streamlit", "https://streamlit.io")

agree = st.checkbox("I agree to the terms")

if agree:
    st.write("Thank you!")


genre = st.radio(
    "Choose your favorite genre:",
    ["Comedy", "Drama", "Documentary"],
    horizontal=True  # Display horizontally
)

st.write(f"You selected: {genre}")

genre = st.radio(
    "Choose your favorite genre:",
    ["Comedy", "Drama", "Documentary"],
      # Display horizontally
)

st.write(f"You selected: {genre}")


option = st.selectbox(
    "Choose a color:",
    ["Red", "Green", "Blue", "Yellow"],
    index=0  # Default selection
)

options = st.multiselect(
    "Choose your favorite fruits:",
    ["Apple", "Banana", "Cherry", "Date"],
    default=["Apple"]  # Pre-selected options
)

# Simple slider
age = st.slider("Select your age:", 0, 100,25)

# Range slider
values = st.slider(
    "Select a range:",
    0.0, 100.0, (25.0, 75.0)
)

# Step slider
temp = st.slider("Temperature", -10, 40, 25, step=2)

size = st.select_slider(
    "Select size:",
    options=["XS", "S", "M", "L", "XL", "XXL"],
    value="M"
)

name = st.text_input("Enter your name: ")

name = st.text_input(
    "Enter your name:",
    value="",  # Default value
    max_chars=50,  # Character limit
    placeholder="John Doe",
    type="password"  # "default" or "password"
)

message = st.text_area(
    "Enter your message:",
    height=100,
    max_chars=500,
    placeholder="Type here..."
)

number = st.number_input(
    "Enter a number:",
    min_value=0,
    max_value=100,
    value=50,
    step=1
)

from datetime import date

selected_date = st.date_input(
    "Select a date:",
    value=date.today(),
    min_value=date(2020, 1, 1),
    max_value=date(2025, 12, 31)
)


from datetime import time

selected_time = st.time_input(
    "Select a time:",
    value=time(8, 45)
)


uploaded_file = st.file_uploader(
    "Choose a file:",
    type=['csv', 'txt', 'pdf'],
    accept_multiple_files=False
)

uploaded_files = st.file_uploader(
    "Choose files:",
    accept_multiple_files=True
)


picture = st.camera_input("Take a picture")

if picture:
    st.image(picture)

color = st.color_picker("Pick a color:", "#00f900")
st.write(f"Selected color: {color}")


# From URL
st.image(
    "https://www.guvi.in/assets/CPYoUJqK-guvilogo-hcl.webp",
    caption="Image caption",
)

# From local file
st.image("C:\\Users\\Digital Suppliers\\Downloads\\Copilot_20250612_134627.png")

# Multiple images
# st.image(["img1.jpg", "img2.jpg", "img3.jpg"])


# From URL
st.audio("https://example.com/audio.mp3")

# From local file
# audio_file = open("audio.mp3", "rb")
# st.audio(audio_file.read())

# From URL
st.video("https://youtu.be/xYo67Z4ZMWA?si=mQwCIAju9h7CxkeM")

# From local file
video_file = open("C:\\Users\\Digital Suppliers\\Downloads\\a_castle_formed_from_living_trees_seen (4).mp4", "rb")
st.video(video_file.read())


# Add widgets to sidebar
st.sidebar.title("Sidebar Title")
st.sidebar.write("Sidebar content")

option = st.sidebar.selectbox(
    "Choose option:",
    ["Option 1", "Option 2"]
)

# Equal width columns
col1, col2, col3 = st.columns(3)

with col1:
    st.write("Column 1")

with col2:
    st.write("Column 2")

with col3:
    st.write("Column 3")


col1, col2 = st.columns([2, 1])  # 2:1 ratio

with col1:
    st.write("Wide column")

with col2:
    st.write("Narrow column")


tab1, tab2, tab3 = st.tabs(["Tab 1", "Tab 2", "Tab 3"])

with tab1:
    st.write("Content for Tab 1")

with tab2:
    st.write("Content for Tab 2")

with tab3:
    st.write("Content for Tab 3")

with st.expander("Click to expand"):
    st.write("Hidden content inside expander")
    #st.image("image.jpg")

container = st.container(border=True)
container.write("Content inside container")
container.button("Button in container")

placeholder = st.empty()

# Update placeholder later
placeholder.text("Initial text")

# Update again
placeholder.success("Updated content!")

with st.popover("Open popover"):
    st.write("Content inside popover")
    st.button("Button in popover")

@st.dialog("Dialog Title")
def show_dialog():
    st.write("This is a dialog/modal!")
    st.text_input("Input in dialog")
    
    if st.button("Close"):
        st.rerun()

if st.button("Open Dialog"):
    show_dialog()


st.success("This is a success message!")
st.info("This is an info message!")
st.warning("This is a warning message!")
st.error("This is an error message!")

import time

progress_text = "Operation in progress..."
my_bar = st.progress(0, text=progress_text)

for percent_complete in range(100):
    time.sleep(0.01)
    my_bar.progress(percent_complete + 1, text=progress_text)

my_bar.empty()


with st.spinner("Loading..."):
    time.sleep(2)
st.success("Done!")

st.toast("This is a toast notification!", icon="🎉")

st.balloons()
st.snow()