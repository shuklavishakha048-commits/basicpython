import streamlit as st
import requests

st.set_page_config(page_title="language translation tool",page_icon=":🌐:",layout="centered")

st.title(" 🌐Language Translation Tool")
st.write("Welcome to our language translation tool!😊")

languages= ["English","Hindi","Spanish","French","German","Chinese","Japanese","Korean","Italian","Turkish"]

col1,col2 = st.columns(2)

with col1:
    src_lang = st.selectbox("🗂️source language",languages ,index = 0)

with col2:
    tar_lang = st.selectbox("🗂️target language",languages,index = 1)  
      
text =st.text_area("enter text to translate:",height =200 , placeholder = "enter text to translate..." ) 
url = "https://api.mymemory.translated.net/get"   

if st.button("🔄 Translate", use_container_width=True):

    if text.strip() == "":
        st.warning("Please enter some text first.")

    elif src_lang == tar_lang:
        st.warning("Source and target languages should be different.")

    elif  url=="https://api.mymemory.translated.net/get":
          params={
              "q":text,
               "langpair": f"{src_lang[:2].lower()}|{tar_lang[:2].lower()}" 
          }  

          response = requests.get(url,params=params)   
          data = response.json()
          translated_text = data["responseData"]["translatedText"]
          st.subheader("Translated Text") 
          st.success("Translation successful!")
          st.write(translated_text)

          st.code(translated_text, language=None)

    else:
        st.error("Translation failed. Please try again later.")

if st.button("📋 Copy Translation"):
    st.write("Select and copy the translated text from the box above.")
    
    
       