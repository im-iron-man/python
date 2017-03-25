from PIL import Image

# default characters
chars = [
    '$', '@', '&', '%', '#', 'B', 'b', '=',
    '-', '.', ' ',
]
    
def im2text(frompath, topath, height=None, width=None, chars=chars):
    
    # read image
    im = Image.open(frompath)

    # resize image
    w, h = im.size
    if height:
        h = height
    if width:
        w = width
    im = im.resize((w, h), Image.NEAREST)

    # process image to gray
    im = im.convert('L')

    # image to text
    txt = ''
    unit = 256.0/len(chars)
    for x in xrange(h):
        for y in xrange(w):
            txt += chars[int(im.getpixel((y, x))/unit)]
        txt += '\n'

    # write text into file
    with open(topath, 'wb') as f:
        f.write(txt)

if __name__ == '__main__':
    im2text('1.png', 'a.txt', 40, 50)
    im2text('2.jpg', 'b.txt', 40, 50)
    im2text('3.jpg', 'c.txt', 40, 50)
