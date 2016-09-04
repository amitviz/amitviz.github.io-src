Title: Interleaving two pdf files
Date: 2016-08-28
Category: Notes
Tags: code, pdf, bash
Slug: interleavepdf
Authors: Amit

    #!bash
    pdftk $1 burst output %04d_A.pdf
    pdftk $2 burst output %04d_B.pdf
    
    rm $1
    rm $2
    
    pdftk *.pdf cat output output.pdf
    
    rm ????_?.pdf