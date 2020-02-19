#!/usr/bin/env python3
# importing the needed modules for using the inputs through thr html form
import cgi
import cgitb

# enabling this module is needed to log errors to the browser
cgitb.enable()
# this stores the inputs in the FieldStorage Class
form = cgi.FieldStorage()
# this stores the value from the input in a variable
# the + \n is needed because when creating a list Python puts a \n at the end of each list item because there is a new line in the file. This was the easiest workaround for the problem.
color = str(form.getvalue("color").title()) + "\n"

# theese are the variables used to create the html
website_if_true = """
<!DOCTYPE html>
<html>
    <head>
        <title>Page Title</title>
    </head>
    <body>
        <h1>{} is a color.</h1>
    </body>
</html>
""".format(color)

website_if_false = """
<!DOCTYPE html>
<html>
    <head>
        <title>Page Title</title>
    </head>
    <body>
        <h1>{} is not a color.</h1>
        <div></div>
    </body>
</html>
""".format(color)

# open the text file in read mode
file = open("cgi-bin/colors.txt", "r")

# make a list out of the file and store it
list_of_colors = list(file)

# logic to decide whether or not something is a color
if color in list_of_colors:
    print(website_if_true)
else:
    print(website_if_false)

# closing the file again
file.close()