from models import GuestBookItem, Price
from wtforms_alchemy import ModelForm 

class GuestBookForm(ModelForm):
    class Meta:
        model = GuestBookItem
        include=['author',
                 'text',
            ]
class PriceForm(ModelForm):
    class Meta:
        model = Price
        inclide=['guest_book',
                 'price'
            ]
            