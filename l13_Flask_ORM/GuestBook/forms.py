from models import GuestBookItem
from wtforms_alchemy import ModelForm 

class GuestBookForm(ModelForm):
    class Meta:
        model = GuestBookItem
        include=['author',
                 'text',
        ]
