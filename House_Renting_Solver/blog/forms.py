from django import forms
from django.contrib.auth.models import User
from .models import Post1,Post3

class CreatePostForm(forms.ModelForm):
    
    class Meta:
        model = Post3
        #fields = ['bed_room_image']
        fields = ['house_type','renter_preference','family_member','religion_preference','occupation_priority',
            'address','floor','bed_room','bed_room_image','drawing_room','drawing_room_image','dinning_room','dinning_room_image','kitchen',
            'kitchen_room_image','bathroom','bath_room_image','washing_Machine','hot_water','IPS','Generator','Belcony','Oven','lift','refrigerator','sofa','wifi','ac','television','gas','security',
            'parking','house_rent','electricity_rent','gas_rent','water_rent','service_rent','rent_date','any_special_instructions']
        widgets = {
                'house_type': forms.RadioSelect(),
                'renter_preference':forms.RadioSelect(),
                'family_member':forms.RadioSelect(),
                'religion_preference':forms.RadioSelect(),
                'occupation_priority':forms.RadioSelect(),
                'floor':forms.RadioSelect(),
                'bed_room':forms.RadioSelect(),
                'drawing_room':forms.RadioSelect(),
                'dinning_room':forms.RadioSelect(),
                'kitchen':forms.RadioSelect(),
                'bathroom':forms.RadioSelect(),
                'washing_Machine':forms.RadioSelect(),
                'hot_water':forms.RadioSelect(),
                'IPS':forms.RadioSelect(),
                'Generator':forms.RadioSelect(),
                'Belcony':forms.RadioSelect(),
                'Oven':forms.RadioSelect(),
                'lift':forms.RadioSelect(),
                'refrigerator':forms.RadioSelect(),
                'sofa':forms.RadioSelect(),
                'wifi':forms.RadioSelect(),
                'ac':forms.RadioSelect(),
                'television':forms.RadioSelect(),
                'gas':forms.RadioSelect(),
                'security':forms.RadioSelect(),
                'parking':forms.RadioSelect(),
                
            }     

        
            