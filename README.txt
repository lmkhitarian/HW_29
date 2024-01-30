# Task

        -- Preconditions:
                - Set up PyTest and Allure on your local computer


        --Note:
                -Get the driver as a fixture in conftest and use it in the test case. 
                Generate Allure Report with run result, make a screenshot and commit with your code.


        --Steps to reproduce:
                1)Navigate to auto.am
                2)Search car brand as – ‘Kia’
                3)Check that the result is not null




# Main  scenario is:
  - test_run files  => where  run test and locates are  locatored. 
  - Created custom fucntions in  helpper.py file
  - Created  conftest.py with driver function (get as fixture)  and pytest_confugure with logging configurations. 
  - config file stores url, log file name , input  and rootPath 
  - deleteFiles file stores fucntion for  deleting pycache files.
  - report folder with allure jsons
  - AllureScreen.jpg file  