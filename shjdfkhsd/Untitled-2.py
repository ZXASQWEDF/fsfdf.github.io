#！ /usr/bin/env python
# -*- coding:utf-8 -*-


salary = input("请输入本月工资：")  #提示用户输入工资

if  salary.isdigit():   #判断用户输入的是否是数字，如果不是则提示错误信息直接退出
    salary = int(salary)
else:
    exit("输入错误，再见")

welcome_msg = '欢迎来到LikePython超市'.center(50, '-')  #如果用户输入的是数字，则打印欢迎信息
print(welcome_msg)

exit_flag = False  #为了能够随时判断用户是否主动退出，在此设置一个退出标志位

product_list = [   #以列表形式保存商品信息，还可以以字典形式保存商品信息
    ('Iphone', 5888),
    ('Mac Air', 8000),
    ('Mac Pro', 9000),
    ('XiaoMi', 100),
    ('Coffee', 19.9),
    ('Tesla', 820000),
    ('Bike', 700),
    ('Cloth', 200),
]

shopping_cart = []   #定义购物车

while not exit_flag:  #当exit_flag不为真时
    print("\n")
    print("商品列表".center(50,'='))
    '''
    for product_item in product_list:
        p_name,p_price = product_item  #这是循环显示列表中商品的一种方法

    for p_name,p_price in enumerate(product_list):   #这是循环显示列表中商品的另一种方法
        print(p_name,p_price)
    '''
    for item in enumerate(product_list):  #将每件商品的下标显示出来
        index = item[0]
        p_name = item[1][0]
        p_price = item[1][1]
        print(index,'.',p_name,p_price)

    user_choice = input("[q=quit,c=check]请输入商品编号：")
    if user_choice.isdigit():  #如果用户输入了数字，则肯定是要选商品
        user_choice = int(user_choice)  #将用户输入转换成整型
        if user_choice < len(product_list):  #判断用户输入的数字是否在商品列表范围内，如果是，则确定了商品在列表中的下标
            p_item = product_list[user_choice]  #取出了用户的商品，取出的数据形式为"Iphone 5888"
            if p_item[1] <= salary:  #从取出的数据"Iphone 5888"中取出商品的价格，判断是否小于等于用户输入的工资
                shopping_cart.append(p_item)  #将用户买的起的商品放入购物车
                salary -= p_item[1]   #减钱
                print("已购买了[%s]，现有可用余额\033[31;1m [%s] \033[0m " % (p_item,salary))  #用户购买商品后显示已购买的商品及当前余额
            else:
                print("当前余额为[%s]，余额不足！" % (salary))  #用户当前余额不足
    else:
        if user_choice == 'q' or user_choice == 'quit':  #如果用户输入的是q或quit，表示用户要退出程序
            print("已购买的商品列表如下".center(40, '*'))
            for buied_products in shopping_cart:    #打印用户已购买的商品
                print(buied_products)
            print("列表结束".center(40, '*'))
            print("当前余额为[%s]" % (salary))     #打印用户当前余额
            print("再见")
            exit_flag = True    #将退出标志位置为True即可退出
        elif user_choice == 'c' or user_choice == 'check':
            print("已购买的商品列表如下".center(40, '*'))
            for buied_products in shopping_cart:  # 打印用户已购买的商品
                print(buied_products)
            print("列表结束".center(40, '*'))
            print("当前余额为\033[41;1m[%s]\033[0m" % (salary))  # 打印用户当前余额




'''
插入一个知识点：

a = ['zhangsan','lisi','wangwu']   #准备一个列表
for index,i in enumerate(a):  #循环列表，注意此处的enumerate
    print(index,i)  #打印列表
#Python3下打印结果如下
0 zhangsan
1 lisi
2 wangwu
'''