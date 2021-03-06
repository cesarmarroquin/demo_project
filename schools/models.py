from datetime import date
from parents.models import *
from teachers.models import *
import stripe

class School(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.name)


class SchoolClass(models.Model):
    name = models.CharField(max_length=255)
    teacher = models.ForeignKey(Teacher)
    school = models.ForeignKey(School, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return "{}".format(self.name)


class Student(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    parent = models.ManyToManyField(Parent)
    school_class = models.ManyToManyField(SchoolClass)
    profile_picture = models.ImageField(upload_to='student_profile_pictures', blank=True, null=True)
    picture_url = models.URLField(default="http://res.cloudinary.com/dpkceqvfi/image/upload/v1450429700/default_profile_ru96fo.png")
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}, {}".format(self.last_name, self.first_name)


class ClassHomework(models.Model):
    school_class = models.ForeignKey(SchoolClass)
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='class_homework_images', blank=True, null=True)
    file = models.FileField(null=True, upload_to='class_homework/%Y/%m/%d')
    picture_url = models.URLField(default="http://res.cloudinary.com/dpkceqvfi/image/upload/v1450429700/default_profile_ru96fo.png")
    due_date = models.DateField(default=date.today)
    points = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.title)

class StudentHomework(models.Model):
    class_homework = models.ForeignKey(ClassHomework)
    student = models.ForeignKey(Student)
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='class_homework_images', blank=True, null=True)
    file = models.FileField(null=True, upload_to='student_homework/%Y/%m/%d')
    picture_url = models.URLField(default="http://res.cloudinary.com/dpkceqvfi/image/upload/v1450429700/default_profile_ru96fo.png")
    due_date = models.DateField(default=date.today)
    turned_in = models.DateField(null=True)
    points = models.IntegerField(default=0)
    total_points = models.IntegerField(default=0)
    grade = models.CharField(default="none", max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return "{}, {}".format(self.title, self.student)


class StudentHomeworkGrade(models.Model):
    student_homework = models.OneToOneField(StudentHomework)
    grade = models.CharField(default='F', max_length=1)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.student_homework)

class StudentAttendance(models.Model):
    student = models.ForeignKey(Student)
    school_class = models.ForeignKey(SchoolClass, null=True)
    date = models.DateField(default=date.today)
    absent = models.BooleanField(default=False)
    tardy = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}, {}".format(self.date, self.student.first_name)

class StudentBehavior(models.Model):
    student = models.ForeignKey(Student)
    school_class = models.ForeignKey(SchoolClass, null=True)
    date = models.DateField(default=date.today)
    good_behavior = models.BooleanField(default=True)
    description = models.TextField(default="Behavior was good for today.")
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}, {}".format(self.date, self.student.first_name)

class SchoolEvent(models.Model):
    school = models.ForeignKey(School)
    name = models.CharField(max_length=255)
    description = models.TextField(default="school event description")
    date = models.DateField(default=date.today)
    image = models.ImageField(upload_to='school_event_images', blank=True, null=True)
    picture_url = models.URLField(default="http://res.cloudinary.com/dpkceqvfi/image/upload/v1450429700/default_profile_ru96fo.png")
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.name)


class ClassEvent(models.Model):
    school_class = models.ForeignKey(SchoolClass)
    name = models.CharField(max_length=255)
    description = models.TextField(default="class event description")
    date = models.DateField(default=date.today)
    image = models.ImageField(upload_to='class_event_images', blank=True, null=True)
    picture_url = models.URLField(default="http://res.cloudinary.com/dpkceqvfi/image/upload/v1450429700/default_profile_ru96fo.png")
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.name)

class ClassForm(models.Model):
    school_class = models.ForeignKey(SchoolClass)
    file = models.FileField(upload_to='class_forms/%Y/%m/%d', null=True)
    title =  models.CharField(max_length=255, default="title goes here")
    subject = models.TextField(default="subject goes here")
    message = models.TextField(default="message goes here")
    due_date = models.DateField(default=date.today)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.title)


class StudentForm(models.Model):
    class_form = models.ForeignKey(ClassForm)
    student = models.ForeignKey(Student, default=1)
    file = models.FileField(upload_to='student_forms/%Y/%m/%d')
    sign_url = models.URLField(null=True)
    title = models.CharField(max_length=255, default="title goes here")
    subject = models.TextField(default="subject goes here")
    message = models.TextField(default="message goes here")
    due_date = models.DateField(default=date.today)
    signer = models.CharField(max_length=255, null=True)
    viewed = models.BooleanField(default=False)
    view_count = models.IntegerField(default=0)
    signed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.title)


class ClassFee(models.Model):
    school_class = models.ForeignKey(SchoolClass)
    name = models.CharField(max_length=255)
    description = models.TextField()
    amount = models.DecimalField(max_digits=9, decimal_places=2)
    image = models.ImageField(upload_to='class_fee_images', blank=True, null=True)
    picture_url = models.URLField(default="http://res.cloudinary.com/dpkceqvfi/image/upload/v1450429700/default_profile_ru96fo.png")
    date = models.DateField(default=date.today)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.name)

class ClassFeePayment(models.Model):
    student = models.ForeignKey(Student)
    class_fee = models.ForeignKey(ClassFee)
    name = models.CharField(max_length=255, null=True)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to='class_fee_images', blank=True, null=True)
    picture_url = models.URLField(default="http://res.cloudinary.com/dpkceqvfi/image/upload/v1450429700/default_profile_ru96fo.png")
    date = models.DateField(null=True)
    amount_needed = models.DecimalField(max_digits=9, decimal_places=2, default=0, null=True)
    payment_amount = models.DecimalField(max_digits=9, decimal_places=2, default=0)
    charge_id = models.CharField(max_length=255, null=True)
    refunded = models.BooleanField(default=False)
    is_paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def refund(self):
        re = stripe.Refund.create(charge= self.charge.id)
        self.refunded = True

    def __str__(self):
        return "{}, {}, paid = {}".format(self.class_fee, self.payment_amount, self.is_paid)

import schools.signals