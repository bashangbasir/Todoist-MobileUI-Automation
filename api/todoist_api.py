"""
This module is for todoist api 
"""
import json
import requests as requests
import uuid

class TodoistAPI:

    def __init__(self):
        with open("api_config.json","r") as api_config_file:
            api_config = json.load(api_config_file)

        self.auth_token = api_config["auth_token"]
        self.base_url = api_config["base_url"]

    def create_project(self,project_name):
        url = self.base_url + "/projects"
        
        response = requests.post( 
            url,
            data=json.dumps({
                "name": project_name
            }),
            headers={
                "Content-Type": "application/json",
                "X-Request-Id": str(uuid.uuid4()),
                "Authorization": self.auth_token
        })
        
        return response

    def get_projects(self):
        url = self.base_url + "/projects"
        response = requests.get(
            url,
            headers={
                "Authorization": self.auth_token
        })
        return response

    def create_task(self,content,project_id):
        
        url = self.base_url+ "/tasks"
        response = requests.post(
            url,
            data=json.dumps({
                "content": content,
                "project_id": project_id
            }),
            headers={
                "Content-Type": "application/json",
                "X-Request-Id": str(uuid.uuid4()),
                "Authorization": self.auth_token
        })

        return response

    def reopen_task(self,task_id):
        url = self.base_url + "/tasks" + task_id +"/reopen"
        response = requests.post( 
            url, 
            headers={
                "Authorization": "Bearer " + self.auth_token
        })
        return response
    
        

# if __name__ == "__main__":
#     API = TodoistAPI()
#     #print(API.auth_token,API.base_url)
#     try:
#         response = API.create_project("Bassam cccc")
#         print(response.status_code,response.text)
#         print(type(response.status_code),response.status_code)
#     except Exception as e:
#         print(e)
#     response = API.get_projects()
#     # print(response.status_code,response.json())