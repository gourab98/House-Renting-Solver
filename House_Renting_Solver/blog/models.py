from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):

    location = models.CharField(max_length = 100)
    content = models.TextField()
    date_posted = models.DateTimeField(default = timezone.now)
    owner = models.ForeignKey(User, on_delete= models.CASCADE)


    def __str__(self):
        return self.location

    def get_absolute_url(self):
      return reverse('post-detail', kwargs={'pk': self.pk})

HOUSE_CHOICES = (
    ('one','Flat'),
    ('two','Seat'),
    ('three','Sub-let'),
    ('four','mess'),
    ('five','hostel'),
)

RENTER_CHOICES = (
    ('one','Family'),
    ('two','Bachelor'),
    ('three','Working Man'),
    ('four','Working Woman'),
    ('five','Anyone'),
)
MEMBER_CHOICES = (
    ('zero','0'),
    ('one','1'),
    ('two','2'),
    ('three','3'),
    ('four','4'),
    ('five','5'),
    ('six','6'),
    ('seven','7'),
    ('eight','8'),
)
RELIGION_CHOICES = (
    ('one','Islam'),
    ('two','Hinduism'),
    ('three','Christianity'),
    ('four','Buddism'),
    ('five','Anyone')
)
OCCUPATION_CHOICES = (
    ('one','Service Holder'),
    ('two','Business Man'),
    ('three','Students'),
    ('five','Anyone')
)
BED_CHOICES = (
    ('zero','0'),
    ('one','1'),
    ('two','2'),
    ('three','3'),
    ('four','4'),
    ('five','5')
)

FACILITY_CHOICES = (
    ('one','Yes'),
    ('two','No'),
)

GAS_CHOICES = (
    ('one','Pipeline'),
    ('two','Cylinder')
)
FLOOR_CHOICES = (
    ('zero','0'),
    ('one','1'),
    ('two','2'),
    ('three','3'),
    ('four','4'),
    ('five','5'),
    ('six','6'),
    ('seven','7'),
    ('eight','8'),
    ('nine','9'),
    ('ten','10'),
)

class Post3(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)
    house_type = models.CharField(max_length=5,choices=HOUSE_CHOICES)
    renter_preference = models.CharField(max_length=5,choices=RENTER_CHOICES)
    family_member = models.CharField(max_length=5,choices=MEMBER_CHOICES)
    religion_preference = models.CharField(max_length=5,choices=RELIGION_CHOICES)
    occupation_priority = models.CharField(max_length=5,choices=OCCUPATION_CHOICES)
    address = models.CharField(max_length=150)
    floor = models.CharField(max_length=10,choices=FLOOR_CHOICES)
    bed_room = models.CharField(max_length=5,choices=BED_CHOICES)
    bed_room_image = models.ImageField(upload_to='profile_pics',null=True,blank=True)
    drawing_room = models.CharField(max_length=5,choices=BED_CHOICES)
    drawing_room_image = models.ImageField(upload_to='profile_pics',null=True,blank=True)
    dinning_room = models.CharField(max_length=5,choices=BED_CHOICES)
    dinning_room_image = models.ImageField(upload_to='profile_pics',null=True,blank=True)
    kitchen = models.CharField(max_length=5,choices=BED_CHOICES)
    kitchen_room_image = models.ImageField(upload_to='profile_pics',null=True,blank=True)
    bathroom = models.CharField(max_length=5,choices=BED_CHOICES)
    bath_room_image = models.ImageField(upload_to='profile_pics',null=True,blank=True)
    washing_Machine = models.CharField(max_length=3,choices=FACILITY_CHOICES)
    hot_water = models.CharField(max_length=3,choices=FACILITY_CHOICES)
    IPS = models.CharField(max_length=3,choices=FACILITY_CHOICES)
    Generator = models.CharField(max_length=3,choices=FACILITY_CHOICES)
    Belcony = models.CharField(max_length=3,choices=FACILITY_CHOICES)
    Oven = models.CharField(max_length=3,choices=FACILITY_CHOICES)
    lift = models.CharField(max_length=3,choices=FACILITY_CHOICES)
    refrigerator = models.CharField(max_length=3,choices=FACILITY_CHOICES)
    sofa = models.CharField(max_length=3,choices=FACILITY_CHOICES)
    wifi = models.CharField(max_length=3,choices=FACILITY_CHOICES)
    ac = models.CharField(max_length=3,choices=FACILITY_CHOICES)
    television = models.CharField(max_length=3,choices=FACILITY_CHOICES)
    gas = models.CharField(max_length=3,choices=GAS_CHOICES)
    security = models.CharField(max_length=3,choices=FACILITY_CHOICES)
    parking = models.CharField(max_length=3,choices=FACILITY_CHOICES)
    house_rent = models.CharField(max_length=10)
    electricity_rent = models.CharField(max_length=5,null=True)
    gas_rent = models.CharField(max_length=5,null=True)
    water_rent = models.CharField(max_length=5,null=True)
    service_rent = models.CharField(max_length=5,null=True)
    rent_date = models.DateTimeField()
    any_special_instructions = models.TextField()

    def __str__(self):
        return self.owner.username

    def get_absolute_url(self):
      return reverse('post-detail', kwargs={'pk': self.pk})



class Post1(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)
    house_type = models.CharField(max_length=5,choices=HOUSE_CHOICES)
    renter_preference = models.CharField(max_length=5,choices=RENTER_CHOICES)
    family_member = models.CharField(max_length=5,choices=MEMBER_CHOICES)
    religion_preference = models.CharField(max_length=5,choices=RELIGION_CHOICES)
    occupation_priority = models.CharField(max_length=5,choices=OCCUPATION_CHOICES)
    address = models.CharField(max_length=150)
    bed_room = models.CharField(max_length=5,choices=BED_CHOICES)
    bed_room_image = models.ImageField(upload_to='profile_pics')
    drawing_room = models.CharField(max_length=5,choices=BED_CHOICES)
    drawing_room_image = models.ImageField(upload_to='profile_pics')
    dinning_room = models.CharField(max_length=5,choices=BED_CHOICES)
    dinning_room_image = models.ImageField(upload_to='profile_pics')
    kitchen = models.CharField(max_length=5,choices=BED_CHOICES)
    kitchen_room_image = models.ImageField(upload_to='profile_pics')
    bathroom = models.CharField(max_length=5,choices=BED_CHOICES)
    bath_room_image = models.ImageField(upload_to='profile_pics')
    washing_Machine = models.CharField(max_length=3,choices=FACILITY_CHOICES)
    hot_water = models.CharField(max_length=3,choices=FACILITY_CHOICES)
    IPS = models.CharField(max_length=3,choices=FACILITY_CHOICES)
    Generator = models.CharField(max_length=3,choices=FACILITY_CHOICES)
    Belcony = models.CharField(max_length=3,choices=FACILITY_CHOICES)
    Oven = models.CharField(max_length=3,choices=FACILITY_CHOICES)
    lift = models.CharField(max_length=3,choices=FACILITY_CHOICES)
    refrigerator = models.CharField(max_length=3,choices=FACILITY_CHOICES)
    sofa = models.CharField(max_length=3,choices=FACILITY_CHOICES)
    wifi = models.CharField(max_length=3,choices=FACILITY_CHOICES)
    ac = models.CharField(max_length=3,choices=FACILITY_CHOICES)
    television = models.CharField(max_length=3,choices=FACILITY_CHOICES)
    gas = models.CharField(max_length=3,choices=GAS_CHOICES)
    security = models.CharField(max_length=3,choices=FACILITY_CHOICES)
    parking = models.CharField(max_length=3,choices=FACILITY_CHOICES)
    house_rent = models.CharField(max_length=10)
    electricity_rent = models.CharField(max_length=5,null=True)
    gas_rent = models.CharField(max_length=5,null=True)
    water_rent = models.CharField(max_length=5,null=True)
    service_rent = models.CharField(max_length=5,null=True)
    any_special_instructions = models.TextField()

    def __str__(self):
        return self.owner.username

    def get_absolute_url(self):
      return reverse('post-detail', kwargs={'pk': self.pk})



class Post2(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)
    house_type = models.CharField(max_length=5,choices=HOUSE_CHOICES)
    renter_preference = models.CharField(max_length=5,choices=RENTER_CHOICES)
    family_member = models.CharField(max_length=5,choices=MEMBER_CHOICES)
    religion_preference = models.CharField(max_length=5,choices=RELIGION_CHOICES)
    occupation_priority = models.CharField(max_length=5,choices=OCCUPATION_CHOICES)
    address = models.CharField(max_length=150)
    floor = models.CharField(max_length=10,choices=FLOOR_CHOICES)
    bed_room = models.CharField(max_length=5,choices=BED_CHOICES)
    bed_room_image = models.ImageField(upload_to='profile_pics')
    drawing_room = models.CharField(max_length=5,choices=BED_CHOICES)
    drawing_room_image = models.ImageField(upload_to='profile_pics')
    dinning_room = models.CharField(max_length=5,choices=BED_CHOICES)
    dinning_room_image = models.ImageField(upload_to='profile_pics')
    kitchen = models.CharField(max_length=5,choices=BED_CHOICES)
    kitchen_room_image = models.ImageField(upload_to='profile_pics')
    bathroom = models.CharField(max_length=5,choices=BED_CHOICES)
    bath_room_image = models.ImageField(upload_to='profile_pics')
    washing_Machine = models.CharField(max_length=3,choices=FACILITY_CHOICES)
    hot_water = models.CharField(max_length=3,choices=FACILITY_CHOICES)
    IPS = models.CharField(max_length=3,choices=FACILITY_CHOICES)
    Generator = models.CharField(max_length=3,choices=FACILITY_CHOICES)
    Belcony = models.CharField(max_length=3,choices=FACILITY_CHOICES)
    Oven = models.CharField(max_length=3,choices=FACILITY_CHOICES)
    lift = models.CharField(max_length=3,choices=FACILITY_CHOICES)
    refrigerator = models.CharField(max_length=3,choices=FACILITY_CHOICES)
    sofa = models.CharField(max_length=3,choices=FACILITY_CHOICES)
    wifi = models.CharField(max_length=3,choices=FACILITY_CHOICES)
    ac = models.CharField(max_length=3,choices=FACILITY_CHOICES)
    television = models.CharField(max_length=3,choices=FACILITY_CHOICES)
    gas = models.CharField(max_length=3,choices=GAS_CHOICES)
    security = models.CharField(max_length=3,choices=FACILITY_CHOICES)
    parking = models.CharField(max_length=3,choices=FACILITY_CHOICES)
    house_rent = models.CharField(max_length=10)
    electricity_rent = models.CharField(max_length=5,null=True)
    gas_rent = models.CharField(max_length=5,null=True)
    water_rent = models.CharField(max_length=5,null=True)
    service_rent = models.CharField(max_length=5,null=True)
    rent_date = models.DateTimeField()
    any_special_instructions = models.TextField()

    def __str__(self):
        return self.owner.username