from html.parser import HTMLParser
from functools import reduce
from operator import add


class MinifyHTMLParser(HTMLParser):
    code = ""

    def handle_decl(self, decl):
        self.code += "<!%s>" % decl

    def handle_starttag(self, tag, attrs):
        attr = lambda x: ' %s="%s"' % (x[0], x[1])
        strattrs = reduce(add, map(attr, attrs), "")
        content = tag + strattrs
        self.code += "<%s>" % content

    def handle_endtag(self, tag):
        self.code += "</" + tag + ">"

    def handle_data(self, data):
        if data.rstrip() != "":
            self.code += data
