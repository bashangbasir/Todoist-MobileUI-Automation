 """
TEST CASE 1 - “Create Project”
1.Create test project via API.
2.Login into mobile application.
3.Verify on mobile that project is created

TEST CASE 2 - “Create Task via mobile phone”
1.Create test task via mobile application in test project.
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

test_task_id = ""
task_name = "Create Task 1"
project_id = ""
project_name = "Test Project 1"

def test_create_project(driver):

    #1.Create test project via API.
    api = TodoistAPI()
    r = api.create_project(project_name)
    project_id = r.json()["id"]
    assert (r.status_code == 200), "Project not created."

    #2.Login into mobile application.
    welcome_page = WelcomePage(driver)
    assert "Welcome to Todoist" in welcome_page.get_welcome_message(),"Wrong Welcome title"
    welcome_page.start_login_with_email()
    login_page = LoginPage(driver)
    login_page.login()
    user_home_page = UserHomePage(driver)
    assert "Today" in user_home_page.get_toolbar_title() , "Wrong toolbar title"

    #Verify on mobile that project is created
    all_projects = user_home_page.get_all_projects()
    assert project_name in all_projects , "The created project is not in the mobile app" 
    print(project_id)
    raise Exception("Test Incomplete!")

def test_create_task_via_mobile_app(driver):
   #TODO
   pass

def test_reopen_task(driver):
    #TODO
    pass
