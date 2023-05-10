import datetime
import streamlit as st
from pymongo import MongoClient

uri = "mongodb+srv://teena:iamteena@atlascluster.jigryku.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri)
db = client['Udaan']
collection = db['Participants']

# Designing our web page with Title and a Small description
st.set_page_config(
    page_title=" UDAAN Registrations")
st.title(":office: UDAAN 2023")

# Displaying an image on road accidents
st.image("https://media.istockphoto.com/id/1350787994/photo/light-bulbs-with-event-management-concept.jpg?b=1&s=170667a&w=0&k=20&c=GvH8NqOq5dU3AIPCsKIoXLkD8SijfcJiB0VhnS5RUV8=", caption=" Creator: A melange of various activities ", use_column_width=True, clamp=255, channels="RGB", output_format="auto")
st.write("""
   We are hosting an intercollegiate national-level technical fest organized by RYAN (Deemed to be University) Pune. 
   It brings forth a mélange of events and competitions in different disciplines of Computer Science, Economics, logical reasoning, presentation expertise, and the art of humor. 
   Your participation is welcomed. Kindly fill in the form to participate in a week long event. 

    You are free to select various groups to volunteer in. The details of each group are mentioned below.
    1. Poster making: Creating catchy and informative posters for all the events 
    2. Sponsorship: Persuasive in finding and contacting sponsors for the event 
    3. Invitation: Contacting other universities and colleges for participation in the event  
    4. Social media: Creating and managing  social media page 
    5. Content: Generating content which will be used for communication like emails, social media, etc. 
    6. Graphics: Creating graphics for the event
    7. Video editing: creating and editing promotional videos and teasers for the event 

    """)

# Create a function to collect the student's details
def get_student_details():
    st.write("Enter student details:")
    name = st.text_input("Name")
    regNo = st.text_input("Registration No.:")
    dept = st.selectbox('Enter your Department', ['BBA', 'B.Com', 'Law', 'Data Science', 'MBA'])
    class1 = st.text_input('Enter your Class')
    mobile = st.text_input("Enter your Whatsapp Number")
    dob = st.date_input("Enter your DOB:", datetime.date(2001, 1, 1))
    gender = st.selectbox("Gender", ["Male", "Female", "Rather Not Say"])
    email = st.text_input("Email")
    address = st.text_area("Address")
    return name, regNo, dept, class1, mobile,dob, gender, email, address


# Create a function to collect the student's academic details
def get_student_academic_details():
    st.write("Enter student academic details and event preferences:")
    semester = st.number_input("Enter the number of semesters:", min_value=1, max_value=10, step=1)
    cgpa = {}
    # Loop over the number of semesters and ask the user for their CGPA
    for i in range(semester):
        semester = f"Semester {i + 1}"
        cgpa1 = st.number_input(f"Enter CGPA for Semester {i + 1}:", min_value=0.0, max_value=4.0, step=0.01)
        cgpa[semester] = cgpa1
    choices = ['Poster making', 'Sponsorship','Invitation', 'Social media', 'Content', 'Graphics', 'Video editing']
    selected_choices = st.multiselect('Select your event preference:', choices)
    return semester,  cgpa, selected_choices


# Create a function to submit the student's application
def submit_application():
    st.write("Application submitted!")


# Create the main application
def main():
    name, regNo, dept, class1, mobile, dob, gender, email, address = get_student_details()
    semester, cgpa, selected_choices = get_student_academic_details()

    if st.button("Submit"):
        submit_application()
        st.balloons()
        data = {'name': name, 'regno': regNo,'department' : dept, 'class': class1,'mobile': mobile, 'dob': dob, 'gender' : gender, 'email': email, 'address': address, 'cgpa' : cgpa, 'event': selected_choices}
        collection.insert_one(data)
        st.write('Form data inserted into MongoDB database.')

if __name__ == "__main__":
    main()

import streamlit_text_rating

st.markdown("For more information")
for text in ["Are you willing to participate in the versatility run?"]:
    response = streamlit_text_rating.st_text_rater(text=text)
    if response:
        st.write("Thanks for your feedback")
