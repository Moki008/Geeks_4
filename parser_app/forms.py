from django import forms
from . import models, litrez_parser, parser_rezka


class ParserForm(forms.Form):
    CHOICES = (
        ('litrez.ru','litrez.ru'),
        ('rezka.ag','rezka.ag'),
    )
    method = forms.ChoiceField(choices=CHOICES)

    class Meta:
        fields = [
            'method',
        ]

    def parser_data(self):
        if self.data['method'] == 'litrez.ru':
            litrez = litrez_parser.parsing_litrez()
            for item in litrez:
                models.LitrezModel.objects.create(**item)

        elif self.data['method'] == 'rezka.ag':
            rezka = parser_rezka.parsing_rezka()
            for item in rezka:
                models.RezkaModel.objects.create(**item)



