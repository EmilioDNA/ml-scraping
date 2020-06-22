# Mercado Libre Scraping
This is a basic project.

# Description

This is a basic App that uses Scrapy and Python to get the title, description, and price of a specific category of products in Mercado Libre.

For this project, I only cover the basic functionality of Scrapy in order to perform both horizontal and vertical web scraping.

The results got from this operation are saved in a .json file.

## Getting Started

### Installing Dependencies

#### Python 3.7 

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

I recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organized. Instructions for setting up a virtual environment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### Pip Dependencies

Once you have your virtual environment setup and running, install dependencies by navigating to the `/ml-scraping` directory and running:

```bash
pip install -r requirements.txt
```
I included all the needed dependencies for this project in the `requirements.txt` file.

##### Key Dependencies

- [Scrapy](https://scrapy.org/)  is an open source and collaborative framework for extracting data from websites.

- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) is a Python library that is mainly used to get data from XML or HTML files. 


## Running the script

From within the `ml-scraping` directory
ensure you are working using your created virtual environment.

To run the script, execute:

```bash
scrapy runspider ml-scraping.py -o ml.json -t json
```

Specifying the  `-o` command will establish the name outcome file, you are welcome to name it as you prefer. 

Specifing the  `-t` command will establish the type outcome file. 

