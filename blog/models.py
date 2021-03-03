from django.db import models


#
#
# #
# # class Post(models.Model):
# #     title = models.CharField(max_length=100)
# #     content = models.TextField()
# #     img = models.ImageField()
# #     created_at = models.DateTimeField(auto_now_add=True)
# #
# #     def __str__(self):
# #         return self.title
# #
# #
# # class Comment(models.Model):
# #     post = models.ForeignKey(Post, on_delete=models.CASCADE)
# #     title = models.CharField(max_length=100)
# #     text = models.TextField()
# #
# #     def __str__(self):
# #         return self.title
# #
# # class Admin_Comment(models.Model):
# #     post = models.OneToOneField(Post, on_delete=models.CASCADE)
# #     title = models.CharField(max_length=100)
# #     text = models.TextField()
# #
# #     def __str__(self):
# #         return self.title
#
#
# class Group(models.Model):
#     name_of_group = models.CharField(max_length=100)
#     photo_of_group = models.ImageField(null=True, blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return self.name_of_group
#
#
# class Student(models.Model):
#     group = models.ForeignKey(Group, on_delete=models.CASCADE)
#     name_of_student = models.CharField(max_length=100)
#     date_of_birthday = models.DateField()
#     photo_of_student = models.ImageField(null=True, blank=True)
#
#     def __str__(self):
#         return self.name_of_student
#
#
# class Work(models.Model):
#     work = models.ForeignKey(Student, on_delete=models.CASCADE)
#     name_of_work = models.CharField(max_length=100)
#     about_work = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return self.name_of_work
#
#
# class Book(models.Model):
#     student = models.ManyToManyField(Student)
#     name = models.CharField(max_length=100)
#     pages = models.IntegerField()
#
#     def __str__(self):
#         return self.name
#

class School(models.Model):
    number = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.number


class Group(models.Model):
    number = models.CharField(max_length=100)
    profile_group = models.CharField(max_length=100)
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    def __str__(self):
        return self.number


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name
