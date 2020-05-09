from settingsapp.models import *

import hashlib

class VolunteerPortalServices:

    def hash_pass(password):
        h = hashlib.new('ripemd160')
        h.update(password.encode('utf-8'))
        return h.hexdigest()
