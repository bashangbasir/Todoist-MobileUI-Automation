"""
This module contain the page object for the user home page.
"""

from appium.webdriver.common.mobileby import MobileBy 
import time

class UserHomePage:
    
    BURGER_NAV = (MobileBy.ACCESSIBILITY_ID,"Change the current view")
    ALL_PROJECT_LISTS = (MobileBy.XPATH,"*//android.widget.RelativeLayout[@resource-id='android:id/content']")
    PROJECT_TEXT = (MobileBy.XPATH,"//android.widget.TextView[@resource-id='com.todoist:id/name']")
    PROJECTS_BTN = (MobileBy.XPATH,"*//android.widget.RelativeLayout/android.widget.TextView[@text='Projects']")
    CREATE_TASK_BTN = (MobileBy.ID,"com.todoist:id/fab")
    TASK_CONTENT_TEXTBOX = (MobileBy.ID,"android:id/message")
    ADD_TASK_BTN = (MobileBy.ACCESSIBILITY_ID,"Add")
    TASKS_LISTS = (MobileBy.ID,"com.todoist:id/root")
    TASK_TEXT = (MobileBy.XPATH)


    def __init__(self,driver):
        self.driver = driver

    def get_toolbar_title(self,toolbar):
        xpath = "*//android.view.ViewGroup[@resource-id='com.todoist:id/toolbar']/android.widget.TextView[@text='{}']".format(toolbar)
        return self.driver.find_element(MobileBy.XPATH,xpath).text

    def get_all_projects(self):
        all_projects = []
        self.driver.find_element(*self.BURGER_NAV).click()
        self.driver.find_element(*self.PROJECTS_BTN).click()
        project_elems = self.driver.find_elements(*self.ALL_PROJECT_LISTS)
        for elem in project_elems:
            #append all the project name seen from mobile app 
            all_projects.append(elem.find_element(*self.PROJECT_TEXT).text)
        return all_projects

    def go_to_project(self,project_name):
        xpath_project = "*//android.widget.RelativeLayout/android.widget.TextView[@text='{}'".format(project_name)
        self.driver.find_element(*self.BURGER_NAV).click()
        self.driver.find_element(*self.PROJECTS_BTN).click()
        project_elems = self.driver.find_elements(*self.ALL_PROJECT_LISTS)
        for elem in project_elems:
            if project_name == elem.find_element(*self.PROJECT_TEXT).text:
                elem.find_element(*self.PROJECT_TEXT).click()

        

    def create_task(self,task_name):
        self.driver.find_element(*self.CREATE_TASK_BTN).click()
        self.driver.find_element(*self.TASK_CONTENT_TEXTBOX).send_keys(task_name)
        self.driver.find_element(*self.ADD_TASK_BTN).click()
        self.driver.find_element(*self.ADD_TASK_BTN).click()
        
        #self.driver.press_keycode(4)






