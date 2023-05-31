import os

fileLocation = "C:\\Users\\mortiz\\Desktop\\a\\"
fileList = os.listdir(fileLocation)


# creating a variable and storing the text
# that we want to search
search_text = "_visor.svg"

# creating a variable and storing the text
# that we want to add
replace_text = ".svg"


for filename in os.listdir('C:\\Users\\mortiz\\Desktop\\a\\'):
    if filename.endswith('.sld'):
        with open(r ii) as file:

            	# Reading the content of the file
            	# using the read() function and storing
            	# them in a new variable
            	data = file.read()

            	# Searching and replacing the text
            	# using the replace() function
            	data = data.replace(search_text, replace_text)

            # Opening our text file in write only
            # mode to write the replaced content
            with open(r ii, 'w') as file:

            	# Writing the replaced data in our
            	# text file
            	file.write(data)

            # Printing Text replaced
            print("Text replaced")

