1.2 Install on Windows 7/10

Open Command Prompt and check whether python is installed correctly
	python
	exit()
	
Download the NumPy package and OpenCV package
	https://www.lfd.uci.edu/~gohlke/pythonlibs/#numpy
	https://www.lfd.uci.edu/~gohlke/pythonlibs/#opencv
	https://www.lfd.uci.edu/~gohlke/pythonlibs/#matplotlib
	
Upgrade the pip library
	python -m pip install --upgrade pip
	
Install the NumPy and OpenCV packages
Open Command Prompt as Administrator
Go to the downloads folder where the packages are downloaded and copy the file path
	cd /path
	dir
	pip install "numpy <PRESS TAB TO AUTO-COMPLETE>
	pip install "opencv <PRESS TAB TO AUTO-COMPLETE>
	
1.3 Test the install
Open Command Prompt
Enter the Python runtime enviornment
	python
To test that the install was successful we're going to run two imports
NumPy:
	import numpy
	numpy.__version__
OpenCV
	import cv2
	cv2.__version__
Matplotlib
	import matplotlib
	matplotlib.__version__
	
This shows tat the installation was successful



