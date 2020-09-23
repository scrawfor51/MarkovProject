# Stephen Crawford
# Computational Creativity
# 9.22.2020
# This program uses the principles behind a Markov Chain to create a randomized piece of visual art: a comic strip!
# The program consists of the ComicPage class and the driver main file. During execution, the program accesses a text file
# stored in the resources directory which contains a text document of quotes from the television show Curb Your Enthusiasm.
# It then takes the text from that file, reads it, and stores it inside an array. Using this array, the program determines
# the amount of lines within the text file and randomly selects one of the lines in the file to use. It then takes
# this text and inserts it into a Batman (2016) comic strip which was found for free on the internet at readcomiconline.to.
# The comic strip is altered in its near original form aside from the fact that the text bubbles were turned white in order
# for the original text to be hidden. This was done with GIMP.
# Please see README for further details and proper crediting of resources and creators.

import random
import os
import os.path
from PIL import Image, ImageDraw, ImageFont


from ComicPage import ComicPage


# Count the number of images in resources folder
# Return the number of images
def file_count():
    fileCount = 0
    for path in os.listdir("../MarkovProject/resources"):
        fileCount += 1
    return fileCount


# Generate a random number up to the number of images in the resources folder
# @param fileCount -- the number of files in the resource folder
# @return a random int value
def gen_num(fileCount):
    return random.randint(0, fileCount - 2)


# Find the file associated with the randomly generated index from gen_num
# Get that file from the resources folder and then return the img extension
# @randNum the randomly generated number from gen_num
# @return the image file extension for the randomly selected image
def grabImage(randNumb):
    counter = 0
    for img in os.listdir("../MarkovProject/resources"):
        if counter == randNumb:
            return img
        else:
            counter += 1
            continue


# Convert a text file into a string array of the lines in the file
# @param textSource -- The text file to be converted into a string array
# @return A string array containing the lines in the file
def readText(textSource):

    textAsArray = []
    with open(textSource, "r") as textFile:
        lines = textFile.readlines()
        for line in lines:
            if line.__len__() > 0:
                lineStripped = line.rstrip()
                textAsArray.append(lineStripped)
    return textAsArray


# Insert text method which uses the arguments to rewrite a source's text within a given page of the comic book.
# @param page -- Take in the file extension for the image we want to generate text within
# @param textSource -- Take the textSource document for which text we will use to fill the comic strips
def insertText(page, text):
    try:
        toEdit = ComicPage
    except:
        print("Oops something went wrong! Check to see that you only have image files in your resources folder.")
    # I am sorry for what this looks like and wish I had been able to figure out a better solution, but I didn't want
    # to fall behind on the group project or my other classes.
    # May this be the ugliest code I ever write...
    if page == "batman-cover.png":
        toEdit = ComicPage("batman-cover.png", 1, [((524, 2800), (524, 2880), (524, 2960), (525, 3120))])
        font = ImageFont.truetype("./font/Heroes Legend.ttf", 40)
    elif page == "batman-page-1.png":
        toEdit = ComicPage("batman-page-1.png", 1, [((600, 2450), (600, 2530), (600, 2610), (600, 2690))])
        font = ImageFont.truetype("./font/Heroes Legend.ttf", 40)
    elif page == "batman-page-2.png":
        toEdit = ComicPage("batman-page-2.png", 5, [[(970, 850), (970, 870), (970, 890), (970, 910)], [(670, 1300),
        (670, 1350), (670, 1400), (670, 1450)], [(80, 1920), (80, 1970), (80, 2020), (80, 2070)], [(620, 1950),
        (620, 2020), (620, 2090), (620, 2160)], [(500, 2500), (500, 2550), (500, 2600), (500, 2650)]])
        font = ImageFont.truetype("./font/Heroes Legend.ttf", 10)
    elif page == "batman-page-3.png":
        toEdit = ComicPage("batman-page-3.png", 7, [((500, 230), (500, 280), (500, 330), (500, 310)),
        ((600, 360), (600, 420), (600, 480), (600, 560)), ((428, 440), (428, 500), (428, 560), (428, 620)), ((680, 550),
        (680, 600), (680, 650), (680, 700)), ((260, 1500), (260, 1550), (260, 1600), (260, 1650)), ((720, 1580),
        (720, 1650), (720, 1720), (720, 1800)), ((160, 2800), (160, 2850), (160, 2900), (160, 2950))])
        font = ImageFont.truetype("./font/Heroes Legend.ttf", 12)
    elif page == "batman-page-4.png":
        toEdit = ComicPage("batman-page-4.png", 5, [((170, 330), (170, 400), (170, 470), (170, 540)), ((1450, 100),
        (1450, 140), (1450, 180), (1450, 200)), ((680, 920), (680, 1000), (680, 1080), (680, 1160)), ((350, 1250),
        (350, 1300), (350, 1350), (350, 1400)), ((1430, 1330), (1438, 1380), (1438, 1460), (1438, 1540))])
        font = ImageFont.truetype("./font/Heroes Legend.ttf", 24)
    elif page == "batman-page-5.png":
        toEdit = ComicPage("batman-page-5.png", 8, [((1330, 220), (1330, 270), (1330, 320), (1330, 370)), ((1320, 420),
        (1320, 470), (1320, 440), (1320, 520)), ((440, 1070), (440, 1140), (440, 1210), (440, 1280)), ((1660, 1050),
        (1660, 1100), (1660, 1150), (1660, 1200)), ((50, 1950), (50, 2000), (50, 1970), (50, 2050)), ((350, 1940),
        (350, 1990), (350, 2040), (350, 2090)), ((660, 2060), (660, 2120), (660, 2180), (660, 2240)), ((1200, 2000),
        (1200, 2050), (1200, 2100), (1200, 2150))])
        font = ImageFont.truetype("./font/Heroes Legend.ttf", 10)
    elif page == "batman-page-6.png":
        toEdit = ComicPage("batman-page-6.png", 9, [((140, 115), (140, 185), (140, 255), (140, 325)), ((750, 120),
        (750, 200), (750, 240), (750, 280)), ((100, 1000), (100, 1030), (100, 1060), (100, 1090)), ((400, 1040),
        (400, 1070), (400, 1100), (400, 1130)), ((920, 1170), (920, 1220), (920, 1270), (920, 1320)), ((1630, 1180),
        (1630, 1230), (1630, 1280), (1630, 1320)), ((1550, 1380), (1550, 1440), (1550, 1500), (1550, 1560)),
        ((1280, 1620), (1280, 1650), (1280, 1680), (1280, 1710)), ((220, 2610), (220, 2660), (220, 2710), (220, 2760)),
        ((1015, 2760), (1015, 2820), (1015, 2880), (1015, 2940))])
        font = ImageFont.truetype("./font/Heroes Legend.ttf", 10)
    elif page == "batman-page-7.png":
        toEdit = ComicPage("batman-page-7.png", 5, [((110, 115), (110, 185), (110, 245), (110, 315)), ((1615, 280),
        (1615, 340), (1615, 400), (1615, 460)), ((130, 2260), (130, 2320), (130, 2380), (130, 2460)), ((150, 2550),
        (150, 2600), (150, 2650), (150, 270)), ((1010, 2270), (1010, 2300), (1010, 2340), (1010, 2470))])
        font = ImageFont.truetype("./font/Heroes Legend.ttf", 24)
    # This is the actual body of the method and deals with editing the comic pages with the Pillow Draw module
    img = Image.open("./resources/" + toEdit.file_ext)
    draw = ImageDraw.Draw(img)
    for place in toEdit.pixel_coordinates:
        lineCounter = 0
        blankLines = []
        j = 0
        while j < text.__len__():
            lineCounter += 1
            if text[j] == '':
                blankLines.append(j)
            j += 1
        num = random.choice(blankLines)
        i = 0
        while i < 3:
            try:
                draw.multiline_text(place[i], text[num + i - 3], (0, 0, 0), font=font, align="center")
                i += 1
            except:
                i = 3
    img.show()


# Driver function which executes the helper methods within the main file
if __name__ == '__main__':
    fCount = file_count()
    randNum = gen_num(fCount)
    ePage = grabImage(randNum)
    textInput = readText("./documents/CurbQuotes.txt")
    insertText(ePage, textInput)
