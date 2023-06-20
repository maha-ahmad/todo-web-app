import streamlit as st
import functions


todos = functions.get_todos()

def add_todo():
    todo = st.session_state.new_todo.strip() + '\n'
    todos.append(todo)
    functions.write_todos(todos)


st.title('To-Do List App')
st.write('This app is to increase your productivity...')

if len(todos) > 0:
    for index, todo in enumerate(todos):
        checked = st.checkbox(todo, key=todo)
        if checked:
            todos.pop(index)
            functions.write_todos(todos)
            del st.session_state[todo]
            st.experimental_rerun()
else:
    st.write('To-Do list is empty..')

st.text_input(label="New To-do: ", placeholder='Add a new to-do...', on_change=add_todo, key='new_todo')

