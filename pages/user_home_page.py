"""
This module contain the page object for the user home page.
"""

from appium.webdriver.common.mobileby import MobileBy 
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction


class UserHomePage:
    
    BURGER_NAV = (MobileBy.ACCESSIBILITY_ID,"Change the current view")
    ALL_PROJECT_LISTS = (MobileBy.XPATH,"*//android.widget.RelativeLayout[@resource-id='android:id/content']")
    PROJECT_TEXT = (MobileBy.XPATH,"//android.widget.TextView[@resource-id='com.todoist:id/name']")
    PROJECTS_BTN = (MobileBy.XPATH,"*//android.widget.RelativeLayout/android.widget.TextView[@text='Projects']")
    CREATE_TASK_BTN = (MobileBy.ID,"com.todoist:id/fab")
    TASK_CONTENT_TEXTBOX = (MobileBy.ID,"android:id/message")
    ADD_TASK_BTN = (MobileBy.ACCESSIBILITY_ID,"Add")

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
        xpath_project = f"//android.widget.RelativeLayout//android.widget.TextView[@text='{project_name}']"
        self.driver.find_element(*self.BURGER_NAV).click()
        self.driver.find_element(*self.PROJECTS_BTN).click()
        self.driver.find_element(MobileBy.XPATH,xpath_project).click()
        #project_elems = self.driver.find_elements(*self.ALL_PROJECT_LISTS)

        

    def create_task(self,task_name):
        self.driver.find_element(*self.CREATE_TASK_BTN).click()
        self.driver.find_element(*self.TASK_CONTENT_TEXTBOX).send_keys(task_name)
        self.driver.find_element(*self.ADD_TASK_BTN).click()
        self.driver.find_element(*self.ADD_TASK_BTN).click()
        
        #self.driver.press_keycode(4)

    def complete_task(self,task_name):
        self.driver.find_element(MobileBy.XPATH, f"//android.widget.TextView[@text='{task_name}']").click()
        self.driver.find_element_by_id("com.todoist:id/item_checkmark").click()
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((MobileBy.ID, "com.todoist:id/snackbar_text")))
        return self.driver.find_element_by_id("com.todoist:id/snackbar_text").text


    def refresh_page_by_swipe(self):
        TouchAction(self.driver).press(x=515, y=1200).move_to(x=515, y=1600).release().perform()
        

    def get_task(self,task_name):
        return self.driver.find_element(MobileBy.XPATH, f"//android.widget.TextView[@text='{task_name}']").text
        





