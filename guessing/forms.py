# -*- coding: utf-8 -*-
import guessing.models as models
from guessing.utilities import ParticipantMixIn
import ptree.forms


class GuessForm(ParticipantMixIn, ptree.forms.Form):

    class Meta:
        model = models.Participant
        fields = ['guess_value']

    def labels(self):
        return {'guess_value': "What's your Guess?"}

    def guess_value_error_message(self, value):
        if (value < 0) or (value > 100):
            return 'Guess value should be between {} and {}'.format(0,100)
