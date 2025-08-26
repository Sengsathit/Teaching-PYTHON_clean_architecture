from typing import List
from time import sleep
from domain.entities import Product
from domain.interfaces import ProductRepository

class DbProductRepository(ProductRepository):
    """Simule un repository qui irait chercher dans une base de données."""

    def get_all_products(self) -> List[Product]:
        print("[DB] Connexion à la base...")
        sleep(3)  # petite latence pour simuler l'accès DB
        print("[DB] SELECT * FROM products;")

        # On retourne des données comme si elles venaient d'une vraie table
        return [
            Product(1, "Keyboard", 29.9),
            Product(2, "Mouse", 19.9),
            Product(3, "Monitor", 149.0),
        ]