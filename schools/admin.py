from django.contrib import admin
from schools.models import *
# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    fields = ('first_name', 'last_name', 'parent', 'school_class')


@admin.register(SchoolClass)
class SchoolClassAdmin(admin.ModelAdmin):
    fields = ('name', 'teacher', 'school',)


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    fields = ('name',)

@admin.register(SchoolEvent)
class SchoolEventAdmin(admin.ModelAdmin):
    fields = ('name','school', 'description', 'date', 'image')

@admin.register(ClassEvent)
class ClassEventAdmin(admin.ModelAdmin):
    fields = ('name','school_class', 'description', 'date', 'image')


@admin.register(ClassFee)
class ClassFeeAdmin(admin.ModelAdmin):
    fields = ('school_class', 'name', 'description','amount', 'date', 'image', )

@admin.register(ClassFeePayment)
class ClassFeePaymentAdmin(admin.ModelAdmin):
    fields = ('student', 'class_fee', 'payment_amount','is_paid' )

@admin.register(ClassHomework)
class ClassHomeworkAdmin(admin.ModelAdmin):
    fields = ('school_class','title','description','file','due_date','points')

@admin.register(StudentHomework)
class StudentHomeworkAdmin(admin.ModelAdmin):
    fields = ('class_homework','student','title','description','file','due_date','points', 'total_points' )


@admin.register(StudentHomeworkGrade)
class StudentHomeworkGradeAdmin(admin.ModelAdmin):
    fields = ('student_homework', 'grade')

@admin.register(StudentAttendance)
class StudnentAttendanceAdmin(admin.ModelAdmin):
    fields = ('student', 'date', 'absent', 'tardy')


@admin.register(ClassForm)
class ClassFormAdmin(admin.ModelAdmin):
    fields =('school_class','file','title','subject' ,'message','due_date')


@admin.register(StudentForm)
class StudentFormAdmin(admin.ModelAdmin):
    fields = ('class_form', 'student','file','title','subject' ,'message','signer', 'viewed', 'view_count', 'signed')