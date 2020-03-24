#你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。
from PIL import Image

def change_image_size(image_path='0000.png',size=(1136,640)):
    im=Image.open(image_path)
    size=(size[1],size[0]) if im.size[1]>im.size[0] else size
    #原始图片的缩略图
    im.thumbnail(size,Image.ANTIALIAS)
    im.save('result+'+image_path)#用加号不能用逗号
#change_image_size('0000-r.png')

change_image_size('0000.png')


