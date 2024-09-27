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

async def top_killers_cumulative(request):
    try:
        guide = provider.Provider()
        players = guide.top_killers_cumulative()
        players = json.dumps(players, indent=4)
        data = {'players': json.loads(players)}
        return web.json_response(data)

    except:
        raise web.HTTPInternalServerError


async def top_killers_cumulative_week(request):
    try:
        guide = provider.Provider()
        players = guide.top_killers_cumulative_week()
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


async def top_weapons(request):
    try:
        guide = provider.Provider()
        weapons = guide.get_top_weapons_by_player()
        weapons = json.dumps(weapons, indent=4)
        data = {'weapons': json.loads(weapons)}
        return web.json_response(data)

    except:
        raise web.HTTPInternalServerError


async def get_player(request):
    try:
        if steam_64 := request.rel_url.query['steam_64']:
            guide = provider.Provider()
            players = guide.get_player_by_steam64(steam_64)
            players = json.dumps(players, indent=4)
            data = {'data': json.loads(players)}
            return web.json_response(data)

        if not steam_64:
            return web.HTTPBadRequest(text='Please Provide Steam64 ID')

    except:
        raise web.HTTPBadRequest


async def get_player_stats(request):
    try:
        if steam_64 := request.rel_url.query['steam_64']:
            guide = provider.Provider()
            players = guide.get_player_stats_by_steam64(steam_64)
            players = json.dumps(players, indent=4)
            data = {'data': json.loads(players)}
            return web.json_response(data)

        if not steam_64:
            return web.HTTPBadRequest(text='Please Provide Steam64 ID')

    except:
        raise web.HTTPBadRequest


async def get_player_weapon_stats(request):
    try:
        if steam_64 := request.rel_url.query['steam_64']:
            guide = provider.Provider()
            weapons = guide.get_weapon_stats_by_steam64(steam_64)
            weapons = json.dumps(weapons, indent=4)
            data = {'data': json.loads(weapons)}
            return web.json_response(data)

        if not steam_64:
            return web.HTTPBadRequest(text='Please Provide Steam64 ID')

    except:
        raise web.HTTPBadRequest


async def get_kill_records(request):
    try:
        steam_64 = []
        if steam_64 := request.rel_url.query['limit']:
            guide = provider.Provider()
            players = guide.get_player_by_steam64(steam_64)
            players = json.dumps(players, indent=4)
            data = {'data': json.loads(players)}
            return web.json_response(data)

    except:
        raise web.HTTPBadRequest


async def scoreboard(request):
    try:
        guide = provider.Provider()
        stats = guide.top_stats()
        hundred_club = guide.killers_club(100)
        stats['100_club'] = hundred_club
        two_hundred_club = guide.killers_club(200)
        stats['200_club'] = two_hundred_club
        three_hundred_club = guide.killers_club(300)
        stats['300_club'] = three_hundred_club
        stats = json.dumps(stats, indent=4)
        data = {'data': json.loads(stats)}
        return web.json_response(data)

    except:
        raise web.HTTPInternalServerError


async def top_stats(request):
    try:
        guide = provider.Provider()
        stats = guide.short_stats()
        stats = json.dumps(stats, indent=4)
        data = {'data': json.loads(stats)}
        return web.json_response(data)

    except:
        raise web.HTTPInternalServerError


app = web.Application()
app.add_routes([
    web.get('/status', status),
    web.get('/player', get_player),
    web.get('/player_lifetime', get_player_stats),
    web.get('/player_weapons_lifetime', get_player_weapon_stats),
    web.get('/top_week', week_top_killers),
    web.get('/top_killers', top_killers),
    web.get('/top_killers_cumulative', top_killers_cumulative),
    web.get('/top_killers_cumulative_week', top_killers_cumulative_week),
    web.get('/top_weapons', top_weapons),
    web.get('/scoreboard', scoreboard),
    web.get('/top_stats', top_stats),
    ])

web.run_app(app)
