from django.core.exceptions import ValidationError

class ContainsLetterValidator:
    def validate(self, password, user=None):
        if not any(char.isalpha() for char in password):
            raise ValidationError('Le mot de passe doit au moins contenir une lettre', code='password_no_letters')

    def get_help_text(self):
        return 'Votre mot de passe doit au moins contenir une lettre majuscule ou une lettre minuscule'    
        
