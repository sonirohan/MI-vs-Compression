# MI-vs-Compression
Using MINE (Mutual Information Neural Estimator) to examine changes in Mutual Information (MI) between Male/Female labels and differently compressed images (different pixel sizes).
CelebA dataset (link: https://mmlab.ie.cuhk.edu.hk/projects/CelebA.html) was used for images of faces and attribute labels. 202599 faces were in the dataset, but only 60000 were used as training data (10000 more for test data) for this experiment. 

**image_processor.py** is a program that takes in the unprocessed CelebA images (downloaded from the above link to the CelebA dataset), uses Python's Pillow Library to grayscale and shrink them down to different square sizes (ranging from 5x5 to 50x50, in increments of 5), then saves them. The file paths will need to be changed for your own computer.

**male_or_female_lister.py** is a program that grabs all the male/female labels from the original CelebA dataset attribute list. _There is no need to run this program at this time_ because the labels are already parsed into **male_or_female.txt**.

**male_or_female.txt** contains the labels for all 202599 images for identifying gender (downloaded and parsed directly from CelebA website). Labels with 0 represent female images, and labels with 1 represent male images (changed from -1 and 1 labels to be consistent with previous MINE code).  

**MI_Estimation_Image_Size.ipynb** is the first experiment done to estimate the MI between the first 60000 images processed by **image_processor.py** (the original plan was to compress images up to 175x175, but the trend of MI plateau'ed after 30x30 and it would take too long). It shows the MI Estimation curves for each different image compression on one plot, as well as the trend in MI vs. compression.

**DNN_Image_Classification.ipynb** is used for validation: after comparing the MI between images and labels using MINE, this program is used to train classifiers then test those classifiers on 10000 new images and labels and noting the difference in accuracy between image sizes. The result is both a graph with all the ROC curves for each tested image size and a graph with the same trend (and plateau point) as the MI vs. compression graph generated previously.

**Notes:** 
 - Change the file paths in each program to match your own local drive if you would like to run them yourself.
 - Running the .ipynb files requires a GPU (not a built-in GPU, but free Google Colab GPU service works well). 
 - The .ipynb files were developed in Google Colab (using T4 GPU) and the .py files were developed using Spyder.

**References:**
 - All work was done under supervision of Homa Esfahanizadeh, Postdoctoral Associate at Massachusetts Institute of Technology.
 - All work was inspired by and based on MINE paper: https://proceedings.mlr.press/v80/belghazi18a/belghazi18a.pdf 
 - Homa Esfahanizadeh's MINE Base Repository was the basis of the experiment in **MI_Estimation_Image_Size.ipynb:** https://github.com/hesfahanizadeh/MI_ESTIMATION_BASE
 - Homa Esfahanizadeh's Deep Neural Network program for classification tasks was the basis of **DNN_Image_Classification.ipynb:** https://colab.research.google.com/drive/1a5DF6P7au89G4uuy0gbCg0VhJKu3LSaj?usp=sharing
