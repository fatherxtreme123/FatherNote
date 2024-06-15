# Simple Note Application

## Overview

This is a simple note-taking application built with Streamlit. The application allows users to create new notes, open existing notes, and save their changes securely with password protection. The notes are stored locally in a JSON file.

## Features

- **Create New Note**: Users can create a new note by providing a name and a password.
- **Open Existing Note**: Users can open an existing note by providing the correct name and password.
- **Edit and Save Note**: Users can edit the content of their notes and save their changes.

## Installation

To run this application, you need to have Python and Streamlit installed. Follow the steps below to get started.

### Prerequisites

- Python 3.6 or later
- Streamlit

### Steps

1. **Clone the Repository**
   
   Clone this repository to your local machine using the following command:
   ```sh
   git clone https://github.com/fatherxtreme123/FatherNote
   ```
   Navigate to the project directory:
   ```sh
   cd FatherNote
   ```

2. **Install Dependencies**

   install Streamlit directly:
   ```sh
   pip install streamlit
   ```

3. **Run the Application**

   Run the Streamlit application using the command:
   ```sh
   streamlit run app.py
   ```

   This will start the Streamlit server and open the application in your default web browser.

## Usage

1. **Home Page**
   
   On the home page, you will see two buttons: "Open" and "Create New".
   - Click **Open** to open an existing note.
   - Click **Create New** to create a new note.

2. **Create New Note**

   If you choose to create a new note:
   - Enter a **Name** for your note.
   - Enter a **Password** for your note.
   - Click the **Create** button to create the note.

3. **Open Existing Note**

   If you choose to open an existing note:
   - Enter the **Name** of your note.
   - Enter the **Password** for your note.
   - Click the **Open** button to open the note.

4. **Edit and Save Note**

   Once you have created or opened a note:
   - Edit the content of your note in the text area provided.
   - Click the **Save** button to save your changes.
