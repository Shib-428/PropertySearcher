from APIHundler.GoogleMapAPIHandler import GoogleMapAPIHandler
from Mapper.PlaceSearchMapper import PlaceSearchMapper
from Mapper.PlaceDetailsMapper import PlaceDetailsMapper
from statics import API_KEY, PLACE_DETAILS_URL, PLACE_SEARCH_URL

if __name__ == "__main__":
    api_key = API_KEY
    handler = GoogleMapAPIHandler(
        api_key=API_KEY,
        place_search_url=PLACE_SEARCH_URL,
        place_details_url=PLACE_DETAILS_URL
    )

    # キーワードで場所検索
    keywords = "Tokyo Sushi Restaurant"
    place_search_returns = handler.get_place_search(keywords)
    """簡略化のため、一時的に上位三件のみ抜粋"""
    place_search_returns = (
        place_search_returns[:3]
        if len(place_search_returns) >= 3
        else place_search_returns
    )
    for place_search_return in place_search_returns:
        place_data = PlaceSearchMapper.map_place_search(place_search_return)
        # 詳細情報を取得
        place_details_return = handler.get_place_details(place_data.place_id)
        PlaceDetailsMapper.map_place_detail(place_data, place_details_return)
        place_data.print_place()