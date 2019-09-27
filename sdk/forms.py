# -*- coding: utf-8 -*-
"""
    Author: 阿慕路泽
    Description：
"""
from wtforms import Form
from wtforms import PasswordField, StringField, IntegerField
from wtforms.validators import DataRequired, Regexp, EqualTo, Optional
from app.sdk.exceptions import ParameterError


class WTForm(Form):

    def __init__(self, data, args):
        super(WTForm, self).__init__(data=data, **args)

    def validate_for_api(self):
        valid = super(WTForm, self).validate()
        if not valid:
            print(self.errors)
            raise ParameterError('parameter error')
        return self


# 更新密码校验
class UpdatePasswordForm(WTForm):
    username = StringField('username', validators=[
        DataRequired('用户名不可为空')
    ])
    old_password = PasswordField('old_password', validators=[
        DataRequired(message="旧密码不能为空"),
        Regexp(r'^[A-Za-z0-9_*&$#@]{6,22}$', message="密码长度必须在6~22位之间，包含字符、数字和 _ "),
        EqualTo('confirm_password', message="两次输入的密码不一致，请输入相同的密码")
    ])
    new_password = PasswordField('new_password', validators=[
        DataRequired(message="新密码不能为空"),
        Regexp(r'^[A-Za-z0-9_*&$#@]{6,22}$', message="密码长度必须在6~22位之间，包含字符、数字和 _ "),
        EqualTo('confirm_new_password', message="两次输入的新密码不一致，请输入相同的密码")
    ])
    confirm_new_password = PasswordField('confirm_new_password', validators=[
        DataRequired(message="请确认新密码")
    ])


# 更新用户名校验
class UpdateUsernameForm(WTForm):
    old_username = StringField('old_username', validators=[
        DataRequired('用户名不可为空')
    ])
    new_username = StringField('new_username', validators=[
        DataRequired('用户名不可为空')
    ])


# 更新邮箱校验
class UpdateEmailForm(WTForm):
    old_email = StringField('old_email', validators=[
        DataRequired('邮箱不可为空')
    ])
    new_email = StringField('new_email', validators=[
        DataRequired('邮箱不可为空'),
        Regexp(r'^[a-zA-Z0-9_.-]+@[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)*\.[a-zA-Z0-9]{2,6}$', message='电子邮箱不符合规范，请输入正确的邮箱')
    ])
