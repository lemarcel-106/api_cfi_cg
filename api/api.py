from ninja import NinjaAPI, Router
from django.shortcuts import get_object_or_404

from .models import Article, Evenement, Donation, Adhesion, Contact
from .schemas import (
    ArticleSchema, ArticleDetailSchema,
    EvenementSchema, EvenementDetailSchema,
    DonationIn, AdhesionIn, ContactIn
)

# Création de l'API principale
api = NinjaAPI(title="API Gestion Contenu")

# Création des routeurs spécialisés
article_router = Router()
evenement_router = Router()
donation_router = Router()
adhesion_router = Router()
contact_router = Router()

# ----------------------------
# ROUTES POUR LES ARTICLES
# ----------------------------

@article_router.get("/", response=list[ArticleSchema], tags=["Articles"])
def list_articles(request):
    """
    Liste tous les articles.
    """
    return Article.objects.all()

@article_router.get("/{article_id}", response=ArticleDetailSchema, tags=["Articles"])
def get_article_detail(request, article_id: int):
    """
    Détail d’un article par ID.
    """
    article = get_object_or_404(Article, id=article_id)
    return {
        "id": article.id,
        "titre": article.titre,
        "image": article.image.url if article.image else None,
        "description_courte": article.description_courte,
        "description_long": article.description_long,
    }

# ----------------------------
# ROUTES POUR LES EVENEMENTS
# ----------------------------

@evenement_router.get("/", response=list[EvenementSchema], tags=["Evenements"])
def list_evenements(request):
    """
    Liste tous les événements.
    """
    return Evenement.objects.all()

@evenement_router.get("/{evenement_id}", response=EvenementDetailSchema, tags=["Evenements"])
def get_evenement_detail(request, evenement_id: int):
    """
    Détail d’un événement par ID.
    """
    evenement = get_object_or_404(Evenement, id=evenement_id)
    return {
        "id": evenement.id,
        "titre": evenement.titre,
        "image": evenement.image.url if evenement.image else None,
        "type": evenement.type,
        "prix": float(evenement.prix),
        "contions": evenement.contions,
        "description_courte": evenement.description_courte,
        "description_long": evenement.description_long,
    }

# ----------------------------
# ROUTE POUR LES DONATIONS
# ----------------------------

@donation_router.post("/", tags=["Donations"])
def create_donation(request, data: DonationIn):
    """
    Enregistre un don.
    """
    Donation.objects.create(**data.dict())
    return {"success": True, "message": "Merci pour votre don !"}

# ----------------------------
# ROUTE POUR LES ADHESIONS
# ----------------------------

@adhesion_router.post("/", tags=["Adhesions"])
def create_adhesion(request, data: AdhesionIn):
    """
    Reçoit une demande d’adhésion.
    """
    Adhesion.objects.create(**data.dict())
    return {"success": True, "message": "Votre demande d'adhésion a été reçue."}

# ----------------------------
# ROUTE POUR LES CONTACTS
# ----------------------------

@contact_router.post("/", tags=["Contacts"])
def create_contact(request, data: ContactIn):
    """
    Reçoit un message de contact.
    """
    Contact.objects.create(**data.dict())
    return {"success": True, "message": "Merci pour votre message."}

# ----------------------------
# ENREGISTREMENT DES ROUTEURS
# ----------------------------

api.add_router("/articles", article_router)
api.add_router("/evenements", evenement_router)
api.add_router("/donation", donation_router)
api.add_router("/adhesion", adhesion_router)
api.add_router("/contact", contact_router)
