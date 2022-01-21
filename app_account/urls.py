from django.urls import path
from .views import (account_view,
                    account_conversation_view,
                    account_card_view,
                    login_view,
                    register_view,
                    logout_view,
                    )

urlpatterns = [
    path('account', account_view, name='accountView'),
    path('accountConversation', account_conversation_view, name='accountConversationView'),
    path('accountCard', account_card_view, name='accountCardView'),
    path('login/', login_view, name='loginView'),
    path('register', register_view, name='registerView'),
    path('logout', logout_view, name='logoutView'),
]
