import streamlit as st
from PIL import image
st.set_page_config(page_title = 'cats')
st.markdown("## Types of cats")
st.write("-persian cat")
st.image("C:\movie\persian cat.jpg")
img = image.open("C:\movie\persian cat.jpg")
st.write("-White cat")
st.image("C:\movie\white cat.jpg")
