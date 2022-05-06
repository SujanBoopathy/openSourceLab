# Import following modules
from pywebio.input import *
from pywebio.output import *
from pywebio.session import *
import re
  
# For checking Email, whether Valid or not.
regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
  
# For checking Phone Number, whether Valid or 
# not.
Pattern = re.compile("(0/91)?[6-9][0-9]{9}")

  

# Taking input from the user
data = input_group("Fill out the form:", [
    input('Username', name='username', type=TEXT,
          required=True, PlaceHolder="@username"),
    
    input('Password', name='pass', type=PASSWORD,
          required=True, PlaceHolder="Password"),
    
    input('Confirm Password', name='passes', type=PASSWORD,
          required=True, PlaceHolder="Confirm Password"),
    
    input('Name', name='name', type=TEXT, required=True, 
          PlaceHolder="name"),
    
    input('Phone', name='phone', type=NUMBER,
          required=True, PlaceHolder="12345"),
    
    input('Email', name='email', type=TEXT,
          required=True, PlaceHolder="user@gmail.com"),
    
    input('Age', name='age', type=NUMBER, required=True,
          PlaceHolder="age"),
    
    
], validate=check_form, cancelable=True)
  
# Create a radio button
gender = radio("Gender", options=['Male', 'Female'], required=True)
  
# Create a skills markdown
skills = select("Tech Stack", options=[
  'C Programming', 'Python', 'Web Development', 'Android Development'],
                required=True)
  
# Create a textarea
text = textarea("Comments/Questions", rows=3,
                placeholder="Write something...", required=True)
  
# Create a checkbox
agree = checkbox("Agreement", options=[
    'I agree to terms and conditions'], required=True)
  
# Display output using popup
popup("Your Details",
      f"Username: @{data['username']}\nName: {data['name']}\
      \nPhone: {str(data['phone'])}\nEmail: {data['email']}\
      \nAge: {str(data['age'])}\
      \nGender: {gender}\nSkill: {skills}\nComments: {text}",
      closable=True)