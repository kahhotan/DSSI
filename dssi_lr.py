# Author: Prakash Sukhwal
# Aug 2021

import streamlit as st
# other libs
import numpy as np
import pandas as pd
import pickle
# import pyautogui # for reset button: pip install pyautogui

# load the model.pkl
# path = r'D:\work\courses\SI-Solution Implementation\SI\code\streamlit\app3\model.pkl'
with open('logr.pkl', "rb") as f:
	model = pickle.load(f)

# Streamlit provides a caching mechanism that allows your app to stay performant 
# even when loading data from the web, manipulating large datasets, 
# or performing expensive computations. This is done with the @st.cache decorator.
@st.cache()

def prediction(SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm):
	# Making predictions
	prediction = model.predict([[SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm]])
	if prediction == 0:
		pred = 'Rejected'
	else:
		pred = 'Approved'
	return pred


# putting the app related codes in main()
def main():
	# -- Set page config
	apptitle = 'DSSI'
	st.set_page_config(page_title=apptitle, page_icon='random', 
		layout= 'wide', initial_sidebar_state="expanded")
	# random icons in the browser tab

	# give a title to your app
	st.title('Solution Implementation')
	#front end elements of the web page 
	# pick colors from: https://www.w3schools.com/tags/ref_colornames.asp
	html_temp = """ <div style ="background-color:AntiqueWhite;padding:15px"> 
       <h1 style ="color:black;text-align:center;">A loan application assessment app</h1> 
       </div> <br/>"""

    #display the front end aspect
	st.markdown(html_temp, unsafe_allow_html = True)
	# let us make infrastructure to provide inputs
	# we will add the inputs to side bar
	st.sidebar.info('Provide input using the panel')
	st.info('Click Assess button below')

	SepalLengthCm = st.sidebar.slider('SepalLengthCm', 4, 8, 5)
	st.write('input SepalLengthCm', SepalLengthCm)
	SepalWidthCm = st.sidebar.slider('SepalWidthCm', 1, 5, 3)
	st.write('input SepalWidthCm', SepalWidthCm)
	PetalLengthCm = st.sidebar.slider('PetalLengthCm', 1, 7, 60)
	st.write('input PetalLengthCm', PetalLengthCm)
	PetalWidthCm = st.sidebar.slider('PetalWidthCm', 0, 3, 1)
	st.write('input PetalWidthCm', PetalWidthCm)

	# assessment button
	if st.button("Predict"):
		assessment = prediction(SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm)
		st.success('**System assessment says:** {}'.format(assessment))

	# if st.button("Reset"):
	# 	pyautogui.hotkey("ctrl","F5")

	# st.balloons()
	st.success("App is working!!") # other tags include st.error, st.warning, st.help etc.

if __name__ == '__main__':
	main()
