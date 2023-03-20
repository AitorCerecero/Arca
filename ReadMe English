# Arca

Hello, this is the read me of my code

 I know what you are thinking, what kind of code is this or what is this newbie doing?

 If I'm honest, it's the first time I upload something to GitHub and I thought I'd upload what I had done since I think it's a good job

 let me explain

The objective of this code (Not from the cloned repository since that one is already done) is to teach you how to use web scrapping in an easy way.

We will start by importing the assets we occupy

Keep in mind that this file is made in python

from bs4 import BeautifulSoup
import requests
import pandas as pd

BeautifulSoup is the extension that will help us manage webscrapping itself
request is the extension that will handle the URL of the site where we will be getting the information
pandas is the high-level library for handling numerical data

Once this is imported we can start

data = requests.get("https://www.highspeedinternet.com/in/mexico")
print(data.status_code)

data is where by means of request we are asking to download the link information (the link is fully customizable)
data.status_code is the way the library notifies you that the import worked, if you get the code 200 it means it was successful, otherwise if you have the code 403 it means something went wrong

xtract = BeautifulSoup(data.content,"html.parser")

xtract is a generic name, you can change it if you want. However, what corresponds will depend on what you put, the BS extension is totally necessary, the data as you can see is where we put the
link name

For what follows I will not be able to put everything, but nevertheless I will explain how to do it

It depends on what you are trying to extract is how you will handle the information, if you want to extract the title of the elements in the list of the page, you have to put the following

titles = xtract.findall("data_type",class_="Name of list)

data_type is the type of data that it is, div, h2, h3, etc and list name is like this. generally the data type and class name will be set, something like

("div",class_="columns small-12 medium-6 small-only-text-center font-medium")

then we pass it to a list

title = list()

we make a cycle that goes through the list in search of that data

for x in range titles:
     title.append(x.text)

the x.text and the append are necessary for the data types to be marked

Finally you can print it as print(title)

or you can put it in a data frame with pandas, something like this

datalink = ('Name: ',title)

DL = pd.DataFrame(data=datalink)

DL.to_csv('ISP_Data.csv')

In the code folder you should see the result

I hope this has served you. Greetings
