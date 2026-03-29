import streamlit as st

# Page config
st.set_page_config(page_title="Student Performance Predictor", page_icon="📊")

# Session state init
if "step" not in st.session_state:
    st.session_state.step = 1

# Step 1: Welcome Page
if st.session_state.step == 1:
    st.title("👋 Hello Student!")
    st.write("Welcome to your Smart Performance Predictor")

    if st.button("Start"):
        st.session_state.step = 2

# Step 2: Ask Name
elif st.session_state.step == 2:
    st.title("🧑‍🎓 Enter Your Name")

    name = st.text_input("Your Name")

    if st.button("Next"):
        if name:
            st.session_state.name = name
            st.session_state.step = 3
        else:
            st.warning("Please enter your name")

# Step 3: Inputs
elif st.session_state.step == 3:
    st.title(f"📚 Hello {st.session_state.name}, Enter Your Details")

    sleep = st.slider("😴 Sleep Hours (per day)", 0, 12, 6)

    subjects = ["Maths", "Physics", "Chemistry"]

    study_hours = {}
    attendance = {}

    for sub in subjects:
        st.subheader(f"{sub}")
        study_hours[sub] = st.slider(f"{sub} Study Hours", 0, 10, 2)
        attendance[sub] = st.slider(f"{sub} Attendance (%)", 0, 100, 75)

    if st.button("Predict Performance"):
        st.session_state.sleep = sleep
        st.session_state.study = study_hours
        st.session_state.attendance = attendance
        st.session_state.step = 4

# Step 4: Prediction
elif st.session_state.step == 4:
    st.title("📊 Your Performance Report")

    sleep = st.session_state.sleep
    study = st.session_state.study
    attendance = st.session_state.attendance

    results = {}
    total_marks = 0

    for sub in study:
        s = study[sub]
        a = attendance[sub]

        # Base score (balanced)
        score = (s * 5) + (a * 0.5)

        # Sleep impact
        if sleep < 5:
            score *= 0.8
        elif sleep > 9:
            score *= 0.9

        # Penalize imbalance
        if s < 2 and a > 80:
            score *= 0.7
        if a < 50 and s > 5:
            score *= 0.75

        # Cap marks
        score = min(100, round(score))

        results[sub] = score
        total_marks += score

    avg = total_marks / len(results)

    st.subheader("📈 Predicted Marks")
    for sub, marks in results.items():
        st.write(f"{sub}: {marks}")

    st.subheader(f"🎯 Overall Average: {round(avg,2)}")

    # Advice Section
    st.subheader("💡 Advice")

    if avg >= 75:
        st.success("Great job! Keep maintaining your consistency 💪")

    elif avg >= 50:
        st.warning("You're doing okay, but improvement is needed!")

    else:
        st.error("You need serious improvement ⚠️")

    # Detailed Advice
    if sleep < 5:
        st.write("👉 Increase your sleep. Low sleep affects performance.")

    if sleep > 9:
        st.write("👉 Too much sleep can reduce productivity. Try to balance.")

    for sub in study:
        if study[sub] < 2:
            st.write(f"👉 Increase study time for {sub}")

        if attendance[sub] < 60:
            st.write(f"👉 Improve attendance in {sub}")

    if st.button("Restart"):
        st.session_state.step = 1
