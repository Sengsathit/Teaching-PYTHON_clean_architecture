from typing import List
from abc import ABC, abstractmethod
from .entities import Product

class ProductRepository(ABC):
    @abstractmethod
    def get_all_products(self) -> List[Product]:
        """Retourne tous les produits disponibles"""
        pass