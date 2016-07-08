# coding:utf-8

#    __author__ = 'Mark sinoberg'
#    __date__ = '2016/7/8'
#    __Desc__ = 将markdown文件转换为带有样式的html文件

from markdown import markdown
import optparse


# 创建一个专门用于处理解析器的工具类
class MDParser:
    # 初始化开始
    def __init__(self):
        print 'Ready to parser markdown source file to html file.'

    # 创建一个对输入文件进行解析的方法，输出文件即为符合html语法的不完整文件
    def parsre(self, infile):
        infile = open(infile, 'rb')
        indata = infile.read()
        indata = u'%s' % indata
        infile.close()
        parsedata = markdown(indata)
        return parsedata

    # 为输出文件添加自定义标题，并且添加缺少的html头部
    def appendHead(self, data, title):
        head = \
            """
            <html><head><meta charset='utf-8'><title>%s</title><meta name="viewport" content="width=device-width, initial-scale=1">
 	 <link rel="stylesheet" href="http://apps.bdimg.com/libs/bootstrap/3.3.0/css/bootstrap.min.css">
 	 <script src="http://apps.bdimg.com/libs/jquery/2.1.1/jquery.min.js"></script>
 	 <script src="http://apps.bdimg.com/libs/bootstrap/3.3.0/js/bootstrap.min.js"></script></head><body><div class='container'><div class="row-fluid">
		<div class="span12">
            """ % title
        newdata = head + data
        return newdata

    # 配合上面的添加头部文件，下面的这个方法适用于添加html尾部标签，使得文件符合html规范
    def appendTail(self, data):
        tail = \
            """
            </div></div></div><script src="http://apps.bdimg.com/libs/jquery/2.1.1/jquery.min.js"></script>
    <script src="http://apps.bdimg.com/libs/bootstrap/3.2.0/js/bootstrap.min.js"></script></body></html>
            """
        data += tail
        return data

    # 将完整的html文件输出到指定的位置
    def output(self, data, outfile):
        outfile = open(outfile, 'wb')
        outfile.write(data)
        outfile.close()
        print "Translated Succeed!"


# OptParser库规范性用法，以实现Unix风格的命令行处理程序
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
