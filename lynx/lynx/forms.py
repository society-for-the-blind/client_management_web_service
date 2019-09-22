from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Contact, Address, Intake, Email, Phone, Referral, IntakeNote, EmergencyContact, Authorization, \
    ProgressReport, LessonNote, SipNote


class ContactForm(forms.ModelForm):

    class Meta:

        model = Contact
        exclude = ('created', 'modified', 'user')


class IntakeForm(forms.ModelForm):
    intake_date = forms.DateField(widget=forms.SelectDateWidget(empty_label="Nothing"))
    eye_condition_date = forms.DateField(widget=forms.SelectDateWidget(empty_label="Nothing"))
    birth_date = forms.DateField(widget=forms.SelectDateWidget(years=range(1900, 2050)))

    class Meta:

        model = Intake
        exclude = ('contact', 'created', 'modified', 'user')


class AddressForm(forms.ModelForm):

    class Meta:

        model = Address
        exclude = ('created', 'modified', 'user', 'billing', 'contact')


class EmergencyForm(forms.ModelForm):

    class Meta:

        model = EmergencyContact
        exclude = ('created', 'modified', 'user', 'contact')


class EmailForm(forms.ModelForm):

    class Meta:

        model = Email
        exclude = ('created', 'modified', 'user', 'contact', 'active')


class PhoneForm(forms.ModelForm):

    class Meta:

        model = Phone
        exclude = ('created', 'modified', 'user', 'contact', 'active')


class IntakeNoteForm(forms.ModelForm):

    class Meta:

        model = IntakeNote
        fields = ('note',)


class AuthorizationForm(forms.ModelForm):
    start_date = forms.DateField(widget=forms.SelectDateWidget(empty_label="Nothing"))
    end_date = forms.DateField(widget=forms.SelectDateWidget(empty_label="Nothing"))

    class Meta:

        model = Authorization
        exclude = ('created', 'modified', 'user', 'contact')


class ProgressReportForm(forms.ModelForm):

    class Meta:

        model = ProgressReport
        exclude = ('created', 'modified', 'user', 'authorization')


class LessonNoteForm(forms.ModelForm):
    date = forms.DateField(widget=forms.SelectDateWidget(empty_label="Nothing"))

    class Meta:

        model = LessonNote
        exclude = ('created', 'modified', 'user', 'authorization')


class SipNoteForm(forms.ModelForm):
    note_date = forms.DateField(widget=forms.SelectDateWidget(empty_label="Nothing"))

    class Meta:

        model = SipNote
        exclude = ('created', 'modified', 'user', 'contact')
