import streamlit as st
from calendar import TextCalendar
from datetime import datetime, timedelta
from colorama import Fore, Style

# Streamlit App Setup
st.set_page_config(page_title="Calendar Assistant", layout="centered")

# Banner
st.markdown(
    f"""
    <div style="text-align: center; font-size: 22px; font-weight: bold; color: cyan;">
        ╔══════════════════════════════════════╗<br>
        ║          CALENDAR ASSISTANT          ║<br>
        ╚══════════════════════════════════════╝
    </div>
    """,
    unsafe_allow_html=True,
)

# Sidebar Inputs for User Interaction
st.sidebar.header("Input Date")
year = st.sidebar.number_input("Enter Year", min_value=1, max_value=9999, value=datetime.now().year)
month = st.sidebar.number_input("Enter Month", min_value=1, max_value=12, value=datetime.now().month)
day = st.sidebar.number_input("Enter Day", min_value=1, max_value=31, value=datetime.now().day)

# Compute Date and Validation
try:
    input_date = datetime(year, month, day)
    
    # Header Output
    st.markdown(f"### Calendar for: **{input_date.strftime('%B %Y')}**")

    # Generate and Display Calendar
    cal = TextCalendar()
    month_calendar = cal.formatmonth(year, month)
    st.text(month_calendar)  # Display the plain text calendar

    # Display Selected Day Information
    day_of_week = input_date.strftime("%A")
    st.markdown(f"**Selected Date:** {input_date.strftime('%Y-%m-%d')} (**{day_of_week}**)")

    # Compute Previous and Next Dates
    prev_date = input_date - timedelta(days=1)
    next_date = input_date + timedelta(days=1)
    st.markdown(f"**Previous Date:** {prev_date.strftime('%Y-%m-%d')} (**{prev_date.strftime('%A')}**)")
    st.markdown(f"**Next Date:** {next_date.strftime('%Y-%m-%d')} (**{next_date.strftime('%A')}**)")

except ValueError as e:
    st.error("Invalid date. Please check your inputs.")

# Footer or Credits
st.markdown(
    """
    <hr>
    <div style="text-align: center; color: grey;">
        Created with ❤️ in Streamlit
    </div>
    """,
    unsafe_allow_html=True,
)
