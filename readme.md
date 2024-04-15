# OCR to Anki
This project is a simple OCR to Anki deck generator. Its purpose is to convert a pdf document of questions I need to learn for my Physics exam. The main purpose of the repository is to provide a source of inspiration for others who want to do something similar. The code is not very clean and is not meant to be used as a library. It is just a simple script that I wrote to solve a problem I had. I hope it can help you solve yours.

If you happen to study physics at TUM and also need to learn the "Kurzfragen Katalog" for the Physik 3 or 4 exam, you can download the apkg file from the releases section.

## How to use it

1. First follow the install instructions below.

1. To convert the pdf to high res images I used the following website: https://pdftoimage.com/pdf-to-jpg
The images then have to be placed in the assets/[subject]/images folder. The images should be named in the following format: "0001.jpg", "0002.jpg", etc.
1. Then run ```python3 ./ocrImages.py```. Make sure the correct folder is set as the sourceFolder in the ```settings.py```
1. Then go in the index.json and clean it up (Either via vs-code prettier or manually (See below)).
1. Then run ```python3 ./generateAnki.py```.
1. Now the apkg files "TUMExphys3Kurzfragen_Sortiert.apkg" and "TUMExphys3Kurzfragen.apkg" should have been generated.

## How it works
The `ocrImages.py` script uses pytesseract to extract the text from the images. Then some filtering functions are applied to filter out only title and losung text. The coordinates of these text markers are used to crop the images. Then the cropped images are saved in the assets/[subject]output folder and the paths are saved in the index.json file. The index.json file is then used to generate the apkg files with the `generateAnki.py` script.

## Notes
- The `ocrImages.py` script is not very robust. It is very specific to the pdf I used. If you want to use it for your own pdf, you will have to adapt it to your needs.
- There is a latex error for chapter 18.18. There is a specific rule in the `src/textFilter.py` file to fix this. If this gets fixed in the future, the rule can be removed.
- The images are compressed to 40% of their original size. This is done to reduce the size of the apkg files. This can be changed in the `src/screenshot.py` file.

## Install (WSL2)

Requirements:

- python 3.6+
- pip3

Installing:

- Install tesseract:

```
sudo apt install tesseract-ocr
sudo apt install libtesseract-dev
```

- Install Pillow:

```
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade Pillow
```

- Install pytesseract:

```
pip3 install pytesseract
```

- Install opencv:

```
pip3 install opencv-contrib-python
```

- Install genanki:

```
pip3 install genanki
```

## Generate the dataset:

```
python3 ocrImages.py
```

## Generate Ankis:

```
python3 generateAnki.py
```

## Clean up Index file:

The generated Index file has some extra characters that need to be removed. Use the following regex to clean it up:

Regex search : ,\s*\n*\s\*\]

Replace with: ]
