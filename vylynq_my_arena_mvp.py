# vylynq_my_arena_mvp.py

import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Vylynq - My Arena", layout="wide", page_icon="🥷")

# Inject custom CSS
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Initialize session state for inputs if not already done
if "habit_states" not in st.session_state:
    st.session_state.habit_states = {}

if "selected_mood" not in st.session_state:
    st.session_state.selected_mood = "Happy"

if "notification_freq" not in st.session_state:
    st.session_state.notification_freq = "Every 1 hour"

if "notification_routines" not in st.session_state:
    st.session_state.notification_routines = []

# Navigation Tabs
selected_tab = st.sidebar.radio("", ["My Arena", "Mood Meals", "Notification Rituals"])

# --- MY ARENA ---
if selected_tab == "My Arena":
    st.markdown("<h1 class='title'>My Arena 🥷</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>Where you either rise or scroll.</p>", unsafe_allow_html=True)

    habits = [
        "Moved my body",
        "Drank actual water",
        "Didn't lose it on a Zoom call",
        "Ate like an adult",
        "Touched grass"
    ]

    st.markdown("<h3>Daily Rituals</h3>", unsafe_allow_html=True)

    for habit in habits:
        key = f"habit_{habit.replace(' ', '_')}"
        current_value = st.session_state.habit_states.get(key, False)
        checked = st.checkbox(habit, value=current_value, key=key)
        st.session_state.habit_states[key] = checked

        if checked:
            st.success(f"Flex much? '{habit}' – nailed it.")
        else:
            st.warning(f"Still waiting on you to '{habit}'. No pressure, just your life.")

    st.markdown("<hr>")
    st.markdown(f"<small>{datetime.now().strftime('%A, %B %d, %Y')}</small>", unsafe_allow_html=True)

# --- MOOD MEALS ---
elif selected_tab == "Mood Meals":
    st.markdown("<h1 class='title'>Mood Meals 🍕</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>Feed your feels (but like... smarter).</p>", unsafe_allow_html=True)

    mood = st.selectbox(
        "How are you feeling right now?",
        ["Happy", "Sad", "Angry", "Tired", "Anxious", "Bored"],
        index=["Happy", "Sad", "Angry", "Tired", "Anxious", "Bored"].index(st.session_state.selected_mood),
        key="mood_selector"
    )
    st.session_state.selected_mood = mood

    mood_suggestions = {
        "Happy": "Ride that high. Maybe something light – fruit bowl or protein smoothie?",
        "Sad": "Comfort food – go for warm dal rice, or chocolate (we see you).",
        "Angry": "Spicy food. Burn the rage with a plate of schezwan magic.",
        "Tired": "Banana, almonds, or something hydrating like coconut water.",
        "Anxious": "Chamomile tea, oats with peanut butter – calm meets full.",
        "Bored": "Don’t eat out of boredom. But hey, popcorn isn’t a crime."
    }

    if mood:
        st.info(mood_suggestions[mood])

# --- NOTIFICATION RITUALS ---
elif selected_tab == "Notification Rituals":
    st.markdown("<h1 class='title'>Notification Rituals 🔔</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>Set your vibe. We'll ping you like a clingy ex.</p>", unsafe_allow_html=True)

    freq = st.selectbox(
        "How often do you want notifications?",
        ["Every 30 mins", "Every 1 hour", "Every 2 hours", "Don't disturb me unless the world ends"],
        index=["Every 30 mins", "Every 1 hour", "Every 2 hours", "Don't disturb me unless the world ends"].index(st.session_state.notification_freq),
        key="notification_freq_selector"
    )
    st.session_state.notification_freq = freq

    routine = st.multiselect(
        "What do you want to be reminded about?",
        ["Drink Water", "Eat a Meal", "Take a Break", "Touch Grass", "Breathe Intentionally"],
        default=st.session_state.notification_routines,
        key="notification_routines_selector"
    )
    st.session_state.notification_routines = routine

    if freq and routine:
        st.success(f"Cool. You’ll be annoyed every: {freq} \nWith reminders for: {', '.join(routine)}")
    elif not routine:
        st.warning("Select at least one ritual, superstar.")
