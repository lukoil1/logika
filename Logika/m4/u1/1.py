from PIL import Image , ImageFilter

with Image.open('m4/u1/dog.jpg') as original:
    #original.show()
    print(original.size)
    print(original.mode)
    print(original.format)
    grej = original.convert('L')
    #grej.show()
    blur = original.filter(ImageFilter.BLUR)
    #blur.show()
    left = original.transpose(Image.ROTATE_90)
    #left.show()
    grej.save('m4/u1/grej_dog.jpg')
    blur.save('m4/u1/blur_dog.jpg')
    left.save('m4/u1/left_dog.jpg')