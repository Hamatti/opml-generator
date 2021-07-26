import sys
from pathlib import Path

if len(sys.argv) < 2: 
    raise Exception("Please provide input filename")

opml_output = '''
  <opml version="1.0">
    <head>
      <title>Developer Blogs</title>
    </head>
    <body>
    '''

filename = sys.argv[1]
with open(filename, 'r') as f:
    for line in f:
        url = line.strip()
        opml_output = f'{opml_output}<outline type="rss" xmlUrl="{url}"/>\n'

opml_output = f'''{opml_output}
</body>
</opml>'''

with open(f'{Path(filename).stem}.opml', 'w') as outfile:
    outfile.write(opml_output)
