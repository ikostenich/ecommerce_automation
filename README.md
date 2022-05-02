# ecommerce_automation

INTRODUCTION
------------

The repository contains the codebase for automated test of nopCommerce website Search functionality.



INSTALLATION
------------
 
 ## 1. Running tests using docker
 
 ### Preconditions:
 * linux-based of mac_os operation system
 * docker installed
 
 ### Steps:
 1. Clone the repository
  ```linux
git clone https://github.com/ikostenich/ecommerce_automation.git
```
 2. Go to the project root directory
 
 ```linux
cd ecommerce_automation
```

3. Build the docker image from Dockerfile
 ```linux
docker build -t ecommerce .
```
As the result "ecommerce" docker image will be created and set up

4. Run the automated tests via "run_in_docker.sh" bash script which automates container launch
 ```linux
bash run_in_docker.sh
```
