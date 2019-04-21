# HTML minify


Example:
```python
from parser import MinifyHTMLParser
parser = MinifyHTMLParser()
with open('index.html', 'r') as source:
    code = parser.feed(''.join(source.readlines()))

with open('index.html', 'w') as target:
    target.write(parser.code)
```
