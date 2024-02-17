from aiohttp import web
import json
import provider


routes = web.RouteTableDef()

async def status(request):
    return web.Response(text="Server is Alive")

async def week_top_killers(request):
    guide = provider.Provider()
    players = guide.week_top_killers()
    data = {'players': json.dumps(players, indent=4)}
    return web.json_response(data)

async def get_player(request):
    steam_64 = request.rel_url.query['steam_64']
    guide = provider.Provider()
    players = guide.get_player_by_steam64(steam_64)
    data = {'players': json.dumps(players, indent=4)}
    return web.json_response(data)

app = web.Application()
app.add_routes([
    web.get('/status', status),
    web.get('/player', get_player),
    web.get('/top_week', week_top_killers),
    ])

web.run_app(app)
