import streamlit as st
import json
from pathlib import Path
from coach import InterviewCoach

def load_questions():
    """Load interview questions from JSON file."""
    questions_path = Path(__file__).parent.parent / 'data' / 'questions.json'
    with open(questions_path, 'r') as f:
        return json.load(f)

def display_feedback(feedback: dict):
    """Display feedback in a structured format."""
    # Display strengths
    st.subheader("💪 Strengths")
    for strength in feedback['strengths']:
        st.markdown(f"- {strength}")

    # Display areas for improvement
    st.subheader("🌱 Areas for Growth")
    for area in feedback['areas_for_improvement']:
        st.markdown(f"- {area}")

    # Display action items
    st.subheader("✅ Action Items")
    for item in feedback['action_items']:
        st.markdown(f"- {item}")

    # Display tips
    st.subheader("💡 Tips")
    for tip in feedback['tips']:
        st.markdown(f"- {tip}")

    # Display confidence score
    st.subheader("Confidence Score")
    st.progress(feedback['confidence_score'] / 100)
    st.write(f"Score: {feedback['confidence_score']:.0f}/100")

def main():
    st.set_page_config(
        page_title="Interview Coach",
        page_icon="👩‍💼",
        layout="wide"
    )

    st.title("Professional Development Interview Coach")
    st.markdown("""
    Practice your interview skills and get feedback on your responses. 
    Focus on leadership, negotiation, and professional growth.
    """)

    # Initialize coach if not in session state
    if 'coach' not in st.session_state:
        st.session_state.coach = InterviewCoach()

    # Load questions
    questions = load_questions()

    # Create two columns
    col1, col2 = st.columns([1, 2])

    with col1:
        # Question selection
        category = st.selectbox(
            "Select Category",
            options=questions.keys(),
            help="Choose the type of question you want to practice"
        )

        # Get questions for selected category
        category_questions = questions[category]["questions"]
        selected_question = st.selectbox(
            "Select Question",
            options=[q["question"] for q in category_questions],
            help="Choose a specific question to answer"
        )

    with col2:
        # Response input
        user_response = st.text_area(
            "Your Response",
            height=150,
            help="Type your response here. Try to be specific and provide examples."
        )

        if st.button("Get Feedback", type="primary"):
            if user_response:
                # Get feedback from coach
                feedback = st.session_state.coach.analyze_response(
                    selected_question,
                    user_response,
                    category
                )
                
                # Save feedback
                st.session_state.coach.save_feedback(feedback)
                
                # Display feedback
                display_feedback(feedback)
            else:
                st.warning("Please enter your response before requesting feedback.")

if __name__ == "__main__":
    main()