from aiohttp import web
import json
import provider


routes = web.RouteTableDef()

async def status(request):
    return web.Response(text="Server is Alive")


async def top_killers(request):
    try:
        guide = provider.Provider()
        players = guide.top_killers()
        players = json.dumps(players, indent=4)
        data = {'players': json.loads(players)}
        return web.json_response(data)

    except:
        raise web.HTTPInternalServerError


async def week_top_killers(request):
    try:
        guide = provider.Provider()
        players = guide.week_top_killers()
        players = json.dumps(players, indent=4)
        data = {'players': json.loads(players)}
        return web.json_response(data)

    except:
        raise web.HTTPInternalServerError


async def get_player(request):
    try:
        steam_64 = []
        if steam_64 := request.rel_url.query['steam_64']:
            guide = provider.Provider()
            players = guide.get_player_by_steam64(steam_64)
            players = json.dumps(players, indent=4)
            data = {'players': json.loads(players)}
            return web.json_response(data)

    except:
        raise web.HTTPBadRequest


app = web.Application()
app.add_routes([
    web.get('/status', status),
    web.get('/player', get_player),
    web.get('/top_week', week_top_killers),
    web.get('/top_killers', top_killers),
    ])

web.run_app(app)
