import numpy
from PIL import Image


image = Image.open("C:/Users/beast/Desktop/Portfolio/ROM/LettterRom.png")
pix = image.load()
width, height = image.size

chars = width / 5

st = "["

for c in range(int(chars)):
    for y in range(7):
        for x in range(5 * c, 5 * c + 5):
            if(pix[x,y] == 1):
                st = st + "0, "
            else:
                st = st + "1, "
        st = st + "\n"
    st = st[:-3]
    st = st + "],\n["
st = st[:-3]
print(st + "]")