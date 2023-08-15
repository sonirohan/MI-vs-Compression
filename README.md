# MI-vs-Compression
Using MINE to examine changes in Mutual Information (MI) between Male/Female labels and differently compressed images (different pixel sizes).
CelebA dataset was used for images of faces and attribute labels. 202599 faces were in the dataset, but only 60000 were used as training data (10000 more for test data) for this experiment. Link to CelebA dataset: https://mmlab.ie.cuhk.edu.hk/projects/CelebA.html

male_or_female.txt
  contains the labels for all 202599 images for identifying gender (downloaded and parsed directly from CelebA website).

DNN_Image_Classification.ipynb
  used for validation: after comparing the MI between images and labels using MINE, this program is used to train classifiers then test those classifiers on 10000 new images and labels and noting the difference in accuracy between image sizes. The result is both a graph with all the ROC curves for each tested image size and a graph with the same trend (and plateau point) as the MI vs. Compression graph generated previously.

