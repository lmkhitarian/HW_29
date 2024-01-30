from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
import logging
import os
   


class Helper:
    def __init__(self, browser):
        self.browser = browser

    def get_the_page(self, url):
        try:
            self.browser.get(url)
            self.browser.set_page_load_timeout(60)
            logging.info(f"Navigated to URL: '{url}'.")
        except TimeoutException as error:
            logging.error(f"Timeout: {str(error)}")
        except Exception as e:
            logging.error(f"Exception in 'navigate_to_url': {e}")


    def getMyUrl(self):
        try:
            my_url = self.browser.current_url.lower()
            logging.info(f"Successfully got the URL: {my_url}")
            return my_url
        except Exception as e:
            logging.error(f"Exception in the process of getting the current URL: {e}")
            return None  

 
    def move_to_element(self, element_locator):
        try:
            element = self.browser.find_element(*element_locator)
            self.browser.execute_script("arguments[0].scrollIntoView();", element) 
            return element
        except Exception as e:
                logging.error(f"Exception in 'move_to_element': {e}")

        
    def wait_elements_visibility(self, element, timeout):
        try:
            elements = WebDriverWait(self.browser, timeout).until(EC.presence_of_all_elements_located(element))
            return elements
        except TimeoutException as e:
            logging.error(f"Timeout waiting for the element: {str(e)}")
            self.browser.save_screenshot(os.path.join(os.path.dirname(__file__), "wait.png"))
            return None
        except Exception as e:
            logging.error(f"An error occurred while waiting for the element: {str(e)}")
            self.browser.save_screenshot(os.path.join(os.path.dirname(__file__), "wait.png"))
            return None
        
    

    def clickElement(self, element_locator):
        element = self.move_to_element(element_locator)

        try:
            self.browser.execute_script("arguments[0].scrollIntoView(true);", element)
            element.click()
            logging.info(f"Successfully clicked  the element {element}")
        except Exception as e:
            logging.error("Element not found or not clickable within the specified timeout.")



    def getList(self, element_locator, timeout):
        try:
            elements = self.wait_elements_visibility(element_locator, timeout)
            logging.info(f"Successfully got list {elements}")
            return elements
        except NoSuchElementException as e:
            logging.error(f"Element not found: {str(e)}")
        except Exception as e:
            logging.error(f"An error occurred during the copying action: {str(e)}")
        return None
    
    def get_firstElm_Text(self, element_locator, timeout):
        try:
            elements = self.wait_elements_visibility(element_locator, timeout)

            if elements:
                element_text = elements[0].text
                logging.info(f"Successfully copied text from element with locator {element_locator}")
                return element_text
            else:
                logging.error(f"No elements found with locator {element_locator}")
        except NoSuchElementException as e:
            logging.error(f"Element not found: {str(e)}")
        except Exception as e:
            logging.error(f"An error occurred during the copying action: {str(e)}")
        return None

    def enterValue(self, element_locator, input):
        element = self.move_to_element(element_locator)
        try:
            element.click()
            element.clear()
            element.send_keys(input)
            logging.info(f"Successfully entered value {input} to  the element {element}")
        except ElementNotInteractableException as e:
            logging.error(f"The element {element} is not interactable: {str(e)}")
        except Exception as e:
            logging.error(f"An error occurred while entering value to the element {element}: {str(e)}")

    


            

           






  



    
 
            

    







        
