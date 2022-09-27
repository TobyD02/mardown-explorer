import markdown
import os

# TODO:
# - Open a given directory
#   - For each child, if file is .md then convert to html, if folder then enter it recursively

# Prints each file in directory
def main(dir=os.getcwd()):
    res = []
    for path in os.listdir(dir):
        if os.path.isfile(os.path.join(dir, path)):
            res.append(path)

    print(res)

main()