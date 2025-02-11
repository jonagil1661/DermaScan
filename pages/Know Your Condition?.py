import streamlit as st
import urllib.parse

st.title("Already Know Your Condition? Find a Dermatologist!")

st.write("### Enter Disease or Condition")
condition = st.text_input("Enter a skin condition (e.g., Acne, Eczema, Psoriasis)")

st.write("### Enter Your Location")
user_location = st.text_input("Enter your city (and state if needed)")

if st.button("Find Specialists"):
    if condition and user_location:
        formatted_condition = urllib.parse.quote_plus(condition.strip())
        formatted_location = urllib.parse.quote_plus(user_location.strip())

        try:
            with open("api_key.txt", "r") as file:
                api_key = file.readline().strip()
        except Exception as e:
            st.error(f"Error reading API key: {e}")
            api_key = None

        if api_key:
            google_maps_url = f"https://www.google.com/maps/embed/v1/search?key={api_key}&q={formatted_condition}+specialist+near+{formatted_location}"

            st.write("### Specialists Near You")
            st.components.v1.html(
                f'<iframe width="600" height="450" style="border:0" loading="lazy" allowfullscreen '
                f'src="{google_maps_url}"></iframe>',
                height=450,
            )
        else:
            st.error("API Key is missing or incorrect.")
    else:
        st.warning("Please enter both a condition and a location.")









