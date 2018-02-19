# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Alertlists(models.Model):
    type = models.CharField(max_length=-1, blank=True, null=True)
    email = models.CharField(max_length=-1, blank=True, null=True)
    facility_id = models.CharField(max_length=-1, blank=True, null=True)
    facility_id2 = models.CharField(max_length=-1, blank=True, null=True)
    action = models.CharField(max_length=-1, blank=True, null=True)
    blockchain_reciept = models.CharField(max_length=-1, blank=True, null=True)
    date_time = models.DateField(blank=True, null=True)
    hash = models.CharField(max_length=-1, blank=True, null=True)
    data = models.CharField(max_length=-1, blank=True, null=True)
    updatedat = models.DateField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'alertlists'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Careplans(models.Model):
    name = models.CharField(max_length=-1, blank=True, null=True)
    episode_type = models.CharField(max_length=-1, blank=True, null=True)
    procedure = models.CharField(max_length=-1, blank=True, null=True)
    days = models.IntegerField(blank=True, null=True)
    updatedat = models.DateField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'careplans'


class Chatgrouplists(models.Model):
    usernameid = models.CharField(max_length=-1, blank=True, null=True)
    groupname = models.CharField(max_length=-1, blank=True, null=True)
    message = models.CharField(max_length=-1, blank=True, null=True)
    joined = models.CharField(max_length=-1, blank=True, null=True)
    dateevent = models.DateField(blank=True, null=True)
    updatedat = models.DateField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'chatGroupLists'


class Chatlists(models.Model):
    usernameidfirst = models.CharField(max_length=-1, blank=True, null=True)
    usernameidsecond = models.CharField(max_length=-1, blank=True, null=True)
    message = models.CharField(max_length=-1, blank=True, null=True)
    blockchain_reciept = models.CharField(max_length=-1, blank=True, null=True)
    dateevent = models.DateField(blank=True, null=True)
    updatedat = models.DateField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'chatLists'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Episodes(models.Model):
    account_number = models.IntegerField(blank=True, null=True)
    primary_practice = models.CharField(max_length=-1, blank=True, null=True)
    patient_first_name = models.CharField(max_length=-1, blank=True, null=True)
    patient_last_name = models.CharField(max_length=-1, blank=True, null=True)
    patient_dob = models.DateField(blank=True, null=True)
    episode_type = models.CharField(max_length=-1, blank=True, null=True)
    reimbursement = models.IntegerField(blank=True, null=True)
    episode_start = models.DateField(blank=True, null=True)
    visit_procedure = models.CharField(max_length=-1, blank=True, null=True)
    visit_date = models.DateField(blank=True, null=True)
    visit_provider = models.CharField(max_length=-1, blank=True, null=True)
    visit_practice = models.CharField(max_length=-1, blank=True, null=True)
    visit_practice_type = models.CharField(max_length=-1, blank=True, null=True)
    visit_cost = models.IntegerField(blank=True, null=True)
    blockchain_reciept = models.CharField(max_length=-1, blank=True, null=True)
    ccd_status = models.CharField(max_length=-1, blank=True, null=True)
    occured = models.NullBooleanField()
    risk_level = models.IntegerField(blank=True, null=True)
    los_date = models.DateField(blank=True, null=True)
    ih = models.IntegerField(blank=True, null=True)
    snf = models.IntegerField(blank=True, null=True)
    hha = models.IntegerField(blank=True, null=True)
    ipru = models.IntegerField(blank=True, null=True)
    ih_total = models.IntegerField(blank=True, null=True)
    snf_total = models.IntegerField(blank=True, null=True)
    hha_total = models.IntegerField(blank=True, null=True)
    ipru_total = models.IntegerField(blank=True, null=True)
    alerted = models.NullBooleanField()
    archived = models.NullBooleanField()
    facility_id = models.CharField(max_length=-1, blank=True, null=True)
    mrn = models.CharField(max_length=-1, blank=True, null=True)
    new_careplan = models.NullBooleanField()
    npi = models.CharField(max_length=-1, blank=True, null=True)
    caretaker = models.CharField(max_length=-1, blank=True, null=True)
    attending = models.CharField(max_length=-1, blank=True, null=True)
    note = models.CharField(max_length=-1, blank=True, null=True)
    updatedat = models.DateField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'episodes'


class Friendlist(models.Model):
    usernameidfirst = models.CharField(max_length=-1, blank=True, null=True)
    usernameidsecond = models.CharField(max_length=-1, blank=True, null=True)
    status = models.CharField(max_length=-1, blank=True, null=True)
    updatedat = models.DateField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'friendList'


class Friendlists(models.Model):
    usernameidfirst = models.CharField(max_length=-1, blank=True, null=True)
    usernameidsecond = models.CharField(max_length=-1, blank=True, null=True)
    status = models.CharField(max_length=-1, blank=True, null=True)
    updatedat = models.DateField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'friendLists'


class Loginattempts(models.Model):
    invalid = models.CharField(max_length=-1, blank=True, null=True)
    email = models.CharField(max_length=-1, blank=True, null=True)
    dateevent = models.DateField(blank=True, null=True)
    userid = models.CharField(db_column='userId', max_length=-1, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'loginAttempts'


class Messagelists(models.Model):
    image = models.CharField(max_length=-1, blank=True, null=True)
    usernameidfirst = models.CharField(max_length=-1, blank=True, null=True)
    account_number = models.CharField(max_length=-1, blank=True, null=True)
    blockchain_reciept = models.CharField(max_length=-1, blank=True, null=True)
    chat = models.CharField(max_length=-1, blank=True, null=True)
    dateevent = models.DateField(blank=True, null=True)
    updatedat = models.DateField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'messageLists'


class Users(models.Model):
    firstname = models.CharField(max_length=-1, blank=True, null=True)
    lastname = models.CharField(max_length=-1, blank=True, null=True)
    password = models.CharField(max_length=-1, blank=True, null=True)
    medicalprofessional = models.NullBooleanField()
    picture_url = models.CharField(max_length=-1, blank=True, null=True)
    email = models.CharField(max_length=-1, blank=True, null=True)
    lastlogin = models.DateField(blank=True, null=True)
    failed_attempts = models.IntegerField(blank=True, null=True)
    valid = models.NullBooleanField()
    location = models.CharField(max_length=-1, blank=True, null=True)
    npi = models.CharField(max_length=-1, blank=True, null=True)
    license = models.CharField(max_length=-1, blank=True, null=True)
    facility_id = models.CharField(max_length=-1, blank=True, null=True)
    register_id = models.CharField(max_length=-1, blank=True, null=True)
    company = models.NullBooleanField()
    admin = models.NullBooleanField()
    phone = models.CharField(max_length=-1, blank=True, null=True)
    updatedat = models.DateField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.
    userid = models.CharField(db_column='userId', max_length=-1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'users'


class Userspasswords(models.Model):
    password = models.CharField(max_length=-1, blank=True, null=True)
    email = models.CharField(max_length=-1, blank=True, null=True)
    dateevent = models.DateField(blank=True, null=True)
    userid = models.CharField(db_column='userId', max_length=-1, blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'usersPasswords'


class Usersauthorizeds(models.Model):
    email = models.CharField(max_length=-1, blank=True, null=True)
    npi = models.CharField(max_length=-1, blank=True, null=True)
    mrn = models.CharField(max_length=-1, blank=True, null=True)
    account_number = models.CharField(max_length=-1, blank=True, null=True)
    facility_id = models.CharField(max_length=-1, blank=True, null=True)
    blockchain_reciept = models.CharField(max_length=-1, blank=True, null=True)
    location = models.CharField(max_length=-1, blank=True, null=True)
    updatedat = models.DateField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'usersauthorizeds'
