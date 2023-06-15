import unittest
import bintree

class TestBinTreeMethods(unittest.TestCase):

    def test_calcAltura(self):
        tree=bintree.Tree()
        tree.insert(4)
        tree.insert(6)
        tree.insert(5)
        tree.insert(7)
        tree.insert(2)
        tree.insert(1)
        tree.insert(3)
        self.assertEqual(tree.calcAltura(), 3)
    
    def test_inserir(self):
        tree=bintree.Tree()
        self.assertEqual(tree.insert(), 'i')

        
if __name__== '__main__':
    unittest.main()



