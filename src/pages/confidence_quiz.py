import streamlit as st
from confidence_quiz import ConfidenceQuiz

def main():
    st.title("Workplace Confidence Assessment")
    st.markdown("""
    Evaluate your workplace confidence level with this quick assessment. 
    Your responses will help identify strengths and areas for growth.
    """)
    
    # Initialize quiz
    if 'quiz' not in st.session_state:
        st.session_state.quiz = ConfidenceQuiz()
    
    # Initialize answers if not in session state
    if 'answers' not in st.session_state:
        st.session_state.answers = []
    
    # Initialize current question if not in session state
    if 'current_question' not in st.session_state:
        st.session_state.current_question = 0
    
    quiz = st.session_state.quiz
    
    if st.session_state.current_question < len(quiz.questions):
        # Show current question
        question = quiz.questions[st.session_state.current_question]
        st.subheader(f"Question {st.session_state.current_question + 1}")
        st.write(question["question"])
        
        # Create radio buttons for answers
        answer = st.radio(
            "Choose your response:",
            options=list(question["options"].keys()),
            format_func=lambda x: f"{x}: {question['options'][x]}"
        )
        
        # Next button
        if st.button("Next"):
            st.session_state.answers.append(answer)
            st.session_state.current_question += 1
            st.rerun()
            
    else:
        # Calculate and show results
        if len(st.session_state.answers) == len(quiz.questions):
            results = quiz.calculate_score(st.session_state.answers)
            
            # Display score
            st.header("Your Confidence Assessment Results")
            col1, col2, col3 = st.columns([1,2,1])
            with col2:
                st.metric(
                    "Confidence Score", 
                    f"{results['percentage']:.0f}%",
                    help="Based on your responses to the assessment"
                )
            
            # Display feedback
            st.subheader(f"Level: {results['feedback']['level']}")
            st.write(results['feedback']['summary'])
            
            # Display strengths
            st.subheader("💪 Your Strengths")
            for strength in results['feedback']['strengths']:
                st.markdown(f"- {strength}")
            
            # Display next steps
            st.subheader("🎯 Recommended Next Steps")
            for step in results['feedback']['next_steps']:
                st.markdown(f"- {step}")
            
            # Display interview tips
            st.subheader("💡 Interview Strategy Tips")
            for tip in results['feedback']['interview_tips']:
                st.markdown(f"- {tip}")
            
            # Reset button
            if st.button("Take Assessment Again"):
                st.session_state.answers = []
                st.session_state.current_question = 0
                st.rerun()

if __name__ == "__main__":
    main()