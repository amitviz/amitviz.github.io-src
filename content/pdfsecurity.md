Title: Remove security from a PDF file
Date: 2013-07-31
Category: Notes
Tags: code, pdf
Slug: 
Authors: Amit

    #!bash
    gs -q -dNOPAUSE -dBATCH -sDEVICE=pdfwrite -sOutputFile=$output -c .setpdfwrite -f $1
    
