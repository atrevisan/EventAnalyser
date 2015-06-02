# -*- coding: utf-8 -*-

# A simple setup script to create an executable using PyQt4. This also
# demonstrates the method for creating a Windows executable that does not have
# an associated console.
#
# main.py is a very simple type of PyQt4 application
#
# Run the build process by running the command 'python setup.py build'
#
# If everything works well you should find a subdirectory in the build
# subdirectory that contains the files needed to run the application

import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

include_file = [(r'C:\Users\Allan\Documents\Visual Studio 2013\Projects\twitter_analysis\twitter_analysis\core\gui\assets\save_2.png',
				 r'core\gui\assets\save_2.png'),
				(r'C:\Users\Allan\Documents\Visual Studio 2013\Projects\twitter_analysis\twitter_analysis\core\gui\assets\save.png',
				 r'core\gui\assets\save.png'),
				(r'C:\Users\Allan\Documents\Visual Studio 2013\Projects\twitter_analysis\twitter_analysis\core\gui\assets\mg2.png',
				 r'core\gui\assets\mg2.png'),
				(r'C:\Users\Allan\Documents\Visual Studio 2013\Projects\twitter_analysis\twitter_analysis\core\gui\assets\mg.png',
				 r'core\gui\assets\mg.png'),
				(r'C:\Users\Allan\Documents\Visual Studio 2013\Projects\twitter_analysis\twitter_analysis\core\gui\twithon_params.txt',
				 r'core\gui\twithon_params.txt'),
				(r'C:\Users\Allan\Documents\Visual Studio 2013\Projects\twitter_analysis\twitter_analysis\core\gui\sentiment_classification_model_path.clf',
				 r'core\gui\sentiment_classification_model_path.clf'),
				(r'C:\Users\Allan\Documents\Visual Studio 2013\Projects\twitter_analysis\twitter_analysis\core\gui\clusterized_dataset_path.pkl',
				 r'core\gui\clusterized_dataset_path.pkl'),
				(r'C:\Users\Allan\Documents\Visual Studio 2013\Projects\twitter_analysis\twitter_analysis\core\textutils\stopwords.txt',
				 r'core\textutils\stopwords.txt'),
				(r'C:\Users\Allan\Documents\Visual Studio 2013\Projects\twitter_analysis\twitter_analysis\core\textutils\arial.ttf',
				 r'core\textutils\arial.ttf')]
	
options = {
	
    'build_exe': {
		'include_files': include_file,
		'namespace_packages': [],
        'includes': 'atexit'
    }	
}

executables = [
    Executable('main.py', base=base)
]

setup(name='Twitter analysis',
      version='0.1',
      description='A tool for twitter data exploration',
      options=options,
      executables=executables
      )