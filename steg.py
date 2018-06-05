from PIL import Image


original = Image.open('container.png')

width, height = original.size

steg = Image.new ('RGB', (width,height))

bits = [1,0,0,1,1,]

for i in range (width):
    for j in range(height):
        r,g,b = original.getpixel((i,j))
        if bits [idx] == 0:
            r &= 254
        else:
            r |= 1
         steg.putpixel((i,j)),(r,g,b)
        idx +=1