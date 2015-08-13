"""
http://stackoverflow.com/questions/9142825/transparent-png-resizing-with-python-image-library-and-the-halo-effect
"""
import Image, numpy

def resize(srcPath, dstPath):
    img = Image.open(srcPath)
    premult = numpy.fromstring(img.tostring(), dtype=numpy.uint8)
    alphaLayer = premult[3::4] / 255.0
    premult[::4] *= alphaLayer
    premult[1::4] *= alphaLayer
    premult[2::4] *= alphaLayer
    img = Image.fromstring("RGBA", img.size, premult.tostring())
    #img.resize((64,64), Image.ANTIALIAS).save(dstPath)
    img.resize((100,64), Image.ANTIALIAS).save(dstPath)

srcPath = '../CSMWeb/static/img/brain-net.png'
dstPath = '../CSMWeb/static/zinnia/theme/img/logo.png'
resize(srcPath, dstPath)

