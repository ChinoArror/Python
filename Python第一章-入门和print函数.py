    #Python入门和print函数
#将内容输入到文件中,open函数的第二个参数是打开模式，a+是编辑打开，没有文件自动创建一个
d=open('D:/test.txt','a+')
print('hello world',file=d)
d.close()

#转义字符
print('hello\nworld') #  \   +转义功能的首字母   n→newline的首字母，表示换行，不带空格
print('hello\tworld') # 给后面的内容添加制表符
print('hello\rworld') #换行

#转义字符 \ 使其后的一个字符变为字符串
print('https:\\\\www.baidu.com') #第一个和第三个 \ 使第二个和第四个 \ 变为字符串，不起转义字符的作用
print('老师说:\'大家好\'') #两个 \ 使其后的两个单引号变为字符串，正常输出

#原字符，不希望字符串中的转义字符起作用，就使用原字符，就是在字符串前加上r，或R
print(r'hello\nworld')
#注意事项，字符串中最后一个字符不能是 \ 。
#错误： print(r'hello\nworld\') 
