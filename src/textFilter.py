
min_conf = 20
x_max = 380
min_height = 30

def filterOcrTexts(text, conf, left, top, width, height):
    if conf < min_conf:
        return False
    
    if text == "":
        return False
    
    if text == "Losung":
        return True
    
    #check if first character is a number
    if text[0].isdigit():
        #Remove dot if it is the last character //Exphys4 11.14.
        if(text[-1] == "."):
            text = text[:-1]
        
        if(len(text) > 5):
            return False
        #check if text contains special characters except for dots
        if not any(char.isdigit() or char == "." for char in text):
            return False
        
        if(left > x_max):
            print(text + "is to far left")
            return False
        
        if(height < min_height):
            print( text + "is to small")
            return False
        return True
    
    return False
    
def classifyText(text):
    #trim text
    text = text.strip()
    #if the last character is a dot, remove it (artefact from OCR)
    if(text.endswith(".")):
        text = text[:-1]
    
    if(text == "Losung"):
        return "Losung"
    
    #MainChapter if no dot or if a dot exits but no number after the dot
    if (text.count(".") == 0 and any(char.isdigit() for char in text)) or (text.count(".") == 1 and not text.split(".")[1].isdigit()):
        if(text == "1So"):  #Special case for Exphys4
            return "Losung" 
        print(text)
        return "MainChapter"
    
    #Chapter if in the format 1.11
    if(text.count(".") == 1):
        if(text == "18.18"): #Special case for 18.18 since there is an latex error in the original document
            return "Losung"
        
        return "Chapter"
    
    return ""