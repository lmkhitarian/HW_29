from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from config import logFileName
import logging
import pytest
import os

def pytest_configure():
    log_file_path = os.path.join(os.path.dirname(__file__), logFileName)
    logging.basicConfig(
                        level=logging.INFO,
                        format="%(asctime)s %(levelname)s - %(message)s",
                        datefmt="%Y-%m-%d %H:%M:%S",
                        filename=log_file_path,
                        filemode="w"
                        )

@pytest.fixture()
def driver():
    try:
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        driver = webdriver.Chrome(options=options)
        logging.info("Browser is opened successfully")
        driver.maximize_window()
        yield driver
    except WebDriverException as web_driver_error:
        raise web_driver_error
    except Exception as error:
        raise Exception(error)
    finally:
        driver.quit()
        logging.info("Browser is closed successfully")
        
