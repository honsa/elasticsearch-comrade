from sanic import Blueprint
from sanic.response import json

from connections import get_client

index_bp = Blueprint('index')


@index_bp.route('/<index>/close')
async def close_index(request, index):
    client = get_client(request)
    await client.indices.close(index=index, expand_wildcards='none')
    return json({"status": "ok"})


@index_bp.route('/<index>/open')
async def open_index(request, index):
    client = get_client(request)
    await client.indices.open(index=index, expand_wildcards='none')
    return json({"status": "ok"})


@index_bp.route('/<index>/stats')
async def index_stats(request, index):
    client = get_client(request)
    return json(await client.indices.stats(index=index))


@index_bp.route('/<index>/settings')
async def index_settings(request, index):
    client = get_client(request)
    return json(await client.indices.get_settings(index=index, flat_settings=True))


@index_bp.route('/<index>/mapping')
async def get_mapping(request, index):
    client = get_client(request)
    return json(await client.indices.get_mapping(index=index))


@index_bp.route('/<index>/head')
async def head_index(request, index):
    client = get_client(request)
    content = await client.search(index=index)
    return json(x['_source'] for x in content['hits']['hits'])


@index_bp.route('/<index>/flush')
async def flush_index(request, index):
    client = get_client(request)
    await client.indices.flush(index=index)
    return json({"status": "ok"})


@index_bp.route('/<index>/forcemerge')
async def merge_index(request, index):
    client = get_client(request)
    await client.indices.forcemerge(index=index)
    return json({"status": "ok"})


@index_bp.route('/<index>/delete')
async def delete_index(request, index):
    client = get_client(request)
    await client.indices.delete(index=index)
    return json({"status": "ok"})
