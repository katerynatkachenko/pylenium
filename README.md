# Challenge: Have I've been pwned

##  Quick start

### To execute the following Test Suits, please clone the repository from github:

`git clone git@github.com:katerynatkachenko/pylenium.git`

##### There are two options to run the tests: from docker container and without it

### Outside the container [Linux Ubuntu Environment]

1. From the root project directory, first run `sudo chmod +x ./setup.sh` to grant executable permission to `setup.sh` file
2. Then execute `setup.sh` file by running the following command: `./setup.sh`
3. To run the tests use the following command `python3 main.py`

### Inside the container 

#### 1. Execute the following command from the project root directory: 

`docker run -d --privileged --rm --name selenium-debug -p 4444:4444 -v $(pwd):/app:rw -w /app -p 5900:5900 --shm-size=2g katerynatkachenko/selenium-perseus:latest`

#### 2. Connect VNC viewer of your preference on `localhost:5900` and the password: `secret` 

To install VNC viewer on Linux Ubuntu use `sudo apt install remina`
   
#### 3. Execute the test suite by running 

`docker exec selenium-debug python3 main.py`
   
### Test Suite Description

1. Test Suite 'TestStringMethods' which is located in `main.py` file consists of 3 case scenarios + `setUp` and `tearDown` tests 

2. SetUp test consists of the set-up commands that are used in all 3 test cases. List of emails has been added for the third test case.
   
3. TearDown test consists of warning filter and `driver.close()` method.
   
4. First test scenario inserts `test@something.com` email and clicks the `pwned` button
   It waits for `Oh no - pwned!` to appear and with help of unit test library and `assertEqual()` method it checks if the text on the banner equal to expected string value.
  
   If yes - the test passed successfully.
   
5. The same goes with the second scenario test, the only difference, that test cleans the search bar first and inserts different email: `qwerty@somehting.com` and expects other assert result value: `Good news — no pwnage found!`

6. In the third test scenario we loop though the list of emails, that were declared in setUp test, and create an object of the results which is saved into `data.yaml` file. 
