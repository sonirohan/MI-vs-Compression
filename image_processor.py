# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 14:01:52 2023

@author: thebr
"""

from PIL import Image
import os
import time


#grayscales and shrinks images to 28x28 pixels
def process(og_image_filename, new_image_filename, new_size, num_samples):
    num_samples = str(int(num_samples/1000)) + "k"
    #file naming
    root = f"C:/Desktop/Rohan/Python Programs/MIT Internship/CelebA Dataset (MINE)/UnprocessedImages/img_align_celeba/"
    #path = "C:/Desktop/Rohan/Python Programs/000001.jpg"
    path = root + og_image_filename
    #new_path = "C:/Desktop/Rohan/Python Programs/000001_gray_28x28_2.jpg"
    new_root = f"C:/Desktop/Rohan/Python Programs/MIT Internship/CelebA Dataset (MINE)/ProcessedMinibatches/{num_samples}samples_size{new_size[0]}x{new_size[1]}/"
    if not os.path.isdir(new_root):
        os.mkdir(f"C:/Desktop/Rohan/Python Programs/MIT Internship/CelebA Dataset (MINE)/ProcessedMinibatches/{num_samples}samples_size{new_size[0]}x{new_size[1]}")
    
    new_path = new_root + new_image_filename
    
    #processing
    img_rgb = Image.open(path)
    img_gray = img_rgb.convert('L')
    #img_gray.resize((178*2, 218*2))
    img_gray_resized = img_gray.resize((int(new_size[0]), int(new_size[1])))
    #print(img_gray_resized.size)
    #img_gray.show()
    #img_gray_resized.show()
    img_gray_resized.save(new_path)

def mass_process(num_samples, new_size):
    #process 60000 image samples from the CelebA dataset
    origin = time.time(); print("Start time: " + str(origin))
    
    for i in range(60001, 60001 + num_samples):
        curr = time.time()
        if i % 1000 == 0:
            print(f"Finished {i}th image:")
            print(f"Estimated total time: {round((curr - origin) * i / num_samples, 1)} seconds")
            print(f"Estimated remaining time: {round(((curr - origin) * i / num_samples) - (curr - origin), 1)} seconds\n")
        i_str = str(i)
        old_filename = str(i) + ".jpg"
        new_filename = str(i) + f"_processed_size{new_size[0]}x{new_size[1]}.jpg"
        for i in range(6 - len(i_str)):
            old_filename = "0" + old_filename
            new_filename = "0" + new_filename
        process(old_filename, new_filename, new_size, num_samples)

"""
sizes = [i for i in range(5, 55, 5)]
for size in sizes:
    mass_process(10000, (size, size))
"""\

#now only process images 60001 to 70000 (test images for the ML classifier)

"""
for i in range(1, 35):
    if 5*i not in sizes_done:
        mass_process(60000, (5*i, 5*i))
"""
