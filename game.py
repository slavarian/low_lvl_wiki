class Game:
    """Модель книги для нашего проекта."""

    def __init__(
        self,
        title: str,
        description: str,
        genre: str,
        price: float,
        release_date:int
    ) -> None:
        self.title = title
        self.description = description
        self.genre = genre
        self.price = price 
        self.release_datet = release_date
