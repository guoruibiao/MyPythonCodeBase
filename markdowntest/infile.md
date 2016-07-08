
## A tool for markdown to html

coding:utf-8<br>
__author__ = 'Mark sinoberg'<br>
__date__ = '2016/7/8'<br>

```
from markdown import markdown
import optparse

class MDParser:

    def __init__(self):
        print 'Ready to parser markdown source file to html file.'

    def parsre(self, infile):
        infile = open(infile, 'rb')
        indata = infile.read()
        indata = u'%s'%indata
        infile.close()
        parsedata = markdown(indata)
        return parsedata

    def appendHead(self, data, title):
        head = \
            """
            <html><head><meta charset='utf-8'><title>%s</title><meta name="viewport" content="width=device-width, initial-scale=1">
 	 <link rel="stylesheet" href="http://apps.bdimg.com/libs/bootstrap/3.3.0/css/bootstrap.min.css">
 	 <script src="http://apps.bdimg.com/libs/jquery/2.1.1/jquery.min.js"></script>
 	 <script src="http://apps.bdimg.com/libs/bootstrap/3.3.0/js/bootstrap.min.js"></script></head><body><div class='container' align='center'>
            """ % title
        newdata = head + data
        return newdata

    def appendTail(self, data):
        tail = \
            """
            </div><script src="http://apps.bdimg.com/libs/jquery/2.1.1/jquery.min.js"></script>
    <script src="http://apps.bdimg.com/libs/bootstrap/3.2.0/js/bootstrap.min.js"></script></body></html>
            """
        data += tail
        return data

    def output(self, data, outfile):
        outfile = open(outfile, 'wb')
        outfile.write(data)
        outfile.close()
        print "Translated Succeed!"

```

```
    usage = \
        """
        '-i', --infile . source markdown file
        '-o', --outfile. target html file
        '-s', --style. stylesheet for output html file,this is not for mandatory
        """
    parser = optparse.OptionParser(usage)

    parser.add_option('-i', '--input', dest='infile', type='string', help='input markdown source file')
    parser.add_option('-o', '--output', dest='outfile', type='string', help='out put html file')
    (options, args) = parser.parse_args()
    infile = options.infile
    outfile = options.outfile

    if __name__ == "__main__":
        tool = MDParser()
        title = raw_input('Please input the title you want:\n')
        parsedata = tool.parsre(infile)
        data = tool.appendHead(parsedata, title)
        fulldata = tool.appendTail(data)
        tool.output(fulldata, outfile)

```