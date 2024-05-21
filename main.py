#!/user/bin/env python

import streamlit as st

st.set_page_config(layout="wide",)

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-color: #111111;
background-size: cover;
background-position: center center;
background-repeat: no-repeat;
background-attachment: local;
color: white;
}}
[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
color: white;
}}
h1 {{
color: white;
}}
h2 {{
color: white;
}}
a.stDownloadButton {{
  color: white !important;
  text-decoration: none;
}}
a.stDownloadButton:hover {{
  color: black !important;
}}
.img-container {{
  width: 100%;
  height: 450px;
  overflow: hidden;
}}
.img-container img {{
  width: 100%;
  height: 100%;
  object-fit: cover;
  -webkit-transform: scale(1);
  -moz-transform: scale(1);
  -ms-transform: scale(1);
  -o-transform: scale(1);
  transform: scale(1);
  -webkit-transition: all 0.3s linear;
  -moz-transition: all 0.3s linear;
  -ms-transition: all 0.3s linear;
  -o-transition: all 0.3s linear;
  transition: all 0.3s linear;
}}
.img-container:hover img {{
  transform: scale(1.1); 
}}
.transition {{
  -webkit-transition: all 0.3s linear;
  -moz-transition: all 0.3s linear;
  -ms-transition: all 0.3s linear;
  -o-transition: all 0.3s linear;
  transition: all 0.3s linear;
}}
article div.box-wrapper {{
  width: 100%;
  display: flex;
  flex-wrap: nowrap;
  justify-content: space-between;
  padding: 20px;
}}
div.box-wrapper div.box {{
  width: 33%;
  height: auto;
  overflow: hidden;
  position: relative;
  display: inline-block;
}}
div.box-wrapper div.box:hover {{
  z-index: 999;
  box-shadow: 0 0 10px rgba(0,0,0,0.3);
}}
div.box img {{
  width: 100%;
  height: auto;
}}
h3 {{
color: white;
}}
.center {{
  display: flex;
  justify-content: center;
}}
.stDownloadButton {{
  background-color: #000000;
  color: white;
  border: solid;
  border-color: #ffffff;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 4px 2px;
  cursor: pointer;
  border-radius: 8px;
}}
.stDownloadButton:hover {{
  background-color: #ffffff;
}}
.blockquote {{
background-color: black;
border-radius:5px;
border: solid;
margin: 20px;
padding 60px;
color: white;
font-size: 16px;
}}
.blockquote:hover {{
background-color: white;
border-radius:5px;
border: solid;
margin: 20px;
padding 60px;
color: black;
}}

</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

st.title("Pedro Schreier")

col1, col2 = st.columns(2)

with col1:
    #st.image("https://i.ibb.co/rpJJ5Fk/Pedro-Shooting-2-76.jpg")
    st.markdown(
        f'<div class="img-container"><img src="https://i.ibb.co/rpJJ5Fk/Pedro\
        -Shooting-2-76.jpg" style="width:90%; height:100%; \
                     object-fit:cover;"></div>',
        unsafe_allow_html=True
    )

with col2:
    st.header("Brand Manager & Developer")
    st.markdown(
        f'<div class="blockquote">"I’d have asked my customers what they \
        wanted, they would\
     have told me <span style="font-weight:bold;">"A faster horse"</span>.-\
      Henry Ford</div>', unsafe_allow_html=True)
    st.toast("Please, text me first for best service and results.")
    content = """
    **Pedro Schreier** is seasoned brand marketing manager and web developer \
    who worked for multiple agencies and industries.

    """
    st.markdown(content)

st.header("Brand Marketing Manager | Hamburg, Capetown & Berlin")

col1, col2 = st.columns(2)

with col1:



    st.subheader("Companies")
    tasks = """
        - **Campaign Management** 
        - **Copywriting**
        - **Market Analysis & Target Audience Profiling**
        - **Product Development & Process automation**
        - **Key Account Management**
        - **Sales & product demo**
        - **Team & department management**
        """
    st.markdown(tasks)
with col2:
    st.subheader("Skills")
    skills = """
           - **Google Sheets automation** 
           - **Copywriting**
           - **Data Analysis and reporting**
           - **Sales & prompt engineering**
           - **Project management**
           - **Landing page optimization**
           - **Brand consultation**
           - **Frontend development**
           - **Campaign management**
           """
    st.markdown(skills)



little = """
    Pedro  Schreier | 2024
    """

st.write(little)
