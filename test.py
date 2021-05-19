import streamlit as st
import cv2
run1 = st.checkbox('Open Camera')
FRAME_WINDOW= st.image([])
vs = cv2.VideoCapture(0)
while run1:
	_, frame = vs.read()
	frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
	FRAME_WINDOW.image(frame,caption='Real time Face Mask Detection')

	