"""
Session Businnes Logic Module
"""

from photography_blog.business_logic.base_business_logic import BaseBusinessLogic
from photography_blog.models.session import Session


class SessionBusinssLogic(BaseBusinessLogic):
    """
    This is the business logic for Session.
    """

    def __init__(self):
        super().__init__(model_entity=Session)
