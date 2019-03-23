from django.db import models


class AccountEmailaddress(models.Model):
    email = models.CharField(unique=True, max_length=254)
    verified = models.IntegerField()
    primary = models.IntegerField()
    user = models.ForeignKey('UsersUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_emailaddress'


class AccountEmailconfirmation(models.Model):
    created = models.DateTimeField()
    sent = models.DateTimeField(blank=True, null=True)
    key = models.CharField(unique=True, max_length=64)
    email_address = models.ForeignKey(AccountEmailaddress, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_emailconfirmation'


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


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('UsersUser', models.DO_NOTHING)

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


class DjangoSite(models.Model):
    domain = models.CharField(unique=True, max_length=100)
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'django_site'


class SocialaccountSocialaccount(models.Model):
    provider = models.CharField(max_length=30)
    uid = models.CharField(max_length=191)
    last_login = models.DateTimeField()
    date_joined = models.DateTimeField()
    extra_data = models.TextField()
    user = models.ForeignKey('UsersUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialaccount'
        unique_together = (('provider', 'uid'),)


class SocialaccountSocialapp(models.Model):
    provider = models.CharField(max_length=30)
    name = models.CharField(max_length=40)
    client_id = models.CharField(max_length=191)
    secret = models.CharField(max_length=191)
    key = models.CharField(max_length=191)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialapp'


class SocialaccountSocialappSites(models.Model):
    socialapp = models.ForeignKey(SocialaccountSocialapp, models.DO_NOTHING)
    site = models.ForeignKey(DjangoSite, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialapp_sites'
        unique_together = (('socialapp', 'site'),)


class SocialaccountSocialtoken(models.Model):
    token = models.TextField()
    token_secret = models.TextField()
    expires_at = models.DateTimeField(blank=True, null=True)
    account = models.ForeignKey(SocialaccountSocialaccount, models.DO_NOTHING)
    app = models.ForeignKey(SocialaccountSocialapp, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialtoken'
        unique_together = (('app', 'account'),)


class UsersUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'users_user'


class UsersUserGroups(models.Model):
    user = models.ForeignKey(UsersUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'users_user_groups'
        unique_together = (('user', 'group'),)


class UsersUserUserPermissions(models.Model):
    user = models.ForeignKey(UsersUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'users_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Wp2Popularpostsdata(models.Model):
    postid = models.BigIntegerField(primary_key=True)
    day = models.DateTimeField()
    last_viewed = models.DateTimeField()
    pageviews = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_2_popularpostsdata'


class Wp2Popularpostssummary(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    postid = models.BigIntegerField()
    pageviews = models.BigIntegerField()
    view_date = models.DateField()
    last_viewed = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'wp_2_popularpostssummary'
        unique_together = (('postid', 'view_date'),)


class Wp2Taxonomyfield(models.Model):
    field_id = models.BigAutoField(primary_key=True)
    tax_name = models.CharField(max_length=255)
    field_name = models.CharField(max_length=255, blank=True, null=True)
    field_label = models.CharField(max_length=255, blank=True, null=True)
    field_type = models.CharField(max_length=255, blank=True, null=True)
    field_desc = models.TextField(blank=True, null=True)
    field_val = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_2_taxonomyfield'


class Wp2Taxonomymeta(models.Model):
    meta_id = models.BigAutoField(primary_key=True)
    taxonomy_id = models.BigIntegerField()
    meta_key = models.CharField(max_length=255, blank=True, null=True)
    meta_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_2_taxonomymeta'


class Wp3Popularpostsdata(models.Model):
    postid = models.BigIntegerField(primary_key=True)
    day = models.DateTimeField()
    last_viewed = models.DateTimeField()
    pageviews = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_3_popularpostsdata'


class Wp3Popularpostssummary(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    postid = models.BigIntegerField()
    pageviews = models.BigIntegerField()
    view_date = models.DateField()
    last_viewed = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'wp_3_popularpostssummary'
        unique_together = (('postid', 'view_date'),)


class Wp4Popularpostsdata(models.Model):
    postid = models.BigIntegerField(primary_key=True)
    day = models.DateTimeField()
    last_viewed = models.DateTimeField()
    pageviews = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_4_popularpostsdata'


class Wp4Popularpostssummary(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    postid = models.BigIntegerField()
    pageviews = models.BigIntegerField()
    view_date = models.DateField()
    last_viewed = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'wp_4_popularpostssummary'
        unique_together = (('postid', 'view_date'),)


class Wp5Popularpostsdata(models.Model):
    postid = models.BigIntegerField(primary_key=True)
    day = models.DateTimeField()
    last_viewed = models.DateTimeField()
    pageviews = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_5_popularpostsdata'


class Wp5Popularpostssummary(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    postid = models.BigIntegerField()
    pageviews = models.BigIntegerField()
    view_date = models.DateField()
    last_viewed = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'wp_5_popularpostssummary'
        unique_together = (('postid', 'view_date'),)


class Wp6IclContentStatus(models.Model):
    rid = models.BigIntegerField(primary_key=True)
    nid = models.BigIntegerField()
    timestamp = models.DateTimeField()
    md5 = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'wp_6_icl_content_status'


class Wp6IclCoreStatus(models.Model):
    id = models.BigAutoField(primary_key=True)
    rid = models.BigIntegerField()
    module = models.CharField(max_length=16)
    origin = models.CharField(max_length=64)
    target = models.CharField(max_length=64)
    status = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'wp_6_icl_core_status'


class Wp6IclFlags(models.Model):
    lang_code = models.CharField(unique=True, max_length=10)
    flag = models.CharField(max_length=32)
    from_template = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'wp_6_icl_flags'


class Wp6IclLanguages(models.Model):
    code = models.CharField(unique=True, max_length=7)
    english_name = models.CharField(unique=True, max_length=128)
    major = models.IntegerField()
    active = models.IntegerField()
    default_locale = models.CharField(max_length=35, blank=True, null=True)
    tag = models.CharField(max_length=35, blank=True, null=True)
    encode_url = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'wp_6_icl_languages'


class Wp6IclLanguagesTranslations(models.Model):
    language_code = models.CharField(max_length=7)
    display_language_code = models.CharField(max_length=7)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'wp_6_icl_languages_translations'
        unique_together = (('language_code', 'display_language_code'),)


class Wp6IclLocaleMap(models.Model):
    code = models.CharField(max_length=7)
    locale = models.CharField(max_length=35)

    class Meta:
        managed = False
        db_table = 'wp_6_icl_locale_map'
        unique_together = (('code', 'locale'),)


class Wp6IclMessageStatus(models.Model):
    id = models.BigAutoField(primary_key=True)
    rid = models.BigIntegerField(unique=True)
    object_id = models.BigIntegerField()
    from_language = models.CharField(max_length=10)
    to_language = models.CharField(max_length=10)
    timestamp = models.DateTimeField()
    md5 = models.CharField(max_length=32)
    object_type = models.CharField(max_length=64)
    status = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'wp_6_icl_message_status'


class Wp6IclNode(models.Model):
    nid = models.BigIntegerField(primary_key=True)
    md5 = models.CharField(max_length=32)
    links_fixed = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'wp_6_icl_node'


class Wp6IclReminders(models.Model):
    id = models.BigIntegerField(primary_key=True)
    message = models.TextField()
    url = models.TextField()
    can_delete = models.IntegerField()
    show = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'wp_6_icl_reminders'


class Wp6IclStringPositions(models.Model):
    id = models.BigAutoField(primary_key=True)
    string_id = models.BigIntegerField()
    kind = models.IntegerField(blank=True, null=True)
    position_in_page = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'wp_6_icl_string_positions'


class Wp6IclStringStatus(models.Model):
    id = models.BigAutoField(primary_key=True)
    rid = models.BigIntegerField()
    string_translation_id = models.BigIntegerField()
    timestamp = models.DateTimeField()
    md5 = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'wp_6_icl_string_status'


class Wp6IclStringTranslations(models.Model):
    id = models.BigAutoField(primary_key=True)
    string_id = models.BigIntegerField()
    language = models.CharField(max_length=10)
    status = models.IntegerField()
    value = models.TextField(blank=True, null=True)
    translator_id = models.BigIntegerField(blank=True, null=True)
    translation_service = models.CharField(max_length=16)
    batch_id = models.IntegerField()
    translation_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'wp_6_icl_string_translations'
        unique_together = (('string_id', 'language'),)


class Wp6IclStrings(models.Model):
    id = models.BigAutoField(primary_key=True)
    language = models.CharField(max_length=7)
    context = models.CharField(max_length=160)
    name = models.CharField(max_length=160)
    value = models.TextField()
    string_package_id = models.BigIntegerField(blank=True, null=True)
    type = models.CharField(max_length=40)
    title = models.CharField(max_length=160, blank=True, null=True)
    status = models.IntegerField()
    gettext_context = models.TextField()
    domain_name_context_md5 = models.CharField(unique=True, max_length=32)

    class Meta:
        managed = False
        db_table = 'wp_6_icl_strings'


class Wp6IclTranslate(models.Model):
    tid = models.BigAutoField(primary_key=True)
    job_id = models.BigIntegerField()
    content_id = models.BigIntegerField()
    timestamp = models.DateTimeField()
    field_type = models.CharField(max_length=160)
    field_format = models.CharField(max_length=16)
    field_translate = models.IntegerField()
    field_data = models.TextField()
    field_data_translated = models.TextField()
    field_finished = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'wp_6_icl_translate'


class Wp6IclTranslateJob(models.Model):
    job_id = models.BigAutoField(primary_key=True)
    rid = models.BigIntegerField()
    translator_id = models.PositiveIntegerField()
    translated = models.PositiveIntegerField()
    manager_id = models.PositiveIntegerField()
    revision = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_6_icl_translate_job'


class Wp6IclTranslationBatches(models.Model):
    batch_name = models.TextField()
    tp_id = models.IntegerField(blank=True, null=True)
    ts_url = models.TextField(blank=True, null=True)
    last_update = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_6_icl_translation_batches'


class Wp6IclTranslationStatus(models.Model):
    rid = models.BigAutoField(primary_key=True)
    translation_id = models.BigIntegerField(unique=True)
    status = models.IntegerField()
    translator_id = models.BigIntegerField()
    needs_update = models.IntegerField()
    md5 = models.CharField(max_length=32)
    translation_service = models.CharField(max_length=16)
    batch_id = models.IntegerField()
    translation_package = models.TextField()
    timestamp = models.DateTimeField()
    links_fixed = models.IntegerField()
    field_prevstate = models.TextField(db_column='_prevstate', blank=True, null=True)  # Field renamed because it started with '_'.

    class Meta:
        managed = False
        db_table = 'wp_6_icl_translation_status'


class Wp6IclTranslations(models.Model):
    translation_id = models.BigAutoField(primary_key=True)
    element_type = models.CharField(max_length=36)
    element_id = models.BigIntegerField(blank=True, null=True)
    trid = models.BigIntegerField()
    language_code = models.CharField(max_length=7)
    source_language_code = models.CharField(max_length=7, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_6_icl_translations'
        unique_together = (('trid', 'language_code'), ('element_type', 'element_id'),)


class Wp6Popularpostsdata(models.Model):
    postid = models.BigIntegerField(primary_key=True)
    day = models.DateTimeField()
    last_viewed = models.DateTimeField()
    pageviews = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_6_popularpostsdata'


class Wp6Popularpostssummary(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    postid = models.BigIntegerField()
    pageviews = models.BigIntegerField()
    view_date = models.DateField()
    last_viewed = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'wp_6_popularpostssummary'
        unique_together = (('postid', 'view_date'),)


class Wp6WpRpTags(models.Model):
    post_id = models.IntegerField(blank=True, null=True)
    post_date = models.DateTimeField()
    label = models.CharField(max_length=32)
    weight = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_6_wp_rp_tags'


class Wp7Popularpostsdata(models.Model):
    postid = models.BigIntegerField(primary_key=True)
    day = models.DateTimeField()
    last_viewed = models.DateTimeField()
    pageviews = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_7_popularpostsdata'


class Wp7Popularpostssummary(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    postid = models.BigIntegerField()
    pageviews = models.BigIntegerField()
    view_date = models.DateField()
    last_viewed = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'wp_7_popularpostssummary'
        unique_together = (('postid', 'view_date'),)


class Wp8Popularpostsdata(models.Model):
    postid = models.BigIntegerField(primary_key=True)
    day = models.DateTimeField()
    last_viewed = models.DateTimeField()
    pageviews = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_8_popularpostsdata'


class Wp8Popularpostssummary(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    postid = models.BigIntegerField()
    pageviews = models.BigIntegerField()
    view_date = models.DateField()
    last_viewed = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'wp_8_popularpostssummary'
        unique_together = (('postid', 'view_date'),)


class WpBlogVersions(models.Model):
    blog_id = models.BigIntegerField(primary_key=True)
    db_version = models.CharField(max_length=20)
    last_updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'wp_blog_versions'


class WpBlogs(models.Model):
    blog_id = models.BigAutoField(primary_key=True)
    site_id = models.BigIntegerField()
    domain = models.CharField(max_length=200)
    path = models.CharField(max_length=100)
    registered = models.DateTimeField()
    last_updated = models.DateTimeField()
    public = models.IntegerField()
    archived = models.IntegerField()
    mature = models.IntegerField()
    spam = models.IntegerField()
    deleted = models.IntegerField()
    lang_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'wp_blogs'


class WpCommentmeta(models.Model):
    meta_id = models.BigAutoField(primary_key=True)
    comment_id = models.BigIntegerField()
    meta_key = models.CharField(max_length=255, blank=True, null=True)
    meta_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_commentmeta'


class WpComments(models.Model):
    comment_id = models.BigAutoField(db_column='comment_ID', primary_key=True)  # Field name made lowercase.
    comment_post_id = models.BigIntegerField(db_column='comment_post_ID')  # Field name made lowercase.
    comment_author = models.TextField()
    comment_author_email = models.CharField(max_length=100)
    comment_author_url = models.CharField(max_length=200)
    comment_author_ip = models.CharField(db_column='comment_author_IP', max_length=100)  # Field name made lowercase.
    comment_date = models.DateTimeField()
    comment_date_gmt = models.DateTimeField()
    comment_content = models.TextField()
    comment_karma = models.IntegerField()
    comment_approved = models.CharField(max_length=20)
    comment_agent = models.CharField(max_length=255)
    comment_type = models.CharField(max_length=20)
    comment_parent = models.BigIntegerField()
    user_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'wp_comments'


class WpDomainMapping(models.Model):
    id = models.BigAutoField(primary_key=True)
    blog_id = models.BigIntegerField()
    domain = models.CharField(max_length=255)
    active = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_domain_mapping'


class WpGfDraftSubmissions(models.Model):
    uuid = models.CharField(primary_key=True, max_length=32)
    email = models.CharField(max_length=255, blank=True, null=True)
    form_id = models.PositiveIntegerField()
    date_created = models.DateTimeField()
    ip = models.CharField(max_length=39)
    source_url = models.TextField()
    submission = models.TextField()

    class Meta:
        managed = False
        db_table = 'wp_gf_draft_submissions'


class WpGfEntry(models.Model):
    form_id = models.PositiveIntegerField()
    post_id = models.BigIntegerField(blank=True, null=True)
    date_created = models.DateTimeField()
    date_updated = models.DateTimeField(blank=True, null=True)
    is_starred = models.IntegerField()
    is_read = models.IntegerField()
    ip = models.CharField(max_length=39)
    source_url = models.CharField(max_length=200)
    user_agent = models.CharField(max_length=250)
    currency = models.CharField(max_length=5, blank=True, null=True)
    payment_status = models.CharField(max_length=15, blank=True, null=True)
    payment_date = models.DateTimeField(blank=True, null=True)
    payment_amount = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    payment_method = models.CharField(max_length=30, blank=True, null=True)
    transaction_id = models.CharField(max_length=50, blank=True, null=True)
    is_fulfilled = models.IntegerField(blank=True, null=True)
    created_by = models.BigIntegerField(blank=True, null=True)
    transaction_type = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'wp_gf_entry'


class WpGfEntryMeta(models.Model):
    id = models.BigAutoField(primary_key=True)
    form_id = models.PositiveIntegerField()
    entry_id = models.BigIntegerField()
    meta_key = models.CharField(max_length=255, blank=True, null=True)
    meta_value = models.TextField(blank=True, null=True)
    item_index = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_gf_entry_meta'


class WpGfEntryNotes(models.Model):
    entry_id = models.PositiveIntegerField()
    user_name = models.CharField(max_length=250, blank=True, null=True)
    user_id = models.BigIntegerField(blank=True, null=True)
    date_created = models.DateTimeField()
    value = models.TextField(blank=True, null=True)
    note_type = models.CharField(max_length=50, blank=True, null=True)
    sub_type = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_gf_entry_notes'


class WpGfForm(models.Model):
    title = models.CharField(max_length=150)
    date_created = models.DateTimeField()
    date_updated = models.DateTimeField(blank=True, null=True)
    is_active = models.IntegerField()
    is_trash = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'wp_gf_form'


class WpGfFormMeta(models.Model):
    form_id = models.PositiveIntegerField(primary_key=True)
    display_meta = models.TextField(blank=True, null=True)
    entries_grid_meta = models.TextField(blank=True, null=True)
    confirmations = models.TextField(blank=True, null=True)
    notifications = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_gf_form_meta'


class WpGfFormRevisions(models.Model):
    id = models.BigAutoField(primary_key=True)
    form_id = models.PositiveIntegerField()
    display_meta = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'wp_gf_form_revisions'


class WpGfFormView(models.Model):
    id = models.BigAutoField(primary_key=True)
    form_id = models.PositiveIntegerField()
    date_created = models.DateTimeField()
    ip = models.CharField(max_length=15, blank=True, null=True)
    count = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'wp_gf_form_view'


class WpIclCmsNavCache(models.Model):
    id = models.BigAutoField(primary_key=True)
    cache_key = models.CharField(max_length=128)
    type = models.CharField(max_length=128)
    data = models.TextField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'wp_icl_cms_nav_cache'


class WpIclContentStatus(models.Model):
    rid = models.BigIntegerField(primary_key=True)
    nid = models.BigIntegerField()
    timestamp = models.DateTimeField()
    md5 = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'wp_icl_content_status'


class WpIclCoreStatus(models.Model):
    id = models.BigAutoField(primary_key=True)
    rid = models.BigIntegerField()
    module = models.CharField(max_length=16)
    origin = models.CharField(max_length=64)
    target = models.CharField(max_length=64)
    status = models.SmallIntegerField()
    tp_revision = models.IntegerField()
    ts_status = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_icl_core_status'


class WpIclFlags(models.Model):
    lang_code = models.CharField(unique=True, max_length=10)
    flag = models.CharField(max_length=32)
    from_template = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'wp_icl_flags'


class WpIclLanguages(models.Model):
    code = models.CharField(unique=True, max_length=7)
    english_name = models.CharField(unique=True, max_length=128)
    major = models.IntegerField()
    active = models.IntegerField()
    default_locale = models.CharField(max_length=35, blank=True, null=True)
    encode_url = models.IntegerField()
    tag = models.CharField(max_length=35, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_icl_languages'


class WpIclLanguagesTranslations(models.Model):
    language_code = models.CharField(max_length=7)
    display_language_code = models.CharField(max_length=7)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'wp_icl_languages_translations'
        unique_together = (('language_code', 'display_language_code'),)


class WpIclLocaleMap(models.Model):
    code = models.CharField(max_length=8)
    locale = models.CharField(max_length=35, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_icl_locale_map'
        unique_together = (('code', 'locale'),)


class WpIclMessageStatus(models.Model):
    id = models.BigAutoField(primary_key=True)
    rid = models.BigIntegerField(unique=True)
    object_id = models.BigIntegerField()
    from_language = models.CharField(max_length=10)
    to_language = models.CharField(max_length=10)
    timestamp = models.DateTimeField()
    md5 = models.CharField(max_length=32)
    object_type = models.CharField(max_length=64)
    status = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'wp_icl_message_status'


class WpIclMoFilesDomains(models.Model):
    file_path = models.CharField(max_length=250)
    file_path_md5 = models.CharField(unique=True, max_length=32)
    domain = models.CharField(max_length=45)
    status = models.CharField(max_length=20)
    num_of_strings = models.IntegerField()
    last_modified = models.IntegerField()
    component_type = models.CharField(max_length=6)
    component_id = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_icl_mo_files_domains'


class WpIclNode(models.Model):
    nid = models.BigIntegerField(primary_key=True)
    md5 = models.CharField(max_length=32)
    links_fixed = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'wp_icl_node'


class WpIclReminders(models.Model):
    id = models.BigIntegerField(primary_key=True)
    message = models.TextField()
    url = models.TextField()
    can_delete = models.IntegerField()
    show = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'wp_icl_reminders'


class WpIclStringPackages(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    kind_slug = models.CharField(max_length=160)
    kind = models.CharField(max_length=160)
    name = models.CharField(max_length=160)
    title = models.CharField(max_length=160)
    edit_link = models.TextField()
    view_link = models.TextField()
    post_id = models.IntegerField(blank=True, null=True)
    word_count = models.CharField(max_length=2000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_icl_string_packages'


class WpIclStringPages(models.Model):
    id = models.BigAutoField(primary_key=True)
    string_id = models.BigIntegerField()
    url_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'wp_icl_string_pages'


class WpIclStringPositions(models.Model):
    id = models.BigAutoField(primary_key=True)
    string_id = models.BigIntegerField()
    kind = models.IntegerField(blank=True, null=True)
    position_in_page = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'wp_icl_string_positions'


class WpIclStringStatus(models.Model):
    id = models.BigAutoField(primary_key=True)
    rid = models.BigIntegerField()
    string_translation_id = models.BigIntegerField()
    timestamp = models.DateTimeField()
    md5 = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'wp_icl_string_status'


class WpIclStringTranslations(models.Model):
    id = models.BigAutoField(primary_key=True)
    string_id = models.BigIntegerField()
    language = models.CharField(max_length=10)
    status = models.IntegerField()
    value = models.TextField(blank=True, null=True)
    mo_string = models.TextField(blank=True, null=True)
    translator_id = models.BigIntegerField(blank=True, null=True)
    translation_date = models.DateTimeField()
    batch_id = models.IntegerField()
    translation_service = models.CharField(max_length=16)

    class Meta:
        managed = False
        db_table = 'wp_icl_string_translations'
        unique_together = (('string_id', 'language'),)


class WpIclStringUrls(models.Model):
    id = models.BigAutoField(primary_key=True)
    language = models.CharField(max_length=7, blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_icl_string_urls'
        unique_together = (('language', 'url'),)


class WpIclStrings(models.Model):
    id = models.BigAutoField(primary_key=True)
    language = models.CharField(max_length=10)
    context = models.CharField(max_length=160, blank=True, null=True)
    name = models.CharField(max_length=160, blank=True, null=True)
    value = models.TextField()
    string_package_id = models.BigIntegerField(blank=True, null=True)
    type = models.CharField(max_length=40)
    title = models.CharField(max_length=160, blank=True, null=True)
    status = models.IntegerField()
    gettext_context = models.TextField()
    domain_name_context_md5 = models.CharField(unique=True, max_length=32, blank=True, null=True)
    location = models.BigIntegerField(blank=True, null=True)
    word_count = models.PositiveIntegerField(blank=True, null=True)
    translation_priority = models.CharField(max_length=160)

    class Meta:
        managed = False
        db_table = 'wp_icl_strings'


class WpIclTranslate(models.Model):
    tid = models.BigAutoField(primary_key=True)
    job_id = models.BigIntegerField()
    content_id = models.BigIntegerField()
    timestamp = models.DateTimeField()
    field_type = models.CharField(max_length=160)
    field_format = models.CharField(max_length=16)
    field_translate = models.IntegerField()
    field_data = models.TextField()
    field_data_translated = models.TextField()
    field_finished = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'wp_icl_translate'


class WpIclTranslateJob(models.Model):
    job_id = models.BigAutoField(primary_key=True)
    rid = models.BigIntegerField()
    translator_id = models.PositiveIntegerField()
    translated = models.PositiveIntegerField()
    manager_id = models.PositiveIntegerField()
    revision = models.PositiveIntegerField(blank=True, null=True)
    title = models.CharField(max_length=160, blank=True, null=True)
    deadline_date = models.DateTimeField(blank=True, null=True)
    completed_date = models.DateTimeField(blank=True, null=True)
    editor = models.CharField(max_length=16, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_icl_translate_job'


class WpIclTranslationBatches(models.Model):
    batch_name = models.TextField()
    tp_id = models.IntegerField(blank=True, null=True)
    ts_url = models.TextField(blank=True, null=True)
    last_update = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_icl_translation_batches'


class WpIclTranslationStatus(models.Model):
    rid = models.BigAutoField(primary_key=True)
    translation_id = models.BigIntegerField(unique=True)
    status = models.IntegerField()
    translator_id = models.BigIntegerField()
    needs_update = models.IntegerField()
    md5 = models.CharField(max_length=32)
    translation_service = models.CharField(max_length=16)
    translation_package = models.TextField()
    timestamp = models.DateTimeField()
    links_fixed = models.IntegerField()
    field_prevstate = models.TextField(db_column='_prevstate', blank=True, null=True)  # Field renamed because it started with '_'.
    batch_id = models.IntegerField()
    uuid = models.CharField(max_length=36, blank=True, null=True)
    tp_id = models.IntegerField(blank=True, null=True)
    tp_revision = models.IntegerField()
    ts_status = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_icl_translation_status'


class WpIclTranslations(models.Model):
    translation_id = models.BigAutoField(primary_key=True)
    element_type = models.CharField(max_length=60)
    element_id = models.BigIntegerField(blank=True, null=True)
    trid = models.BigIntegerField()
    language_code = models.CharField(max_length=7)
    source_language_code = models.CharField(max_length=7, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_icl_translations'
        unique_together = (('trid', 'language_code'), ('element_type', 'element_id'),)


class WpInboundEvents(models.Model):
    event_name = models.CharField(max_length=255)
    page_id = models.BigIntegerField()
    variation_id = models.BigIntegerField()
    form_id = models.BigIntegerField()
    cta_id = models.BigIntegerField()
    email_id = models.BigIntegerField()
    rule_id = models.BigIntegerField()
    job_id = models.BigIntegerField()
    list_id = models.BigIntegerField()
    lead_id = models.BigIntegerField()
    comment_id = models.BigIntegerField()
    lead_uid = models.CharField(max_length=255)
    session_id = models.CharField(max_length=255)
    event_details = models.TextField()
    source = models.TextField()
    funnel = models.TextField()
    datetime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'wp_inbound_events'


class WpInboundPageViews(models.Model):
    page_id = models.BigIntegerField()
    cta_id = models.BigIntegerField()
    variation_id = models.BigIntegerField()
    lead_id = models.BigIntegerField()
    lead_uid = models.CharField(max_length=255)
    list_id = models.BigIntegerField()
    session_id = models.CharField(max_length=255)
    source = models.TextField()
    datetime = models.DateTimeField()
    ip = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'wp_inbound_page_views'


class WpInboundTrackedLinks(models.Model):
    token = models.TextField()
    args = models.TextField()

    class Meta:
        managed = False
        db_table = 'wp_inbound_tracked_links'


class WpItsecLockouts(models.Model):
    lockout_id = models.BigAutoField(primary_key=True)
    lockout_type = models.CharField(max_length=20)
    lockout_start = models.DateTimeField()
    lockout_start_gmt = models.DateTimeField()
    lockout_expire = models.DateTimeField()
    lockout_expire_gmt = models.DateTimeField()
    lockout_host = models.CharField(max_length=40, blank=True, null=True)
    lockout_user = models.BigIntegerField(blank=True, null=True)
    lockout_username = models.CharField(max_length=60, blank=True, null=True)
    lockout_active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'wp_itsec_lockouts'


class WpItsecLog(models.Model):
    log_id = models.BigAutoField(primary_key=True)
    log_type = models.CharField(max_length=20)
    log_function = models.CharField(max_length=255)
    log_priority = models.IntegerField()
    log_date = models.DateTimeField()
    log_date_gmt = models.DateTimeField()
    log_host = models.CharField(max_length=40, blank=True, null=True)
    log_username = models.CharField(max_length=60, blank=True, null=True)
    log_user = models.BigIntegerField(blank=True, null=True)
    log_url = models.CharField(max_length=255, blank=True, null=True)
    log_referrer = models.CharField(max_length=255, blank=True, null=True)
    log_data = models.TextField()

    class Meta:
        managed = False
        db_table = 'wp_itsec_log'


class WpItsecTemp(models.Model):
    temp_id = models.BigAutoField(primary_key=True)
    temp_type = models.CharField(max_length=20)
    temp_date = models.DateTimeField()
    temp_date_gmt = models.DateTimeField()
    temp_host = models.CharField(max_length=40, blank=True, null=True)
    temp_user = models.BigIntegerField(blank=True, null=True)
    temp_username = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_itsec_temp'


class WpLinks(models.Model):
    link_id = models.BigAutoField(primary_key=True)
    link_url = models.CharField(max_length=255)
    link_name = models.CharField(max_length=255)
    link_image = models.CharField(max_length=255)
    link_target = models.CharField(max_length=25)
    link_description = models.CharField(max_length=255)
    link_visible = models.CharField(max_length=20)
    link_owner = models.BigIntegerField()
    link_rating = models.IntegerField()
    link_updated = models.DateTimeField()
    link_rel = models.CharField(max_length=255)
    link_notes = models.TextField()
    link_rss = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'wp_links'


class WpNewsSubs(models.Model):
    email = models.TextField()
    timestamp = models.TextField()
    estado = models.IntegerField()
    lang = models.TextField()

    class Meta:
        managed = False
        db_table = 'wp_news_subs'


class WpNf3ActionMeta(models.Model):
    parent_id = models.IntegerField()
    key = models.TextField()
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_nf3_action_meta'


class WpNf3Actions(models.Model):
    title = models.TextField(blank=True, null=True)
    key = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    active = models.IntegerField(blank=True, null=True)
    parent_id = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_nf3_actions'


class WpNf3Chunks(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_nf3_chunks'


class WpNf3FieldMeta(models.Model):
    parent_id = models.IntegerField()
    key = models.TextField()
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_nf3_field_meta'
