from Model.PlaceModel import PlaceModel
from Services.Services import Services


class PlaceServices(Services):
    def __init__(self, data: PlaceModel) -> None:
        self.data = data