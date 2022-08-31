install: 
	pip install --upgrade pip &&\
		pip install -r requirements.txt

lint: 
	pylint --disable=R, hello.py
	
all: install lint 