#!/usr/bin/env python3
import string
# -*- coding: utf-8 -*-
print(chr(97));
print(len('chan'));
print("abc".encode().decode());
str = "hello %s %s %s";

print(str % ('word', 'py', 'moon'))
print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)

fz = (82 - 72) / 72 * 100
print('{0:.2f}%'.format(fz));