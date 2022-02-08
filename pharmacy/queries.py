from core.errors import APIError, Error
from pharmacy.models import Pharmacy


def list_pharmacy() -> Pharmacy:
    return Pharmacy.objects.all()


def get_pharmacy_by_id(id:int) -> Pharmacy:
    try:
        return Pharmacy.objects.get(pk=id)
    except BaseException:
        raise APIError(Error.INSTANCE_NOT_FOUND, extra=[
                       Pharmacy._meta.model_name])
