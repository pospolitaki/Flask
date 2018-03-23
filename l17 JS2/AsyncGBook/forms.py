from models import Message
from wtforms_alchemy import ModelForm

class MessageForm(ModelForm):
    class Meta:
        model = Message
        include = ['name',
                   'message',
                ]
