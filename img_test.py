# -*- coding: utf-8 -*-
import cStringIO
from PIL import Image
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True


def read_img():
    path = '/Users/w3/Downloads/IMG_20140321_164139.jpg'
    with open(path, 'rb') as f:
        return f.read()

def test():
    img = read_img()
    img = cStringIO.StringIO(img)
    ori_img = Image.open(img)

    f = open('/Users/w3/Downloads/aa.jpg', 'wb')
    ori_img.save(f)

    width, height = ori_img.size
    print width, height
    #
    # w = 4000
    # h = int(height * float(w) / width)
    #
    # # Image.resize
    # tmp_img = ori_img.resize((w, h), Image.ANTIALIAS)
    # tmp = cStringIO.StringIO()
    # tmp_img.save(tmp, 'JPEG', quality=80)

    # print tmp.getvalue()


if __name__ == '__main__':
    test()