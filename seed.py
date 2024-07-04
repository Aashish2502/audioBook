from pymongo import MongoClient

audiobooks = [
    {
        'title': 'Fire and Blood',
        'author': 'George R.R. Martin',
        'coverImage': 'https://m.media-amazon.com/images/I/51+EyQja6PL._SY580_.jpg',
        'description': 'Centuries before A Game of Thrones, an even greater game began, one that set the skies alight with dragon flame and saw the Seven Kingdoms turned to ash. So began the Targaryens’ bloody rule, with fire and blood. Setting brother against brother, mother against daughter, and dragon against dragon. Chronicled by a learned maester of the Citadel, this thrilling and bloody history of Westeros tells the story of where the battle for the Iron Throne began...',
        'genre': 'Fiction',
        'reviews': [],
        'rating': 5,
    },
    {
        'title': 'Sapiens',
        'author': 'Yuval Noah Harari',
        'coverImage': 'https://m.media-amazon.com/images/I/41voLKA8u4L._SL250_.jpg',
        'description': 'Tracking humankind from its origin, more than 70,000 years ago, is no easy feat, but it’s exactly what writer Yuval Noah Harari does with deft precision in Sapiens: A Brief History of Humankind. Focusing on the appearance of modern cognition, Harari tracks the evolution of humans and why five other species went extinct. He breaks up our history into four key areas: the evolution of imagination, the introduction of agriculture, the emergence of politics and organisations, and the rise of science',
        'genre': 'Non-fiction',
        'reviews': [],
        'rating': 4,
    },
    {
        'title': 'Ikigai',
        'author': 'Héctor García, Francesc Miralles',
        'coverImage': 'https://m.media-amazon.com/images/I/511HccWipML._SL250_.jpg',
        'description': 'This international bestseller by Héctor García and Francesc Miralles introduces the Japanese concept of Ikigai; meaning ‘a reason to live’. Your Ikigai is a place where your needs, desires, ambitions and satisfactions meet, achieving balance in your life. This audiobook takes the listener on a spiritual journey of finding their Ikigai; taking into account their skills, interests, desires and history to give the listener a reason to jump out of bed in the morning and achieve their full purpose. With finding your Ikigai being closely linked to living a longer life, this listen empowers the audience to live a fuller and more satisfying life and gives them the power of finding their destiny with the help of Japanese wisdom.',
        'genre': 'Non-fiction',
        'reviews': [],
        'rating': 4,
    },
    {
        'title': 'The Sandman',
        'author': 'Neil Gaiman, Dirk Maggs',
        'coverImage': 'https://m.media-amazon.com/images/I/61CEI+8TpdL._SL250_.jpg',
        'description': 'The Sandman, or Lord Morpheus, is the immortal king of dreams, stories and the imagination. Forcefully dragged away from his realm and imprisoned on Earth, he suffers in captivity for decades before finally escaping. However, his escape is only the beginning as he is forced to search for three tools that will restore the powers that he lost during his imprisonment. This listen follows The Sandman on his descent to Hell to confront Lucifer, on his encounters with various DC universe characters, the pursuit of the nightmares that escaped his realm, and time travel through real-world history. ',
        'genre': 'Sci-fi',
        'reviews': [],
        'rating': 3,
    },
    {
        'title': 'The Hidden Hindu',
        'author': 'Akshat Gupta',
        'coverImage': 'https://m.media-amazon.com/images/I/51bEDtL-z8L._SL500_.jpg',
        'description': "Prithvi, a twenty-one-year-old, is searching for a mysterious middle-aged aghori (Shiva devotee), Om Shastri, who was traced more than 200 years ago before he was captured and transported to a high-tech facility on an isolated Indian island. When the aghori was drugged and hypnotized for interrogation by a team of specialists, he claimed to have witnessed all four yugas (the epochs in Hinduism) and even participated in both Ramayana and Mahabharata. Om's revelations of his incredible past that defied the nature of mortality left everyone baffled....",
        'genre': 'Fiction',
        'reviews': [],
        'rating': 5,
    },
    {
        'title': 'The Immortals of Meluha',
        'author': 'Amish Tripathi',
        'coverImage': 'https://m.media-amazon.com/images/I/51MGcZVLSoL._SL250_.jpg',
        'description': 'The year 1900 BC. In what modern Indians mistakenly call the Indus Valley Civilisation. The inhabitants of that period called it the land of Meluha–a near perfect empire created many centuries earlier by Lord Ram, one of the greatest monarchs that ever lived.This once proud empire and its Suryavanshi rulers face severe perils as its primary river, the revered Saraswati, is slowly drying to extinction. They also face devastating terrorist attacks from the east, the land of the Chandravanshis. To make matters worse, the Chandravanshis appear to have allied with the Nagas, an ostracised and sinister race of deformed humans with astonishing martial skills...',
        'genre': 'Fiction',
        'reviews': [],
        'rating': 4,
    },
    {
        'title': 'The Martian',
        'author': 'Andy Weir',
        'coverImage': 'https://m.media-amazon.com/images/I/414J3xG+7+L._SL250_.jpg',
        'description': 'Explore life beyond planet Earth in this modern reinvention of Andy Weir’s sci-fi classic. This updated performance of The Martian takes us on an outer space journey as astronaut Mark Watney becomes the first person to walk, and possibly die, on planet Mars. Stranded and alone, Mark must work against the clock to overcome his fate. Voiced by the iconic sci-fi actor and Star Trek legend, Wil Wheaton, Mark’s journey is complete with a healthy dose of sarcasm. ',
        'genre': 'Sci-fi',
        'reviews': [],
        'rating': 3,
    },
    {
        'title': 'Red Rising',
        'author': 'Pierce Brown',
        'coverImage': 'https://m.media-amazon.com/images/I/51IM+e-toYL._SL250_.jpg',
        'description': 'Author Pierce Brown’s debut Red Rising is set in a futuristic Mars colony organised by a colour-coded class hierarchy in which the physically superior Golds rule over the lowly working-class Reds. Among the Reds is Darrow, a young man who is caught in a restricted area and sentenced to be hanged—only to find himself alive, spared by the work of a rebel group called the Sons of Ares. On their suggestion, he agrees to be surgically transformed into a Gold so he can infiltrate the upper ranks and bring the system down from within. But in the process, Darrow finds his external transformation could make it difficult to remain true to who he is inside.',
        'genre': 'Sci-fi',
        'reviews': [],
        'rating': 4,
    },
    {
        'title': 'Good to Great',
        'author': 'Jim Collins',
        'coverImage': 'https://m.media-amazon.com/images/I/41tCQsn8UGL._SL250_.jpg',
        'description': 'Jim Collins believes that good is the enemy of great, so he opens Good to Great by saying just that. Collins sets out to discover if any business can go from good to great, or if greatness is something a business needs from the very start. This listen explores the idea that the acceptance of good or even mediocrity, can prevent businesses and ideas from becoming outstanding and innovative. Built on five years of research, this listen is narrated by Collins himself as he compares 28 different companies with an articulate, educational tone.',
        'genre': 'Business',
        'reviews': [],
        'rating': 5,
    },
]

client = MongoClient('mongodb://localhost:27017/')
client.drop_database("audiobookDB")

db = client.audiobookDB

db.audiobooks.insert_many(audiobooks)
print('Audiobooks inserted successfully.')
