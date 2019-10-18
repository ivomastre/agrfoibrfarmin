from django import forms

class CidadeForm(forms.Form):
    cidade = forms.CharField(label='Cidade: ', max_length=100)

class AcaoForm(forms.Form):
    acao = forms.CharField(label='Nome da Ação: ' , max_length=100 )
