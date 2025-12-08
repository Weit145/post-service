from abc import ABC, abstractmethod

class IUserService(ABC):

    @abstractmethod
    def __init__(self, host: str, port: int) -> None:
        pass

    @abstractmethod
    async def get_user_by_username(self, username: str)-> int:
        pass

    @abstractmethod
    async def get_user_by_id(self, user_id: int)-> str:
        pass