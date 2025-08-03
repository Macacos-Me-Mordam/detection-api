import httpx
from app.config import settings

async def programmatic_login():
    token_url = (
        f"{settings.keycloak_url}/realms/{settings.keycloak_realm}"
        "/protocol/openid-connect/token"
    )

    payload = {
        "grant_type": "password",
        "client_id": settings.keycloak_client_id,
        "client_secret": settings.keycloak_client_secret,
        "username": settings.keycloak_username,
        "password": settings.keycloak_password,
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(token_url, data=payload)

    if response.status_code != 200:
        raise Exception(f"Erro ao autenticar com Keycloak: {response.text}")

    data = response.json()
    return data["access_token"]