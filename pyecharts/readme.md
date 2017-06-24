## `pyecharts`

总的来说，这个实现的有点鸡肋。本意是后台通过代码提供数据，然后获取前台浏览器渲染后的echarts图片，再用于程序的其他方面的`展示`。

---

### 需要注意的是：

- 安装了selenium以及相关驱动。
- selenium 下载的图片文件会被保存到`C:\users\{username}\downloads\下载.png`。所以可能需要自己控制路径修改。
- canvas转图片其实不是真正的转图片，通过`canvas.toDataURL()`得到的是一个base64编码的图片路径。详细可参考：[toDataURL详解](http://aiyouu.net/data-uris-explained/)

---

### 用法

对于templates目录下的index.html文件的js部分，需要更改的就是`option`部分，结合后台提供的数据即可显示相关的`echarts`图片信息。

当然也可以将不相关的js文件提取出来，放到`static`目录下，进行更灵活的处理。

