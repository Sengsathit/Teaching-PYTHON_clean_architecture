from typing import List, Dict
from .interfaces import ProductRepository

class GetProductsUseCase:
    """Use case pour récupérer la liste des produits."""
    def __init__(self, repo: ProductRepository):
        self.repo = repo

    def execute(self) -> List[Dict]:
        return [
            {"id": p.id, "name": p.name, "price": p.price}
            for p in self.repo.get_all_products()
        ]