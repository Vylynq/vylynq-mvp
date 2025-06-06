# vylynq_my_arena_mvp.py

import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Vylynq - Energy Score", layout="wide", page_icon="⚡")

# Inject custom CSS
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Initialize session state for inputs if not already done
if "energy_wallet" not in st.session_state:
    st.session_state.energy_wallet = 100

if "energy_activity_states" not in st.session_state:
    st.session_state.energy_activity_states = {}

# Navigation Tabs
selected_tab = st.sidebar.radio("", ["Energy Score"])

# --- ENERGY SCORE ---
if selected_tab == "Energy Score":
    st.markdown("<h1 class='title'>Energy Score ⚡</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>You started the day with 100 points. Earn more, lose some, outscore your past self.</p>", unsafe_allow_html=True)

    activities = {
        "Ate junk food": -20,
        "Doomscrolled Instagram for 1hr": -30,
        "Slept less than 5 hours": -25,
        "Moved your body": +30,
        "Drank enough water": +20,
        "Laughed out loud": +10
    }

    st.markdown("### What did you do today?")
    net_energy = 100  # reset daily baseline

    for activity, value in activities.items():
        key = f"energy_{activity.replace(' ', '_')}"
        checked = st.checkbox(activity, key=key)
        st.session_state.energy_activity_states[key] = checked
        if checked:
            net_energy += value

    st.markdown("---")
    if net_energy >= 100:
        st.success(f"💯 You're full of energy! ({net_energy} points)")
    elif 60 <= net_energy < 100:
        st.info(f"⚡ You’re doing okay – keep going. ({net_energy} points)")
    elif 30 <= net_energy < 60:
        st.warning(f"🥱 Energy dipping. Time for a recharge. ({net_energy} points)")
    else:
        st.error(f"🔋 You’re running on fumes. Go rest. ({net_energy} points)")
