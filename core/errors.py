from typing import Iterable
from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import ValidationError
from enum import Enum


class Error(Enum):
    DEFAULT_ERROR = {'code': -2323, 'detail': _('Something went wrong!')}
    INVALID_JWT_TOKEN = {'code': -100, 'detail': _('Invalid token!')}
    INSTANCE_NOT_FOUND = {'code': -404, 'detail': _('{} not found!')}
    DATA_IS_MISSING = {'code': -101, 'detail': _('Data is missing!')}
    INVALID_LONGITUDE = {'code': 0, 'detail': _('Invalid longitude!')}
    INVALID_LATITUDE = {'code': 0, 'detail': _('Invalid latitude!')}
    EXPIRED_TOKEN = {'code': -460, 'detail': _("Your token has expired!")}
    WORNG_PASSWORD = {'code': -440, 'detail': _("wrong password!")}
    USER_NOT_FOUND = {'code': -460, 'detail': _("user not found!")}


class APIError:
    def __init__(self, error: Error, extra=None):
        self.error = error
        self.extra = extra or None
        error_detail = error.value
        if self.extra:
            # Extra values can be used in foramtting a string that contains {}
            if isinstance(self.extra, list):
                error_detail['detail'] = error_detail['detail'].format(*extra)
        try:
            logger.info(error.value)
        except BaseException:
            pass
        raise ValidationError(**error_detail)
