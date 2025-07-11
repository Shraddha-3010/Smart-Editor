import json

from flask import Flask, render_template, request, redirect, url_for, flash,jsonify,session
import os, sys, io, subprocess
from pathlib import Path


# Import the Python SDK
import google.generativeai as genai
# Used to securely store your API key
#from google.colab import userdata

"""from flask_wtf import FlaskForm"""
from src.usermodel import UserManager

app = Flask(__name__)
app.secret_key = 'your_secret_key'


project_files_path ="static/project_files/"
userMgrObj = UserManager()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/new-content', methods=["POST"] )
def save_content():
    print("saveContent")
    data = request.get_json()
    filename = data.get('filename', '')
    content = data.get('content', '')
    try:
        with open(project_files_path + filename, 'w') as f:
            f.write(content)
        print(f"saved file: {filename}")
        return "File Saved"
    except Exception as e:
        print("Error in saving file:")
        return "Error"


    #saved in list
@app.route('/list-files', methods=["GET"])
def list_files():
    try:
        files = os.listdir(project_files_path)
        return jsonify({"status": "success", "files": files})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

    #load file method


@app.route('/load-content', methods=["POST"])
def load_file():
    data = request.get_json()
    filename = data.get('filename')
    full_path = os.path.join(project_files_path, filename)

    try:
        with open(full_path, 'r') as f:
            content = f.read()
        return jsonify({"status": "success", "content": content})
    except FileNotFoundError:
        return jsonify({"status": "error", "message": "File not found."})


@app.route('/register', methods=["POST","GET"] )
def register():
    response=""
    if request.method == "POST":
        name = request.form.get("username")
        email = request.form.get("email")
        contactnumber = request.form.get("number")
        password = request.form.get("pwd")
        confirm_password = request.form.get("conpwd")

        if password != confirm_password:
            print("Confirm Password does not match!")
            response = "Confirm Password does not match!"

        else:
            isvalid, msg = userMgrObj.validate_user(email, password)
            registration = False
            if not isvalid:
                registration = userMgrObj.register_user(name, email, password, contactnumber)
                print("registration successful")
                response ="registration successful"
                return render_template('login.html', response=response)
            else:
                response = "User with email "+ email + " already registered!"

    print("registration un-successful")
    return render_template('register.html', response=response)


@app.route('/login', methods=["POST","GET"] )
def login():
    isvalid=False
    msg =""
    print("login")
    print( request.method )
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("pwd")
        print(email, password)
        isvalid, msg = userMgrObj.validate_user(email, password)
        if isvalid:
            session['user'] = email  # Store user in session
            return redirect(url_for('editor'))
        else:
            flash('Invalid credentials. Please try again.')
            return redirect(url_for('login'))

    return render_template('login.html', response=msg)

@app.route('/editor')
def editor():
    if 'user' not in session:
        return redirect(url_for('login'))
    try:
        files = os.listdir(project_files_path)
    except Exception as e:
        files = []
    return render_template('editor.html', savedfiles=files)


import re

def extract_json_from_text(text):

    # Use regular expression to find JSON structure in the text

    #json_match = re.search(r'\{.*\}', text, re.DOTALL)
    json_match = re.search(r"```json\s*(\{.*\})\s*```", text, re.DOTALL)
    if json_match:
        json_str = json_match.group(1)
        return json.loads(json_str)
    return None

@app.route('/ai-prompt', methods=['POST'])
def ai_prompt():
    try:
        # Get the Python code from the request
        print("prompt")
        data = request.json
        prompt = data.get('prompt', '')
        context = data.get('context', '')


        # Execute the ai prompt
        genai.configure(api_key="AIzaSyBalyBj_PXyVFr7UauzJP5Y1yohWY9U-zc")
        model = genai.GenerativeModel('gemini-1.5-flash')

        pre_prompt= ("Please provide the solution to my Python programming question in JSON format. Use the key 'python_code' for "
                     "the Python script and the key 'explanation' for a detailed explanation of the code. only give best "
                     "solution. not more than one, for the prompt. ")

        prompt = pre_prompt + prompt
        if context !="":
            prompt =  prompt + " refer this code context: " + context
        # print(prompt)
        response = model.generate_content(prompt)
        print(response)
        #print(response.text)

        formated_output  =extract_json_from_text(response.text)

        print(formated_output  )
        return jsonify({'status': 'success', 'result': formated_output["explanation"], 'code': formated_output["python_code"]})

    except Exception as e:
        # Ensure stdout is restored even on error
        return jsonify({'status': 'error', 'message': str(e)})


# run route

@app.route('/run-python', methods=['POST'])
def run_python(old_stdoute=None):
    try:
        # Get the Python code from the reques
        data = request.json
        python_code = data.get('code', '')

        # Redirect stdout to capture print outputplp-
        old_stdout = sys.stdout
        redirected_output = io.StringIO()
        sys.stdout = redirected_output

        # Execute the Python code
        exec_globals = {}
        exec(python_code, exec_globals)

        # Reset stdout
        sys.stdout = old_stdoute

        # Get print output
        output = redirected_output.getvalue()

        # Check if there's a `result` variable to include
        result_var = exec_globals.get('result')
        if result_var is not None:
            output += f"\nresult = {result_var}"

        return jsonify({'status': 'success', 'result': output})

    except Exception as e:
        # Ensure stdout is restored even on error
        sys.stdout = old_stdout
        return jsonify({'status': 'error', 'message': str(e)})


@app.route('/create-project_files', methods=['POST'])
def create_project():
    data = request.get_json()
    project_name = data.get('project_files')
    path = os.path.join(project_files_path, project_name)
    try:
        os.makedirs(path)
        return jsonify({'status': 'success'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})


import os

@app.route("/project-structure")
def project_structure():
    def build_tree(path):
        if os.path.isdir(path):
            return {
                "name": os.path.basename(path),
                "type": "folder",
                "children": [build_tree(os.path.join(path, f)) for f in os.listdir(path)]
            }
        else:
            return {"name": os.path.basename(path), "type": "file", "path": path}

    root_path = "your_project_root"
    return jsonify(build_tree(root_path))







@app.route('/create-file', methods=["POST"])
def create_file():
    data = request.json
    file_path = os.path.join("static/projects", data.get("filepath"))

    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w') as f:
            f.write("")  # empty file
        return jsonify({"status": "success", "message": f"File '{file_path}' created."})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

@app.route('/create-folder', methods=["POST"])
def create_folder():
    data = request.json
    folder_path = os.path.join("static/projects", data.get("folderpath"))

    try:
        os.makedirs(folder_path, exist_ok=True)
        return jsonify({"status": "success", "message": f"Folder '{folder_path}' created."})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})


@app.route('/delete-path', methods=["POST"])
def delete_path():
    data = request.json
    rel_path = data.get("path")
    abs_path = os.path.join("static/projects", rel_path)

    try:
        if os.path.isdir(abs_path):
            os.rmdir(abs_path)  # only works if empty
        else:
            os.remove(abs_path)
        return jsonify({"status": "success", "message": f"Deleted {rel_path}."})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})


@app.route('/rename-path', methods=["POST"])
def rename_path():
    data = request.json
    old_path = os.path.join("static/projects", data.get("old_path"))
    new_path = os.path.join("static/projects", data.get("new_path"))

    try:
        os.rename(old_path, new_path)
        return jsonify({"status": "success", "message": "Renamed successfully."})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})





if __name__ == '__main__':
    app.run(debug=True)
    #app.add_url_rule('/',"\'hello', hello_world)