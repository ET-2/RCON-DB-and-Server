from alchemy.database import (
    get_player_by_steam64,
    get_top_killers,
    get_top_week_killers,
    get_player_kills,
    get_player_kills_week,
    get_top_weapons_by_player,
    get_player_kill_count,
    get_players,
    )

class Provider:

    def __init__(self):
    	pass


    def top_stats(self):
        players = get_players()
        weapons = get_top_weapons_by_player()
        ret_data = {}

        stat_items = {
            'kills': 0,
            'deaths': 0,
            'kills_streak': 0,
            'deaths_without_kill_streak': 0,
            'teamkills': 0,
            'teamkills_streak': 0,
            'deaths_by_tk': 0,
            'deaths_by_tk_streak': 0,
            'nb_vote_started': 0,
            'nb_voted_yes': 0,
            'nb_voted_no': 0,
            'kills_per_minute': 0,
            'deaths_per_minute': 0,
            'kill_death_ratio': 0,
            'combat': 0,
            'offense': 0,
            'defense': 0,
            'support': 0,
        }

        stat_players = {
            'kills': 0,
            'deaths': 0,
            'kills_streak': 0,
            'deaths_without_kill_streak': 0,
            'teamkills': 0,
            'teamkills_streak': 0,
            'deaths_by_tk': 0,
            'deaths_by_tk_streak': 0,
            'nb_vote_started': 0,
            'nb_voted_yes': 0,
            'nb_voted_no': 0,
            'kills_per_minute': 0,
            'deaths_per_minute': 0,
            'kill_death_ratio': 0,
            'combat': 0,
            'offense': 0,
            'defense': 0,
            'support': 0,
        }

        us_infantry = {
            'M1A1 THOMPSON': 0,
            'M3 GREASE GUN': 0,
            'M1 GARAND': 0,
            'M1 CARBINE': 0,
            'M1918A2 BAR': 0,
            'M97 TRENCH GUN': 0,
            'BROWNING M1919': 0,
            'M1903 SPRINGFIELD': 0,
            'COLT M1911': 0,
            'M2 FLAMETHROWER': 0,
            'M3 KNIFE': 0,
            'MK2 GRENADE': 0,
            'M2 AP MINE': 0,
            'BAZOOKA': 0,
            '57MM CANNON [M1 57mm]': 0,
            'M3 Half-track': 0,
            'M2 Browning [M3 Half-track]': 0,
            'GMC CCKW 353 (Transport)': 0,
            'GMC CCKW 353 (Supply)': 0,
            'Jeep Willys': 0,
        }

        us_infantry_players = {
            'M1A1 THOMPSON': 0,
            'M3 GREASE GUN': 0,
            'M1 GARAND': 0,
            'M1 CARBINE': 0,
            'M1918A2 BAR': 0,
            'M97 TRENCH GUN': 0,
            'BROWNING M1919': 0,
            'M1903 SPRINGFIELD': 0,
            'COLT M1911': 0,
            'M2 FLAMETHROWER': 0,
            'M3 KNIFE': 0,
            'MK2 GRENADE': 0,
            'M2 AP MINE': 0,
            'BAZOOKA': 0,
            '57MM CANNON [M1 57mm]': 0,
            'M3 Half-track': 0,
            'M2 Browning [M3 Half-track]': 0,
            'GMC CCKW 353 (Transport)': 0,
            'GMC CCKW 353 (Supply)': 0,
            'Jeep Willys': 0,
        }

        us_arty = {
            '155MM HOWITZER [M114]': 0,
        }

        us_arty_player = {
            '155MM HOWITZER [M114]': 0,
        }

        us_armour = {
            'M8 Greyhound': 0,
            'M6 37mm [M8 Greyhound]': 0,
            'COAXIAL M1919 [M8 Greyhound]': 0,
            'Stuart M5A1': 0,
            '37MM CANNON [Stuart M5A1]': 0,
            'COAXIAL M1919 [Stuart M5A1]': 0,
            'HULL M1919 [Stuart M5A1]': 0,
            'Sherman M4A3(75)W': 0,
            '75MM CANNON [Sherman M4A3(75)W]': 0,
            'COAXIAL M1919 [Sherman M4A3(75)W]': 0,
            'HULL M1919 [Sherman M4A3(75)W]': 0,
            'Sherman M4A3E2': 0,
            '75MM M3 GUN [Sherman M4A3E2]': 0,
            'COAXIAL M1919 [Sherman M4A3E2]': 0,
            'HULL M1919 [Sherman M4A3E2]': 0,
            'Sherman M4A3E2(76)': 0,
            '76MM M1 GUN [Sherman M4A3E2(76)]': 0,
            'COAXIAL M1919 [Sherman M4A3E2(76)]': 0,
            'HULL M1919 [Sherman M4A3E2(76)]': 0,
        }

        us_armour_players = {
            'M8 Greyhound': 0,
            'M6 37mm [M8 Greyhound]': 0,
            'COAXIAL M1919 [M8 Greyhound]': 0,
            'Stuart M5A1': 0,
            '37MM CANNON [Stuart M5A1]': 0,
            'COAXIAL M1919 [Stuart M5A1]': 0,
            'HULL M1919 [Stuart M5A1]': 0,
            'Sherman M4A3(75)W': 0,
            '75MM CANNON [Sherman M4A3(75)W]': 0,
            'COAXIAL M1919 [Sherman M4A3(75)W]': 0,
            'HULL M1919 [Sherman M4A3(75)W]': 0,
            'Sherman M4A3E2': 0,
            '75MM M3 GUN [Sherman M4A3E2]': 0,
            'COAXIAL M1919 [Sherman M4A3E2]': 0,
            'HULL M1919 [Sherman M4A3E2]': 0,
            'Sherman M4A3E2(76)': 0,
            '76MM M1 GUN [Sherman M4A3E2(76)]': 0,
            'COAXIAL M1919 [Sherman M4A3E2(76)]': 0,
            'HULL M1919 [Sherman M4A3E2(76)]': 0,
        }

        ger_infantry = {
            'MP40': 0,
            'GEWEHR 43': 0,
            'KARABINER 98K': 0,
            'STG44': 0,
            'FG42': 0,
            'MG34': 0,
            'MG42': 0,
            'KARABINER 98K x8': 0,
            'FG42 x4': 0,
            'WALTHER P38': 0,
            'LUGER P08': 0,
            'FLAMMENWERFER 41': 0,
            'FELDSPATEN': 0,
            'M24 STIELHANDGRANATE': 0,
            'M43 STIELHANDGRANATE': 0,
            'S-MINE': 0,
            'TELLERMINE 43': 0,
            'PANZERSCHRECK': 0,
            '75MM CANNON [PAK 40]': 0,
            'Sd.Kfz 251 Half-track': 0,
            'MG 42 [Sd.Kfz 251 Half-track]': 0,
            'Opel Blitz (Transport)': 0,
            'Opel Blitz (Supply)': 0,
            'Kubelwagen': 0,
        }

        ger_infantry_players = {
            'MP40': 0,
            'GEWEHR 43': 0,
            'KARABINER 98K': 0,
            'STG44': 0,
            'FG42': 0,
            'MG34': 0,
            'MG42': 0,
            'KARABINER 98K x8': 0,
            'FG42 x4': 0,
            'WALTHER P38': 0,
            'LUGER P08': 0,
            'FLAMMENWERFER 41': 0,
            'FELDSPATEN': 0,
            'M24 STIELHANDGRANATE': 0,
            'M43 STIELHANDGRANATE': 0,
            'S-MINE': 0,
            'TELLERMINE 43': 0,
            'PANZERSCHRECK': 0,
            '75MM CANNON [PAK 40]': 0,
            'Sd.Kfz 251 Half-track': 0,
            'MG 42 [Sd.Kfz 251 Half-track]': 0,
            'Opel Blitz (Transport)': 0,
            'Opel Blitz (Supply)': 0,
            'Kubelwagen': 0,
        }

        ger_arty = {
            '150MM HOWITZER [sFH 18]': 0,
        }

        ger_arty_player = {
            '150MM HOWITZER [sFH 18]': 0,
        }

        ger_armour = {
            'Sd.Kfz.234 Puma': 0,
            '50mm KwK 39/1 [Sd.Kfz.234 Puma]': 0,
            'COAXIAL MG34 [Sd.Kfz.234 Puma]': 0,
            'Sd.Kfz.121 Luchs': 0,
            '20MM KWK 30 [Sd.Kfz.121 Luchs]': 0,
            'COAXIAL MG34 [Sd.Kfz.121 Luchs]': 0,
            'Sd.Kfz.161 Panzer IV': 0,
            '75MM CANNON [Sd.Kfz.161 Panzer IV]': 0,
            'COAXIAL MG34 [Sd.Kfz.161 Panzer IV]': 0,
            'HULL MG34 [Sd.Kfz.161 Panzer IV]': 0,
            'Sd.Kfz.181 Tiger 1': 0,
            '88 KWK 36 L/56 [Sd.Kfz.181 Tiger 1]': 0,
            'COAXIAL MG34 [Sd.Kfz.181 Tiger 1]': 0,
            'HULL MG34 [Sd.Kfz.181 Tiger 1]': 0,
            'Sd.Kfz.171 Panther': 0,
            '75MM CANNON [Sd.Kfz.171 Panther]': 0,
            'COAXIAL MG34 [Sd.Kfz.171 Panther]': 0,
            'HULL MG34 [Sd.Kfz.171 Panther]': 0,
        }

        ger_armour_players = {
            'M8 Greyhound': 0,
            'M6 37mm [M8 Greyhound]': 0,
            'COAXIAL M1919 [M8 Greyhound]': 0,
            'Stuart M5A1': 0,
            '37MM CANNON [Stuart M5A1]': 0,
            'COAXIAL M1919 [Stuart M5A1]': 0,
            'HULL M1919 [Stuart M5A1]': 0,
            'Sherman M4A3(75)W': 0,
            '75MM CANNON [Sherman M4A3(75)W]': 0,
            'COAXIAL M1919 [Sherman M4A3(75)W]': 0,
            'HULL M1919 [Sherman M4A3(75)W]': 0,
            'Sherman M4A3E2': 0,
            '75MM M3 GUN [Sherman M4A3E2]': 0,
            'COAXIAL M1919 [Sherman M4A3E2]': 0,
            'HULL M1919 [Sherman M4A3E2]': 0,
            'Sherman M4A3E2(76)': 0,
            '76MM M1 GUN [Sherman M4A3E2(76)]': 0,
            'COAXIAL M1919 [Sherman M4A3E2(76)]': 0,
            'HULL M1919 [Sherman M4A3E2(76)]': 0,
        }

        rus_infantry = {
            'PPSH 41': 0,
            'PPSH 41 W/DRUM': 0,
            'SVT40': 0,
            'MOSIN NAGANT 1891': 0,
            'MOSIN NAGANT 91/30': 0,
            'MOSIN NAGANT M38': 0,
            'DP-27': 0,
            'SCOPED MOSIN NAGANT 91/30': 0,
            'SCOPED SVT40': 0,
            'NAGANT M1895': 0,
            'TOKAREV TT33': 0,
            'MPL-50 SPADE': 0,
            'RG-42 GRENADE': 0,
            'MOLOTOV': 0,
            'POMZ AP MINE': 0,
            'TM-35 AT MINE': 0,
            'PTRS-41': 0,
            '57MM CANNON [ZiS-2]': 0,
            'ZIS-5 (Transport)': 0,
            'ZIS-5 (Supply)': 0,
            'GAZ-67': 0,
        }

        rus_infantry_players = {
            'PPSH 41': 0,
            'PPSH 41 W/DRUM': 0,
            'SVT40': 0,
            'MOSIN NAGANT 1891': 0,
            'MOSIN NAGANT 91/30': 0,
            'MOSIN NAGANT M38': 0,
            'DP-27': 0,
            'SCOPED MOSIN NAGANT 91/30': 0,
            'SCOPED SVT40': 0,
            'NAGANT M1895': 0,
            'TOKAREV TT33': 0,
            'MPL-50 SPADE': 0,
            'RG-42 GRENADE': 0,
            'MOLOTOV': 0,
            'POMZ AP MINE': 0,
            'TM-35 AT MINE': 0,
            'PTRS-41': 0,
            '57MM CANNON [ZiS-2]': 0,
            'ZIS-5 (Transport)': 0,
            'ZIS-5 (Supply)': 0,
            'GAZ-67': 0,
        }

        rus_arty = {
            '122MM HOWITZER [M1938 (M-30)]': 0,
        }

        rus_arty_player = {
            '122MM HOWITZER [M1938 (M-30)]': 0,
        }

        rus_armour = {
            'BA-10': 0,
            '19-K 45MM [BA-10]': 0,
            'COAXIAL DT [BA-10]': 0,
            'T70': 0,
            '45MM M1937 [T70]': 0,
            'COAXIAL DT [T70]': 0,
            'T34/76': 0,
            '76MM ZiS-5 [T34/76]': 0,
            'COAXIAL DT [T34/76]': 0,
            'HULL DT [T34/76]': 0,
            'IS-1': 0,
            'D-5T 85MM [IS-1]': 0,
            'COAXIAL DT [IS-1]': 0,
            'HULL DT [IS-1]': 0,
        }

        rus_armour_players = {
            'BA-10': 0,
            '19-K 45MM [BA-10]': 0,
            'COAXIAL DT [BA-10]': 0,
            'T70': 0,
            '45MM M1937 [T70]': 0,
            'COAXIAL DT [T70]': 0,
            'T34/76': 0,
            '76MM ZiS-5 [T34/76]': 0,
            'COAXIAL DT [T34/76]': 0,
            'HULL DT [T34/76]': 0,
            'IS-1': 0,
            'D-5T 85MM [IS-1]': 0,
            'COAXIAL DT [IS-1]': 0,
            'HULL DT [IS-1]': 0,
        }

        gb_infantry = {
            'Sten Gun Mk.II': 0,
            'Sten Gun Mk.V': 0,
            'Lanchester': 0,
            'M1928A1 THOMPSON': 0,
            'SMLE No.1 Mk III': 0,
            'Rifle No.4 Mk I': 0,
            'Rifle No.5 Mk I': 0,
            'Bren Gun': 0,
            'Lewis Gun': 0,
            'Lee-Enfield Pattern 1914 Sniper': 0,
            'Rifle No.4 Mk I Sniper': 0,
            'Webley MK VI': 0,
            'FLAMETHROWER': 0,
            'Fairbairn–Sykes': 0,
            'Mills Bomb': 0,
            'No.82 Grenade': 0,
            'A.P. Shrapnel Mine Mk II': 0,
            'A.T. Mine G.S. Mk V': 0,
            'PIAT': 0,
            'Boys Anti-tank Rifle': 0,
            'QF 6-POUNDER [QF 6-Pounder]': 0,
            'Bedford OYD (Transport)': 0,
            'Bedford OYD (Supply)': 0,
        }

        gb_infantry_players = {
            'Sten Gun Mk.II': 0,
            'Sten Gun Mk.V': 0,
            'Lanchester': 0,
            'M1928A1 THOMPSON': 0,
            'SMLE No.1 Mk III': 0,
            'Rifle No.4 Mk I': 0,
            'Rifle No.5 Mk I': 0,
            'Bren Gun': 0,
            'Lewis Gun': 0,
            'Lee-Enfield Pattern 1914 Sniper': 0,
            'Rifle No.4 Mk I Sniper': 0,
            'Webley MK VI': 0,
            'FLAMETHROWER': 0,
            'Fairbairn–Sykes': 0,
            'Mills Bomb': 0,
            'No.82 Grenade': 0,
            'A.P. Shrapnel Mine Mk II': 0,
            'A.T. Mine G.S. Mk V': 0,
            'PIAT': 0,
            'Boys Anti-tank Rifle': 0,
            'QF 6-POUNDER [QF 6-Pounder]': 0,
            'Bedford OYD (Transport)': 0,
            'Bedford OYD (Supply)': 0,
        }

        gb_arty = {
            'QF 25-POUNDER [QF 25-Pounder]': 0,
        }

        gb_arty_player = {
            'QF 25-POUNDER [QF 25-Pounder]': 0,
        }

        gb_armour = {
            'Daimler': 0,
            'QF 2-POUNDER [Daimler]': 0,
            'COAXIAL BESA [Daimler]': 0,
            'Tetrarch': 0,
            'QF 2-POUNDER [Tetrarch]': 0,
            'COAXIAL BESA [Tetrarch]': 0,
            'M3 Stuart Honey': 0,
            '37MM CANNON [M3 Stuart Honey]': 0,
            'COAXIAL M1919 [M3 Stuart Honey]': 0,
            'HULL M1919 [M3 Stuart Honey]': 0,
            'Cromwell': 0,
            'QF 75MM [Cromwell]': 0,
            'COAXIAL BESA [Cromwell]': 0,
            'HULL BESA [Cromwell]': 0,
            'Crusader Mk.III': 0,
            'OQF 57MM [Crusader Mk.III]': 0,
            'COAXIAL BESA [Crusader Mk.III]': 0,
            'Firefly': 0,
            'QF 17-POUNDER [Firefly]': 0,
            'COAXIAL M1919 [Firefly]': 0,
            'Churchill Mk.III': 0,
            'OQF 57MM [Churchill Mk.III]': 0,
            'COAXIAL BESA 7.92mm [Churchill Mk.III]': 0,
            'HULL BESA 7.92mm [Churchill Mk.III]': 0,
            'Churchill Mk.VII': 0,
            'OQF 57MM [Churchill Mk.VII]': 0,
            'COAXIAL BESA 7.92mm [Churchill Mk.VII]': 0,
            'HULL BESA 7.92mm [Churchill Mk.VII]': 0,
        }

        gb_armour_players = {
            'Daimler': 0,
            'QF 2-POUNDER [Daimler]': 0,
            'COAXIAL BESA [Daimler]': 0,
            'Tetrarch': 0,
            'QF 2-POUNDER [Tetrarch]': 0,
            'COAXIAL BESA [Tetrarch]': 0,
            'M3 Stuart Honey': 0,
            '37MM CANNON [M3 Stuart Honey]': 0,
            'COAXIAL M1919 [M3 Stuart Honey]': 0,
            'HULL M1919 [M3 Stuart Honey]': 0,
            'Cromwell': 0,
            'QF 75MM [Cromwell]': 0,
            'COAXIAL BESA [Cromwell]': 0,
            'HULL BESA [Cromwell]': 0,
            'Crusader Mk.III': 0,
            'OQF 57MM [Crusader Mk.III]': 0,
            'COAXIAL BESA [Crusader Mk.III]': 0,
            'Firefly': 0,
            'QF 17-POUNDER [Firefly]': 0,
            'COAXIAL M1919 [Firefly]': 0,
            'Churchill Mk.III': 0,
            'OQF 57MM [Churchill Mk.III]': 0,
            'COAXIAL BESA 7.92mm [Churchill Mk.III]': 0,
            'HULL BESA 7.92mm [Churchill Mk.III]': 0,
            'Churchill Mk.VII': 0,
            'OQF 57MM [Churchill Mk.VII]': 0,
            'COAXIAL BESA 7.92mm [Churchill Mk.VII]': 0,
            'HULL BESA 7.92mm [Churchill Mk.VII]': 0,
        }

        for player in players:
            data = dict([
                ('steam_64', player.steam_id_64),
                ('match_id', player.match_id),
                ('creation_time', player.creation_time),
                ('name', player.player),
                ('kills', player.kills),
                ('deaths', player.deaths),
                ('kills_streak', player.kills_streak),
                ('deaths_without_kill_streak', player.deaths_without_kill_streak),
                ('teamkills', player.teamkills),
                ('teamkills_streak', player.teamkills_streak),
                ('deaths_by_tk', player.deaths_by_tk),
                ('deaths_by_tk_streak', player.deaths_by_tk_streak),
                ('nb_vote_started', player.nb_vote_started),
                ('nb_voted_yes', player.nb_voted_yes),
                ('nb_voted_no', player.nb_voted_no),
                ('time_seconds', player.time_seconds),
                ('kills_per_minute', player.kills_per_minute),
                ('deaths_per_minute', player.deaths_per_minute),
                ('kill_death_ratio', player.kill_death_ratio),
                ('longest_life_secs', player.longest_life_secs),
                ('shortest_life_secs', player.shortest_life_secs),
                ('combat', player.combat),
                ('offense', player.offense),
                ('defense', player.defense),
                ('support', player.support),
            ])

            for k, v in stat_items.items():
                if data[k] > v:
                    stat_players[k] = data
                    stat_items[k] = data[k]
            
        for weapon in weapons:
            data = dict([
                ('weaponkill_id', weapon.weaponkill_id),
                ('player_name', weapon.player_name),
                ('player_id', weapon.player_id),
                ('steam_id_64', weapon.steam_id_64),
                ('match_id', weapon.match_id),
                ('match_time', weapon.match_time),
                ('weapon', weapon.weapon),
                ('kills', weapon.kills),
            ])

            for k, v in us_infantry.items():
                if (weapon.weapon == k and weapon.kills > v):
                    us_infantry_players[k] = data
                    us_infantry[k] = weapon.kills

            for k, v in us_arty.items():
                if (weapon.weapon == k and weapon.kills > v):
                    us_arty_player[k] = data
                    us_arty[k] = weapon.kills

            for k, v in us_armour.items():
                if (weapon.weapon == k and weapon.kills > v):
                    us_armour_players[k] = data
                    us_armour[k] = weapon.kills

            for k, v in ger_infantry.items():
                if (weapon.weapon == k and weapon.kills > v):
                    ger_infantry_players[k] = data
                    ger_infantry[k] = weapon.kills

            for k, v in ger_arty.items():
                if (weapon.weapon == k and weapon.kills > v):
                    ger_arty_player[k] = data
                    ger_arty[k] = weapon.kills

            for k, v in ger_armour.items():
                if (weapon.weapon == k and weapon.kills > v):
                    ger_armour_players[k] = data
                    ger_armour[k] = weapon.kills

            for k, v in rus_infantry.items():
                if (weapon.weapon == k and weapon.kills > v):
                    rus_infantry_players[k] = data
                    rus_infantry[k] = weapon.kills

            for k, v in rus_arty.items():
                if (weapon.weapon == k and weapon.kills > v):
                    rus_arty_player[k] = data
                    rus_arty[k] = weapon.kills

            for k, v in rus_armour.items():
                if (weapon.weapon == k and weapon.kills > v):
                    rus_armour_players[k] = data
                    rus_armour[k] = weapon.kills

            for k, v in gb_infantry.items():
                if (weapon.weapon == k and weapon.kills > v):
                    gb_infantry_players[k] = data
                    gb_infantry[k] = weapon.kills

            for k, v in gb_arty.items():
                if (weapon.weapon == k and weapon.kills > v):
                    gb_arty_player[k] = data
                    gb_arty[k] = weapon.kills

            for k, v in gb_armour.items():
                if (weapon.weapon == k and weapon.kills > v):
                    gb_armour_players[k] = data
                    gb_armour[k] = weapon.kills

        ret_data['stats'] = stat_players
        ret_data['us_infantry'] = us_infantry_players
        ret_data['us_arty'] = us_arty_player
        ret_data['us_armour'] = us_armour_players
        ret_data['ger_infantry'] = ger_infantry_players
        ret_data['ger_arty'] = ger_arty_player
        ret_data['ger_armour'] = ger_armour_players
        ret_data['rus_infantry'] = rus_infantry_players
        ret_data['rus_arty'] = rus_arty_player
        ret_data['rus_armour'] = rus_armour_players
        ret_data['gb_infantry'] = gb_infantry_players
        ret_data['gb_arty'] = gb_arty_player
        ret_data['gb_armour'] = gb_armour_players
        return ret_data


    def top_killers(self):
        players = get_top_killers()
        ret_players = []

        for player in players:
            data = dict([
                ('steam_64', player.steam_id_64),
                ('name', player.player),
                ('kills', player.kills),
            ])
            ret_players.append(data)

        return ret_players


    def killers_club(self, kill_count):
        players = get_player_kill_count(kill_count)
        dict_name = f'{kill_count}_kills'
        ret_players = {dict_name: []}

        for player in players:
            data = dict([
                ('steam_64', player.steam_id_64),
                ('match_id', player.match_id),
                ('creation_time', player.creation_time),
                ('name', player.player),
                ('kills', player.kills),
                ('deaths', player.deaths),
                ('kill_streak', player.kills_streak),
                ('deaths_without_kill_streak', player.deaths_without_kill_streak),
                ('teamkills', player.teamkills),
                ('teamkills_streak', player.teamkills_streak),
                ('deaths_by_tk', player.deaths_by_tk),
                ('deaths_by_tk_streak', player.deaths_by_tk_streak),
                ('nb_vote_started', player.nb_vote_started),
                ('nb_voted_yes', player.nb_voted_yes),
                ('nb_voted_no', player.nb_voted_no),
                ('time_seconds', player.time_seconds),
                ('kills_per_minute', player.kills_per_minute),
                ('deaths_per_minute', player.deaths_per_minute),
                ('kill_death_ratio', player.kill_death_ratio),
                ('longest_life_secs', player.longest_life_secs),
                ('shortest_life_secs', player.shortest_life_secs),
                ('combat', player.combat),
                ('offense', player.offense),
                ('defense', player.defense),
                ('support', player.support),
            ])
            ret_players[dict_name].append(data)

        return ret_players


    def top_killers_cumulative(self):
        players = get_player_kills()
        data_players = {}

        for player in players:
            if player.steam_id_64 in data_players:
                data_players[player.steam_id_64]['kills'] += player.kills
                data_players[player.steam_id_64]['name'] = player.player

            if player.steam_id_64 not in data_players:
                data_players[player.steam_id_64] = {}
                data_players[player.steam_id_64]['kills'] = player.kills
                data_players[player.steam_id_64]['name'] = player.player

        players_sorted = {key: val for key, val in sorted(data_players.items(), key = lambda ele: ele[1]['kills'], reverse = True)}

        ret_players = []
        for k, v in players_sorted.items():
            data = dict([
                ('position', int(len(ret_players) + 1)),
                ('steam_64', k),
                ('name', v['name']),
                ('kills', v['kills']),
            ])
            if (len(ret_players) >= 200):
                break
            else:
                ret_players.append(data)

        return ret_players


    def top_killers_cumulative_week(self):
        players = get_player_kills_week()
        data_players = {}

        for player in players:
            if player.steam_id_64 in data_players:
                data_players[player.steam_id_64]['kills'] += player.kills
                data_players[player.steam_id_64]['name'] = player.player

            if player.steam_id_64 not in data_players:
                data_players[player.steam_id_64] = {}
                data_players[player.steam_id_64]['kills'] = player.kills
                data_players[player.steam_id_64]['name'] = player.player

        players_sorted = {key: val for key, val in sorted(data_players.items(), key = lambda ele: ele[1]['kills'], reverse = True)}

        ret_players = []
        for k, v in players_sorted.items():
            data = dict([
                ('position', int(len(ret_players) + 1)),
                ('steam_64', k),
                ('name', v['name']),
                ('kills', v['kills']),
            ])
            if (len(ret_players) >= 200):
                break
            else:
                ret_players.append(data)

        return ret_players


    def week_top_killers(self):
        players = get_top_week_killers()
        ret_players = []

        for player in players:
        	data = dict([
        		('steam_64', player.steam_id_64),
        		('name', player.player),
        		('kills', player.kills),
        	])
        	ret_players.append(data)

        return ret_players


    def get_player_by_steam64(self, steam_64):
        players = get_player_by_steam64(steam_64)
        ret_players = []

        for player in players:
            data = dict([
                ('steam_64', player.steam_id_64),
                ('match_id', player.match_id),
                ('creation_time', player.creation_time),
                ('name', player.player),
                ('kills', player.kills),
                ('deaths', player.deaths),
                ('kill_streak', player.kills_streak),
                ('deaths_without_kill_streak', player.deaths_without_kill_streak),
                ('teamkills', player.teamkills),
                ('teamkills_streak', player.teamkills_streak),
                ('deaths_by_tk', player.deaths_by_tk),
                ('deaths_by_tk_streak', player.deaths_by_tk_streak),
                ('nb_vote_started', player.nb_vote_started),
                ('nb_voted_yes', player.nb_voted_yes),
                ('nb_voted_no', player.nb_voted_no),
                ('time_seconds', player.time_seconds),
                ('kills_per_minute', player.kills_per_minute),
                ('deaths_per_minute', player.deaths_per_minute),
                ('kill_death_ratio', player.kill_death_ratio),
                ('longest_life_secs', player.longest_life_secs),
                ('shortest_life_secs', player.shortest_life_secs),
                ('combat', player.combat),
                ('offense', player.offense),
                ('defense', player.defense),
                ('support', player.support),
            ])
            ret_players.append(data)

        return ret_players


    def get_top_weapons_by_player(self):
        weapons = get_top_weapons_by_player()
        weapons_data = {}

        for weapon in weapons:
            if ((weapon.weapon in weapons_data) and (weapon.kills >= weapons_data[weapon.weapon]['kills'])):
                weapons_data[weapon.weapon] = dict([
                    ('steam_64', weapon.steam_id_64),
                    ('player_name', weapon.player_name),
                    ('match_id', weapon.match_id),
                    ('match_time', weapon.match_time),
                    ('kills', weapon.kills),
                ])

            if weapon.weapon not in weapons_data:
                weapons_data[weapon.weapon] = dict([
                    ('steam_64', weapon.steam_id_64),
                    ('player_name', weapon.player_name),
                    ('match_id', weapon.match_id),
                    ('match_time', weapon.match_time),
                    ('kills', weapon.kills),
                ])

        weapons_sorted = {key: val for key, val in sorted(weapons_data.items(), key = lambda ele: ele[1]['kills'], reverse = True)}
        return weapons_sorted
