from PIL import Image

def JPGtoPNG():
    im = Image.open("image.jpg").convert("RGB")
    im.save("image.png", "png")
    
def PNGtoJPG():
    im = Image.open("image.png").convert("RGB")
    im.save("image.jpg", "jpeg")
    
def JPGtoWEBP():
    im = Image.open("image.jpg").convert("RGB")
    im.save("image.webp", "webp")
    
def WEBPtoJPEG():
    im = Image.open("image.webp").convert("RGB")
    im.save("image.jpg", "jpeg")
    
def PNGtoWEBP():
    im = Image.open("image.png").convert("RGB")
    im.save("image.webp", "webp")
    
def WEBPtoPNG():
    im = Image.open("image.webp").convert("RGB")
    im.save("image.png", "png")


select = input("Select conversion: \n 1º JPG to PNG \n 2º PNG to JPG \n 3º JPG to WEBP \n 4º WEBP to JPEG \n 5º PNG to WEBP \n 6º WEBP to PNG \n ")

if select == '1':
    JPGtoPNG()
elif select == '2':
    PNGtoJPG()
elif select == '3':
    JPGtoWEBP()
elif select == '4':
    WEBPtoJPEG()
elif select == '5':
    PNGtoWEBP()
elif select == '6':
    WEBPtoPNG()
else:
    print("Select 1, 2, 3, 4, 5, 6. ")
    