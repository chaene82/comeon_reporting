# superset_config.py

# Setze die Basis-Konfiguration
class Config:
    # Setze die Datenbank-Verbindungs-URL (z.B. PostgreSQL)
    SQLALCHEMY_DATABASE_URI = 'postgresql://superset:superset@db:5432/superset'
    # Setze den Pfad für das Superset-Verzeichnis
    SUPERSET_HOME = '/etc/superset'
    # Aktiviere die Entwicklungsumgebung (nicht in Produktion verwenden)
    DEBUG = True

# Erstelle eine Instanz der Konfiguration
config = Config()
