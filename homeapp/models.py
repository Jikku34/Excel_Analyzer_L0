from django.db import models
import os


# Create your models here.
class ExcelFile(models.Model):
    filename = models.CharField(max_length=100, null=True)
    exel_file = models.FileField(upload_to='excelfile', null=True)

    class Meta:
        db_table = "excelfileinfotable0"

    def __str__(self):
        return self.filename


class StudentRegistration(models.Model):
    student_reg_date = models.DateField(null=True)
    student_reg_no = models.CharField(max_length=20, null=True)
    branch = models.CharField(max_length=100, null=True)
    student_name = models.CharField(max_length=100, null=True)
    student_phone = models.CharField(max_length=100, null=True)
    student_email = models.CharField(max_length=100, null=True)
    student_address = models.CharField(max_length=200, null=True)
    student_dist = models.CharField(max_length=100, null=True)
    student_state = models.CharField(max_length=100, null=True)
    student_company = models.CharField(max_length=100, null=True)
    student_specialisation = models.CharField(max_length=100, null=True)
    student_guardian_name = models.CharField(max_length=100, null=True)
    student_guardian_phone = models.CharField(max_length=100, null=True)
    student_enquiry_Source = models.CharField(max_length=100, null=True)
    student_referral = models.CharField(max_length=100, null=True)
    student_staff = models.CharField(max_length=100, null=True)
    student_department = models.CharField(max_length=100, null=True)
    student_Course = models.CharField(max_length=100, null=True)
    student_effective_fee = models.IntegerField(null=True)
    student_reg_fee = models.IntegerField(null=True)

    class Meta:
        db_table = "student_registration_table"

    def __str__(self):
        return self.student_reg_no


class StudentAdmission(models.Model):
    student_admission_date = models.DateField(null=True)
    student_admission_no = models.CharField(max_length=20, null=True)
    student_reg_date = models.DateField(null=True)
    student_reg_no = models.CharField(max_length=20, null=True)
    branch = models.CharField(max_length=100, null=True)
    student_name = models.CharField(max_length=100, null=True)
    student_phone = models.CharField(max_length=100, null=True)
    student_email = models.CharField(max_length=100, null=True)
    student_address = models.CharField(max_length=200, null=True)
    student_dist = models.CharField(max_length=100, null=True)
    student_state = models.CharField(max_length=100, null=True)
    student_company = models.CharField(max_length=100, null=True)
    student_specialisation = models.CharField(max_length=100, null=True)
    student_guardian_name = models.CharField(max_length=100, null=True)
    student_guardian_phone = models.CharField(max_length=100, null=True)
    student_enquiry_Source = models.CharField(max_length=100, null=True)
    student_referral = models.CharField(max_length=100, null=True)
    student_staff = models.CharField(max_length=100, null=True)
    student_department = models.CharField(max_length=100, null=True)
    student_Course = models.CharField(max_length=100, null=True)
    student_effective_fee = models.IntegerField(null=True)
    student_mode_training = models.CharField(max_length=100, null=True)
    student_start_date = models.DateField(null=True)

    class Meta:
        db_table = "student_admission_table"

    def __str__(self):
        return self.student_reg_no


class StudentFee(models.Model):
    student_date_fee = models.DateField(null=True)
    student_id = models.CharField(max_length=100, null=True)
    student_name = models.CharField(max_length=100, null=True)
    student_fee = models.IntegerField(null=True)

    class Meta:
        db_table = "student_fee_table"

    def __str__(self):
        return self.student_id


class StudentFeepaid(models.Model):
    student_last_date_fee_paid = models.DateField(null=True)
    student_id = models.CharField(max_length=100, null=True)
    student_name = models.CharField(max_length=100, null=True)
    student_effective_fee = models.IntegerField(null=True)
    student_fee_paid = models.IntegerField(null=True)
    student_balance_fee = models.IntegerField(null=True)
    student_Course = models.CharField(max_length=100, null=True)
    student_fee_status = models.CharField(max_length=100, null=True)

    class Meta:
        db_table = "student_fee_paid_table"

    def __str__(self):
        return self.student_id

