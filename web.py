import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo = st.session_state['new todo'] + '\n'
    todos.append(todo)
    functions.write_todos(todos)


st.title('My Todo App')
st.subheader("This is my Todoapp")
st.write("This app is to increase your productivity")

for i, todo in enumerate(todos):
    checkbox = st.checkbox(f"{i+1}- {todo}", key=todo)
    if checkbox:
        todos.pop(i)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="Enter a ToDo:", placeholder="Add a new todo...",
              on_change=add_todo, key='new todo')
