# Discord Bot Roadmap

## 1. Define Requirements & Features
✅ **Twitch Notifications**: Alert when a followed Twitch channel starts streaming.  
✅ **School Calendar Notifications**: Daily reminders about tasks and events.  
✅ **Git Push Notifications**: Notify when a push is made to specific repositories.  
✅ **Additional Features**: Consider adding other integrations like weather updates, RSS feeds, or a personal to-do list.  

## 2. Strucutre of the project
```bash
discord-bot/
│── bot.py                # Fichier principal
│── config.py             # Fichier de configuration
│── .env                  # Fichier pour stocker les secrets
│── requirements.txt       # Liste des dépendances
│── cogs/                 # Modules (extensions) du bot
│   │── __init__.py
│   │── twitch.py         # Gestion des notifications Twitch
│   │── calendar.py       # Gestion des rappels du calendrier
│   │── github.py         # Gestion des notifications GitHub
│── utils/                # Fonctions utilitaires
│   │── twitch_api.py     # Gestion des appels à l'API Twitch
│   │── github_api.py     # Gestion des appels à l'API GitHub
│── logs/                 # Dossier pour stocker les logs
│── data/                 # Dossier pour stocker les données (JSON, SQLite)
```

📌 Explication des fichiers
- bot.py → Le point d'entrée du bot.
- config.py → Contient les configurations globales.
- .env → Contient les tokens et secrets (évite de les exposer dans le code).
- requirements.txt → Liste des dépendances pour l'installation.
- cogs/ → Contient les modules pour les fonctionnalités (Twitch, GitHub, etc.).
- utils/ → Contient des scripts pour les appels API et autres fonctionnalités utilitaires.
- logs/ → Stocke les logs pour le débogage.
- data/ → Peut contenir des fichiers JSON ou une base de données SQLite.
