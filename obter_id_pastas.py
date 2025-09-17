import requests

def get_access_token(tenant_id, client_id, client_secret):
    url = f"https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = {
        "client_id": client_id,
        "scope": "https://graph.microsoft.com/.default",
        "client_secret": client_secret,
        "grant_type": "client_credentials"
    }

    response = requests.post(url, headers=headers, data=data)
    response.raise_for_status()
    return response.json()["access_token"]

def listar_pastas_email(access_token, email):
    url = f"https://graph.microsoft.com/v1.0/users/{email}/mailFolders"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()["value"]

def main():
    try:
        tenant_id = tenant_id
        client_id = client_id
        client_secret = client_secret
        email = "email@dominio.com"

        access_token = get_access_token(tenant_id, client_id, client_secret)
        pastas = listar_pastas_email(access_token, email)

        print("\nPastas encontradas:")
        for pasta in pastas:
            print(f" Nome: {pasta['displayName']} | ID: {pasta['id']}")

    except Exception as e:
        print(f"Erro ao listar pastas: {e}")

if __name__ == "__main__":
    main()