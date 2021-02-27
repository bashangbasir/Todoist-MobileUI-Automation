"""
TEST CASE 1 - “Create Project”
1.Create test project via API.
2.Login into mobile application.
3.Verify on mobile that project is created

TEST CASE 2 - “Create Task via mobile phone”
1. Create test task via mobile application in test project.
2. API: Verify that task created correctly.

TEST CASE 3 - “Reopen Task”
1. Open mobile application
2. Open test project
3. Created test task
4. Complete test task.
5. Reopen test task via API.
6. Mobile: Verify that test task appears in your test project.
"""
import pytest
from pages.welcome_page import WelcomePage
from pages.login_page import LoginPage
from pages.user_home_page import UserHomePage
from api.todoist_api import TodoistAPI
import time

def test_create_project(driver):

    #1.Create test project via API.
    todoist_api = TodoistAPI()
    r = todoist_api.create_project("TEST PROJECT")
    todoist_api.save_response(r,"project.json")
    assert (r.status_code == 200), "Project not created."

    #2.Login into mobile application.
    welcome_page = WelcomePage(driver)
    assert "Welcome to Todoist" in welcome_page.get_welcome_message(),"Wrong Welcome title"
    welcome_page.start_login_with_email()
    login_page = LoginPage(driver)
    login_page.login()
    user_home_page = UserHomePage(driver)
    assert "Today" in user_home_page.get_toolbar_title("Today") , "Wrong toolbar title"

    #Verify on mobile that project is created
    all_projects = user_home_page.get_all_projects()
    assert todoist_api.load_save_data("project.json")["name"] in all_projects , "The created project is not in the mobile app" 
    
    #raise Exception("Test Incomplete!")

def test_create_task_via_mobile_app(driver):
    todoist_api = TodoistAPI()
    #read the saved reponse previous test
    data = todoist_api.load_save_data("project.json")
    project_name = data["name"]
    project_id = data["id"]
    #1. Create test task via mobile application in test project.
    welcome_page = WelcomePage(driver)
    assert "Welcome to Todoist" in welcome_page.get_welcome_message(),"Wrong Welcome title"
    welcome_page.start_login_with_email()
    login_page = LoginPage(driver)
    login_page.login()
    user_home_page = UserHomePage(driver)
    assert "Today" in user_home_page.get_toolbar_title("Today") , "Wrong toolbar title"
    user_home_page.go_to_project(project_name)
    assert project_name in user_home_page.get_toolbar_title(project_name), "Wrong project"
    task_name = "TASK CREATE"
    user_home_page.create_task(task_name)
    print(project_id)
   
    #2. API: Verify that task created correctly.
    time.sleep(3)
    r = todoist_api.get_active_tasks(project_id)
    #save response
    todoist_api.save_response(r,"task.json")
    assert r.status_code == 200 , "not able to get active task"
    assert r.json()[0]["content"] == task_name , "Task is not created"
    
    #raise Exception("Test Incomplete!")
    

def test_reopen_task(driver):
    #TODO
    raise Exception("Test Incomplete!")
    pass
