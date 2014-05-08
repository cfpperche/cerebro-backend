# # coding: utf-8
# from django.test import TestCase
# from django.core.urlresolvers import reverse as r


# class HomeTest(TestCase):
#     def setUp(self):
#         self.resp = self.client.get(r('core:home'))

#     def test_get(self):
#         """
#         GET / must return status code 200.
#         """
#         self.assertEqual(200, self.resp.status_code)

#     def test_template(self):
#         """
#         Home must use template index.html
#         """
#         self.assertTemplateUsed(self.resp, 'index.html')

# class SingUpTest(TestCase):
#     def setUp(self):
#         self.resp = self.client.get(r('core:singup'))

#     def test_get(self):
#         """
#         GET / must return status code 200.
#         """
#         self.assertEqual(200, self.resp.status_code)

#     def test_template(self):
#         """
#         SingUp must use template pricing.html
#         """
#         self.assertTemplateUsed(self.resp, 'pricing.html')

# class SingInTest(TestCase):
#     def setUp(self):
#         self.resp = self.client.get(r('core:singin'))

#     def test_get(self):
#         """
#         GET / must return status code 200.
#         """
#         self.assertEqual(200, self.resp.status_code)

#     def test_template(self):
#         """
#         SingIn must use template singin.html
#         """
#         self.assertTemplateUsed(self.resp, 'singin.html')