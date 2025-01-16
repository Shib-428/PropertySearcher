from typing import Dict, Any
from Model.PlaceModel import PlaceModel
from Mapper.ReviewMapper import ReviewMapper

class PlaceDetailsMapper:
    @staticmethod
    def map_place_detail(place_data: PlaceModel, place_details_return: Dict[str, Any]) -> None:
        """レスポンス内の詳細情報をPlaceDetailデータクラスにマッピングする。

        Args:
            place_data (PlaceModel): 基礎情報をマッピング済みのPlace_dataデータクラス。
            place_detail_return (Dict): 辞書としてのplace_detail_returnのレスポンス。
        """
        reviews_data = place_details_return.get("reviews", [])
        reviews = [
            ReviewMapper.map_review(review_data)
            for review_data in reviews_data
        ]
        place_data.formatted_phone_number = place_details_return["formatted_phone_number"],
        place_data.opening_hours = place_details_return["opening_hours"]
        place_data.reviews = reviews
        place_data.url = place_details_return["url"]