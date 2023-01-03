import streamlit as st
import function_todo

todos = function_todo.get_todos()


def add_todo():
    new_todo = st.session_state['new_todo']+'\n'
    todos.append(new_todo)
    function_todo.write_todos(todos)


st.title("To-Do App")
st.subheader("Your Daily Friend")
st.write("Let's Get Started")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        function_todo.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label='', placeholder='Add new todo....', on_change=add_todo, key='new_todo')
