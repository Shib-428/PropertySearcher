from typing import Dict
from Model.ReviewModel import ReviewModel

class ReviewMapper:
    @staticmethod
    def map_review(review_data: Dict) -> ReviewModel:
        """レスポンス内のレビュー情報をReviewデータクラスにマッピングする。

        Args:
            review_data (Dict): レスポンス内のレビュー情報。

        Returns:
            Review: マッピングされたReviewデータクラス。
        """
        review = ReviewModel(
            author_name=review_data.get("author_name", "Unknown"),
            rating=review_data.get("rating"),
            text=review_data.get("text", ""),
            relative_time_description=review_data.get("relative_time_description", "N/A")
        )
        
        return review