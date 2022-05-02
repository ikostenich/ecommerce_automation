# ecommerce_automation

INTRODUCTION
------------

The repository contains the codebase for automated test of nopCommerce website Search functionality.



INSTALLATION
------------
 
 ## 1. Running tests using docker
 
 ### Preconditions:
 * linux-based or mac_os operation system
 * docker installed
 
 ### Steps:
####  1. Clone the repository
  ```linux
git clone https://github.com/ikostenich/ecommerce_automation.git
```
####  2. Go to the project root directory
 
 ```linux
cd ecommerce_automation
```

#### 3. Build the docker image from Dockerfile
 ```linux
docker build -t ecommerce .
```
As the result "ecommerce" docker image will be created and set up

#### 4. Run the automated tests via "run_in_docker.sh" bash script which automates container launch
 ```linux
bash run_in_docker.sh
```
You'll see tests running and bhief results of particular test cases
![image](https://user-images.githubusercontent.com/18323106/166266198-cc155c1a-edef-47a8-8771-3bb34d72ae0c.png)

Note: tests are running in headless chrome browser.

 
 ## 2. Running manually (without docker)
 
 ### Preconditions:
 * linux-based or mac_os operation system. Recommend using Ubuntu 20.04 desktop.
 * sudo rights to install packages
 
 ### Steps:
####  1. Clone the repository
  ```linux
git clone https://github.com/ikostenich/ecommerce_automation.git
```
####  2. Go to the project root directory
 
 ```linux
cd ecommerce_automation
```

#### 3. Check if python installed. 3.8+ version is required.    
```linux
python3 -V
```
If not installed: 
```linux
sudo apt-get update
sudo apt-get install python3.8
```

#### 4. Install python venv package. For 3.8 python:
```linux
sudo apt install python3.8-venv
```

#### 5. Installing Google Chrome and Chromedriver.

Run the shell script "install_selenium_manually.sh" in the project root
```linux
bash install_selenium_manually.sh
```

The script install Google Chrome browser, downloads latest chromedriver, moves the chromedriver to /usr/local/bin folder (that way chromedriver will be in PATH). Oterwise if you don't want to move to /usr/local/bin - you can add chromedriver folder to PATH manually.

Check the installation:
```linux
google-chrome --version
which chromedriver
```
For both commands you should see output:
![image](https://user-images.githubusercontent.com/18323106/166290193-ad2d53bf-f2b9-4f56-b9be-4df667497ada.png)


### 6. Export environment variables

Note: some parameters like which browser to use (chrome or headlesschrome), url (testing environment) are used as environment variables. You need to export them before test (every time for new bash/terminal).

```linux
source env.sh
```

#### 7. Create python virtual environment

```linux
python3 -m venv ./venv
```


#### 8. Activate the virtual environment

```linux
source venv/bin/activate
```
you should see (venv) left to user name in terminal
![image](https://user-images.githubusercontent.com/18323106/166293034-d3d023dc-155b-4207-9bef-812c16a4207d.png)


#### 8. Install the required python packages
```linux
pip install -r requirements.txt
```

#### 8. Run tests
```linux
python3 -m pytest
```

Note: test will run in chrome (not headless chrome). In case you don't want chrome to open or if you linux has no UI - export another browser as environment variable
```linux
export BROWSER=headlesschrome
```
