import requests
import json
from fastapi import APIRouter, HTTPException

nasa = APIRouter()

NASA_API_ROOT = 'https://images-api.nasa.gov'

@nasa.get('/search')
async def search(q:str = None, description:str = None, media_type:str = None):
    params = {
        'q': q,
        'description': description,
        "media_type": media_type
    }

    response = requests.get(f'{NASA_API_ROOT}/search', params=params)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)
    #with open('data.json', 'w') as json_file:
     #   json.dump(response.json(), json_file, indent=2)
    return response.json()

@nasa.get('/asset/{nasa_id}')
async def get_asset(nasa_id:str):
    response = requests.get(f'{NASA_API_ROOT}/asset/{nasa_id}')
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)
    with open('data.json', 'w') as json_file:
        json.dump(response.json(), json_file, indent=2)
    return response.json()

@nasa.get('/metadata/{nasa_id}')
async def get_metadata(nasa_id:str):
    response = requests.get(f'{NASA_API_ROOT}/metadata/{nasa_id}')
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)
    #with open('data.json', 'w') as json_file:
     #   json.dump(response.json(), json_file, indent=2)
    return response.json()

@nasa.get('/captions/{nasa_id}')
async def get_captions(nasa_id:str):
    response = requests.get(f'{NASA_API_ROOT}/captions/{nasa_id}')
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)
    #with open('data.json', 'w') as json_file:
     #   json.dump(response.json(), json_file, indent=2)
    return response.json()

@nasa.get('/album/{album_name}')
async def get_album(album_name:str, page:int = 1):
    params = {
        'page': page
    }
    response = requests.get(f'{NASA_API_ROOT}/album/{album_name}', params=params)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)
    #with open('data.json', 'w') as json_file:
     #   json.dump(response.json(), json_file, indent=2)
    return response.json()