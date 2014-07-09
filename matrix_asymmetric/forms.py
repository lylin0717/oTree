# -*- coding: utf-8 -*-
import matrix_asymmetric.models as models
from matrix_asymmetric.utilities import ParticipantMixIn
import ptree.forms


class DecisionForm(ParticipantMixIn, ptree.forms.Form):

    class Meta:
        model = models.Participant
        fields = ['decision']

    def labels(self):
        return {'decision': 'Make a choice: Either 1 or 2'}

    def decision_error_message(self, value):
        if (value < 1) or (value > 2):
            return 'Choice should be either {} and {}'.format(1, 2)
