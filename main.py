import streamlit as st
import json
import os

SETTINGS_FILE = 'settings.json'

def load_settings():
    if os.path.exists(SETTINGS_FILE):
        with open(SETTINGS_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_settings(settings):
    with open(SETTINGS_FILE, 'w') as f:
        json.dump(settings, f)

def create_new_note():
    st.session_state['page'] = 'create_new'

def open_note():
    st.session_state['page'] = 'open_note'

def main():
    
    if 'page' not in st.session_state:
        st.session_state['page'] = 'home'
    
    if st.session_state['page'] == 'home':
        st.button("Open", on_click=open_note)
        st.button("Create New", on_click=create_new_note)
    
    elif st.session_state['page'] == 'create_new':
        name = st.text_input("Name")
        password = st.text_input("Password", type="password")
        if st.button("Create"):
            settings = load_settings()
            settings[name] = {'password': password, 'note': ''}
            save_settings(settings)
            st.session_state['name'] = name
            st.session_state['page'] = 'note'
    
    elif st.session_state['page'] == 'open_note':
        name = st.text_input("Name")
        password = st.text_input("Password", type="password")
        if st.button("Open"):
            settings = load_settings()
            if name in settings and settings[name]['password'] == password:
                st.session_state['name'] = name
                st.session_state['page'] = 'note'
    
    elif st.session_state['page'] == 'note':
        settings = load_settings()
        note = st.text_area("Note", value=settings[st.session_state['name']]['note'], height=700)
        st.session_state['note'] = note
        if st.button("Save"):
            save_note()

def save_note():
    settings = load_settings()
    settings[st.session_state['name']]['note'] = st.session_state['note']
    save_settings(settings)
    st.success("Note saved")

if __name__ == "__main__":
    main()