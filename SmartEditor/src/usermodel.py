import json

class UserManager:
    def __init__(self):
        self.userRecords = {}
        # Opening JSON file
        with open('src/userdata.json') as json_file:
            self.userRecords = json.load(json_file)

    def register_user(self, name, email, pwd, contactnumber):
        user = {
            "name": name,
            "email": email,
            "password": pwd,
            "contactnumber": contactnumber
        }
        self.userRecords.update({email: user})

        print("User have been registered successfully.")
        print(self.userRecords)
        # Opening JSON file
        with open('src/userdata.json', "w") as json_file:
            json_file.write(json.dumps(self.userRecords))
           # json.dump(self.userRecords, json_file)

        return True

    def validate_user(self, email, pwd):
            print(self.userRecords.keys())
            if email in self.userRecords.keys():
                user = self.userRecords[email]
                if user["password"] ==pwd:
                    print("User authenticated successfully.")
                    return True, "User authenticated successfully."
                else:
                    print("In-correct password")
                return False, "In correct password"
            else:
                print("User is not registered")
            return False, "User is not registered"

    def update_user_profile(self, email, new_name, new_contact):
        try:
            if email in self.userRecords:
                self.userRecords[email]["name"] = new_name
                self.userRecords[email]["contactnumber"] = new_contact
                with open('src/userdata.json', "w") as json_file:
                    json.dump(self.userRecords, json_file)
                return True
            else:
                return False
        except Exception as e:
            print(f"Error updating user profile: {e}")
            return False

    def get_user_by_email(self, email):
        try:
            if email in self.userRecords:
                user = self.userRecords[email]
                return {
                    "name": user["name"],
                    "email": user["email"],
                    "contact": user["contactnumber"]
                }
            else:
                return None
        except Exception as e:
            print(f"Error fetching user: {e}")
            return None
