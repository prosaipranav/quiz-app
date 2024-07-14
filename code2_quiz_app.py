import streamlit as st
from quiz_data import quiz_data

# Function to display the current question and choices
def show_question():
    question = quiz_data[st.session_state.current_question] 
    st.info(question['question']) # Selects the question within the dictionary being accessed by previous line within the quiz_data list.
    selected_choice = st.radio("Select your answer:", question['choices']) 
    submit_button = st.button("Submit ") 
    st.write("---")
    next_q=st.button("Next Question")
    if submit_button:
        check_answer(selected_choice)
        st.session_state.show_question = False
        next_question()

    
    

# Function to check the selected answer and provide feedback
def check_answer(selected_choice):
    question = quiz_data[st.session_state.current_question]
    if selected_choice == question["answer"]:
        st.success("Correct!:tada:")
        st.balloons()
        st.session_state.score += 1

        
    else:
        st.error(f"Sorry, that's incorrect :exclamation:. The correct answer is: {question['answer']}")
    

# function to move onto the next question
def next_question():
    current_question = st.session_state.current_question + 1
    if current_question < len(quiz_data): 
        st.session_state.current_question = current_question 
        st.session_state.show_question = True 
    else:
        st.success("Quiz Complete! Your Score: {}/{}".format(st.session_state.score, len(quiz_data)))

# Main function - initialising the 3 session state variables.
def main():
    if 'current_question' not in st.session_state:
        st.session_state.current_question = 0 
    if 'score' not in st.session_state:
        st.session_state.score = 0
    if 'show_question' not in st.session_state:
        st.session_state.show_question = True

    st.title(" Quiz")
    
    if st.session_state.show_question:
        show_question()

if __name__ == "__main__":
    main()