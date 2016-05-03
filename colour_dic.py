COLOUR={"AliceBlue":"#f0f8ff","AntiqueWhite":"#faebd7","BlanchedAlmond":"#ffebcd","BlueViolet":"#8a2be2","CornflowerBlue":"#6495ed","DarkKhaki":"#bdb76b","DarkSeaGreen":"#8fbc8f","DarkSlateGray":"#2f4f4f","Lavender":"#e6e6fa","LawnGreen":"#7cfc00"}

name=input("Enter colour name:")
while name!="":
    if name in COLOUR:
        print("The code of {} is {}".format(name,COLOUR[name]))
    else:
        print("Invalid name")
    name=input("Enter colour name:")



