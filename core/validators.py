from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator


_NAME_REGEX = RegexValidator(
    regex=r"^[\u0600-\u065F\u066A-\u06EF\u06FA-\u06FFa-zA-Z]+[\u0600-\u065F\u066A-\u06EF\u06FA-\u06FFa-zA-Z ]*$",
    message=_("Special characters and digits are now allowed."),
)


_PHONE_REGEX = RegexValidator(
    regex=r"^\d{11}$", message=_("Mobile number must be 10 digits starting with '01'."),
)