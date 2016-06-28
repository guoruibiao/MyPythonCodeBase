# coding:UTF-8
import Sample
import urllib
def main():
    str = "http://www.baidu.com"
    result = urllib.urlopen(str).read()
    print result

if __name__ == "__main__":
    main()
