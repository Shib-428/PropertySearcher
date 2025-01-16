from dataclasses import dataclass
from typing import List, Dict, Optional
from Model.ReviewModel import ReviewModel

@dataclass
class PlaceModel:
    name: str                             # Text Search
    place_id: str                         # Text Search
    formatted_address: str                # Text Search
    formatted_phone_number: Optional[str] # Details
    opening_hours: Optional[Dict]         # Details
    rating: Optional[float]               # Text Search 評価件数が0ならnull
    user_rating_total: int                # Text Search
    reviews: List[ReviewModel]            # Details
    url: Optional[str]                    # Details 注意：Google MapのURL

    """追加する可能性があるフィールド
        website: Optional[str]                # ウェブサイトのurl
        business_status:Optional[str ]        # 営業状況
        price_level: Optional[int]            # 価格帯
    """

    def print_place(self):
        print(
            f"name: {self.name}", "\n",
            f"place_id: {self.place_id}", "\n",
            f"formatted_address: {self.formatted_address}", "\n",
            f"formatted_phone_number: {self.formatted_phone_number}", "\n",
            f"opening_hours: {self.opening_hours}", "\n",
            f"rating: {self.rating}", "\n",
            f"user_rating_total: {self.user_rating_total}", "\n"
        )
        [review.print_review() for review in self.reviews]
        print(f"url: {self.url}", "\n")



    """実際のPlaceModelのデータ例
        name: 'Hakkoku'
        place_id: 'ChIJPYBAAuaLGGARTwNCf6ag05s'
        formatted_address: 'Japan, 〒104-0061 Tokyo, Chuo City, Ginza, 6 Chome−7−6 ラペビル ３F'
        formatted_phone_number: ('03-6280-6555',)
        opening_hours: {
            'open_now': False,
            'periods': [
                {'close': {'day': 1, 'time': '1400'}, 'open': {'day': 1, 'time': '1130'}},
                {'close': {'day': 1, 'time': '2300'}, 'open': {'day': 1, 'time': '1700'}},
                {'close': {'day': 2, 'time': '1400'}, 'open': {'day': 2, 'time': '1130'}},
                {'close': {'day': 2, 'time': '2300'}, 'open': {'day': 2, 'time': '1700'}},
                {'close': {'day': 3, 'time': '1400'}, 'open': {'day': 3, 'time': '1130'}},
                {'close': {'day': 3, 'time': '2300'}, 'open': {'day': 3, 'time': '1700'}},
                {'close': {'day': 4, 'time': '1400'}, 'open': {'day': 4, 'time': '1130'}},
                {'close': {'day': 4, 'time': '2300'}, 'open': {'day': 4, 'time': '1700'}},
                {'close': {'day': 5, 'time': '1400'}, 'open': {'day': 5, 'time': '1130'}},
                {'close': {'day': 5, 'time': '2300'}, 'open': {'day': 5, 'time': '1700'}},
                {'close': {'day': 6, 'time': '1400'}, 'open': {'day': 6, 'time': '1130'}},
                {'close': {'day': 6, 'time': '2300'}, 'open': {'day': 6, 'time': '1700'}}
            ],
            'weekday_text': [
                'Monday: 11:30\u202fAM\u2009–\u20092:00\u202fPM,5:00\u2009–\u200911:00\u202fPM',
                'Tuesday: 11:30\u202fAM\u2009–\u20092:00\u202fPM, 5:00\u2009–\u200911:00\u202fPM',
                'Wednesday: 11:30\u202fAM\u2009–\u20092:00\u202fPM, 5:00\u2009–\u200911:00\u202fPM',
                'Thursday: 11:30\u202fAM\u2009–\u20092:00\u202fPM, 5:00\u2009–\u200911:00\u202fPM',
                'Friday: 11:30\u202fAM\u2009–\u20092:00\u202fPM, 5:00\u2009–\u200911:00\u202fPM',
                'Saturday: 11:30\u202fAM\u2009–\u20092:00\u202fPM, 5:00\u2009–\u200911:00\u202fPM',
                'Sunday: Closed'
            ]
        }
        rating: 4.3
        user_rating_total: 352

        review: [ReviewModel.py参照]

        url: 'https://maps.google.com/?cid=11228494932924826447'
    """