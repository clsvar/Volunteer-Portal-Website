from settingsapp.models import *

import hashlib

class VolunteerPortalServices:

    def hash_pass(password):
        h = hashlib.new('SHA256')
        h.update(password.encode('utf-8'))
        return h.hexdigest()
