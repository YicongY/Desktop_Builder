#Project for Desktop_Builder:

#Usage:
#Step one: setting up the database and crawl the information from Newegg
	-build the database base on the sql query inside the code
	-install the requirements and scrape the website using command
	“scrapy crawl * ” where * could be 
		neweggcpu
		neweggintelboard
		neweggra
		newegggpu
		neweggcase
		newegghdd
		neweggpsu

#Step two:run the backend server
	-python backend_server.py 

#Step three:visit the localhost
	-go to localhost:1111 to use the system 


