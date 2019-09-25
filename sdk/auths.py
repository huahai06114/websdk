# -*- coding: utf-8 -*-
"""
    Author: 阿慕路泽
    Description：
"""
import jwt
import datetime
import hashlib

from .configs import configs


class Auth(object):
    @staticmethod
    def encode_auth_token(user_id):
        """
        生成认证 token
        :param user_id:
        :return: bytes
        """
        try:
            headers = {
                "typ": "JWT",
                "alg": "HS256",
                "user_id": user_id
            }

            playload = {
                "headers": headers,
                "iss": "robot",
                "exp": datetime.datetime.utcnow() + datetime.timedelta(days=0, hours=1, minutes=0, seconds=0),
                "iat": datetime.datetime.utcnow()
            }
            signature = jwt.encode(playload, configs['SECRET_KEY'], algorithm="HS256")
            return signature
        except Exception as e:
            print(e)
            return e

    @staticmethod
    def decode_auth_token(auth_token):
        """
        验证 Token
        :param auth_token:
        :return:
        """
        try:
            payload = jwt.decode(auth_token, configs['SECRET_KEY'], options={'verify_exp': False})
            if payload:
                return payload
            else:
                raise jwt.InvalidTokenError
        except jwt.ExpiredSignatureError:
            raise jwt.ExpiredSignatureError
        except jwt.InvalidTokenError:
            raise jwt.InvalidTokenError


def gen_md5(pd):
    m2 = hashlib.md5()
    m2.update(pd.encode("utf-8"))
    return m2.hexdigest()
