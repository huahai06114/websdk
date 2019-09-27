# -*- coding: utf-8 -*-
"""
    Author: 阿慕路泽
    Description： 用户认证
"""
import jwt
import datetime
import hashlib

from .configs import configs


class AuthToken(object):
    def __init__(self):
        self.token_secret = configs.get('token_secret', '3AIiOq18i~H=WWTIGq4ODQyMzcsIdfghs')

    def encode_auth_token(self, **kwargs):
        """
        生成认证 token
        :param user_id:
        :return: bytes
        """
        try:
            exp_time = kwargs.get('exp_time', 1)
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=int(exp_time), seconds=10),
                'nbf': datetime.datetime.utcnow() - datetime.timedelta(seconds=10),
                'iat': datetime.datetime.utcnow(),
                'iss': 'auth: ss',
                'sub': 'my token',
                'id': '15618718060',
                'data': {
                    'user_id': kwargs.get('user_id', ''),
                    'username': kwargs.get('username', ''),
                    'nickname': kwargs.get('nickname', ''),
                    'email': kwargs.get('email', ''),
                    'is_superuser': kwargs.get('is_superuser', False)
                }
            }
            return jwt.encode(
                payload,
                self.token_secret,
                algorithm='HS256'
            )

        except Exception as e:
            return e

    def decode_auth_token(self, auth_token):
        """
        验证 Token
        :param auth_token:
        :return:
        """
        try:
            payload = jwt.decode(auth_token, self.token_secret, algorithms=['HS256'],
                                 leeway=datetime.timedelta(seconds=10))
            if 'data' in payload and 'user_id' in payload['data']:
                return payload['data']
            else:
                raise jwt.InvalidTokenError
        except jwt.ExpiredSignatureError:
            return dict(status=-1, msg='Token过期')
        except jwt.InvalidTokenError:
            return dict(status=-2, msg='无效Token')


def gen_md5(pd):
    m2 = hashlib.md5()
    m2.update(pd.encode("utf-8"))
    return m2.hexdigest()
