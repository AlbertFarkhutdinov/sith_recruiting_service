# sith_recruiting_service
The recruiting service for the Order of the Sith realized on the Django framework

## Requirements

1. Before you start, make sure that you have Python 3.7 or later versions. Input this command into terminal:

		python --version

2. Install the necessary libraries in your environment:

		pip install -r requirements.txt

## Start

You can run the following command in terminal from root directory to start a project at first time:

	launcher
	
This command removes database and all migrations, if they already existed, then creates new database, applies migrations and fill the database with data from 'json' directory, then runs the project. 
If you don't want to remove existing database, run the following command in terminal from root directory to start a project:

	run
	
Now that the server’s running, visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) with your Web browser.  
