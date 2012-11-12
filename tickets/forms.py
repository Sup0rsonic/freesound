#
# Freesound is (c) MUSIC TECHNOLOGY GROUP, UNIVERSITAT POMPEU FABRA
#
# Freesound is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# Freesound is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors:
#     See AUTHORS file.
#

from django import forms
from models import UserAnnotation
from utils.forms import RecaptchaForm
from tickets import *

class ModeratorMessageForm(forms.Form):
    message     = forms.CharField(widget=forms.Textarea,)
    moderator_only = forms.BooleanField(required=False)

class UserMessageForm(forms.Form):
    message     = forms.CharField(widget=forms.Textarea)

class UserContactForm(UserMessageForm):
    title       = forms.CharField()

    def __init__(self, *args, **kwargs):
        super(UserContactForm, self).__init__(*args, **kwargs)
        self.fields.keyOrder = ['title', 'message']

class AnonymousMessageForm(RecaptchaForm):
    message     = forms.CharField(widget=forms.Textarea)

class AnonymousContactForm(AnonymousMessageForm):
    title       = forms.CharField()
    email       = forms.EmailField()

    def __init__(self, *args, **kwargs):
        super(AnonymousContactForm, self).__init__(*args, **kwargs)
        self.fields.keyOrder = ['email', 'title', 'message']

# Sound moderation forms
MODERATION_CHOICES = [(x,x) for x in \
                      ['Approve',
                       'Delete',
                       'Defer',
                       'Return',
                       'Whitelist']]

class SoundModerationForm(forms.Form):
    action      = forms.ChoiceField(choices=MODERATION_CHOICES,
                                    required=True,
                                    widget=forms.RadioSelect(),
                                    label='')
    ticket      = forms.IntegerField(widget=forms.widgets.HiddenInput)

class ModerationMessageForm(forms.Form):
    message     = forms.CharField(widget=forms.Textarea,
                                  required=False,
                                  label='')
    moderator_only = forms.BooleanField(required=False)

class UserAnnotationForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea,
                           required=True,
                           label='')


TICKET_STATUS_CHOICES = [(x,x.capitalize()) for x in \
                         [TICKET_STATUS_ACCEPTED,
                          TICKET_STATUS_CLOSED,
                          TICKET_STATUS_DEFERRED,
                          TICKET_STATUS_NEW]]

class TicketModerationForm(forms.Form):
    status      = forms.ChoiceField(choices=TICKET_STATUS_CHOICES,
                                    required=False,
                                    label='Ticket status')

class SoundStateForm(forms.Form):
    state       = forms.ChoiceField(choices=[("OK", "OK"),
                                             ("PE", "Pending"),
                                             ("DE", "Delete")],
                                    required=False,
                                    label='Sound state')
