# cookbook
Cookbook search engine

## What it is
This is a tool for searching a cookbook for recipes containing tags. It spits out the pages of each recipe containing the tag. It is meant as a cooking aid.

## Requirements
 - Python
 - (Termcolor)[https://pypi.org/project/termcolor/] python package

Term color isn't needed, but you'll have to modify the output everywhere

## Setup
The input needs to come in the form
'
page#, tag 1, tag 2, tag 3, ...
'
in the raw.txt file. Included is an example.
If entering the information using the inprogram option, follow the prompts.
The search database needs to be refreshed after any updates to the database (this means after adding entries as well).


### How it works
The raw file is separated into tags and the associated page number. The tags are enumerated and sorted alphabetically using the builtin python list sort function. The tags are added to the search file along with each page number it occurs at. The search is a binary search for the tags
