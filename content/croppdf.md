Title: Cropping a pdf file
Date: 2016-08-27
Category: Notes
Tags: code, pdf, bash
Slug: croppdf
Authors: Amit

    #!bash
    gs -o $output -sDEVICE=pdfwrite -c "[/CropBox [$x0 $y0 $x1 $y1]" -c " /PAGES pdfmark" -f $1
    
