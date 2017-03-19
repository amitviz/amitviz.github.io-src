Title: Scrapy
Date: 2017-01-21
Category: Notes
Tags: code, python
Slug: 
Authors: Amit

# What is Scrapy?

[Scrapy][scrapy] is an awesome web scraper using Python. I've done my own web scraping before using BeautifulSoup, but it required a lot of writing supporting code around it, and it was slow. Scrapy has most of what I need built in, and it is fast because it implements a scheduler and a parallel downloader.

# Installation and documentation

I installed Scrapy in a Conda environment - the default Conda repo doesn't have the latest version, but Scrapy does provide the latest version in Conda-forge (the community repo). It can be installed from [here][scrapy-conda]:

    :::bash
    conda install -c conda-forge scrapy=1.3.0

The documentation is [here][scrapy-doc], and includes a good tutorial to get started. These are just my notes from having followed the tutorial. 

The tutorial example uses the following quotes website as an example site to scrape: 

* [http://quotes.toscrape.com/page/1/][quotes]

# Using CSS selectors

Scrapy has a couple of different methods for extracting data from a page, but the only one I've used is CSS selectors. This seems to be fairly simple. To get a feel for how Scrapy works, we can bring up an interactive Scrapy shell: 

    :::bash
    scrapy shell 'http://quotes.toscrape.com/page/1/'
    
This pulls the target website into a local `response` object that we can start querying.

# Starting a project

# Defining items and a Spider

# Running the spider

[scrapy]: https://scrapy.org/
[scrapy-conda]: https://anaconda.org/conda-forge/scrapy
[scrapy-doc]: 
[quotes]: http://quotes.toscrape.com/page/1/
