# Assumes your markdown links will be placed in a subfolder called /images
# adjacent to the .md file.

# example_obsidian_link = "![[something.png]]"
# example_markdown_link = "![](images/something.png)"

# Converts ![](images/input_string) into ![[input_string]]
def markdown_to_obsidian(input_string):
    new_text = input_string
    new_text = new_text.replace("[", "[[")
    # todo: add a conditional that checks for an images folder
    # if new_text.contains("images/"): else:
    new_text = new_text.replace("](images/", "")
    new_text = new_text.replace(")", "]]")
    return new_text

# Converts ![[input_string]] to ![](images/input_string)
def obsidian_to_markdown(input_string):
    new_text = input_string
    new_text = new_text.replace("]]", ")")
    new_text = new_text.replace("[[", "[](images/")
    return new_text
