Title: Markdown
Date: 2015-11-10
Category: Notes
Tags: code, pelican, markdown
Slug: markdown
Authors: Amit
Summary: Markdown reference

The posts on this blog are written in Markdown. The full specs of Markdown are [here] [md], but the most useful commands are summarized here.

[md]: //daringfireball.net/projects/markdown/syntax

Markdown is written in a plain text file.

## Headings

Headings are denoted by a series of `#` characters for heading levels 1-6:

    # Heading 1
    ## Heading 2
    ### Heading 3
    #### Heading 4
    ##### Heading 5
    ###### Heading 6

# Heading 1
## Heading 2
### Heading 3
#### Heading 4
##### Heading 5
###### Heading 6

## Formatting

Paragraphs are separated by blank lines.  
Line breaks are added by terminating lines with two spaces.

    Text formatting: *italic*, **bold**, `monospace`.

Text formatting: *italic*, **bold**, `monospace`.

The monospace formatting is also useful for escaping certain characters and strings, but also see the code block section below. The escape code for special characters is `\`.

Horizontal rules are specified by three or more  `-` characters on a line.

    ---

---

## Links

There are two main kinds of link, I'll call them inline and referenced.

    :::markdown
    This is an [inline](//www.example.com) link.
    
    And this is a [referenced] [ref] link.
    [ref]: //www.example.com
    
This is an [inline](//www.example.com) link.

And this is a [referenced] [ref] link.
[ref]: //www.example.com

## Code
A code block is indicated by starting the line with 4 spaces (a tab in most of the text editors I've set up). This will format the code in a monospace font, and ensure that everything in the block remains escaped (rather than parsed as Markdown).

Pelican also has syntax highlighting support via Pygments. To invoke this, add `:::<language>` to the beginning of the code block, where `<language>` is replaced by whatever language you want to highlight for. Alternatively, use `#!<language>` to add line numbering.


There's a demonstration of this on [this](/pythonexample.html) page.

## Images

Images are incorporated as a special kind of link, preceeded by the `!` character. They too come in inline and referenced forms.

Inline

    ![Alt text](/path/to/img.jpg)
    ![Alt text](/path/to/img.jpg "Optional title")

Referenced

    ![Alt text][id]
    [id]: url/to/image  "Optional title attribute"


## Anything else

HTML can be incorporated directly into Markdown for anything that's not otherwise easily accomplished.