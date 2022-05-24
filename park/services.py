from park.models import ParkPofile

class ParkService:
    @staticmethod
    def create_park(
        name: str,
        mobile_number: int,
        country: str,
        city: str,
        address: str
    ) -> ParkPofile:
        park = ParkPofile.objects.create(
            name=name, mobile_number=mobile_number, country=country, city=city, address=address)
        return park
        