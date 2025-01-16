from dataclasses import dataclass
from typing import Optional

@dataclass
class ReviewModel:
    author_name: str
    rating: Optional[float]
    text: str
    relative_time_description: Optional[str]

    def print_review(self):
        print(
            f"auther_name: {self.author_name}", "\n",
            f"rating: {self.rating}", "\n",
            f"text: {self.text}", "\n",
            f"relative_time_description: {self.relative_time_description}", "\n"
        )

# 実際のReviewModelインスタンスのデータ例
    """例1
        auther_name: 'Daniel Schiff'
        rating: 5
        text: '''
            100/10 - one of the best sushi I’ve had in my life. And I’ve had quite a few
            Super minimalistic. Clean. Perfect rice, perfectly balanced, every fish was well treated, with the accurate amount of sauce.
            Chef was very friendly and the atmosphere was magical.
            Can’t wait to be back.
            This is what sushi is all about.
        '''
        relative_time_description: '3 months ago'
    """

    """例2
        auther_name: 'Mark Cheung'
        rating: 5
        text: '''
            Hakkoku is a must visit, Be prepared for 25 pieces, try to go on a pretty empty stomach.

            There is a great variety of fish which kept the night interesting, the various tuna courses were great as was the uni, mackerel, anago and ankimo.

            The service was good and the waitress was very friendly.

            chef Sato is a renown sushi chef and has done quite a few global collaborations across hallmark restaurants overseas including at Bondi icebergs. He was very friendly and added a great atmosphere to the sitting.

            Highly recommend and without a doubt one of the best Omakase restaurants I’ve been to.
        '''
        relative_time_description: '3 months ago'
    """
    
    """例3
        auther_name: 'Hooke Wando'
        rating: 5
        text: '''
            Such an exquisite experience - something to behold, observing a master of his craft preparing each dish, each serving with utter care to perfection.

            You’re greeted at the counter by someone who would store your belongings in a cupboard for you, before being ushered to your seats.

            The chef’s assistants will share the menu, ask about allergies and offer drinks.

            Note that still/sparkling water seems to already be included.

            The number of courses seem daunting, but should actually be adequate.

            Total dinner service should take no more than an hour and a half.
        '''
        relative_time_description: '7 months ago'
    """
    
    """例4
        auther_name: 'Jud Valeski'
        rating: 5
        text: '''
            Fish quality was on-point. Chef was diligent, professional, and experienced. Wonderfully nice ambiance and quaint bar.
        '''
        relative_time_description: 'a month ago'
    """

    """例5
        auther_name: 'U Cara W'
        rating: 5
        text: '''
            Visited Hakkoku and was blown away by their dinner course, which includes 25 pieces of fresh and delicious sushi, along with some entrees, vegetables, and desserts. Despite the generous amount of sushi, the small portion of rice created a perfect balance with the sashimi. Even my friends and I, who don't usually have big appetites, managed to finish all the dishes.
            Their wide variety of sake was another highlight. The restaurant offers sakes in carafe, allowing us to try a few, and even recommended some for pairing! The ambiance was pleasant and the staff was attentive and friendly. Highly recommended!
        '''
        relative_time_description: 9 months ago
    """