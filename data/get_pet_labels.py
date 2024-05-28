#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels_hints.py
#                                                                             
# PROGRAMMER: Fatima Hasanat
# DATE CREATED: 26/5/2024                                  
# REVISED DATE: 
# PURPOSE: This is a *hints* file to help guide students in creating the 
#          function get_pet_labels that creates the pet labels from the image's
#          filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

# TODO 2: EDIT and ADD code BELOW to do the following that's stated in the 
#       comments below that start with "TODO: 2" for the get_pet_labels function 
#       Please be certain to replace None in the return statement with 
#       results_dic dictionary that you create with this function
# 
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    # Creates list of files in directory
    in_files = listdir(image_dir)

    results_dic = dict()
   
    # Processes through each file in the directory, extracting only the words
    # of the file that contain the pet image label
    for idx in range(0, len(in_files), 1):
       
       # Skips file if starts with . (like .DS_Store of Mac OSX) because it 
       # isn't an pet image file
       if in_files[idx][0] != ".":
           
           # Creates temporary label variable to hold pet label name extracted 
           pet_label = ""
           filename_part = in_files[idx].split("_")
           pet_label = " ".join(filename_part[:-1]).lower().strip()
           # If filename doesn't already exist in dictionary add it and it's
           # pet label - otherwise print an error message because indicates 
           # duplicate files (filenames)
           if in_files[idx] not in results_dic:
              results_dic[in_files[idx]] = [pet_label]
              print(pet_label)
              
           else:
               print("** Warning: Duplicate files exist in directory:", 
                     in_files[idx])
 
    # TODO 2b. Replace None with the results_dic dictionary that you created
    # with this function
    print("results_dic",results_dic)
    return results_dic
#test line you can remove 
#get_pet_labels("C:/Users/FHasanat/Downloads/9664b117-d773-4799-b6a3-d4640ed702182-master/9664b117-d773-4799-b6a3-d4640ed702182-master/data/pet_images")
