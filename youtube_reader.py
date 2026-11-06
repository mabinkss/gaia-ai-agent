
import os
import time
import requests
from urllib.parse import urlparse


def extract_youtube_transcript(url: str) -> str:
    api_key = os.getenv("SUPADATA_API_KEY")

    if not api_key:
        raise RuntimeError("Clé Supadata introuvable.")

    url = url.strip()

    if url.startswith(("www.", "youtu.be/")):
        url = "https://" + url

    parsed = urlparse(url)

    if parsed.scheme != "https" or parsed.hostname not in (
        "youtube.com", "www.youtube.com",
        "m.youtube.com", "youtu.be"
    ):
        raise ValueError("Lien YouTube invalide.")

    endpoint = "https://api.supadata.ai/v1/transcript"
    headers = {"x-api-key": api_key}

    response = requests.get(
        endpoint,
        headers=headers,
        params={
            "url": url,
            "text": "true",
            "mode": "auto"
        },
        timeout=30
    )

    response.raise_for_status()
    data = response.json()

    if response.status_code == 202:
        job_id = data["jobId"]

        for attempt in range(30):
            time.sleep(2)

            result = requests.get(
                f"{endpoint}/{job_id}",
                headers=headers,
                timeout=30
            )
            result.raise_for_status()
            data = result.json()

            if data.get("status") == "completed":
                break

            if data.get("status") == "failed":
                raise RuntimeError(
                    "La transcription a échoué."
                )
        else:
            raise TimeoutError(
                "La transcription prend trop de temps."
            )

    content = data.get("content", "")

    if isinstance(content, list):
        content = " ".join(
            item.get("text", "") for item in content
        )

    if not content.strip():
        raise ValueError("Aucune transcription disponible.")

    return content[:25000]
