## Python Behave Web Testing Accelerator

<br/>

>### This solution/accelerator helps in automating Web scenarios in python using Behave Framework. This will help in automating complex functional scenarios and can be executed on different environments as per the requirement. This solution supports different data parsers such as google sheets, excel, csv, json. This solution supports parallel and sequential execution and after completion of execution the standard reports are available.

<br />

### Folder structure
    src
    |- allure_reports
        |--reports
            |--- ...
        |--results
            |--- ... 
    |- config
        |-- ...                  
    |- data_providers
        |-- ...
    |- reports
        |-- ...                 
    |- logs
        |-- ...               
    |- tests
        |-- features
            |--- ...
        |-- steps
            |--- ...
        |-- pages
            |--- ...
        |-- utils
            |--- ...
        |-- web_element
            |--- ...
        |- readme.md
        |- requirements.txt
        |- behave-parallel.py
    
- In BDD we write test cases in .feature file and it should be created under `src\tests\<folder>`.
- Test data should be kept under the folders `\src\tests\testdata\<env>` in respective folder as per the environment.
- Common utility files can be found under `src\utils`.
- Project utility files can be found under `src\tests\utils`.
- Config files can be found under `src\config`.
- Data Provider files can be found `under src\data_providers`.
- Page Object Models can be found `under src\tests\pages`.
- Web elements can be found under `src\tests\web_elements`.
- Test steps can be found under `src\tests\steps`.
- Feature Files can be found under `src\tests\<folder>`.

### Dependencies
-   Python version 2.7.x
-   behave 1.2.6
-   WooCommerce 2.1.1
-   Faker 3.0.1
-   configparser 4.0.2
-   msedge-selenium-tools 3.141.2
-   parse 1.17.0
-   selenium 3.141.0
-   xlrd 1.2.0
<br />

- **`To use google-sheets, please install the given below packages:`**
  -   google-api-core 1.22.1
  -   google-api-python-client 1.11.0
  -   google-auth 1.21.1
  -   google-auth-httplib2 0.0.4
  -   httplib2 0.18.1
  -   oauth2client 4.1.3

### Prerequisite
- To execute the test cases, we would need to setup the website on our local machine, please refer to the document:<br />```Setup Application Under Test Locally.docx```

- To use google sheets in your project, follow the instructions given below:
  - In the folder src/config, go to google_config.json file and change the values for the following parameters:
    - project_id
    - private_key_id
    - private_key
    - client_email
    - client_id
    - client_x509_cert_url
  - Go to url ```https://console.cloud.google.com/home/dashboard``` <br /> and perform the below steps:
    - Login with your google account and create a new project.
    - Than enable search for the Sheets API on the url : ```https://console.cloud.google.com/apis/library``` and enable it.
    - Go to the url ```https://console.cloud.google.com/apis/credentials``` and create a service account key by clicking on `+ Create Creadentials > Service account`
    - Give the name and manage the permissions and click on done.
    - Visit the url ```https://console.cloud.google.com/iam-admin/serviceaccounts``` and click on the dots in actions and click on edit.
    - Under the Keys tab, click on `Add keys` and than get all the details from the page and replace the same in file `google_config.json`.<br/>  

- Download dependencies by using the following command:<br />```pip install -r requirements.txt```
- Copy the file ```sheets.googleapis.com-python-quickstart.json``` file from project root folder to ```C://users/{username}/.credentials``` folder.
- Extract the ```allure.zip``` to your preferred location and set the path of ```allure\bin\``` to your System Environment.

### Config Parameters
- The base url of API is configurable and can be configured in `common.py` in `Util` folder.
- Google Sheets data are configurable and can be configured in `google_config.json` in `Config` folder.
- To add logging as to show it in the log file, use the `logger_utility` from `Data providers` folder.


### Running Tests
<br />

- ### Execution from Command line
  - ### Arguments and their usage explanation:
      - **`--processes`:** Used to input number of parallel processes to run at a time.
      - **`--allure_reporting`:** Used to generate allure reports.
      - **`--junit_reporting`:** Used to generate junit reports.
      - **`-D log_level`:** Used to set the level of logging.
      - **`-D browser`:** Used to input the browser to run the tests on.<br/>
      - **`-D headless`:** Used to run the tests on headless mode.<br/>
      - **`-D log_level`:** Used to set the level of logging.<br/>

  - ### Execute a specific test feature without allure reports:
    -  Navigate to src\ in cmd and run below command:
       - ```behave tests/features/$FILE_NAME.feature -k -f plain  -D log_level=$LOG_LEVEL```

  - ### Execute a specific test feature with allure reports:
    -  Navigate to src\ in cmd and run below command:
       - ```behave tests/features/$FILE_NAME.feature -k -f plain -D env=local -D browser=$BROWSER -D log_level=$LOG_LEVEL -f allure_behave.formatter:AllureFormatter -o allure_reports/results```
  
  - ### Execute all features with  Allure Reports and Junit Reports :
    - ### Allure Reports
      Allure reports are generated in CSV and JSON format at first and than it is converted to HTML format.<br/>
    - ### Junit Reports
      - Junit reports are generated in XML format.
      - Output JUnit-compatible reports. When junit is enabled, all stdout and stderr will be redirected and dumped to the junit report, regardless of the “–capture” and “–no-capture” options.
          
    - ### Headless Browser      
      - To execute all tests in sequential in headless browser with Allure and Junit reports:
        - ```python behave-parallel.py --processes=1 -D env=local -D browser=$BROWSER -D headless=true -D log_level=$LOG_LEVEL --allure_reporting=true --junit_reporting=true```<br/>

      - To execute all tests in parallel in headless browser with Allure and Junit reports: 
        - Navigate to src and run
          - ```python behave-parallel.py -D log_level=$LOG_LEVEL -D env=local -D browser=$BROWSER -D headless=true --processes=$NUM_OF_PROCESSES --allure_reporting=true --junit_reporting=true```<br/>
  
    - ### Headed Browser
      - To execute all tests in sequential in headed browser with Allure and Junit reports:
        -  Navigate to src and run
           - ```python behave-parallel.py --processes=1 -D env=local -D browser=$BROWSER -D headless=false -D log_level=$LOG_LEVEL --allure_reporting=TRUE --junit_reporting=true```<br/>

      - To execute all tests in parallel with Allure and Junit reports: 
        - Navigate to src in cmd and run
          - ```python behave-parallel.py --processes=$NUM_OF_PROCESSES -D env=local -D browser=$BROWSER -D headless=false -D log_level=$LOG_LEVEL --allure_reporting=TRUE --junit_reporting=true```<br/> 
  - ### Open Allure HTML report
    - After execution, To open the reports run the following command in terminal:
      -  ```allure open allure/reports``` 
    - We can also open it by navigating to `src/allure/reports` and open `index.html`.
  
  - ### Execute all tests without Allure Reports and Junit Reports :        
     - ### Headless browser
       - To execute all tests in sequential in headless browser without Allure and Junit reports:
         - Navigate to src and run below command:
           - ```python behave-parallel.py --processes=1 -D env=local -D browser=$BROWSER -D headless=true -D log_level=$LOG_LEVEL```<br/>
       - To execute all tests in parallel in headless browser without Allure and Junit reports: 
         - Navigate to src in cmd and run below command:
            -  ```python behave-parallel.py --processes=$NUM_OF_PROCESSES -D env=local -D browser=$BROWSER -D headless=true -D log_level=$LOG_LEVEL```<br/>
    
     - ### Headed browser
       - To execute all tests in sequential in headed browser without Allure and Junit reports: 
         - Navigate to src and run
           - ```python behave-parallel.py --processes=1 -D env=local -D browser=$BROWSER -D headless=false -D log_level=$LOG_LEVEL```<br/>

       - To execute all tests in parallel in headed browser without Allure and Junit reports: 
         - Navigate to src in cmd and run
           - ```python behave-parallel.py --processes=$NUM_OF_PROCESSES -D env=local -D browser=$BROWSER -D headless=false -D log_level=$LOG_LEVEL```<br/>


### Test Logs
-   Test Logs saved in location after execution:<br />`src\logs`.

### Reports
-   Reports saved in location after execution:<br />`src\reports`.

### Allure Reports
-   Allure Reports are saved in location after the execution:<br />`src\allure\html_reports`.