# encoding: UTF-8
"""
分词模块的单元测试
"""


import unittest
import requests
import app

class TestCutting(unittest.TestCase):
    """
    TS模块的本地测试。仅用于在构建镜像之前确保服务正确运行
    """
    def setUp(self):
        self.tpl = 'http://localhost:{}'.format(app.PORT)
        self.text = '凤城何处花枝/等奴来相织'
        self.data = {'text': self.text}

    def test_cut(self):
        """
        测试默认分词模式
        """
        url = self.tpl + '/cut'
        res = requests.post(url, data=self.data)
        self.assertEqual(res.status_code, 200)
        result = res.json()
        self.assertEqual(result['text'], self.text)
        self.assertEqual(''.join(result['words']), self.text)


    def test_cut_all(self):
        """
        测试全分词模式
        """
        url = self.tpl + '/cut_all'
        res = requests.post(url, data=self.data)
        self.assertEqual(res.status_code, 200)
        result = res.json()
        self.assertEqual(result['text'], self.text)
        self.assertTrue(all(map(lambda w: w in self.text, result['words'])))
