# Don't change anything in this file.
import survey.models as models
import ptree.views

class ParticipantMixIn(object):
    z_models = models

    def z_autocomplete(self):
        self.subsession = models.Subsession()
        self.treatment = models.Treatment()
        self.match = models.Match()
        self.participant = models.Participant()

class ExperimenterMixIn(object):

    z_models = models

    def z_autocomplete(self):
        self.subsession = models.Subsession()


class InitializeParticipant(ParticipantMixIn, ptree.views.InitializeParticipant):

    pass


class InitializeExperimenter(ExperimenterMixIn, ptree.views.InitializeExperimenter):

    pass
