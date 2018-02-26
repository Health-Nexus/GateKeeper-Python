from django.db import models

# class Episodes(models.Model):
#     account_number = models.IntegerField(blank=True, null=True)
#     primary_practice = models.CharField(max_length=-1, blank=True, null=True)
#     patient_first_name = models.CharField(max_length=-1, blank=True, null=True)
#     patient_last_name = models.CharField(max_length=-1, blank=True, null=True)
#     patient_dob = models.DateField(blank=True, null=True)
#     episode_type = models.CharField(max_length=-1, blank=True, null=True)
#     reimbursement = models.IntegerField(blank=True, null=True)
#     episode_start = models.DateField(blank=True, null=True)
#     visit_procedure = models.CharField(max_length=-1, blank=True, null=True)
#     visit_date = models.DateField(blank=True, null=True)
#     visit_provider = models.CharField(max_length=-1, blank=True, null=True)
#     visit_practice = models.CharField(max_length=-1, blank=True, null=True)
#     visit_practice_type = models.CharField(max_length=-1, blank=True, null=True)
#     visit_cost = models.IntegerField(blank=True, null=True)
#     blockchain_reciept = models.CharField(max_length=-1, blank=True, null=True)
#     ccd_status = models.CharField(max_length=-1, blank=True, null=True)
#     occured = models.NullBooleanField()
#     risk_level = models.IntegerField(blank=True, null=True)
#     los_date = models.DateField(blank=True, null=True)
#     ih = models.IntegerField(blank=True, null=True)
#     snf = models.IntegerField(blank=True, null=True)
#     hha = models.IntegerField(blank=True, null=True)
#     ipru = models.IntegerField(blank=True, null=True)
#     ih_total = models.IntegerField(blank=True, null=True)
#     snf_total = models.IntegerField(blank=True, null=True)
#     hha_total = models.IntegerField(blank=True, null=True)
#     ipru_total = models.IntegerField(blank=True, null=True)
#     alerted = models.NullBooleanField()
#     archived = models.NullBooleanField()
#     facility_id = models.CharField(max_length=-1, blank=True, null=True)
#     mrn = models.CharField(max_length=-1, blank=True, null=True)
#     new_careplan = models.NullBooleanField()
#     npi = models.CharField(max_length=-1, blank=True, null=True)
#     caretaker = models.CharField(max_length=-1, blank=True, null=True)
#     attending = models.CharField(max_length=-1, blank=True, null=True)
#     note = models.CharField(max_length=-1, blank=True, null=True)
#     updatedat = models.DateField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.
#     createdat = models.DateField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'episodes'
# Create your models here.
