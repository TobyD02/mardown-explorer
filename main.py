import markdown
import os

# TODO:
# - Open a given directory
#   - For each child, if file is .md then convert to html, if folder then enter it recursively | DONE
#   - Convert each md into an html file and store all new html in a new folder
#   - Create a contents page for each html file and sub directory

# Prints each file in directory
def main(dir=os.getcwd()):
    # Gather all markdown files

    res = []
    for path in os.listdir(dir):
        if (os.path.isdir(os.path.join(dir, path))):
            res = res + search_dir(os.path.join(dir, path), path)
        if os.path.isfile(os.path.join(dir, path)) and path[-3:] == '.md':
            res.append(path)


    # Create sub directory
    try:
        os.mkdir(os.path.join(dir, 'Markdown Webpage'))
    except:
        print('directory already exists')

    html = {}

    # Read the files labelled .md, convert to html and store
    for path in res:
        if (path[-3:] == '.md'):
            with open(path) as f:
                html[path[:-3] + '.html'] = convert_to_html(f.read())


    # Sub directories and html files
    for filename, data in html.items():
        dir = 'Markdown Webpage/'
        if ('/' in filename):
            for i in (filename.split('/')):
                if (i[-5:] != '.html'):
                    try: os.mkdir(dir + i)
                    except: pass
                    dir = dir + i + '/'
        f = open('Markdown Webpage/' + filename, 'w')
        f.write(data)
        f.close()

    # Create index file
    index = create_index_page(html.keys())

    f = open('Markdown Webpage/index.html', 'w')
    f.write(index)
    f.close()



def search_dir(dir, rel_dir):
    res = []
    for path in os.listdir(dir):
        if os.path.isdir(os.path.join(dir, path)):
            res = res + search_dir(os.path.join(dir, path), rel_dir + '/' + path)
        if os.path.isfile(os.path.join(dir, path)) and path[-3:] == '.md':
            res.append(rel_dir + '/' + path)

    return res

def convert_to_html(md_text):
    return markdown.markdown(md_text)


def create_index_page(dirs):

    html = \
    """
    <html>
        <head>
        </head>
        <body>
            <ul>
                ***LINKS***
                ***LINKS***
            </ul>
        </body>
    </html>
    """

    html_list = html.split('***LINKS***')

    for location in dirs:
        li_object = "<a href='" + location + "'>" + location.split('/')[-1][:-5] + '</a>\n'
        html_list.insert(1, li_object)

    return ''.join(html_list)



main()
# create_index_page()