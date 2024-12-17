#the concrete observer class

from IteamMember import IteamMember

class teamMember(IteamMember):

    def update(self, context):
        self.memberState = context
        