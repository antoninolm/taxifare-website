import streamlit as st
import requests
import datetime

'''
# TaxiFareModel front
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')

'''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

1. Let's ask for:
- date and time
- pickup longitude
- pickup latitude
- dropoff longitude
- dropoff latitude
- passenger count
'''

pickup_date = st.date_input("Pickup Date", datetime.date.today())
pickup_time = st.time_input("Pickup Time", datetime.datetime.now().time())
pickup_longitude = st.number_input("Pickup Longitude", value=-73.950655, format="%.6f")
pickup_latitude = st.number_input("Pickup Latitude", value=40.783282, format="%.6f")
dropoff_longitude = st.number_input("Dropoff Longitude", value=-73.984365, format="%.6f")
dropoff_latitude = st.number_input("Dropoff Latitude", value=40.769802, format="%.6f")
passenger_count = st.number_input("Passenger Count", min_value=1, max_value=10, value=1, step=1)

# Convert date and time to a single string
datetime_str = f"{pickup_date} {pickup_time}"


'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''

url = 'https://taxifare-373399044828.europe-west1.run.app/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

'''
2. Let's build a dictionary containing the parameters for our API...
'''
dict_params = {
    'pickup_datetime': datetime_str,
    'pickup_longitude': pickup_longitude,
    'pickup_latitude': pickup_latitude,
    'dropoff_longitude': dropoff_longitude,
    'dropoff_latitude': dropoff_latitude,
    'passenger_count': passenger_count
}


# Call API when the user clicks the button
if st.button("Get Fare Prediction"):
    response = requests.get(url, params=dict_params)

    if response.status_code == 200:
        data = response.json()
        #data is a dictionary with this structure: {'fare': 6.319900035858154}
        fare = data.get("fare", "No fare returned")
        #print doesnt work, you need to use this method
        st.success(f"Estimated Fare: ${fare:.2f}")
    else:
        st.error(f"API request failed with status code {response.status_code}")
