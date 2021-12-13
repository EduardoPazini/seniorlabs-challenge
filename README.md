# Senior Labs Challenge

Data science challenge resolution.

The challenge can be found in: https://github.com/SeniorSA/seniorlabs-challenge

## Technologies and preparation

For this solution, I used Python in version 3.8.10.

To facilitate the installation of the necessary libraries, I used virtual environments.

More information about virtual environments: https://docs.python.org/pt-br/3/library/venv.html

## How to use

1) Install and set the virtual enviroment on the root folder:

```
python3 -m venv env
source env/bin/activate
```

2) Install the packages required:
   
```
pip3 install -r requirements.txt
```

obs.: if you do not want to use virtual environments, you can install all libraries listed in <i>requirements.txt</i> on your machine. 

3) Run the main module:

```
python3 code/main.py
```

The graphic results will be saved in the results directory, the others ones will be shown in the terminal.

## Run the tests

After installing pytest among the requirements, run:

```
pytest code/test.py
```
