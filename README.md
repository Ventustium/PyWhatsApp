# PyWhatsapp - Automating broadcasts.

Whatsapp Broadcast Automation using Python and Excel for broadcasting messages and media.  

## Table of Contents

- [Background](#Background)
- [How to use](#How-to-use)
- [Execution](#Execution)
- [Scaffolding](#Scaffolding)
- [Bugs](#Bugs)
- [Authors](#Authors)

## Background

> Whatsapp has a built-in broadcast feature that lets you send messages to **256 contacts** but to reduce spam whatsapp requires that the person whom you are broadcasting should have your number saved. 
> As a workaround to this, Using web whatsapp we can send messages and media to people who don't have our number saved and I just automated the process using selenium and excel. 

## How to use 

### Installation

* First clone the repository by typing this command in terminal 
```
git clone https://github.com/Yilber/readme-boilerplate.git
cd readme-boilerplate
```

* Installing dependencies 
> openpyxl to import and extract excel data 
selenium to automate the chrome web browser
```
pip install selenium openpyxl
```

* Optional dependencies 
> To send documents and attachments, you need to install autoit and PyAutoIt 
First install Autoit and its editor which can be found in install folder
But PyAutoIt sometimes gives error in 64 bit python and works only on 32 bit python 
So don't install it if you just need to send messages and not media 
```
pip install PyAutoIt
```

### Chrome Webdriver
> If the webdriver included in the repository gets outdated you can download from this [link](https://chromedriver.chromium.org/downloads) and replace the it with the current webdriver

### Input format 
> You need to load an excel file with names and number of people.
If the device has the contact saved then write the name in excel file 
Or else just type the number whom you want to broadcast. 
The number format should be 919876543210 or 9876543210 and not +919876543210 
That is it should start with 91 or country code but not with +91
I have included a sample excel file for reference. 

## Execution 
To run the project, run
```
python main.py 
```
It'll open the TKinter GUI in which select the excel file and type the message which you want to send. If you want to send the attachments then select the image and/or document, Image caption is optional.
Once done then it'll open chrome browser and prompt to scan the QR code 
Rest of the process is automated 

Or you can see in this [demo video](https://www.youtube.com/watch?v=7WmeiHPb6cw)

[![](http://img.youtube.com/vi/7WmeiHPb6cw/0.jpg)](http://www.youtube.com/watch?v=7WmeiHPb6cw "")

## Scaffolding
```
PyWhatsApp
├── automation.py
├── chromedriver.exe
├── contacts.xlsx
├── main.py
├── examples
│   └── abc.docx
│   └── pikachu.jpg
├── examples
│   └── autoit-v3-setup.exe
│   └── SciTE4AutoIt3.exe
└── README.md
```

## Bugs

This is a selenium based project which relies heavily on the structure of web pages. 
if web whatsapp makes any changes internally then it can break the working of this project. 
As of January 2021 this project is working as intended. 

## Authors
[Rahil Memon | LinkedIn](https://www.linkedin.com/in/rahil-memon/)

[Palak Shah | LinkedIn](https://www.linkedin.com/in/palakshah99/)

[Shweta Shekhar | LinkedIn](https://www.linkedin.com/in/shweta-shekhar-617962182/)


