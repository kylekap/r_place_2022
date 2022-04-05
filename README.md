# R_Place analysis

Currently only working for the 2017 officially released version of data, will update/do work with 2022 version when data becomes available.

## Data description
Single CSV file located in the Data folder. Currently utilizing Data/2017/tile_placements.csv, which has 5 columns. ts,user,x_coordinate,y_coordinate,color

### Additional notes about data
- Since color is in 0-15, used config file dictionary to redefine to their corresponding hex colors.
- I think the (999,999) is the bottom left corner. This would imply graphing is - X / - Y coordinate space? (Have to actually graph to get a better understanding)
- user is a just a hash value


## ToFix
- [ ] layout of X / Y coordinates

## ToAdd
- [ ] Example
<!--pip freeze > requirements.txt -->

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)