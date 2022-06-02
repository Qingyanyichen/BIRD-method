from __future__ import absolute_import

from torchvision.transforms import *

from PIL import Image
import random
import math
import numpy as np
import torch
import logging
import copy
import cv2
class BIRD(object):

    def __init__(self, probability = 0.25):
        self.probability = probability

    def convert_image_to_bit_planes(self, img, bit_size):
        # split channels in a color (3-channel) image
        r, g, b = img.split()
    
        # convert image integers to bits assuming 8 bit image for each color channel
        b_bits = np.unpackbits(b).reshape(bit_size)
        g_bits = np.unpackbits(g).reshape(bit_size)
        r_bits = np.unpackbits(r).reshape(bit_size)

        return b_bits, g_bits, r_bits

    def convert_bit_planes_to_image(self, b_bits, g_bits, r_bits, img_size):
        # convert back to 8-bit integer in the original shape
        b_aug = np.packbits(b_bits).reshape(img_size)
        g_aug = np.packbits(g_bits).reshape(img_size)
        r_aug = np.packbits(r_bits).reshape(img_size)
        
        cv_img=cv2.merge((b_aug, g_aug, r_aug))
        pil_img = Image.fromarray(cv2.cvtColor(cv_img,cv2.COLOR_BGR2RGB))

        return pil_img

    def bit_plane_slice(self, b_bits, g_bits, r_bits, bit_plane_list):
        if bit_plane_list is not None:
            for bit_plane in bit_plane_list:
                logging.debug('Zeroizing {} bit_plane'.format(int(bit_plane)))
                # zeroize the bit plane in each RGB channel
                bgr = np.random.rand(1)
                if bgr <= 1/3:
                    b_bits[:,:,int(bit_plane)] = 0
                elif bgr <= 2/3:
                    g_bits[:,:,int(bit_plane)] = 0
                else:
                    r_bits[:,:,int(bit_plane)] = 0
    
    def __call__(self, img):
        img2=copy.deepcopy(img)
        ###height, width, channels = img.shape
        height, width, channels = img.height,img.width,3
        img_size = (height, width)
        bit_size = img_size + (8,)
        
        tmp=str(random.randint(2, 7))
        r = np.random.rand(1)
        ###if r < self.probability:
        if r < 0.25:
            b_bits, g_bits, r_bits = self.convert_image_to_bit_planes(img2, bit_size)
            self.bit_plane_slice(b_bits, g_bits, r_bits, [tmp])
            img_bit = self.convert_bit_planes_to_image(b_bits, g_bits, r_bits, img_size)
        
            img=img_bit

        return img

