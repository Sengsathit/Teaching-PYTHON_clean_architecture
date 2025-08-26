import os
from domain.interfaces import ProductRepository
from data.in_memory_repo import InMemoryProductRepository
from data.db_repo import DbProductRepository

def get_repo() -> ProductRepository:
    """Provider principal pour injecter un ProductRepository."""
    # return InMemoryProductRepository()
    return DbProductRepository()