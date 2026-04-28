import streamlit as st

st.title("AI Adoption Readiness Scorer")

leadership = st.slider("Leadership alignment", 1, 5, 3)
decision_rights = st.slider("Decision rights clarity", 1, 5, 3)
skills = st.slider("Workforce AI skills", 1, 5, 3)
governance = st.slider("Governance maturity", 1, 5, 3)
reinforcement = st.slider("Reinforcement mechanisms", 1, 5, 3)

scores = [leadership, decision_rights, skills, governance, reinforcement]

if st.button("Calculate Readiness"):
    readiness = round((sum(scores) / 25) * 100, 1)

    st.subheader(f"Readiness Score: {readiness}%")

    if readiness < 50:
        st.write("High risk: foundational adoption gaps.")
    elif readiness < 75:
        st.write("Moderate readiness: targeted intervention needed.")
    else:
        st.write("Strong readiness: ready to scale.")