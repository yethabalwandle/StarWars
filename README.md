Contains code for testing web and api

**Structure:** 

Highlevel overview
* PageObjects
  * Web
  
    > Contains code to address front-end elements on web
    
    
* Api

    > Contains code to address back-end of web


## Setup 

We recommend to install homebrew
If you are not familiar with it then checkout

[homebrew](https://brew.sh/)

[homebrew requirements](https://docs.brew.sh/Installation)

**Python:**

Install via homebrew [see this](https://docs.python-guide.org/starting/install3/osx/)

**Python dependencies:**

*2 options:*
1. Use requiremnts.txt
`pip install -r requirements.txt`

2. Or virtual environment and setup.py file (run at root of repo)
```
virtualenv venv && \                                                                        
source venv/bin/activate && \
pip install -e .
```

**Selenium Webdriver**

Chrome Driver

  `brew cask install chromedriver`
