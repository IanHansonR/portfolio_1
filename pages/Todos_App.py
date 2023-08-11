import streamlit as st
import my_functions.todos_functions as functions

with open("todos.txt", 'a') as file:
    file.write("")
with open("goals.txt", "a") as file:
    file.write("")

todos = functions.get_todos()
goals = functions.get_goals()


def add_todo():
    if st.session_state.new_todo:
        todos.append(st.session_state.new_todo + "\n")
        functions.write_todos(todos)
        st.session_state.new_todo = ""


def add_goal():
    if st.session_state.new_goal:
        goals.append(st.session_state.new_goal + "\n")
        functions.write_goals(goals)
        st.session_state.new_goal = ""


st.title("Todos App")


st.subheader("Goals:")
new_goal = st.text_input('', placeholder='Enter a goal...',
                         key='new_goal', on_change=add_goal)
if st.button("Info"):
    st.write("Write one to three long-term goals that you would like to "
             "keep in mind while planning your day. You can check them "
             "off to help visualize your progress towards them.")
for index, goal in enumerate(goals):
    checkbox = st.checkbox(goal, key=goal)
if st.button("Delete Goal"):
    if st.session_state:
        goals.pop()
        functions.write_goals(goals)
        st.experimental_rerun()

st.subheader("")

st.subheader("My Todos:")
new_todo_text = st.text_input("", placeholder="Add a new todo...",
                              key='new_todo', on_change=add_todo)
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=index)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        st.experimental_rerun()



