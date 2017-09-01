# -*- coding: utf-8 -*-
import unittest

class TesteLocal(unittest.TestCase):

    def teste_maiusculo(self):
        self.assertEqual('foo'.upper(), 'FO1')

# testar = TesteLocal()
# print testar.teste_maiusculo()

if __name__ == '__main__':
    unittest.main()
