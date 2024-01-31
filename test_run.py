from selenium.webdriver.common.by import By
from helper import Helper
from config import input, url
import time
import os


def test_auto_result(driver):

    inp_search = (By.ID, "searchInp")
    btn_search = (By.ID, "submit_search")
    list_result = (By.XPATH, "//div[@id='search-result']/div//span[@class='card-title bold']")
    dropdown_menu = (By.ID, "//div[@id='searchDiv-small']")
    auto_obj = Helper(driver)

    auto_obj.get_the_page(url)
    auto_obj.enterValue(inp_search, input.lower(), 120)
    auto_obj.wait_element_visibility(dropdown_menu, 20)
    auto_obj.clickElement(btn_search, 80)
    my_url = auto_obj.getMyUrl()


    assert my_url != url.lower() , "Urls are same"
    
    result_list = auto_obj.getList(list_result, 20)
          
    assert len(result_list) > 0
    
    first_elem_text = auto_obj.get_firstElm_Text(list_result, 20).lower()
    
    assert input.lower() in first_elem_text, f"Expected 'kia' to be in the first result, but got: {first_elem_text}"

    
   


