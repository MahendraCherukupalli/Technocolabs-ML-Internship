import streamlit as st
import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler
model=pickle.load(open('model.pkl','rb'))
model1=pickle.load(open("model1.pkl","rb"))




CHOICES = {1: "Graduate school", 2: "University", 3: "High school", 4: "Others"}
def format_func(option):
    return CHOICES[option]



CHOICES1 = {1: "Married", 2: "Single", 3: "Others"}
def format_func1(option):
    return CHOICES1[option]




page_bg_img = '''
<style>
body {
background-image: url("https://www.inhouseops.com/wp-content/uploads/sites/152/2020/01/iStock-1133860020.jpg");
background-size: cover;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)

def Credit_Card_Default_Prediction(LIMIT_BAL,EDUCATION,MARRIAGE,AGE,PAY_1,BILL_AMT1,BILL_AMT2,BILL_AMT3,BILL_AMT4,BILL_AMT5,BILL_AMT6,PAY_AMT1,PAY_AMT2,PAY_AMT3,PAY_AMT4,PAY_AMT5,PAY_AMT6):
    try:
        input=np.array([[LIMIT_BAL,EDUCATION,MARRIAGE,AGE,PAY_1,BILL_AMT1,BILL_AMT2,BILL_AMT3,BILL_AMT4,BILL_AMT5,BILL_AMT6,PAY_AMT1,PAY_AMT2,PAY_AMT3,PAY_AMT4,PAY_AMT5,PAY_AMT6]]).astype(np.float64)
        input=model1.transform(input)
        prediction=model.predict(input)
        return prediction[0]
    except ValueError:
        print("None")
        
        
def main():
    st.markdown("""
    
    <h2 style="color:black;text-align:left;">Technocolabs ML Internship</h2>
    </div>
    """, unsafe_allow_html=True)
    html_temp = """
    
    <h2 style="color:black;text-align:left;">Credit Card Default Prediction</h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    st.text("Please enter all the values given below.")
    

    LIMIT_BAL = st.text_input("LIMIT_BAL")
    EDUCATION = st.selectbox("Select EDUCATION Status", options=list(CHOICES.keys()), format_func=format_func)
    MARRIAGE = st.selectbox("Select MARRIAGE Status", options=list(CHOICES1.keys()), format_func=format_func1)
    AGE = st.slider("Select Age:", min_value=21, max_value=100)
    PAY_1 = st.text_input("PAY_1")
    BILL_AMT1 = st.text_input("BILL_AMT1")
    BILL_AMT2 = st.text_input("BILL_AMT2")
    BILL_AMT3 = st.text_input("BILL_AMT3")
    BILL_AMT4 = st.text_input("BILL_AMT4")
    BILL_AMT5 = st.text_input("BILL_AMT5")            
    BILL_AMT6 = st.text_input("BILL_AMT6")
    PAY_AMT1 = st.text_input("PAY_AMT1")
    PAY_AMT2 = st.text_input("PAY_AMT2")
    PAY_AMT3 = st.text_input("PAY_AMT3")
    PAY_AMT4 = st.text_input("PAY_AMT4")
    PAY_AMT5 = st.text_input("PAY_AMT5")                     
    PAY_AMT6 = st.text_input("PAY_AMT6")                                       
                         
                         
                         
                                    
                         
    no_html="""  
      <div style="background-color:None;padding:10px >
       <h2 style="color:white;text-align:center;">The account owner did not fail to make the minimum payment.</h2>
       </div>
    """
    yes_html="""  
      <div style="background-color:None;padding:10px >
       <h2 style="color:black ;text-align:center;"> The account owner failed to make the minimum payment.</h2>
       </div>
    """
    none_html="""  
      <div style="background-color:None;padding:10px >
       <h2 style="color:black ;text-align:center;">Please enter all the values correctly !</h2>
       </div>
    """

    if st.button("Predict"):
        output=Credit_Card_Default_Prediction(LIMIT_BAL,EDUCATION,MARRIAGE,AGE,PAY_1,BILL_AMT1,BILL_AMT2,BILL_AMT3,BILL_AMT4,BILL_AMT5,BILL_AMT6,PAY_AMT1,PAY_AMT2,PAY_AMT3,PAY_AMT4,PAY_AMT5,PAY_AMT6)
        st.markdown('The Predicted value is: {}'.format(output))

        if output==1:
            st.markdown(yes_html,unsafe_allow_html=True)
        elif output==0:
            st.markdown(no_html,unsafe_allow_html=True)
        else:
            st.markdown(none_html,unsafe_allow_html=True)
  

if __name__=='__main__':
    main()