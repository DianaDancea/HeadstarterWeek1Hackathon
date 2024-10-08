import streamlit as st
import pandas as pd

# Initialize the user data in the session state if it doesn't exist - these are starter values
if 'users_data' not in st.session_state:
    st.session_state.users_data = pd.DataFrame({
        'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
        'location': ['New York', 'New York', 'Los Angeles', 'New York', 'Los Angeles'],
        'sport': ['Basketball', 'Soccer', 'Basketball', 'Soccer', 'Tennis']
    })

# Title of the app
st.title("Voli: Find Your Sports Match")

# Input fields for user data
name = st.text_input("Enter your name")
location = st.text_input("Enter your location")
sport = st.selectbox("Choose a sport", ['Basketball', 'Soccer', 'Tennis', 'Pickleball'])

# Button to find matches
if st.button('Find Matches'):
    if name and location and sport:
        # Add the new user to the session state data - this is dynamically adding the user once they submit
        new_user = pd.DataFrame({'name': [name], 'location': [location], 'sport': [sport]})
        st.session_state.users_data = pd.concat([st.session_state.users_data, new_user], ignore_index=True)

        # Filter users based on location and sport, excluding the current user
        matches = st.session_state.users_data[(st.session_state.users_data['location'] == location) &
                                              (st.session_state.users_data['sport'] == sport) &
                                              (st.session_state.users_data['name'] != name)]

        # Randomly select up to 3 matches
        if not matches.empty:
            matches_list = matches.sample(min(3, len(matches)))
            st.write(f"Found {len(matches_list)} match(es) for you:")
            for index, row in matches_list.iterrows():
                st.write(f"- {row['name']} from {row['location']} interested in {row['sport']}")
        else:
            st.write("No matches found. Try another sport or location.")
    else:
        st.write("Please fill in all the fields.")
