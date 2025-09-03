from django import forms
from django.contrib.auth import get_user_model

class PasswordResetForm(forms.Form):
  email = forms.EmailField(
    max_length = 255, 
    required = True, 
    widget = forms.EmailInput(attrs = {'placeholder': 
                                       'you@example.com'})
  )
  def clean_email(self):
    email = self.cleaned_data.get('email')
    User = get_user_model()
    if not User.objects.filter(email = email).exists():
      raise forms.ValidaationError('' \
      'No account is associated with this email address.')
    
    return email
  
  