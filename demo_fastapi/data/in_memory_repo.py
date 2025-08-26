from typing import List
from domain.entities import Product
from domain.interfaces import ProductRepository

class InMemoryProductRepository(ProductRepository):
    """Implémentation en mémoire (exemple statique) du ProductRepository."""
    
    def get_all_products(self) -> List[Product]:
        return [
            Product(1, "Keyboard", 29.9),
            Product(2, "Mouse", 19.9),
            Product(3, "Monitor", 149.0),
        ]