# main.py
import streamlit as st
from quiz import quiz
from tasks import task

def main():
    st.title("Linux Test App")

    # Sidebar structure
    st.sidebar.markdown("---")

    # Main categories
    main_categories = ["Quiz", "Tasks"]
    main_choice = st.sidebar.selectbox("Select Category", main_categories)

    if main_choice == "Quiz":
        # Nested dropdown for Quizes
        quiz_categories = ["Linux Fundamentals", "Linux for DevOps"]
        quiz_choice = st.sidebar.selectbox("Select Quiz Category", quiz_categories)

        if quiz_choice == "Linux Fundamentals":
            st.title("Linux Fundamentals Quiz...")
            tab1, tab2, tab3 = st.tabs(['SET-1', 'SET-2', 'SET-3'])
            with tab1:
                st.header("Set - 1")
                fpath = 'quiz/quiz-lf/lf-set-1.yaml'
                quiz(fpath, tab_index=1)
                
            with tab2:
                st.header("Set - 2")
                fpath = 'quiz/quiz-lf/lf-set-2.yaml'
                st.session_state.score = 0
                quiz(fpath, tab_index=2)

            with tab3:
                st.header("Set - 3")
                fpath = 'quiz/quiz-lf/lf-set-3.yaml'
                st.session_state.score = 0
                quiz(fpath, tab_index=3)



        elif quiz_choice == "Linux for DevOps":
            st.title("Linux for DevOps Quiz...")
            # Nested dropdown for Linux for DevOps sets
            tab1, tab2, tab3 = st.tabs(['SET-1', 'SET-2', 'SET-3'])
            with tab1:
                st.header("Set - 1")
                fpath = 'quiz/quiz-df/dlf-set-1.yaml'
                quiz(fpath, tab_index=1)
                
            with tab2:
                st.header("Set - 2")
                fpath = 'quiz/quiz-df/dlf-set-2.yaml'
                st.session_state.score = 0
                quiz(fpath, tab_index=2)

            with tab3:
                st.header("Set - 3")
                fpath = 'quiz/quiz-df/dlf-set-3.yaml'
                st.session_state.score = 0
                quiz(fpath, tab_index=3)


    elif main_choice == "Tasks":
        # Nested dropdown for Tasks
        tasks_categories = ["Linux Fundamentals Tasks", "Linux for DevOps Tasks"]
        task_choice = st.sidebar.selectbox("Select Task Category", tasks_categories)
        

        if task_choice == 'Linux Fundamentals Tasks':
            tab1, tab2 = st.tabs(["Beginner Tasks", "Intermeditae Tasks"])

            with tab1:
                st.header(" Beginner Tasks for Linux Fundamentals")
                fpath = 'Tasks/tasks-lf/b-tasks.yaml'
                st.session_state.score = 0
                task(fpath, tab_index=1, category="linux_fundamentals")
                
            with tab2:
                st.header(" Intermediate Tasks for Linux Fundamentals")
                fpath = 'Tasks/tasks-lf/i-tasks.yaml'
                st.session_state.score = 0
                task(fpath, tab_index=2, category="linux_fundamentals")
        

        elif task_choice == 'Linux for DevOps Tasks':
            tab1, tab2 = st.tabs(["Beginner Tasks", "Intermeditae Tasks"])

            with tab1:
                st.header("Linux for DevOps -  Beginner Tasks")
                fpath = 'Tasks/tasks-df/b-df-tasks.yaml'
                st.session_state.score = 0
                task(fpath, tab_index=1, category="linux_devops")
                
            with tab2:
                st.header("Linux for DevOps -  Intermediate Tasks")
                fpath = 'Tasks/tasks-df/i-df-tasks.yaml'
                st.session_state.score = 0
                task(fpath, tab_index=2, category="linux_devops")
            

if __name__ == "__main__":
    main()
