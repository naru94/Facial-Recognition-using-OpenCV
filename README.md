Anaconda and Jupyter notebook 
=======================================================
### 1.1 Install Anaconda

https://www.anaconda.com/products/individual

Download and install the lastest version of Anaconda

### 1.2 Download and install OpenCV and OpenCV contrib
Inside Anaconda open - CMD.exe Prompt

	pip install opencv-python==4.<latest version>
	pip install opencv-contrib-python==4.<latest version>
	
	pip install opencv-python==4.6.0.66
	pip install opencv-contrib-python==4.6.0.66
	
	
Open Jupyter Notebook and you are ready to go.


Windows 7+ and Python IDLE 
================================================
### 1.1 Install Python

www.python.org

#### Download and install the latest package of Python

Open Command Prompt and check whether python is installed correctly

	python
	exit()
	
### 1.2 Upgrade the pip library
	python -m pip install --upgrade pip
	
### 1.3 Download and install Numpy OpenCV Matplotlib	
#### Download the NumPy package and OpenCV package
https://www.lfd.uci.edu/~gohlke/pythonlibs/#numpy

https://www.lfd.uci.edu/~gohlke/pythonlibs/#opencv

https://www.lfd.uci.edu/~gohlke/pythonlibs/#matplotlib
	
#### Install the NumPy and OpenCV packages
Open Command Prompt as Administrator

Go to the downloads folder where the packages are downloaded

	cd /path-where-the-packages-are-downloaded
	dir
	pip install "numpy<PRESS TAB TO AUTO-COMPLETE>
	pip install "opencv<PRESS TAB TO AUTO-COMPLETE>
	pip install "matplot<PRESS TAB TO AUTO-COMPLETE>
	
### 1.4 Test the install
Open Command Prompt
#### Enter the Python runtime enviornment
	python
#### To test that the install was successful we're going to run two imports
#### NumPy:
	import numpy
	numpy.__version__
#### OpenCV:
	import cv2
	cv2.__version__
#### Matplotlib:
	import matplotlib
	matplotlib.__version__
	
This shows that the installation was successful.



