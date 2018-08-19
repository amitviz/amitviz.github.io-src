Title: Resize images using Imagemagick
Date: 2018-08-10
Category: Notes
Tags: linux
Slug: 
Authors: Amit

To resize to a maximum dimension (maintaining aspect ratio):

    #!bash
    convert in.jpg -resize 1280x1280 out.jpg

In batch, on a given folder (in-place, overwriting theoriginal!): 

    #!bash
    parallel "convert  {} -resize 1280x1280 {}" ::: *.jpg
