# Ocr Documents Scanner
![webpage](/static/webpage.png?raw=True "Title") 

Flask application to extract details from Aadhar card, Bank Cheque, Pan card, Driving Licence and also detected the face in document and store it in face folder.
just upload the document in jpg or png format and extract the details 

## Getting Started

### 1. Install Python 3+ and Anaconda 

If you don't already have Python 3+ installed And Anaconda, grab it from <https://www.anaconda.com/products/individual>. You'll will need to download and install the version of **Python 3.6**. because latest version is not compatible with library

### 2. Download Tesseract

To install Tesseract 4 on our Windows system, go to the following link:
<https://digi.bib.uni-mannheim.de/tesseract/>

Download windows executable file by clicking the hyper link titled tesseract-ocr-w64-setup-v4.1.0.20190314.exe. A notification asking you to save an exe file called “Tesseract-ocr-w64-setup-v4.1.0.20190314.exe” will appear. Save this .exe file wherever you have enough storage space.
Open this exe file. If it windows asks you “Do you want to allow this software to make changes to your system”, click yes. You will be taken to the installation section.

### 3. Clone This Repository

<https://github.com/devdatta95/OCR_Documents_With_Flask> On, click the green "Clone or Download" button at the top right of the page. If you want to get started with this script more quickly, click the "Download ZIP" button, and extract the ZIP somewhere on your computer.

you can clone using this command:
```shell
git clone https://github.com/devdatta95/OCR_Documents_With_Flask
cd OCR_Document_With_Flask
```

### 4. Create Conda Environment

execute following command in cmd, it will create anaconda env with python 3.6 version 
```shell
conda create --name `name_of_your_env` python=3.6
```

### 5. Activate conda Enviroment
Activate env
```shell
conda activate `name_of_your_env`
```
### 6. Install Dependencies

In a [command prompt or Terminal window](https://tutorial.djangogirls.org/en/intro_to_command_line/#what-is-the-command-line), [navigate to the directory](https://tutorial.djangogirls.org/en/intro_to_command_line/#change-current-directory) containing this repository's files. Then, type the following, and press enter:

```shell
pip install -r requirements.txt
```
### 4. Enter Tesseract path  (imp step)

Open config.py and enter replace the tesseract exe path in your code 

```shell
TESSRACT_PATH = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
```

### 5. Run the Script

In the same command prompt or Terminal window, type the following, and press enter:

this line will show some warnings you also ignore the warnings 
```shell
python server.py
```
Ignore all warnings 
```shell
python -W ignore server.py
```


### 6. Review the Results

The server.py script will start the python flask server.

```shell
Serving on http://Dev:8090
```
now your flask server is running, installation done!

open the browser and type
```shell
localhost:8090
```
you will be redirected to home page where you can upload the document images. and choose the document type
1. Aadhar Card 
2. Bank Cheque
3. Driving Licence  
4. Pan Card
5. Others

and extract the text data. it can also detect the faces in document and store it in face folder
Enjoy!

## Note:
- only jpg png format are supported 
- all the files are stored to upload folder 
- detected face stored in face folder 
- logs files generated daily 

