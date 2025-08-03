from pydantic import BaseSettings

class Settings(BaseSettings):
    # Keycloak
    keycloak_url: str
    keycloak_realm: str
    keycloak_client_id: str
    keycloak_client_secret: str
    keycloak_username: str
    keycloak_password: str

    # AWS S3
    aws_access_key_id: str
    aws_secret_access_key: str
    aws_bucket_name: str
    aws_region: str

    class Config:
        env_file = ".env"

settings = Settings()