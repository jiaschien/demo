import markdown
markdown_src = """
## Python Code:

"""

print markdown.markdown(src,extensions=["codehilite"])

