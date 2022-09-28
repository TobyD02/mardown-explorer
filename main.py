import markdown
import os

# TODO:
# - Open a given directory
#   - For each child, if file is .md then convert to html, if folder then enter it recursively

# Prints each file in directory
def main(dir=os.getcwd()):
    # Gather all markdown files

    res = []
    for path in os.listdir(dir):
        if (os.path.isdir(os.path.join(dir, path))):
            res = res + search_dir(os.path.join(dir, path), path)
        if os.path.isfile(os.path.join(dir, path)) and path[-3:] == '.md':
            res.append(path)
    print(res)

    # Read the files labelled .md
    # for path in res:
    #     if (path[-3:] == '.md'):
    #         with open(path) as f:
    #             print(f.read())

def search_dir(dir, rel_dir):
    res = []
    for path in os.listdir(dir):
        if os.path.isdir(os.path.join(dir, path)):
            print(dir + '/' + path)
            print('hit')
            res = res + search_dir(os.path.join(dir, path), rel_dir + '/' + path)
        if os.path.isfile(os.path.join(dir, path)) and path[-3:] == '.md':
            res.append(rel_dir + '/' + path)

    return res
main()