from pharmacy.models import Pharmacy


def list_pharmacy() -> Pharmacy:
    return Pharmacy.objects.all()