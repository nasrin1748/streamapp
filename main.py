import streamlit as st
from calendar import TextCalendar
import datetime
from colorama import init, Fore, Style
import time

# Initialize colorama
init()

# ASCII Art Banner
banner = """
╔══════════════════════════════════════╗
║        CALENDAR ASSISTANT           ║
╚══════════════════════════════════════╝
"""

# Loading animation
def loading_animation():
    st.write("Loading calendar", end="")
    for _ in range(3):
        time.sleep(0.5)
        st.write(".", end="", flush=True)

# Print banner
st.write(banner)

# Get user input with Streamlit widgets
try:
    year = st.number_input("Enter Year:", min_value=1, max_value=9999, step=1)
    month = st.number_input("Enter Month (1-12):", min_value=1, max_value=12, step=1)
    day = st.number_input("Enter Day:", min_value=1, max_value=31, step=1)

    # Show loading animation
    loading_animation()

    # Create calendar object
    cal = TextCalendar()

    # Print the month calendar with styling
    st.write("\n═══════════════════════════════════")
    st.write(f"Calendar for {datetime.datetime(year, month, day).strftime('%B %Y')}")
    st.write("═══════════════════════════════════")
    st.write("Mo Tu We Th Fr Sa Su")
    st.write(cal.formatmonth(year, month, w=2, l=1))

    # Print the specific date information
    date = datetime.datetime(year, month, day)
    st.write("\n═══════════════════════════════════")
    st.write(f"Selected Date: {date.strftime('%A, %B %d, %Y')}")
    st.write("═══════════════════════════════════")

    # Print the full year calendar
    st.write("\nFull Year Calendar:")
    st.write(cal.formatyear(year, 2, 1, 8, 3))

except ValueError:
    st.error("Error: Please enter valid numbers for date.")
except Exception as e:
    st.error(f"An error occurred: {str(e)}")
