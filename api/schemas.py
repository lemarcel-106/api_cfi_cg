from ninja import Schema
from typing import Optional

class ArticleSchema(Schema):
    id: int
    titre: str
    image: str
    description_courte: str
    description_long: str

class EvenementSchema(Schema):
    id: int
    titre: str
    image: str
    type: str
    prix: float
    contions: str
    description_courte: str
    description_long: str

class DonationIn(Schema):
    nom: str
    prenom: str
    adresse_email: str
    telephone: str
    message: Optional[str] = None

class AdhesionIn(Schema):
    nom: str
    prenom: str
    adresse_email: str
    telephone: str

class ContactIn(Schema):
    nom: str
    prenom: str
    email: str
    telephone: str
    message: str



class ArticleDetailSchema(Schema):
    id: int
    titre: str
    image: Optional[str]
    description_courte: str
    description_long: str


class EvenementDetailSchema(Schema):
    id: int
    titre: str
    image: Optional[str]
    type: str
    prix: float
    contions: str
    description_courte: str
    description_long: str
