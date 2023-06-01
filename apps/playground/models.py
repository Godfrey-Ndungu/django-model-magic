from django.db import models


class SampleModelWithAllFields(models.Model):
    big_integer_field = models.BigIntegerField(blank=True)
    binary_field = models.BinaryField(blank=True)
    boolean_field = models.BooleanField(blank=True)
    char_field = models.CharField(max_length=255, blank=True)
    date_field = models.DateField(blank=True)
    datetime_field = models.DateTimeField(blank=True)
    decimal_field = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True)
    duration_field = models.DurationField(blank=True)
    email_field = models.EmailField(blank=True)
    file_field = models.FileField(upload_to="files/", blank=True)
    file_path_field = models.FilePathField(path="files/", blank=True)
    float_field = models.FloatField(blank=True)
    generic_ip_address_field = models.GenericIPAddressField(
        blank=True, null=True)
    image_field = models.ImageField(upload_to="images/", blank=True)
    integer_field = models.IntegerField(blank=True)
    json_field = models.JSONField(blank=True)
    positive_big_integer_field = models.PositiveBigIntegerField(blank=True)
    positive_integer_field = models.PositiveIntegerField(blank=True)
    positive_small_integer_field = models.PositiveSmallIntegerField(blank=True)
    slug_field = models.SlugField(blank=True)
    small_auto_field = models.SmallAutoField(primary_key=True, blank=True)
    small_integer_field = models.SmallIntegerField(blank=True)
    text_field = models.TextField(blank=True)
    time_field = models.TimeField(blank=True)
    url_field = models.URLField(blank=True)
    uuid_field = models.UUIDField(blank=True)


# auto_field = models.AutoField(primary_key=True)
# big_auto_field = models.BigAutoField(primary_key=True)

# Relationship fields
# many_to_many = models.ManyToManyField("OtherModel")
# one_to_one = models.OneToOneField("AnotherModel", on_delete=models.CASCADE)
# foreign_key = models.ForeignKey("AnotherModel", on_delete=models.CASCADE)
