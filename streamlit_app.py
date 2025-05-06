### streamlit_app.py — Streamlit App for Traffic Help Assistant (OOP Based)

import streamlit as st
from sympy import sympify

# OOP Classes
class Person:
    def __init__(self, name, phone, location):
        self.name = name
        self.phone = phone
        self.location = location

class Mechanic(Person):
    def __init__(self, name, phone, location, services):
        super().__init__(name, phone, location)
        self.services = services

    def show_details(self):
        return {
            'Name': self.name,
            'Phone': self.phone,
            'Location': self.location,
            'Services': ', '.join(self.services)
        }

class RequestHelp:
    def __init__(self, user_name, user_location, required_service):
        self.user_name = user_name
        self.user_location = user_location
        self.required_service = required_service

    def find_mechanic(self, mechanic_list):
        available = [m for m in mechanic_list if self.required_service.lower() in [s.lower() for s in m.services]]
        return available if available else []

# Example mechanic data
mechanics = [
    Mechanic("Ali Mechanic", "03001234567", "Lahore", ["Tyre", "Engine", "Petrol"]),
    Mechanic("Usman Workshop", "03007654321", "Karachi", ["Battery", "Engine"]),
    Mechanic("Rehan Auto Help", "03111222333", "Islamabad", ["Petrol", "Tyre"])
]

# Streamlit UI
st.set_page_config(page_title="Traffic Help Assistant", layout="centered")
st.title("🚗 Traffic Help Assistant")

with st.form("request_form"):
    name = st.text_input("Your Name")
    location = st.text_input("Your Location")
    service = st.selectbox("What help do you need?", ["", "Tyre", "Petrol", "Engine", "Battery"])
    submit = st.form_submit_button("Find Help")

if submit:
    if not name or not location or not service:
        st.warning("Please fill out all fields.")
    else:
        help_request = RequestHelp(name, location, service)
        found_mechanics = help_request.find_mechanic(mechanics)

        if found_mechanics:
            st.success("Mechanics available for your request:")
            for mech in found_mechanics:
                details = mech.show_details()
                st.markdown("---")
                for key, val in details.items():
                    st.markdown(f"**{key}:** {val}")
        else:
            st.error("No mechanics available for the selected service.")
