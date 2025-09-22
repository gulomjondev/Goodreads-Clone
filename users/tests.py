# from users.models import CustomUser
# from django.test import TestCase
# from django.urls import reverse
#
#
#
#
# class UserRegiserTest(TestCase):
#     def test_user_registration(self):
#         self.client.post(
#             reverse('users:register'),
#
#             data={
#                 'username': 'gulomjon',
#                 'first_name': 'Gulomjon',
#                 'last_name': 'Jakhongirboyev',
#                 'email':'jahongirboyevgulomjon@gmail.com',
#                 'password':'n37L1o7gk7rE3x',
#             }
#         )
#         user = User.objects.get(username= 'gulomjon')
#
#         self.assertEqual(user.username, 'gulomjon')
#         self.assertEqual(user.first_name, 'Gulomjon')
#         self.assertEqual(user.last_name, 'Jakhongirboyev')
#         self.assertEqual(user.email, 'jahongirboyevgulomjon@gmail.com')
#         self.assertNotEqual(user.password, 'n37L1o7gk7rE3x')
#         self.assertTrue(user.check_password('n37L1o7gk7rE3x'))
#
#     def test_required_fields(self):
#         response = self.client.post(
#             reverse('users:register'),
#                 data={
#                     'username': 'gulomjon',
#                     'email':'jahongirboyevgulomjon@gmail.com',
#                 }
#             )
#         user_count = User.objects.count()
#         self.assertEqual(user_count,0)
#         self.assertFormError(response, 'form', 'username', 'This field is required.')
#         self.assertFormError(response, 'form', 'email', 'This field is required.')
#
# class UserLoginTest(TestCase):
#     def test_user_login(self):
#         self.client.post(
#             reverse('users:login'),
#             data={
#                 'username': 'admin',
#                 'password': '12345678',
#             }
#         )
#         user = User.objects.get(username='admin')
#
#         self.assertEqual(user.username, 'admin')
#
# class UserProfileTest(TestCase):
#     def test_user_profile(self):
#         response =self.client.get(reverse('users:profile'))
#
#         self.assertEqual(response.status_code,302)
#         self.assertEqual(response.url, reverse('users:login'))
from users.models import CustomUser
from django.test import TestCase
from django.urls import reverse

class UserRegisterTest(TestCase):
    def test_user_registration(self):
        response = self.client.post(
        reverse('users:register'),
            data={
                'username': 'admin1',
                'first_name': 'admin1',
                'last_name': 'Jakhongirboyev',
                'email': 'jahongirboyevgulomjon@gmail.com',
                'password': 'n37L1o7gk7rE3x',
                'password2': 'n37L1o7gk7rE3x',  # Agar parolni tasdiqlash maydoni kerak bo'lsa
            }
        )
        user = CustomUser.objects.get(username='admin1')
        self.assertEqual(user.username, 'admin1')
        self.assertEqual(user.first_name, 'Gulomjon')
        self.assertEqual(user.last_name, 'Jakhongirboyev')
        self.assertEqual(user.email, 'jahongirboyevgulomjon@gmail.com')
        self.assertNotEqual(user.password, 'n37L1o7gk7rE3x')
        self.assertTrue(user.check_password('n37L1o7gk7rE3x'))

    def test_required_fields(self):
        response = self.client.post(
            reverse('users:register'),
            data={}  # Bo'sh data
        )
        self.assertEqual(CustomUser.objects.count(), 0)
        self.assertContains(response, "This field is required", status_code=200)

class UserLoginTest(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username='admin1',
            password='12345678',
        )

    def test_user_login(self):
        response = self.client.post(
            reverse('users:login'),
            data={
                'username': 'admin1',
                'password': '12345678',
            }
        )
        self.assertEqual(response.status_code, 302)  # Redirect after login
        self.assertTrue(response.wsgi_request.user.is_authenticated)

class UserProfileTest(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username='admin1',
            password='12345678',
        )
    def test_login_required(self):
        response = self.client.get(reverse('users:profile'))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('users:login') + '?next=/users/profile/')

    def test_profile_details(self):
        # Avval login qilamiz
        self.client.login(username='admin1', password='12345678')
        response = self.client.get(reverse('users:profile'))

        self.assertEqual(response.status_code, 200)  # sahifa ochilishi kerak
        self.assertContains(response, 'admin1')
    def test_update_profile(self):
        pass

        # class UserProfileTest(TestCase):
#     def setUp(self):
#         self.user = CustomUser.objects.create_user(
#             username='gulomjon',
#             password='12345678'
#         )
#
#     def test_user_profile_unauthorized(self):
#         response = self.client.get(reverse('users:profile'))
#         self.assertEqual(response.status_code, 302)
#         expected_url = reverse('users:login') + '?next=' + reverse('users:profile')
#         self.assertEqual(response.url, expected_url)
#
#     def test_user_profile_authorized(self):
#         self.client.login(username='gulomjon', password='12345678')
#         response = self.client.get(reverse('users:profile'))
#         self.assertEqual(response.status_code, 200)
