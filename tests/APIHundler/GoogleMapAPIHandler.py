from typing import List, Dict, Any
import requests

class GoogleMapAPIHandler:
    def __init__(self, api_key: str, place_search_url: str, place_details_url: str) -> None:
        self.api_key = api_key
        self.place_search_url = place_search_url
        self.place_details_url = place_details_url
    
    def get_place_search(self, keywords: str) -> List[Dict[str, Any]] | None:
        """
            キーワードに基づいて場所を検索
            戻り値のサンプル：
            sample_return = [
                {
                    "place_id": "Sample_place_id_1",
                    "name": "Sushi Tokyo",
                    "formatted_address": "123 Tokyo St, Tokyo, Japan",
                    "geometry": {
                        "location": {"lat": 35.6895, "lng": 139.6917}
                    },
                    "rating": 4.5,
                    "user_ratings_total": 120
                },
                {
                    "place_id": "Sample_place_id_2",
                    "name": "Sushi Osaka",
                    "formatted_address": "123 Osaka St, Osaka, Japan",
                    "geometry": {
                        "location": {"lat": 34.4010, "lng": 135.3555}
                    },
                    "rating": 5.0,
                    "user_ratings_total": 1200
                }
            ]
        """
        params = {
            "query": keywords,
            "key": self.api_key
        }
        response = requests.get(self.place_search_url, params=params)
        if response.status_code == 200:
            return response.json().get("results", [])
        else:
            response.raise_for_status()
    
    def get_place_details(self, place_id: str) -> Dict[str, Any] | None:
        """
            特定の場所の詳細情報を取得

            戻り値のサンプル
            sample_return = {
                "formatted_phone_number": "+81 3-1234-5678",
                "opening_hours": {
                    "weekday_text": [
                        "Monday: 9:00 AM - 6:00 PM",
                        "Tuesday: 9:00 AM - 6:00 PM",
                        "Wednesday: 9:00 AM - 6:00 PM",
                        "Thursday: 9:00 AM - 6:00 PM",
                        "Friday: 9:00 AM - 6:00 PM"
                    ]
                },
                "reviews": [
                    {
                        "author_name": "John Doe",
                        "rating": 5,
                        "text": "Amazing sushi!",
                        "relative_time_description": "a week ago"
                    },
                    {
                        "author_name": "Jane Smith",
                        "rating": 4,
                        "text": "Good atmosphere, but a bit pricey.",
                        "relative_time_description": "2 weeks ago"
                    }
                ],
                "url": "https://maps.google.com/?cid=1234567890"
            }
        """
        fields = ",".join([
            "formatted_phone_number",
            "opening_hours",
            "reviews",
            "url"
        ])
        params = {
            "place_id": place_id,
            "key": self.api_key,
            "fields": fields
        }
        response = requests.get(self.place_details_url, params=params)
        if response.status_code == 200:
            return response.json().get("result", {})
        else:
            response.raise_for_status()