from django.conf import settings
from django.utils.translation import ugettext_lazy as _

USERPROFILE_SETTINGS = {
    'app_verbose_name': _("Custom User"),
    'register_proxy_auth_group_model': False,
}

if hasattr(settings, 'USERPROFILE'):
    USERPROFILE_SETTINGS.update(settings.USERPROFILE)
