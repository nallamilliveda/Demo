import streamlit as st
st.set_page_config(page_title = 'cats')
st.markdown("## Types of cats")
col1,col2 = st.columns(2)
 with col1:
  st.subheader("-persian cat")
  st.image("https://th.bing.com/th/id/OIP.eZk5ARN29UZ1pOgVsmSixAHaFj?w=233&h=180&c=7&r=0&o=5&dpr=1.1&pid=1.7") 
  st.write("persion cats are cute")
 with col2:
  st.subheader("-White cat")
  st.image("./giphy.gif")
  st.write("white cats are cute")
st.image("./white cat.jpg")  
 
