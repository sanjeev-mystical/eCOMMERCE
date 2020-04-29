from django.db import models
from billing.models import BillingProfile


ADDRESS_TYPES = (
    ('billing','Billing'),
    ('shipping','Shipping'),
)


class Address(models.Model):
    billing_profile = models.ForeignKey(BillingProfile, on_delete=models.CASCADE)
    Address_type = models.CharField(max_length=120,choices=ADDRESS_TYPES)
    Address_line_1 = models.CharField(max_length=120)
    Address_line_2 = models.CharField(max_length=120,null=True,blank=True)
    City = models.CharField(max_length=120)
    Country = models.CharField(max_length=120, default='INDIA')
    State = models.CharField(max_length=120)
    Postal_code = models.CharField(max_length=120)

    def __str__(self):
        return str(self.billing_profile)

    def get_address(self):
        return '{line1}\n{line2}\n{City}\n,{State}{Postal}\n{Country}'.format(line1=self.Address_line_1,
                                                                              line2=self.Address_line_2 or '',
                                                                              City=self.City,
                                                                              State=self.State,
                                                                              Postal=self.Postal_code,
                                                                              Country=self.Country)
