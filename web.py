import streamlit as st
import functions
todos = functions.get_todos('todos.tx')
def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos('todos.tx', todos)


st.title("My todo App")
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo.capitalize(), key = f'checkbox_{index}')
    if checkbox:
        todos.pop(index)
        functions.write_todos('todos.tx', todos)
        del st.session_state[f'checkbox_{index}']



st.text_input(label="", placeholder="Add new todo...", on_change= add_todo, key ='new_todo')
