from config.settings import settings

def test_env_loaded():
    assert settings.ENV == "development"
    assert isinstance(settings.AGENT_TIMEOUT, int)
    assert settings.DATABASE_URL.startswith("postgresql") or settings.DATABASE_URL.startswith("sqlite")
