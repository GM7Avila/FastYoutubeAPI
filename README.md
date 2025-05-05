# FastYoutubeAPI

Utilizando FastAPI para interagir com a API do YouTube (teste).

## Requisitos

- Python 3.9 ou superior

## Rodando o projeto

1. crie e ative seu ambiente virtual: `python -m venv venv` + `source venv/bin/activate`
2. instale dependências: `pip install -r requirements.txt`
3. crie e configure o .env com sua chave `YOUTUBE_API_KEY` (consulte a documentação [aqui](https://developers.google.com/youtube/v3/getting-started))
4. utilize o Makefile com `make run` ou se preferir `uvicorn application.main:app --reload`
5. servidor: [http://127.0.0.1:8000](http://127.0.0.1:8000)

## Endpoints

### 1. GET

#### 1.1. Video Info by Id

- Http Method: `GET`
- Endpoint: `/youtube/video-info/{video_id}`
- Resumo: Retorna informações sobre um vídeo do YouTube. O `video_id` é o identificador único de um vídeo do YouTube.
- Parâmetros: **video_id** (path): O ID do vídeo do YouTube que deseja consultar.

```python
{
  "kind": "youtube#videoListResponse",
  "etag": "string",
  "items": [
    {
      "kind": "youtube#video",
      "etag": "string",
      "id": "string",
      "snippet": {
        "publishedAt": "datetime",
        "channelId": "string",
        "title": "string",
        "description": "string",
        "thumbnails": {
          "default": {
            "url": "string",
            "width": 120,
            "height": 90
          },
          "medium": {
            "url": "string",
            "width": 320,
            "height": 180
          },
          "high": {
            "url": "string",
            "width": 480,
            "height": 360
          },
          "standard": {
            "url": "string",
            "width": 640,
            "height": 480
          }
        },
        "channelTitle": "string",
        "tags": ["string"],
        "categoryId": "string",
        "liveBroadcastContent": "string",
        "localized": {
          "title": "string",
          "description": "string"
        }
      }
    }
  ],
  "pageInfo": {
    "totalResults": 1,
    "resultsPerPage": 1
  }
}
```

- Erro: `500`
