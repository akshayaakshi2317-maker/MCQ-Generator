import streamlit as st
from mcq_generator import generate_mcqs

st.set_page_config(
    page_title="AI MCQ Generator",
    page_icon="📝",
    layout="wide"
)

st.title("📝 AI MCQ Generator")
st.write("Generate multiple-choice questions from your study material.")

text = st.text_area(
    "📚 Enter your study material",
    height=250,
    placeholder="Paste your notes, textbook content, or study material here..."
)

col1, col2 = st.columns(2)

with col1:
    num_questions = st.number_input(
        "Number of Questions",
        min_value=1,
        max_value=20,
        value=5
    )

with col2:
    difficulty = st.selectbox(
        "Difficulty Level",
        ["Easy", "Medium", "Hard"]
    )

if st.button("🚀 Generate MCQs", use_container_width=True):

    if not text.strip():
        st.warning("Please enter some study material first.")
    else:
        with st.spinner("Generating MCQs..."):

            questions = generate_mcqs(
                text,
                num_questions,
                difficulty
            )

        st.success("MCQs generated successfully!")

        for i, question in enumerate(questions, start=1):

            st.subheader(f"Question {i}")
            st.write(question["question"])

            for option in question["options"]:
                st.write(f"**{option}**")

            with st.expander("View Answer"):
                st.write(f"✅ **Correct Answer:** {question['answer']}")
                st.write(f"💡 **Explanation:** {question['explanation']}")