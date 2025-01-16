from Model.ReviewModel import ReviewModel
from Services.Services import Services

class ReviewServices(Services):
    def __init__(self, data: ReviewModel) -> None:
        self.data = data