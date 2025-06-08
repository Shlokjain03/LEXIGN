from flask import Blueprint, render_template

learn = Blueprint('learn', __name__)
flashcards = [

    {"word": "Hello", "sign": "signs/hello.png"},
    {"word": "BathRoom", "sign": "signs/bathroom.png"},
    {"word": "Eat", "sign": "signs/eat.png"},
    {"word": "Friend", "sign": "signs/friend.png"},
    {"word": "ILoveYou", "sign": "signs/iloveyou.png"},
    {"word": "YES", "sign": "signs/yes.png"},
    {"word": "NO", "sign": "signs/no.png"},
    {"word": "Play", "sign": "signs/play.png"},
    {"word": "School", "sign": "signs/school.png"},
    {"word": "Sorry", "sign": "signs/sorry.png"},
]



videos = [
    {
        "title": "Introduction to Sign Language",
        "filename": "videos/25-ASL-Signs.mp4"
    },
    {
        "title": "Common Greetings",
        "filename": "videos/Common-ASL-Phrases.mp4"
    },
    {
        "title": "Basic Conversation",
        "filename": "videos/Basic-ASL-Conversations.mp4"
    },
    {
        "title": "Everyday Sign around the house",
        "filename": "videos/Signs-Around-the-Home.mp4"
    },
    {
        "title": "Emotions and Feelings",
        "filename": "videos/Sign-Feelings-and-Emotions.mp4"
    },
    {
        "title": "Questions and Answers",
        "filename": "videos/Questions-and-Responses.mp4"
    },
]

@learn.route('/')
def learn_home():
    return render_template('learn.html', flashcards=flashcards, videos=videos)
