# MI-vs-Compression
Using MINE to examine changes in Mutual Information (MI) between Male/Female labels and differently compressed images (different pixel sizes).
CelebA dataset (link: https://mmlab.ie.cuhk.edu.hk/projects/CelebA.html) was used for images of faces and attribute labels. 202599 faces were in the dataset, but only 60000 were used as training data (10000 more for test data) for this experiment. 

**image_processor.py** is a program that takes in the unprocessed CelebA images (downloaded from the above link to the CelebA dataset), uses Python's Pillow Library to grayscale and shrink them down to different square sizes (ranging from 5x5 to 50x50, in increments of 5), then saves them. The file paths will need to be changed for your own computer.

**male_or_female_lister.py** is a program that grabs all the male/female labels from the original CelebA dataset attribute list. _There is no need to run this program at this time_ because the labels are already parsed into **male_or_female.txt**.

**male_or_female.txt** contains the labels for all 202599 images for identifying gender (downloaded and parsed directly from CelebA website). Labels with 0 represent female images, and labels with 1 represent male images (changed from -1 and 1 labels to be consistent with previous MINE code).  

**MI_Estimation_Image_Size.ipynb** is the first experiment done to estimate the MI between 60000 human face images and their gender (male/female) labels, repeated for different image compressions. The Python Pillow library was used to compress images that were originally 178x218 pixels to squares ranging from size 5x5 to 50x50 (the original plan was to compress images up to 175x175, but the trend of MI plateau'ed after 30x30 and it would take too long).

**DNN_Image_Classification.ipynb** is used for validation: after comparing the MI between images and labels using MINE, this program is used to train classifiers then test those classifiers on 10000 new images and labels and noting the difference in accuracy between image sizes. The result is both a graph with all the ROC curves for each tested image size and a graph with the same trend (and plateau point) as the MI vs. Compression graph generated previously.

**Notes:** 
 - Change the file paths in each program to match your own local drive if you would like to run them yourself.
 - Running the .ipynb files requires a GPU (not a built-in GPU, but free Google Colab GPU service works well). 
 - The .ipynb files were developed in Google Colab (using T4 GPU) and the .py files were developed using Spyder.
