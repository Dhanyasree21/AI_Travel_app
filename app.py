import streamlit as st
st.title('welcome to travel App!')
Destination=st.text_input('Enter your travel destination:')
Budget=st.number_input('Enter your budget:')
Date=st.date_input('Enter your travel date:')
Accomdation=st.selectbox('Enter yes if you need accomdation or no', ('yes','no'))
Travel_type=st.selectbox('Mode of Transport',[flight, train, bus, car, walk])
if st.button('submit'):
  st.write(f"""
  AI APP
  --------------------------
  Destination: {Destination}
  
  Budget: {Budget}
  
  Date: {Date}
  
  Accomdation: {Accomdation}
           """)
  st.balloons()
