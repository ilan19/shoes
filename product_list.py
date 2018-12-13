from product import Product
from comment import Comment

def get_products():
    return [{
                "id": 0,
                "name": "Nike - Presto",
                "price": 170,
                "image": "1.jpeg",
                "rating": 2,
                "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam",
                "details": [
                    "Nothing beats a fresh pair of trainers",
                    "Ideal for trail running",
                    "Lace-up fastening",
                    "Padded for comfort",
                    "Pull tab",
                    "Makes getting them on a little easier",
                    "EVA sole",
                    "It's soft, light and flexible",
                    "Moulded tread",
                ],
                "comments": [
                    {
                      "username": "Bill",
                      "user_picture": "bill.jpg",
                      "comment": "Super shoes ! J'adore !"
                    },
                    {
                      "username": "Mark",
                      "user_picture": "mark.jpg",
                      "comment": "J'ai vu mieux comme pompes..."
                    },
                    {
                      "username": "Jeff",
                      "user_picture": "jeff.jpg",
                      "comment": "Amazing! Mais je prefere acheter sur Amazon !"
                    }
                  ]
            },
            {
                "id": 1,
                "name": "Adidas - Stan Smith",
                "price": 150,
                "image": "2.jpeg",
                "rating": 2,
                "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam",
                "details": [
                    "Nothing beats a fresh pair of trainers",
                    "Ideal for trail running",
                    "Lace-up fastening",
                    "Padded for comfort",
                    "Pull tab",
                    "Makes getting them on a little easier",
                    "EVA sole",
                    "It's soft, light and flexible",
                    "Moulded tread",
                ]
            },
            {
                "id": 2,
                "name": "Nike - huarache",
                "price": 165,
                "image": "3.jpeg",
                "rating": 4,
                "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam",
                "details": [
                    "Nothing beats a fresh pair of trainers",
                    "Ideal for trail running",
                    "Lace-up fastening",
                    "Padded for comfort",
                    "Pull tab",
                    "Makes getting them on a little easier",
                    "EVA sole",
                    "It's soft, light and flexible",
                    "Moulded tread",
                ]
            },
            {
                "id": 3,
                "name": "Off white",
                "price": 850,
                "image": "4.jpeg",
                "rating": 4,
                "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam",
                "details": [
                    "Nothing beats a fresh pair of trainers",
                    "Ideal for trail running",
                    "Lace-up fastening",
                    "Padded for comfort",
                    "Pull tab",
                    "Makes getting them on a little easier",
                    "EVA sole",
                    "It's soft, light and flexible",
                    "Moulded tread",
                ]
            },
            {
                "id": 4,
                "name": "Balenciaga",
                "price": 500,
                "image": "5.jpeg",
                "rating": 4,
                "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam",
                "details": [
                    "Nothing beats a fresh pair of trainers",
                    "Ideal for trail running",
                    "Lace-up fastening",
                    "Padded for comfort",
                    "Pull tab",
                    "Makes getting them on a little easier",
                    "EVA sole",
                    "It's soft, light and flexible",
                    "Moulded tread",
                ]
            },
            {
                "id": 5,
                "name": "Vans - old skoll",
                "price": 90,
                "image": "6.jpeg",
                "rating": 4,
                "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam",
                "details": [
                    "Nothing beats a fresh pair of trainers",
                    "Ideal for trail running",
                    "Lace-up fastening",
                    "Padded for comfort",
                    "Pull tab",
                    "Makes getting them on a little easier",
                    "EVA sole",
                    "It's soft, light and flexible",
                    "Moulded tread",
                ]
            },
            {
                "id": 6,
                "name": "fila",
                "price": 220,
                "image": "7.jpeg",
                "rating": 4,
                "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam",
                "details": [
                    "Nothing beats a fresh pair of trainers",
                    "Ideal for trail running",
                    "Lace-up fastening",
                    "Padded for comfort",
                    "Pull tab",
                    "Makes getting them on a little easier",
                    "EVA sole",
                    "It's soft, light and flexible",
                    "Moulded tread",
                ]
            },
            {
                "id": 7,
                "name": "Nike - 270",
                "price": 170,
                "image": "8.jpeg",
                "rating": 4,
                "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam",
                "details": [
                    "Nothing beats a fresh pair of trainers",
                    "Ideal for trail running",
                    "Lace-up fastening",
                    "Padded for comfort",
                    "Pull tab",
                    "Makes getting them on a little easier",
                    "EVA sole",
                    "It's soft, light and flexible",
                    "Moulded tread",
                ]
            }
        ]


def dictionnary_to_object():
    products = get_products()
    for product in products:
        new_product = Product(product['name'], product['price'], product['image'], product['rating'], product['description'])

dictionnary_to_object()