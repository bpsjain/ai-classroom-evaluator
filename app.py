import streamlit as st
import os
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Initialize session state
if "history" not in st.session_state:
    st.session_state.history = []

if "latest_result" not in st.session_state:
    st.session_state.latest_result = ""

# Page config
st.set_page_config(page_title="ScienceEval AI", layout="centered")

st.title("ScienceEval AI (V1)")
st.caption("Evaluate student answers quickly using AI")

# Mode selector
mode = st.radio("Select Mode", ["Demo Mode (No API)", "AI Mode (Requires API)"])

# Inputs
question = st.text_area("Enter Question")
answer = st.text_area("Enter Student Answer")

# Evaluate button
if st.button("Evaluate"):

    if not question or not answer:
        st.warning("Please enter both question and answer")

    else:
        # -------- DEMO MODE --------
        if mode == "Demo Mode (No API)":

            result = f"""
Understanding Level:
- Expected: Understand / Apply
- Achieved: Understand

Evidence:
- "{answer}"

Gap:
- Missing deeper explanation of scientific concept

Next Step:
- Add explanation of how the concept works in real context
"""

        # -------- AI MODE --------
        else:
            prompt = f"""
Evaluate the student answer.

Question: {question}
Answer: {answer}

Give:
- Expected level
- Achieved level
- Evidence
- Gap
- Next step
"""

            try:
                with st.spinner("Evaluating answer..."):
                    response = client.chat.completions.create(
                        model="gpt-4o-mini",
                        messages=[{"role": "user", "content": prompt}]
                    )

                result = response.choices[0].message.content

            except Exception as e:
                st.error("API not working. Switch to Demo Mode.")
                st.stop()

        # Save result safely
        st.session_state.latest_result = result

        # Save history
        st.session_state.history.append({
            "question": question,
            "answer": answer,
            "result": result
        })

# -------- DISPLAY RESULT --------
if st.session_state.latest_result:

    st.subheader("Evaluation Result")
    st.write(st.session_state.latest_result)

    # Download button (SAFE)
    st.download_button(
        label="📥 Download Evaluation",
        data=st.session_state.latest_result,
        file_name="evaluation.txt",
        mime="text/plain"
    )

# -------- HISTORY --------
st.markdown("---")
st.subheader("📜 Previous Evaluations")

for item in reversed(st.session_state.history):
    with st.expander("View Evaluation"):
        st.write("**Question:**", item["question"])
        st.write("**Answer:**", item["answer"])
        st.write(item["result"])