
# importing required modules
import pyttsx3
import PyPDF2

textbook = input("Type your pdf file name (e.g. ebook.pdf): ")

# creating a pdf file object
pdfFileObj = open(textbook, 'rb')

# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# printing number of pages in pdf file
print(pdfReader.numPages)

# creating a page object
pageObj = pdfReader.getPage(0)

# extracting text from page
text = pageObj.extractText()

# closing the pdf file object
pdfFileObj.close()


def onWord(name, location, length):
    userStop = input("Type stop to exit: ")
    if userStop == 'stop':
        engine.stop()
        exit()


engine = pyttsx3.init()

# Change Rate
engine.setProperty('rate', 150)

# Change Voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[10].id)


engine.connect('started-word', onWord)
engine.say(text)
engine.runAndWait()
engine.stop()
