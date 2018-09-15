Following are the steps to run the application. There are 2 ways to it. 

1. Run a SERVER method

Download the folder/zip, unzip

(Recommended) Setup a virtual environment

$ pip install virtualenv
$ virtualenv vistar
$ source vistar/bin/activate
$ pip install -r requirements.txt




Incase - without virtual environment
$ pip install -r requirements.txt

(Incase any package fails, simply pip install ‘package-name’)

$ cd vistar_puzzle/

$ python app.py   //to start the server
$ curl -H "Content-type: application/json" -X POST http://127.0.0.1:8080/ -d '{"latitude":48.225214, "longitude":-122.402014}'

Washington


--------------------------
2. Run a Python file method

$ cd vistar_puzzle/
$ python getplace.py 48.225214 -122.402014

Washington

-----------------------------
