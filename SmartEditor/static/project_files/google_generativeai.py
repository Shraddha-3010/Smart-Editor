import json

import re

from http.client import HTTPException


#fdkjsfdjskjf
import google.generativeai as genai   



#my new comment

def responsegenerator(prompt):

    data = None

    try:  # Set your API key

        genai.configure(api_key="AIzaSyBalyBj_PXyVFr7UauzJP5Y1yohWY9U-zc")

        # Generate text

        model = genai.GenerativeModel('gemini-1.5-flash')

        response = model.generate_content(prompt)

        response_text = response.text

        print("Data Type:", type(response_text))
        print("Autosave ")


        data = response_text  #extract_json_from_string(response_text)

        print(data)

    except Exception as e:

        raise HTTPException(status_code=500, detail=f"Error generate_content: {str(e)}")

    return data





def extract_json_from_text(text):

    # Use regular expression to find JSON structure in the text

    json_match = re.search(r'\{.*\}', text, re.DOTALL)

    if json_match:

        json_str = json_match.group(0)

        try:

            # Parse the extracted JSON string

            json_data = json.loads(json_str)

            return json_data

        except json.JSONDecodeError:

            return "Invalid JSON structure in the text"

    else:

        return "No JSON structure found in the text"





# Example usage

# text = '''Provide number of interview rounds along with details of each round for below job description {"company_profile": "software service industry", "summary": "We are looking for an experienced Java Full Stack Developer with skills in Microservices, Spring Boot, and Angular JS. This role is open to candidates located anywhere in India, with the primary work location in Bangalore. Ideal candidates should hold a Bachelor of Engineering degree and possess strong experience in full stack development. Interviews can be conducted remotely.", "description": {"position": "Java Full Stack Developer", "location": "Anywhere in India", "experience_range": "4-6 years", "interview_location": "Remote", "job_location": "Bangalore"}, "job_details": {"job_function": "Technology", "role": "Developer", "job_id": "338123", "required_skills": {"core_skills": ["Java Full Stack Development"], "desired_skills": ["Microservices", "Spring Boot", "Angular JS"]}, "desired_candidate_profile": {"qualifications": "Bachelor of Engineering"}}}. provide the answer in a json format only.'''

#

# # Call the function

# extracted_json = extract_json_from_text(text)

# print(extracted_json)



def extract_json_from_string(text):

    # Regular expression to find JSON block between ```json markers

    json_match = re.search(r"```json\n(.+?)\n```", text, re.DOTALL)



    # Check if JSON block was found

    if json_match:

        json_text = json_match.group(1)



        try:

            # Parse JSON to validate format

            parsed_json = json.loads(json_text)

            return parsed_json

        except json.JSONDecodeError:

            print("Invalid JSON format.")

            return text

    else:

        print("No JSON found in the text.")

        return text



# generate_content('Provide number of interveiw rounds  along with details of each round for below job description  {"comapny_profile": "software service industry", "summary": "We are looking for an experienced Java Full Stack Developer with skills in Microservices, Spring Boot, and Angular JS. This role is open to candidates located anywhere in India, with the primary work location in Bangalore. Ideal candidates should hold a Bachelor of Engineering degree and possess strong experience in full stack development. Interviews can be conducted remotely.", "description": {"position": "Java Full Stack Developer", "location": "Anywhere in India", "experience_range": "4-6 years", "interview_location": "Remote", "job_location": "Bangalore"}, "job_details": {"job_function": "Technology", "role": "Developer", "job_id": "338123", "required_skills": {"core_skills": ["Java Full Stack Development"], "desired_skills": ["Microservices", "Spring Boot", "Angular JS"]}, "desired_candidate_profile": {"qualifications": "Bachelor of Engineering"}}}. provide the answer in a json format only.')

