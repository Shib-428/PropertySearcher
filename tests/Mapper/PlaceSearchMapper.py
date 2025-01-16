from typing import Dict, Any
from Model.PlaceModel import PlaceModel

class PlaceSearchMapper:
    @staticmethod
    def map_place_search(place_searnch_return: Dict[str, Any]) -> PlaceModel:
        """レスポンス内の詳細情報をPlaceDetailデータクラスにマッピングする。

        Args:
            
            place_searnch_return (Dict): 辞書としてのText Searchのレスポンス。

        Returns:
            place_data (PlaceModel): マッピングされたPlaceModelデータクラス。
        """
        place_data = PlaceModel(
            name=place_searnch_return.get("name", "Unknown"),
            place_id=place_searnch_return.get("place_id"),
            formatted_address=place_searnch_return.get("formatted_address", "Unknown"),
            formatted_phone_number=None,
            opening_hours={},
            rating=place_searnch_return.get("rating"),
            user_rating_total=place_searnch_return.get("user_ratings_total"),
            reviews=[],
            url=place_searnch_return.get("url")
        )

        return place_data