"""
This module contains shared fixtures 
"""

import pytest
from appium import webdriver
import json 

@pytest.fixture
def driver():
    
    desired_caps = dict(
        platformName='Android',
        #platformVersion='9',
        avd = "AppiumR",
        automationName='uiautomator2',
        deviceName='emulator-5556',
        appPackage= "com.todoist",
        appActivity= "com.todoist.activity.HomeActivity"
    )

    driver = webdriver.Remote("http://localhost:4723/wd/hub",desired_caps)
    driver.implicitly_wait(10)
    #return driver for setup 
    yield driver

    #quit webdriver for teardown 
    driver.quit()
