import streamlit as st
from model import Inference

# init mode;
model = Inference()
# bypass the server certificate verification on client side
model.allowSelfSignedHttps()
st.sidebar.image('image.jpg')
# st.sidebar.header('Azure Machine Learning Key and Url')
key = st.sidebar.text_input('Enter your Key')
url = st.sidebar.text_input('Enter your Url')

if key is None or url is None:
    st.error('Please enter your key and url for prediction')
else:
    model.input_url_key(url,key)

st.header('Predictive Modeling for Student Performance')
sex = st.selectbox('Sex',('M','F'))
age = st.number_input('Age')
school = st.selectbox("What is your school name ?",('GP','MS'))
reason = st.selectbox('Reason for choose that school',('course','other','home','reputation'))
address = st.selectbox('Address type',('urban','rural'))
famsize = st.selectbox('Famliy size',('less or equal to 3','greater than 3'))
parent_cohabitation_status = st.selectbox('Parent cohabitation status',('apart','living together'))
mother_education = st.selectbox('Mother education',('none','primary education (4th grade)','secondary education',
                                                    '5th to 9th grade','higher education'))
father_education = st.selectbox('Father education',('none','primary education (4th grade)','secondary education',
                                                    '5th to 9th grade','higher education'))
Mjob = st.selectbox('Mother job',('at_home','health','other','services','teacher'))
Fjob = st.selectbox('Father job',('at_home','health','other','services','teacher'))
guardian = st.selectbox('Guardian',('father','mother','other'))
traveltime = st.selectbox('Travel time ',('<15 min','15 to 30 min','30 min to 1 hour','>1 hour'))
studytime = st.selectbox('Study time (weekly)',('<2 hours','2 to 5 hours','5 to 10 hours','>10 hours'))
failures = st.number_input('Number of past class failures')
schoolsup = st.selectbox('Extra educational support',('yes','no'))
famsup = st.selectbox('Family educational support',('yes','no'))
paid = st.selectbox('Extra paid classes within the course subject',('yes','no'))
activities = st.selectbox('Extra-curricular activities',('yes','no'))
nursery = st.selectbox('Attended nursery school',('yes','no'))
higher = st.selectbox('Wants to take higher education',('yes','no'))
internet = st.selectbox('Internet access at home',('yes','no'))
romantic = st.selectbox('With a romantic relationship',('yes','no'))
famrel = st.number_input('Quality of Family relationships (from 1 - very bad to 5 - excellent)')
freetime = st.number_input('Free time after school (from 1 - very low to 5 - very high)')
goout = st.number_input('Going out with friends (from 1 - very low to 5 - very high)')
Dalc = st.number_input('Workday alcohol consumption (from 1 - very low to 5 - very high)')
Walc = st.number_input('Weekend alcohol consumption (from 1 - very low to 5 - very high)')
health = st.number_input('Current health status (from 1 - very bad to 5 - very good)')
absences = st.number_input('Number of school absences')

buttom = st.sidebar.button('Predict')
if buttom:
    model.input_data(school,sex,age,address,famsize,parent_cohabitation_status,mother_education,
        father_education,Mjob,Fjob,reason,guardian,traveltime,studytime,failures,schoolsup,famsup,
        paid,activities,nursery,higher,internet,romantic,famrel,freetime,goout,Dalc,Walc,health,absences)
    result = model.get_result().decode('utf8')
    begin = float(result[15:-16]) - 9.7
    end = float(result[15:-16]) + 9.7
    st.sidebar.text('Student Exam Performance Estimated: {} - {}'.format(round(begin,2),round(end,2)))


