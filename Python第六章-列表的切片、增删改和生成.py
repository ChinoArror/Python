#变量存储的是值的索引
a=10
#列表存储的是所有值的索引
lst1=[1,'hello','word']
print(type(lst1))
print(id(lst1))
print(lst1)

'''创建列表的第一种方式，使用[]'''
lst=['hello','world',98,'hello']

'''创建列表的第二种方式，使用函数list()'''
lst2=list(['hello','world',98,'hello'])

#索引，lst[0]指列表lst中正序第一个元素，lst[1]指正序第二个元素
#lst[-1]指倒序第一个元素，lst[-2]指倒序第二个元素
print(lst[0],lst[-3])

'''查找元素的索引，元素要在列表中'''
print(lst.index('hello')) #如果列表中有相同元素，只返回第一个相同元素的索引
print(lst.index('world'))
print(lst.index('hello',1,4))#在索引1-4的范围内查找元素，返回索引，包含前一个，不包含后一个
                                  #如包含1对应的元素，不包含4对应的元素

'''索引查找元素，索引要在范围内'''
lst3=['hello','world',98,'hello',3224,534]
#希望获取索引为2的元素
print(lst3[2]) #98
#希望获取倒数第三个元素，即索引为-3
print(lst3[-3])

'''一次获取多个元素-切片，切片出来是一个新列表对象，是原列表片段的拷贝'''
'''范围：start-stop，包含start，不包含stop，左闭右开'''
lst4=[10,20,30,40,50,60,70,80,90]
#start=1,stop=6,step=1默认为1,冒号隔开
print(lst4[1:6:1])
print('原列表',type(lst4))
lst5=lst4[1:6:1]
print('切片后',type(lst5))#切片后仍为列表对象

#start=1,stop=6,step=2
print(lst4[1:6:2]) #[20,40,60]
#stop=6,step=2,start采用默认 为0
print(lst4[:6:2]) #[10,30,50]
#start=1,step=1,stop采用默认 ,默认切片到最后一个元素，包含最后一个
print(lst4[1::1]) #[20, 30, 40, 50, 60, 70, 80, 90]

'''步长为负数，从范围的后面向前切片'''
'''步长为负数，start与stop互换，但仍是包含start，不包含stop'''
print('-----------------step步长为负数的情况------------------')
#start stop默认，step=-1
print(lst4[::-1]) #[90, 80, 70, 60, 50, 40, 30, 20, 10]
#start=8,step=-1,stop默认
print(lst4[8::-1]) #[90, 80, 70, 60, 50, 40, 30, 20, 10]

'''列表元素的判断，只能判断整个元素，不能判断其中的一部分'''
lst6=[10,20,'python','hello']
print(10 in lst6) #True
print(100 in lst6) #False
print('python' not in lst6) #False
print('h' in lst6) #False

'''列表元素的遍历，重复循环并将列表中的元素写入变量item中'''
for item in lst6:
    print(item)
    print('python' in str(item)) #int不可迭代，需要转成str格式
    print(type(item))


'''列表添加元素'''
'''列表末尾添加，没有创建新的列表对象，在原列表上改'''
l=[10,20,30]
l1=[10,20,30]
print('添加元素前', l , id(l) )
l.append(100)
print('添加元素后', l , id(l) )

l2=['hello','world']
l1.append(l2) #将l2作为一个元素加入l1的末尾
print(l1)
l.extend(l2) #将l2的每一个元素分别加入l的末尾
print(l)
#在任意位置加入一个元素
l.insert(1,90) #在索引为1的位置上加入一个元素90
print(l)

l3=[True,False,'hello']
#在列表任意位置添加多个元素
print('添加前',l)
l[1:3]=l3 #先选中start=1，stop=3的这部分元素，再将他们替换为l3，至少需要换掉一个元素
            #仍然包含start，不包含stop，不可以设置step
print('添加后',l)


'''删除列表元素'''
#remove()，一次删除一个元素，重复元素只删第一个
s=[10,20,30,40,50,60,30]
print('前',s)
s.remove(30) #移除一个元素，要给出元素名
print('后',s)

#pop()，删除列表中指定索引位置上的一个元素，不指定索引则删除最后一个元素
print('前',s)
s.pop(1)
print('后',s)
s.pop() #不给索引，删最后一个
print('后',s)

print('----------切片操作-删除至少一个元素，将产生一个新的列表对象----------')
n_s=s[1:3]
print('原列表',s)
print('提取出的新列表',n_s)
#删除原列表中的元素，不创建新的列表
s[1:3]=[] #将切片的元素赋值为空，相当于删除这部分
print('删除后',s)

#clear()，清除列表中所有元素
s.clear()
print(s)

#del 语句将列表删除
del s #删除s
#print(s)  #报错，因为已经没有列表s


'''修改列表元素'''
s=[10,20,30,40]
#一次修改一个值
s[2]=50
print(s)
#一次修改多个值
s[1:3]=[200,300,400,500] #相当于为切片的元素重新赋值 
print(s)
s[1:5]=[] #等于空，相当于删除
print(s)


'''为列表中的元素排序'''
s=[20,40,10,98,54]
print('排序前',s,id(s))
#开始排序，调用列表对象的sort方法，id不改变，默认升序
s.sort()
print('排序后',s,id(s))

#通过指定关键字参数，将列表中的参数降序排序
s.sort(reverse=True)
print('排序后',s)
#reverse=True降序，=False升序
s.sort(reverse=False)
print('排序后',s)


#使用sorted()进行排序，将产生一个新的列表对象，默认升序
print('原',s,id(s))
#开始排序
snew=sorted(s)
print(s)
print('新',snew,id(snew))
#指定参数，实现降序排序，True降序，False或不填升序
snew=sorted(s,reverse=True)
print(snew)


'''列表生成式'''
ls=[i for i in range(1,10)] #for in 后要加一个可迭代元素，后半部分给i赋值，真正决定列表内容的是最前面的部分(i)
print(ls) #[1, 2, 3, 4, 5, 6, 7, 8, 9] 输出结果为i
ls=[i*i for i in range(1,10)] #输出结果为i*i
print(ls) #[1, 4, 9, 16, 25, 36, 49, 64, 81]
ls=[2*i for i in range(1,10)]
print(ls) #[2, 4, 6, 8, 10, 12, 14, 16, 18] 输出结果为2*i

