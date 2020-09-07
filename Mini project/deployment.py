import streamlit as st
import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler
model=pickle.load(open('model.pkl','rb'))
model1=pickle.load(open("model1.pkl","rb"))


page_bg_img = '''
<style>
body {
background-image: url("https://1.bp.blogspot.com/-abPSdoy0oos/X1TyZxRXBNI/AAAAAAAAC0U/iGM45JIreosYoTFIId3yZOsnL9V4SrqqACPcBGAYYCw/s2048/20200906_195657-01.jpeg");
background-size: cover;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)

def predict_Parkinson_Disease(MDVPFoHz,MDVPShimmer, ShimmerAPQ3, HNR,spread1,D2,PPE):
    try:
        input=np.array([[MDVPFoHz,MDVPShimmer, ShimmerAPQ3, HNR,spread1,D2,PPE]]).astype(np.float64)
        input=model1.transform(input)
        prediction=model.predict(input)
        return prediction[0]
    except ValueError:
        print("None")
        
def main():
    st.markdown("""
    <div style="background-color:black ;padding:10px">
    <h2 style="color:rgb(248, 253, 127);text-align:center;">Tcehnocolabs ML Internship</h2>
    </div>
    """, unsafe_allow_html=True)
    
    html_temp = """
    <div style="background-color:#1c1818 ;padding:10px">
    <h2 style="color:white;text-align:center;">Parkinson's Disease Prediction</h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    MDVPFoHz = st.text_input("MDVP:Fo(Hz)")
    MDVPShimmer = st.text_input("MDVP:Shimmer")
    ShimmerAPQ3 = st.text_input("Shimmer:APQ3")
    HNR = st.text_input("HNR")
    spread1 = st.text_input("spread1")
    D2 = st.text_input("D2")
    PPE = st.text_input("PPE")
    
    no_html="""  
      <div style="background-color:None;padding:10px >
       <h2 style="color:white;text-align:center;"> Your dont have Parkinson's Disease</h2>
       </div>
    """
    yes_html="""  
      <div style="background-color:None;padding:10px >
       <h2 style="color:black ;text-align:center;"> You have Parkinson's Disease</h2>
       </div>
    """
    none_html="""  
      <div style="background-color:None;padding:10px >
       <h2 style="color:black ;text-align:center;">Please enter all the values !</h2>
       </div>
    """

    if st.button("Predict"):
        output=predict_Parkinson_Disease(MDVPFoHz,MDVPShimmer, ShimmerAPQ3, HNR,spread1,D2,PPE)
        st.markdown('The Predicted value is: {}'.format(output))

        if output==1:
            st.markdown(yes_html,unsafe_allow_html=True)
        elif output==0:
            st.markdown(no_html,unsafe_allow_html=True)
        else:
            st.markdown(none_html,unsafe_allow_html=True)
  

if __name__=='__main__':
    main()