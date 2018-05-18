# -*- coding: utf-8 -*-

from django import forms
from django.core.exceptions import ValidationError

from pizza_app.models import PizzaOrder, Address
from pizza_auth_app.models import CustomUser
from django.contrib.auth.models import AnonymousUser


class DeliveryForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = [
            'full',
        ]


class PizzaOrderForm(forms.ModelForm):
    class Meta:
        model = PizzaOrder
        exclude = [
            'delivered',
            'date_created',
            'date_delivered',
            'delivery',
            'user',
        ]

    def clean(self):
        data = self.cleaned_data
        excluded = data['exclude']

        errors = []
        for item in excluded:
            if item in data['extra']:
                errors.append(str(item))

        if errors:
            raise ValidationError(
                'Ingredients [{}] are in extras and excludes!'.format(
                    ', '.join(errors)
                )
            )
        return data

    def save(self, commit=True, delivery=None, user=None):
        if delivery is None:
            raise ValueError('Delivery was not set')


        inst = super().save(commit=False)
        inst.delivery = delivery

        inst.user = user if isinstance(user, CustomUser) else None
        if commit:
            inst.save()

        return inst
