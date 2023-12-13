import streamlit as st
import yaml

def load_tasks(file_path):
    with open(file_path, 'r') as file:
        tasks_data = yaml.safe_load(file)
    return tasks_data.get('questions', [])  # Use get to handle cases where 'questions' key is not present

def display_task(task_data, task_number):
    # Display the task question and instructions
    st.markdown(f"**Task {task_number}:**")
    st.markdown(f"**Question:** {task_data['question']}")
    st.markdown(f"**Instructions:** {task_data['instructions']}")

    # Provide instructions based on the answer format
    if '\n' in task_data['answer']:
        st.markdown("For this question, provide your answer as a list of items, separated by commas.")
    else:
        st.markdown("For this question, provide your answer in the text input below.")


def show_answer(task_data):
    # Display the answer to the task
    st.markdown(f"**Answer:** {task_data['answer']}")



def submit_answer(task_data, user_answer):
    # Split the correct answer into lines
    correct_answer_lines = task_data['answer'].split('\n')

    # Split the user's answer into lines
    user_answer_lines = [line.strip() for line in user_answer.split(',')]

    # Check each line of the user's answer
    for user_line in user_answer_lines:
        # Check if the user's line is in the list of correct answers
        if user_line in map(str.strip, correct_answer_lines):
            st.success("Correct! 👍")
            return True

    # If none of the lines match
    st.error("Incorrect. 😟 Try again.")
    return False



def task(fpath, tab_index, category):
    # Load tasks data based on the file path
    
    tasks_data = load_tasks(fpath)

    if 'score' not in st.session_state:
        st.session_state.score = 0

    # Display each task
    for i, task_data in enumerate(tasks_data, start=1):
        st.header(f"Task {i}")

        # Display the task and instructions
        display_task(task_data, i)

        # Show Answer button
        show_answer_button_key = f"show_answer_button_{i}_{tab_index}_{category}"
        if st.button("Show Answer", key=show_answer_button_key):
            show_answer(task_data)

        # User input for the answer
        user_answer_key = f"user_answer_{i}_{tab_index}_{category}"
        user_answer = st.text_input("Your Answer:", key=user_answer_key)


        # Submit button
        submit_button_key = f"submit_button_{i}_{tab_index}_{category}"
        if st.button("Submit", key=submit_button_key):
            if submit_answer(task_data, user_answer):
                st.session_state.score += 1
                st.write(f"Your current score: {st.session_state.score}/{len(tasks_data)}")

        st.write("---")  # Separator between tasks

    # Display the final score
    st.success(f"Your final score: {st.session_state.score}/{len(tasks_data)}")
