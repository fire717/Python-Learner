# -*- coding: utf-8 -*-

'''
python为修饰器提供了专门的语法，它使得程序在运行的时候，能够用一个函数来修饰另一个函数

对于调试器这种依靠内省机制的工具，直接编写修饰器会引发奇怪的行为

内置的functools模块提供了名为wraps的修饰器，开发者在定义自己的修饰器时，应该用wraps对其做一些处理以避免问题
'''
