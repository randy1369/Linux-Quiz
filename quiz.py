# quiz.py
import streamlit as st
import yaml


def load_questions(file_path):
    with open(file_path, 'r') as file:
        questions = yaml.safe_load(file)
    return questions['questions']

def display_quiz_question(question_data, index, tab_index):
    st.subheader(str(int(index)+ 1) + ')  ' + question_data['question'])
    options = question_data['options']
    unique_key = f"radio_{tab_index}_{index}"
    user_answer = st.radio("Options", options,key=unique_key, format_func=lambda x: x[3:])
    
    return user_answer

def check_answer(question_data, user_answer):
    return user_answer[0].upper() == question_data['answer'].upper()

def quiz(fpath, tab_index):

    # fpath = 'quiz/lf-set-1.yaml'
    questions = load_questions(fpath)
    
    # Initialize or retrieve the score from st.session_state
    if 'score' not in st.session_state:
        st.session_state.score = 0

    for index, question_data in enumerate(questions):

        user_answer = display_quiz_question(question_data, index, tab_index)
        
        unique_key = f"submit_button_{fpath}_{index}_{tab_index}"

        
        if st.button("Submit", key=unique_key):
            
            if check_answer(question_data, user_answer):
                st.success("Correct!")
                st.session_state.score += 1  # Update the score in st.session_state
            else:
                st.error("Incorrect! Try again.")

            
            # Display the current score after each question
            st.write(f"Your current score: {st.session_state.score}/{len(questions)}")
        st.write("---")  # Separator between tasks
            
    # Display the final score and a congratulatory message
    if st.session_state.score == len(questions):
        st.success("Congratulations! You answered all questions correctly.")
        st.balloons()
    elif st.session_state.score >= len(questions) / 2:
        st.info("Good effort! You answered more than half of the questions correctly. Keep it up.")
    else:
        st.warning("You may want to review the material. Better luck next time.")


