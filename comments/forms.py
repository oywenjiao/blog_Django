#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/12 14:45
# @Author  : OuYang
# @Site    : 
# @File    : forms.py
# @Software: PyCharm
from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'url', 'text']
