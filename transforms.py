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
            rgb = np.random.rand(1)
            if rgb <= 1/3:
                for bit_plane in bit_plane_list:
                    b_bits[:,:,int(bit_plane)] = 0
            elif rgb <= 2/3:
                for bit_plane in bit_plane_list:
                    g_bits[:,:,int(bit_plane)] = 0
            else:
                for bit_plane in bit_plane_list:
                    r_bits[:,:,int(bit_plane)] = 0
    
    def __call__(self, img):
        img2=copy.deepcopy(img)
        ###height, width, channels = img.shape
        height, width, channels = img.height,img.width,3
        img_size = (height, width)
        bit_size = img_size + (8,)
        
        ###bit7=[str(random.randint(2, 7))]
        tmp1=random.randint(8, 13)
        if tmp1==8:
            bit5=['5','6','7']#[2,1,0]dropped,[7,6,5,4,3]extracted
        elif tmp1==9:
            bit5=['4','5','6']#[3,2,1]dropped,[7,6,5,4,0]extracted
        elif tmp1==10:
            bit5=['3','4','5']#[4,3,2]dropped,[7,6,5,1,0]extracted
        elif tmp1==11:
            bit5=['2','3','4']#[5,4,3]dropped,[7,6,2,1,0]extracted
        elif tmp1==12:
            bit5=['4','6','7']#[3,1,0]dropped,[7,6,5,4,2]extracted
        elif tmp1==13:
            bit5=['4','5','7']#[3,2,0]dropped,[7,6,5,4,1]extracted
            
        r = np.random.rand(1)
        ###if r < self.probability:
        if r < 0.25:
            b_bits, g_bits, r_bits = self.convert_image_to_bit_planes(img2, bit_size)
            self.bit_plane_slice(b_bits, g_bits, r_bits, bit5)
            img_bit = self.convert_bit_planes_to_image(b_bits, g_bits, r_bits, img_size)
        
            img=img_bit

        return img

