from django import forms

class ContatoForm(forms.Form):
    nome = forms.CharField(max_length=128, min_length=2)
    email = forms.EmailField(required = False)
    mensagem = forms.CharField(widget = forms.Textarea)

    def clean(self):
        dados = super().clean()

        email = dados.get('email', None)
        mensagem = dados.get('mensagem')
        
        if '@gmail.com' in email:
            self.add_error('email', 'Casca fora, não aceitamos "gmail".')

        palavras = ['problema','defeito','erro']

        for palavra in palavras:
            if palavra in mensagem.lower():
                self.add_error('mensagem','Você não pode denegrir nossa aplicação, se manda.')

        return dados