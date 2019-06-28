from django.test import TestCase
from django.urls import reverse
from .models import TransactionalFunction
from .views import getComplexity, getFunctionPoints
from .forms import TransactionFunctionForm

class TransactionalFunctionTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        TransactionalFunction.objects.create(functionalityName="funcionalityTest1", functionalityType="EE", qtdALR=1, qtdDER=1, functionComplexity="abcd", qtdFunctionPts=1, countName="test")
        TransactionalFunction.objects.create(functionalityName="funcionalityTest2", functionalityType="EE", qtdALR=2, qtdDER=1, functionComplexity="abcd", qtdFunctionPts=1, countName="test")
        TransactionalFunction.objects.create(functionalityName="funcionalityTest3", functionalityType="EE", qtdALR=3, qtdDER=1, functionComplexity="abcd", qtdFunctionPts=1, countName="test")
        TransactionalFunction.objects.create(functionalityName="funcionalityTest4", functionalityType="EE", qtdALR=1, qtdDER=1, functionComplexity="abcd", qtdFunctionPts=1, countName="test")
        TransactionalFunction.objects.create(functionalityName="funcionalityTest5", functionalityType="EE", qtdALR=2, qtdDER=10, functionComplexity="abcd", qtdFunctionPts=1, countName="test")
        TransactionalFunction.objects.create(functionalityName="funcionalityTest6", functionalityType="EE", qtdALR=3, qtdDER=20, functionComplexity="abcd", qtdFunctionPts=1, countName="test")
        TransactionalFunction.objects.create(functionalityName="funcionalityTest7", functionalityType="CE", qtdALR=1, qtdDER=1, functionComplexity="abcd", qtdFunctionPts=1, countName="test")
        TransactionalFunction.objects.create(functionalityName="funcionalityTest8", functionalityType="CE", qtdALR=2, qtdDER=1, functionComplexity="abcd", qtdFunctionPts=1, countName="test")
        TransactionalFunction.objects.create(functionalityName="funcionalityTest9", functionalityType="CE", qtdALR=3, qtdDER=1, functionComplexity="abcd", qtdFunctionPts=1, countName="test")
        TransactionalFunction.objects.create(functionalityName="funcionalityTest10", functionalityType="CE", qtdALR=1, qtdDER=1, functionComplexity="abcd", qtdFunctionPts=1, countName="test")
        TransactionalFunction.objects.create(functionalityName="funcionalityTest11", functionalityType="CE", qtdALR=2, qtdDER=10, functionComplexity="abcd", qtdFunctionPts=1, countName="test")
        TransactionalFunction.objects.create(functionalityName="funcionalityTest12", functionalityType="CE", qtdALR=4, qtdDER=20, functionComplexity="abcd", qtdFunctionPts=1, countName="test")
        TransactionalFunction.objects.create(functionalityName="funcionalityTest13", functionalityType="SE", qtdALR=1, qtdDER=1, functionComplexity="abcd", qtdFunctionPts=1, countName="test")
        TransactionalFunction.objects.create(functionalityName="funcionalityTest14", functionalityType="SE", qtdALR=2, qtdDER=1, functionComplexity="abcd", qtdFunctionPts=1, countName="test")
        TransactionalFunction.objects.create(functionalityName="funcionalityTest15", functionalityType="SE", qtdALR=3, qtdDER=1, functionComplexity="abcd", qtdFunctionPts=1, countName="test")
        TransactionalFunction.objects.create(functionalityName="funcionalityTest16", functionalityType="SE", qtdALR=1, qtdDER=1, functionComplexity="abcd", qtdFunctionPts=1, countName="test")
        TransactionalFunction.objects.create(functionalityName="funcionalityTest17", functionalityType="SE", qtdALR=2, qtdDER=10, functionComplexity="abcd", qtdFunctionPts=1, countName="test")
        TransactionalFunction.objects.create(functionalityName="funcionalityTest18", functionalityType="SE", qtdALR=4, qtdDER=20, functionComplexity="abcd", qtdFunctionPts=1, countName="test")

    def test_transactional_function_creation(self):
        tf = TransactionalFunction.objects.get(id=1)
        self.assertTrue(isinstance(tf, TransactionalFunction))

    def test_get_complexity(self):
        tf = TransactionalFunction.objects.get(id=1)
        c = getComplexity(tf.functionalityType, tf.qtdALR, tf.qtdDER)
        self.assertEqual(c, "baixa")

        tf = TransactionalFunction.objects.get(id=2)
        c = getComplexity(tf.functionalityType, tf.qtdALR, tf.qtdDER)
        self.assertEqual(c, "baixa")

        tf = TransactionalFunction.objects.get(id=3)
        c = getComplexity(tf.functionalityType, tf.qtdALR, tf.qtdDER)
        self.assertEqual(c, "média")

        tf = TransactionalFunction.objects.get(id=4)
        c = getComplexity(tf.functionalityType, tf.qtdALR, tf.qtdDER)
        self.assertEqual(c, "baixa")

        tf = TransactionalFunction.objects.get(id=5)
        c = getComplexity(tf.functionalityType, tf.qtdALR, tf.qtdDER)
        self.assertEqual(c, "média")

        tf = TransactionalFunction.objects.get(id=6)
        c = getComplexity(tf.functionalityType, tf.qtdALR, tf.qtdDER)
        self.assertEqual(c, "alta")

        tf = TransactionalFunction.objects.get(id=7)
        c = getComplexity(tf.functionalityType, tf.qtdALR, tf.qtdDER)
        self.assertEqual(c, "baixa")

        tf = TransactionalFunction.objects.get(id=8)
        c = getComplexity(tf.functionalityType, tf.qtdALR, tf.qtdDER)
        self.assertEqual(c, "baixa")

        tf = TransactionalFunction.objects.get(id=9)
        c = getComplexity(tf.functionalityType, tf.qtdALR, tf.qtdDER)
        self.assertEqual(c, "baixa")

        tf = TransactionalFunction.objects.get(id=10)
        c = getComplexity(tf.functionalityType, tf.qtdALR, tf.qtdDER)
        self.assertEqual(c, "baixa")

        tf = TransactionalFunction.objects.get(id=11)
        c = getComplexity(tf.functionalityType, tf.qtdALR, tf.qtdDER)
        self.assertEqual(c, "média")

        tf = TransactionalFunction.objects.get(id=12)
        c = getComplexity(tf.functionalityType, tf.qtdALR, tf.qtdDER)
        self.assertEqual(c, "alta")

        tf = TransactionalFunction.objects.get(id=13)
        c = getComplexity(tf.functionalityType, tf.qtdALR, tf.qtdDER)
        self.assertEqual(c, "baixa")

        tf = TransactionalFunction.objects.get(id=14)
        c = getComplexity(tf.functionalityType, tf.qtdALR, tf.qtdDER)
        self.assertEqual(c, "baixa")

        tf = TransactionalFunction.objects.get(id=15)
        c = getComplexity(tf.functionalityType, tf.qtdALR, tf.qtdDER)
        self.assertEqual(c, "baixa")

        tf = TransactionalFunction.objects.get(id=16)
        c = getComplexity(tf.functionalityType, tf.qtdALR, tf.qtdDER)
        self.assertEqual(c, "baixa")

        tf = TransactionalFunction.objects.get(id=17)
        c = getComplexity(tf.functionalityType, tf.qtdALR, tf.qtdDER)
        self.assertEqual(c, "média")

        tf = TransactionalFunction.objects.get(id=18)
        c = getComplexity(tf.functionalityType, tf.qtdALR, tf.qtdDER)
        self.assertEqual(c, "alta")

    def test_get_function_points(self):
        tf = TransactionalFunction.objects.get(id=1)
        c = getComplexity(tf.functionalityType, tf.qtdALR, tf.qtdDER)
        fp = getFunctionPoints(tf.functionalityType, c)
        self.assertEqual(fp, 3)

        tf = TransactionalFunction.objects.get(id=5)
        c = getComplexity(tf.functionalityType, tf.qtdALR, tf.qtdDER)
        fp = getFunctionPoints(tf.functionalityType, c)
        self.assertEqual(fp, 4)

        tf = TransactionalFunction.objects.get(id=6)
        c = getComplexity(tf.functionalityType, tf.qtdALR, tf.qtdDER)
        fp = getFunctionPoints(tf.functionalityType, c)
        self.assertEqual(fp, 6)

        tf = TransactionalFunction.objects.get(id=16)
        c = getComplexity(tf.functionalityType, tf.qtdALR, tf.qtdDER)
        fp = getFunctionPoints(tf.functionalityType, c)
        self.assertEqual(fp, 4)

        tf = TransactionalFunction.objects.get(id=17)
        c = getComplexity(tf.functionalityType, tf.qtdALR, tf.qtdDER)
        fp = getFunctionPoints(tf.functionalityType, c)
        self.assertEqual(fp, 5)

        tf = TransactionalFunction.objects.get(id=18)
        c = getComplexity(tf.functionalityType, tf.qtdALR, tf.qtdDER)
        fp = getFunctionPoints(tf.functionalityType, c)
        self.assertEqual(fp, 7)

class TransactionalFunctionListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        TransactionalFunction.objects.create(functionalityName="funcionalityTest", functionalityType="EE", qtdALR=1, qtdDER=1, functionComplexity="abcd", qtdFunctionPts=1, countName="test")
        TransactionalFunction.objects.create(functionalityName="funcionalityTest12", functionalityType="CE", qtdALR=4, qtdDER=20, functionComplexity="abcd", qtdFunctionPts=1, countName="test")
        TransactionalFunction.objects.create(functionalityName="funcionalityTest13", functionalityType="SE", qtdALR=1, qtdDER=1, functionComplexity="abcd", qtdFunctionPts=1, countName="test")
           
    def test_list_of_transactional_functions(self):
        response = self.client.get('', {'complexity-filter': 'test', 'type-filter': 'test'})
        self.assertEqual(response.status_code, 200)

        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

class TransactionalFunctionShowViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        TransactionalFunction.objects.create(functionalityName="funcionalityTest", functionalityType="EE", qtdALR=1, qtdDER=1, functionComplexity="abcd", qtdFunctionPts=1, countName="test")
    
    def test_show_transactional_function(self):
        response = self.client.get('/show/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['transactionalFunction'].functionalityName, "funcionalityTest")

class TransactionalFunctionCreateViewTest(TestCase):    
    def test_create_transactional_function(self):
      response = self.client.post('/create/', { 'functionalityName':'funcionalityTestCreate', 'functionalityType':'EE', 'qtdALR':'1', 'qtdDER':'1', 'functionComplexity':'abcd', 'qtdFunctionPts':'1', 'countName':'test' })
      self.assertEqual(response.status_code, 302)
      created = self.client.get('/show/1')
      self.assertEqual(created.context['transactionalFunction'].functionalityName, "funcionalityTestCreate")

    def test_create_transactional_function_form(self):
      response = self.client.get('/create/')
      self.assertEqual(type(response.context['form']), type(TransactionFunctionForm()))