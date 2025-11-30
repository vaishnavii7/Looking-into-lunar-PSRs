#this script loads image by parsing meta data from xml
# importing libraries
from bs4 import BeautifulSoup #for xml scrapping
import numpy as np #for matrix operation

def xmlread(path):
    """This function returns image by parsing corresponding xml file"""
    # reading content
    file = open(path, "r")
    contents = file.read()

    # parsing xml
    soup = BeautifulSoup(contents, 'xml')
    elements = soup.find_all('elements')

    
    shape = [int(elements[0].get_text()),int(elements[1].get_text())]
    print('shape of image : ',shape)
    dtype = np.dtype('uint8')
    image_path = path[:len(path)-3]+'img'
    i = open(image_path, 'rb')
    
    #loading binary data of .img file into array
    data = np.fromfile(i,dtype)
    img = data.reshape(shape)
    return img