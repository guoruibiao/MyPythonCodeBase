# coding:utf-8

stu_number = '201492115'
password = '285514'

dlut_url = 'http://zhjw.dlut.edu.cn/'
login_url = 'http://zhjw.dlut.edu.cn/loginAction.do'

login_data = {
    'mm': password,
    'zjh': stu_number
}

login_header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Safari/537.36 Edge/13.10586',
    'referer': 'http://zhjw.dlut.edu.cn/',

}

course_url='http://zhjw.dlut.edu.cn/xkAction.do?actionType=6'
course_header={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Safari/537.36 Edge/13.10586',
    'referer':'http://zhjw.dlut.edu.cn/menu/s_main.jsp'
}
