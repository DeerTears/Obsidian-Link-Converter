import obsidian_link_converter
filepath = ""
choice = input("Which file are you converting from? obsidian or markdown: ")
if choice == "obsidian":
    # todo: don't handle one link at a time, but rather pass a file directly and parse every instance of a link to replace
    filepath = input("Enter obsidian link to convert: ")
    filepath = obsidian_link_converter.obsidian_to_markdown(filepath) 
elif choice == "markdown":
    obsidian_link_converter.markdown_to_obsidian(filepath)
    filepath = input("Enter markdown link to convert: ")
    filepath = obsidian_link_converter.markdown_to_obsidian(filepath)
else:
    print("choice not understood, canceling...")
    input()
print(filepath)
input()
