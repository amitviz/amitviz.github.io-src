Title: pygments
Date: 2015-11-06
Modified: 2015-11-07
Category: Notes
Tags: code, python, pygments
Slug: pythonexample
Authors: Amit
Summary: Syntax highlighting test

Pygments is included in my installation of Pelican. Here are a couple of code fragments to test that syntax highlighting is working correctly.

This is an example of a Python file, presented with line numbers:

    #!python
    import unittest
    def median(pool):
        copy = sorted(pool)
        size = len(copy)
        if size % 2 == 1:
            return copy[(size - 1) / 2]
        else:
            return (copy[size/2 - 1] + copy[size/2]) / 2
    class TestMedian(unittest.TestCase):
        def testMedian(self):
            self.failUnlessEqual(median([2, 9, 9, 7, 9, 2, 4, 5, 8]), 7)
    if __name__ == '__main__':
        unittest.main()

And here a matlab function, this time without line numbers:

    :::matlab
    function echo_number
    %
    % Ask the user for a number, and then echo it to the screen.
    %   Quit when the number given is -1.
    %   
    % Arguments:
    %      none
    %                   

    % this is the value we'll use to terminate the loop
    quit_value = -1;

    done_yet = 0;
    while (done_yet == 0)
        user_value = input('gimme a number ');
        fprintf(1, 'you typed %f \n', user_value);

        if (user_value == quit_value)
        done_yet = 1;
        end
        
    end