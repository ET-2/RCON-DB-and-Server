from alchemy.database import (
    get_player_by_steam64,
    get_player_stats_by_steam64,
    get_db_weapon_stats_by_steam64,
    get_player_kills_by_steam64,
    get_player_name_by_steam64,
    get_top_killers,
    get_top_week_killers,
    get_player_kills,
    get_player_kills_week,
    get_top_weapons_by_player,
    get_player_kill_count,
    get_players,
    get_coletrain,
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


    def short_stats(self):
        players = get_players()
        weapons_data = get_top_weapons_by_player()
        ret_data = {}

        infantry = {
            'kills': {'name': '', 'value': 0},
            'deaths': {'name': '', 'value': 0},
            'kills_streak': {'name': '', 'value': 0},
            'kills_per_minute': {'name': '', 'value': 0},
            'combat': {'name': '', 'value': 0},
            'offense': {'name': '', 'value': 0},
            'defense': {'name': '', 'value': 0},
            'support': {'name': '', 'value': 0},
        }

        weapons = {
            'at_gun': {'name': '', 'value': 0},
            'grenade': {'name': '', 'value': 0},
            'molotov': {'name': '', 'value': 0},
            'satchel': {'name': '', 'value': 0},
            'melee': {'name': '', 'value': 0},
            'mine': {'name': '', 'value': 0},
            'roadkills': {'name': '', 'value': 0},
        }

        at_gun = [
            '57MM CANNON [M1 57mm]',
            '75MM CANNON [PAK 40]',
            '57MM CANNON [ZiS-2]',
            'QF 6-POUNDER [QF 6-Pounder]',
        ]

        grenade = [
            'MK2 GRENADE',
            'M43 STIELHANDGRANATE',
            'RG-42 GRENADE',
            'Mills Bomb',
            'No.82 Grenade',
        ]

        satchel = [
            'SATCHEL',
            'SATCHEL CHARGE',
        ]

        melee = [
            'M3 KNIFE',
            'FELDSPATEN',
            'MPL-50 SPADE',
            'Fairbairn–Sykes',
        ]

        mine = [
            'M2 AP MINE',
            'M1A1 AT MINE',
            'S-MINE',
            'TELLERMINE 43',
            'POMZ AP MINE',
            'TM-35 AT MINE',
            'A.P. Shrapnel Mine Mk II',
            'A.T. Mine G.S. Mk V',
        ]

        roadkills = [
            'M3 Half-track',
            'GMC CCKW 353 (Transport)',
            'GMC CCKW 353 (Supply)',
            'Jeep Willys',
            'Sd.Kfz 251 Half-track',
            'Opel Blitz (Transport)',
            'Opel Blitz (Supply)',
            'Kubelwagen',
            'ZIS-5 (Transport)',
            'ZIS-5 (Supply)',
            'GAZ-67',
            'Bedford OYD (Transport)',
            'Bedford OYD (Supply)',
        ]

        machine_gun = {
            'BROWNING M1919': {'name': '', 'value': 0},
            'M1918A2 BAR': {'name': '', 'value': 0},
            'MG34': {'name': '', 'value': 0},
            'MG42': {'name': '', 'value': 0},
            'DP-27': {'name': '', 'value': 0},
            'Lewis Gun': {'name': '', 'value': 0},
        }

        armour = {
            'roadkills': {'name': '', 'value': 0},
            'gunner_primary': {'name': '', 'value': 0},
            'gunner_secondary': {'name': '', 'value': 0},
            'driver_hull': {'name': '', 'value': 0},
        }

        armour_roadkills = [
            'M8 Greyhound',
            'Stuart M5A1',
            'Sherman M4A3(75)W',
            'Sherman M4A3E2',
            'Sherman M4A3E2(76)',
            'Sd.Kfz.234 Puma',
            'Sd.Kfz.121 Luchs',
            'Sd.Kfz.161 Panzer IV',
            'Sd.Kfz.181 Tiger 1',
            'Sd.Kfz.171 Panther',
            'BA-10',
            'T70',
            'T34/76',
            'IS-1',
            'Daimler',
            'Tetrarch',
            'M3 Stuart Honey',
            'Cromwell',
            'Crusader Mk.III',
            'Firefly',
            'Churchill Mk.III',
            'Churchill Mk.VII',
        ]

        armour_gunner_primary = [
            'M6 37mm [M8 Greyhound]',
            '37MM CANNON [Stuart M5A1]',
            '75MM CANNON [Sherman M4A3(75)W]',
            '75MM M3 GUN [Sherman M4A3E2]',
            '76MM M1 GUN [Sherman M4A3E2(76)]',
            '50mm KwK 39/1 [Sd.Kfz.234 Puma]',
            '20MM KWK 30 [Sd.Kfz.121 Luchs]',
            '75MM CANNON [Sd.Kfz.161 Panzer IV]',
            '88 KWK 36 L/56 [Sd.Kfz.181 Tiger 1]',
            '75MM CANNON [Sd.Kfz.171 Panther]',
            '19-K 45MM [BA-10]',
            '45MM M1937 [T70]',
            '76MM ZiS-5 [T34/76]',
            'D-5T 85MM [IS-1]',
            'QF 2-POUNDER [Daimler]',
            'QF 2-POUNDER [Tetrarch]',
            '37MM CANNON [M3 Stuart Honey]',
            'QF 75MM [Cromwell]',
            'OQF 57MM [Crusader Mk.III]',
            'QF 17-POUNDER [Firefly]',
            'OQF 57MM [Churchill Mk.III]',
            'OQF 57MM [Churchill Mk.VII]',
        ]

        armour_gunner_secondary = [
            'COAXIAL M1919 [M8 Greyhound]',
            'COAXIAL M1919 [Stuart M5A1]',
            'COAXIAL M1919 [Sherman M4A3(75)W]',
            'COAXIAL M1919 [Sherman M4A3E2]',
            'COAXIAL M1919 [Sherman M4A3E2(76)]'
            'COAXIAL MG34 [Sd.Kfz.234 Puma]',
            'COAXIAL MG34 [Sd.Kfz.121 Luchs]',
            'COAXIAL MG34 [Sd.Kfz.161 Panzer IV]',
            'COAXIAL MG34 [Sd.Kfz.181 Tiger 1]',
            'COAXIAL MG34 [Sd.Kfz.171 Panther]',
            'COAXIAL DT [BA-10]',
            'COAXIAL DT [T70]',
            'COAXIAL DT [T34/76]',
            'COAXIAL DT [IS-1]',
            'COAXIAL BESA [Daimler]',
            'COAXIAL BESA [Tetrarch]',
            'COAXIAL M1919 [M3 Stuart Honey]',
            'COAXIAL BESA [Cromwell]',
            'COAXIAL BESA [Crusader Mk.III]',
            'COAXIAL M1919 [Firefly]',
            'COAXIAL BESA 7.92mm [Churchill Mk.III]',
            'COAXIAL BESA 7.92mm [Churchill Mk.VII]'
        ]

        armour_driver_hull = [
            'HULL M1919 [Stuart M5A1]',
            'HULL M1919 [Sherman M4A3(75)W]',
            'HULL M1919 [Sherman M4A3E2]',
            'HULL M1919 [Sherman M4A3E2(76)]',
            'HULL MG34 [Sd.Kfz.161 Panzer IV]',
            'HULL MG34 [Sd.Kfz.181 Tiger 1]',
            'HULL MG34 [Sd.Kfz.171 Panther]',
            'HULL DT [T34/76]',
            'HULL DT [IS-1]',
            'HULL M1919 [M3 Stuart Honey]',
            'HULL BESA [Cromwell]',
            'HULL BESA 7.92mm [Churchill Mk.III]',
            'HULL BESA 7.92mm [Churchill Mk.VII]',
        ]

        artillery = {
            '155MM HOWITZER [M114]': {'name': '', 'value': 0},
            '150MM HOWITZER [sFH 18]': {'name': '', 'value': 0},
            '122MM HOWITZER [M1938 (M-30)]': {'name': '', 'value': 0},
            'QF 25-POUNDER [QF 25-Pounder]': {'name': '', 'value': 0},
        }

        club = {
            '100_club': [],
            '200_club': [],
            '300_club': [],
        }

        for player in players:
            if player.kills > infantry['kills']['value']:
                infantry['kills']['value'] = player.kills
                infantry['kills']['name'] = player.player
            if player.deaths > infantry['deaths']['value']:
                infantry['deaths']['value'] = player.deaths
                infantry['deaths']['name'] = player.player
            if player.kills_streak > infantry['kills_streak']['value']:
                infantry['kills_streak']['value'] = player.kills_streak
                infantry['kills_streak']['name'] = player.player
            if player.kills_per_minute > infantry['kills_per_minute']['value']:
                infantry['kills_per_minute']['value'] = player.kills_per_minute
                infantry['kills_per_minute']['name'] = player.player
            if player.combat > infantry['combat']['value']:
                infantry['combat']['value'] = player.combat
                infantry['combat']['name'] = player.player
            if player.offense > infantry['offense']['value']:
                infantry['offense']['value'] = player.offense
                infantry['offense']['name'] = player.player
            if player.defense > infantry['defense']['value']:
                infantry['defense']['value'] = player.defense
                infantry['defense']['name'] = player.player
            if player.support > infantry['support']['value']:
                infantry['support']['value'] = player.support
                infantry['support']['name'] = player.player
            if (player.kills >= 100 and player.kills < 200):
                club['100_club'].append({'name': player.player, 'value': player.kills})
            if (player.kills >= 200 and player.kills < 300):
                club['200_club'].append({'name': player.player, 'value': player.kills})
            if (player.kills >= 300):
                club['300_club'].append({'name': player.player, 'value': player.kills})

        for weapon in weapons_data:
            if (weapon.weapon in at_gun and weapon.kills > weapons['at_gun']['value']):
                weapons['at_gun']['value'] = weapon.kills
                weapons['at_gun']['name'] = weapon.player_name
            if (weapon.weapon in grenade and weapon.kills > weapons['grenade']['value']):
                weapons['grenade']['value'] = weapon.kills
                weapons['grenade']['name'] = weapon.player_name
            if (weapon.weapon == 'MOLOTOV' and weapon.kills > weapons['molotov']['value']):
                weapons['molotov']['value'] = weapon.kills
                weapons['molotov']['name'] = weapon.player_name
            if (weapon.weapon in satchel and weapon.kills > weapons['satchel']['value']):
                weapons['satchel']['value'] = weapon.kills
                weapons['satchel']['name'] = weapon.player_name
            if (weapon.weapon in melee and weapon.kills > weapons['melee']['value']):
                weapons['melee']['value'] = weapon.kills
                weapons['melee']['name'] = weapon.player_name
            if (weapon.weapon in mine and weapon.kills > weapons['mine']['value']):
                weapons['mine']['value'] = weapon.kills
                weapons['mine']['name'] = weapon.player_name
            if (weapon.weapon in roadkills and weapon.kills > weapons['roadkills']['value']):
                weapons['roadkills']['value'] = weapon.kills
                weapons['roadkills']['name'] = weapon.player_name
            if (weapon.weapon in machine_gun.keys() and weapon.kills > machine_gun[weapon.weapon]['value']):
                machine_gun[weapon.weapon]['value'] = weapon.kills
                machine_gun[weapon.weapon]['name'] = weapon.player_name
            if (weapon.weapon in armour_roadkills and weapon.kills > armour['roadkills']['value']):
                armour['roadkills']['value'] = weapon.kills
                armour['roadkills']['name'] = weapon.player_name
            if (weapon.weapon in armour_gunner_primary and weapon.kills > armour['gunner_primary']['value']):
                armour['gunner_primary']['value'] = weapon.kills
                armour['gunner_primary']['name'] = weapon.player_name
            if (weapon.weapon in armour_gunner_secondary and weapon.kills > armour['gunner_secondary']['value']):
                armour['gunner_secondary']['value'] = weapon.kills
                armour['gunner_secondary']['name'] = weapon.player_name
            if (weapon.weapon in armour_driver_hull and weapon.kills > armour['driver_hull']['value']):
                armour['driver_hull']['value'] = weapon.kills
                armour['driver_hull']['name'] = weapon.player_name
            if (weapon.weapon in artillery.keys() and weapon.kills > artillery[weapon.weapon]['value']):
                artillery[weapon.weapon]['value'] = weapon.kills
                artillery[weapon.weapon]['name'] = weapon.player_name

        ret_data['infantry'] = infantry
        ret_data['weapons'] = weapons
        ret_data['machine_guns'] = machine_gun
        ret_data['armour'] = armour
        ret_data['artillery'] = artillery
        ret_data['clubs'] = club

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


    def get_player_stats_by_steam64(self, steam_64):
        player_data = get_player_stats_by_steam64(steam_64)
        name = None
        ret_player = {
            'steam_64': steam_64,
            'name': 0,
            'total_kills': 0,
            'total_deaths': 0,
            'total_teamkills': 0,
            'deaths_by_tk': 0,
            'votes_started': 0,
            'voted_yes': 0,
            'voted_no': 0,
            'kpm': {'average': 0, 'highest': 0},
            'dpm': {'average': 0, 'highest': 0},
            'kdr': {'average': 0, 'highest': 0, 'overall': 0},
            'combat': {'average': 0, 'highest': 0},
            'offense': {'average': 0, 'highest': 0},
            'defense': {'average': 0, 'highest': 0},
            'support': {'average': 0, 'highest': 0},
        }

        kpm_list = []
        dpm_list = []
        kdr_list = []
        combat_list = []
        offense_list = []
        defense_list = []
        support_list = []

        for player in player_data:
            if name == None:
                name = player.player
            ret_player['total_kills'] += player.kills
            ret_player['total_deaths'] += player.deaths
            ret_player['total_teamkills'] += player.teamkills
            ret_player['deaths_by_tk'] += player.deaths_by_tk
            ret_player['votes_started'] += player.nb_vote_started
            ret_player['voted_yes'] += player.nb_voted_yes
            ret_player['voted_no'] += player.nb_voted_no
            kpm_list.append(player.kills_per_minute)
            dpm_list.append(player.deaths_per_minute)
            kdr_list.append(player.kill_death_ratio)
            combat_list.append(player.combat)
            offense_list.append(player.offense)
            defense_list.append(player.defense)
            support_list.append(player.support)

        ret_player['kpm']['average'] = sum(kpm_list) / len(kpm_list)
        ret_player['kpm']['highest'] = max(kpm_list)
        ret_player['dpm']['average'] = sum(dpm_list) / len(dpm_list)
        ret_player['dpm']['highest'] = max(dpm_list)
        ret_player['kdr']['average'] = sum(kdr_list) / len(kdr_list)
        ret_player['kdr']['highest'] = max(kdr_list)
        ret_player['kdr']['overall'] = ret_player['total_kills'] / ret_player['total_deaths']
        ret_player['combat']['average'] = sum(combat_list) / len(combat_list)
        ret_player['combat']['highest'] = max(combat_list)
        ret_player['offense']['average'] = sum(offense_list) / len(offense_list)
        ret_player['offense']['highest'] = max(offense_list)
        ret_player['defense']['average'] = sum(defense_list) / len(defense_list)
        ret_player['defense']['highest'] = max(defense_list)
        ret_player['support']['average'] = sum(support_list) / len(support_list)
        ret_player['support']['highest'] = max(support_list)
        ret_player['name'] = name

        return ret_player


    def get_weapon_stats_by_steam64(self, steam_64):
        weapons_data = get_db_weapon_stats_by_steam64(steam_64)
        name = get_player_name_by_steam64(steam_64)
        weapons = {
            'name': name,
            'infantry': {
                'M1A1 THOMPSON': {'highest': 0, 'total': 0},
                'M3 GREASE GUN': {'highest': 0, 'total': 0},
                'M1 GARAND': {'highest': 0, 'total': 0},
                'M1 CARBINE': {'highest': 0, 'total': 0},
                'M1918A2 BAR': {'highest': 0, 'total': 0},
                'M97 TRENCH GUN': {'highest': 0, 'total': 0},
                'BROWNING M1919': {'highest': 0, 'total': 0},
                'M1903 SPRINGFIELD': {'highest': 0, 'total': 0},
                'COLT M1911': {'highest': 0, 'total': 0},
                'M2 FLAMETHROWER': {'highest': 0, 'total': 0},
                'M3 KNIFE': {'highest': 0, 'total': 0},
                'MK2 GRENADE': {'highest': 0, 'total': 0},
                'M2 AP MINE': {'highest': 0, 'total': 0},
                'BAZOOKA': {'highest': 0, 'total': 0},
                '57MM CANNON [M1 57mm]': {'highest': 0, 'total': 0},
                'MP40': {'highest': 0, 'total': 0},
                'GEWEHR 43': {'highest': 0, 'total': 0},
                'KARABINER 98K': {'highest': 0, 'total': 0},
                'STG44': {'highest': 0, 'total': 0},
                'FG42': {'highest': 0, 'total': 0},
                'MG34': {'highest': 0, 'total': 0},
                'MG42': {'highest': 0, 'total': 0},
                'KARABINER 98K x8': {'highest': 0, 'total': 0},
                'FG42 x4': {'highest': 0, 'total': 0},
                'WALTHER P38': {'highest': 0, 'total': 0},
                'LUGER P08': {'highest': 0, 'total': 0},
                'FLAMMENWERFER 41': {'highest': 0, 'total': 0},
                'FELDSPATEN': {'highest': 0, 'total': 0},
                'M24 STIELHANDGRANATE': {'highest': 0, 'total': 0},
                'M43 STIELHANDGRANATE': {'highest': 0, 'total': 0},
                'S-MINE': {'highest': 0, 'total': 0},
                'TELLERMINE 43': {'highest': 0, 'total': 0},
                'PANZERSCHRECK': {'highest': 0, 'total': 0},
                '75MM CANNON [PAK 40]': {'highest': 0, 'total': 0},
                'PPSH 41': {'highest': 0, 'total': 0},
                'PPSH 41 W/DRUM': {'highest': 0, 'total': 0},
                'SVT40': {'highest': 0, 'total': 0},
                'MOSIN NAGANT 1891': {'highest': 0, 'total': 0},
                'MOSIN NAGANT 91/30': {'highest': 0, 'total': 0},
                'MOSIN NAGANT M38': {'highest': 0, 'total': 0},
                'DP-27': {'highest': 0, 'total': 0},
                'SCOPED MOSIN NAGANT 91/30': {'highest': 0, 'total': 0},
                'SCOPED SVT40': {'highest': 0, 'total': 0},
                'NAGANT M1895': {'highest': 0, 'total': 0},
                'TOKAREV TT33': {'highest': 0, 'total': 0},
                'MPL-50 SPADE': {'highest': 0, 'total': 0},
                'RG-42 GRENADE': {'highest': 0, 'total': 0},
                'MOLOTOV': {'highest': 0, 'total': 0},
                'POMZ AP MINE': {'highest': 0, 'total': 0},
                'TM-35 AT MINE': {'highest': 0, 'total': 0},
                'PTRS-41': {'highest': 0, 'total': 0},
                '57MM CANNON [ZiS-2]ZIS-5 (Transport)': {'highest': 0, 'total': 0},
                'Sten Gun Mk.II': {'highest': 0, 'total': 0},
                'Sten Gun Mk.V': {'highest': 0, 'total': 0},
                'Lanchester': {'highest': 0, 'total': 0},
                'M1928A1 THOMPSON': {'highest': 0, 'total': 0},
                'SMLE No.1 Mk III': {'highest': 0, 'total': 0},
                'Rifle No.4 Mk I': {'highest': 0, 'total': 0},
                'Rifle No.5 Mk I': {'highest': 0, 'total': 0},
                'Bren Gun': {'highest': 0, 'total': 0},
                'Lewis Gun': {'highest': 0, 'total': 0},
                'Lee-Enfield Pattern 1914 Sniper': {'highest': 0, 'total': 0},
                'Rifle No.4 Mk I Sniper': {'highest': 0, 'total': 0},
                'Webley MK VI': {'highest': 0, 'total': 0},
                'FLAMETHROWER': {'highest': 0, 'total': 0},
                'Fairbairn–Sykes': {'highest': 0, 'total': 0},
                'Mills Bomb': {'highest': 0, 'total': 0},
                'No.82 Grenade': {'highest': 0, 'total': 0},
                'A.P. Shrapnel Mine Mk II': {'highest': 0, 'total': 0},
                'A.T. Mine G.S. Mk V': {'highest': 0, 'total': 0},
                'PIAT': {'highest': 0, 'total': 0},
                'Boys Anti-tank Rifle': {'highest': 0, 'total': 0},
                'QF 6-POUNDER [QF 6-Pounder]': {'highest': 0, 'total': 0},
            },
            'roadkills': {
                'M3 Half-track': {'highest': 0, 'total': 0},
                'GMC CCKW 353 (Transport)': {'highest': 0, 'total': 0},
                'GMC CCKW 353 (Supply)': {'highest': 0, 'total': 0},
                'Jeep Willys': {'highest': 0, 'total': 0},
                'M8 Greyhound': {'highest': 0, 'total': 0},
                'Stuart M5A1': {'highest': 0, 'total': 0},
                'Sherman M4A3(75)W': {'highest': 0, 'total': 0},
                'Sherman M4A3E2': {'highest': 0, 'total': 0},
                'Sherman M4A3E2(76)': {'highest': 0, 'total': 0},
                'Sd.Kfz 251 Half-track': {'highest': 0, 'total': 0},
                'Opel Blitz (Transport)': {'highest': 0, 'total': 0},
                'Opel Blitz (Supply)': {'highest': 0, 'total': 0},
                'Kubelwagen': {'highest': 0, 'total': 0},
                'Sd.Kfz.234 Puma': {'highest': 0, 'total': 0},
                'Sd.Kfz.121 Luchs': {'highest': 0, 'total': 0},
                'Sd.Kfz.161 Panzer IV': {'highest': 0, 'total': 0},
                'Sd.Kfz.181 Tiger 1': {'highest': 0, 'total': 0},
                'Sd.Kfz.171 Panther': {'highest': 0, 'total': 0},
                'ZIS-5 (Transport)': {'highest': 0, 'total': 0},
                'ZIS-5 (Supply)': {'highest': 0, 'total': 0},
                'GAZ-67': {'highest': 0, 'total': 0},
                'BA-10': {'highest': 0, 'total': 0},
                'T70': {'highest': 0, 'total': 0},
                'T34/76': {'highest': 0, 'total': 0},
                'IS-1': {'highest': 0, 'total': 0},
                'Bedford OYD (Transport)': {'highest': 0, 'total': 0},
                'Bedford OYD (Supply)': {'highest': 0, 'total': 0},
                'Daimler': {'highest': 0, 'total': 0},
                'Tetrarch': {'highest': 0, 'total': 0},
                'M3 Stuart Honey': {'highest': 0, 'total': 0},
                'Cromwell': {'highest': 0, 'total': 0},
                'Crusader Mk.III': {'highest': 0, 'total': 0},
                'Firefly': {'highest': 0, 'total': 0},
                'Churchill Mk.III': {'highest': 0, 'total': 0},
                'Churchill Mk.VII': {'highest': 0, 'total': 0},
            },
            'armour': {
                'M2 Browning [M3 Half-track]': {'highest': 0, 'total': 0},
                'M6 37mm [M8 Greyhound]': {'highest': 0, 'total': 0},
                'COAXIAL M1919 [M8 Greyhound]': {'highest': 0, 'total': 0},
                '37MM CANNON [Stuart M5A1]': {'highest': 0, 'total': 0},
                'COAXIAL M1919 [Stuart M5A1]': {'highest': 0, 'total': 0},
                'HULL M1919 [Stuart M5A1]': {'highest': 0, 'total': 0},
                '75MM CANNON [Sherman M4A3(75)W]': {'highest': 0, 'total': 0},
                'COAXIAL M1919 [Sherman M4A3(75)W]': {'highest': 0, 'total': 0},
                'HULL M1919 [Sherman M4A3(75)W]': {'highest': 0, 'total': 0},
                '75MM M3 GUN [Sherman M4A3E2]': {'highest': 0, 'total': 0},
                'COAXIAL M1919 [Sherman M4A3E2]': {'highest': 0, 'total': 0},
                'HULL M1919 [Sherman M4A3E2]': {'highest': 0, 'total': 0},
                '76MM M1 GUN [Sherman M4A3E2(76)]': {'highest': 0, 'total': 0},
                'COAXIAL M1919 [Sherman M4A3E2(76)]': {'highest': 0, 'total': 0},
                'HULL M1919 [Sherman M4A3E2(76)]': {'highest': 0, 'total': 0},
                'MG 42 [Sd.Kfz 251 Half-track]': {'highest': 0, 'total': 0},
                '50mm KwK 39/1 [Sd.Kfz.234 Puma]': {'highest': 0, 'total': 0},
                'COAXIAL MG34 [Sd.Kfz.234 Puma]': {'highest': 0, 'total': 0},
                '20MM KWK 30 [Sd.Kfz.121 Luchs]': {'highest': 0, 'total': 0},
                'COAXIAL MG34 [Sd.Kfz.121 Luchs]': {'highest': 0, 'total': 0},
                '75MM CANNON [Sd.Kfz.161 Panzer IV]': {'highest': 0, 'total': 0},
                'COAXIAL MG34 [Sd.Kfz.161 Panzer IV]': {'highest': 0, 'total': 0},
                'HULL MG34 [Sd.Kfz.161 Panzer IV]': {'highest': 0, 'total': 0},
                '88 KWK 36 L/56 [Sd.Kfz.181 Tiger 1]': {'highest': 0, 'total': 0},
                'COAXIAL MG34 [Sd.Kfz.181 Tiger 1]': {'highest': 0, 'total': 0},
                'HULL MG34 [Sd.Kfz.181 Tiger 1]': {'highest': 0, 'total': 0},
                '75MM CANNON [Sd.Kfz.171 Panther]': {'highest': 0, 'total': 0},
                'COAXIAL MG34 [Sd.Kfz.171 Panther]': {'highest': 0, 'total': 0},
                'HULL MG34 [Sd.Kfz.171 Panther]': {'highest': 0, 'total': 0},
                '19-K 45MM [BA-10]': {'highest': 0, 'total': 0},
                'COAXIAL DT [BA-10]': {'highest': 0, 'total': 0},
                '45MM M1937 [T70]': {'highest': 0, 'total': 0},
                'COAXIAL DT [T70]': {'highest': 0, 'total': 0},
                '76MM ZiS-5 [T34/76]': {'highest': 0, 'total': 0},
                'COAXIAL DT [T34/76]': {'highest': 0, 'total': 0},
                'HULL DT [T34/76]': {'highest': 0, 'total': 0},
                'D-5T 85MM [IS-1]': {'highest': 0, 'total': 0},
                'COAXIAL DT [IS-1]': {'highest': 0, 'total': 0},
                'HULL DT [IS-1]': {'highest': 0, 'total': 0},
                'QF 2-POUNDER [Daimler]': {'highest': 0, 'total': 0},
                'COAXIAL BESA [Daimler]': {'highest': 0, 'total': 0},
                'QF 2-POUNDER [Tetrarch]': {'highest': 0, 'total': 0},
                'COAXIAL BESA [Tetrarch]': {'highest': 0, 'total': 0},
                '37MM CANNON [M3 Stuart Honey]': {'highest': 0, 'total': 0},
                'COAXIAL M1919 [M3 Stuart Honey]': {'highest': 0, 'total': 0},
                'HULL M1919 [M3 Stuart Honey]': {'highest': 0, 'total': 0},
                'QF 75MM [Cromwell]': {'highest': 0, 'total': 0},
                'COAXIAL BESA [Cromwell]': {'highest': 0, 'total': 0},
                'HULL BESA [Cromwell]': {'highest': 0, 'total': 0},
                'OQF 57MM [Crusader Mk.III]': {'highest': 0, 'total': 0},
                'COAXIAL BESA [Crusader Mk.III]': {'highest': 0, 'total': 0},
                'QF 17-POUNDER [Firefly]': {'highest': 0, 'total': 0},
                'COAXIAL M1919 [Firefly]': {'highest': 0, 'total': 0},
                'OQF 57MM [Churchill Mk.III]': {'highest': 0, 'total': 0},
                'COAXIAL BESA 7.92mm [Churchill Mk.III]': {'highest': 0, 'total': 0},
                'HULL BESA 7.92mm [Churchill Mk.III]': {'highest': 0, 'total': 0},
                'OQF 57MM [Churchill Mk.VII]': {'highest': 0, 'total': 0},
                'COAXIAL BESA 7.92mm [Churchill Mk.VII]': {'highest': 0, 'total': 0},
                'HULL BESA 7.92mm [Churchill Mk.VII]': {'highest': 0, 'total': 0},
            },
            'arty': {
                '155MM HOWITZER [M114]': {'highest': 0, 'total': 0},
                '150MM HOWITZER [sFH 18]': {'highest': 0, 'total': 0},
                '122MM HOWITZER [M1938 (M-30)]': {'highest': 0, 'total': 0},
                'QF 25-POUNDER [QF 25-Pounder]': {'highest': 0, 'total': 0},
            }
        }

        infantry_keys = weapons['infantry'].keys()
        roadkills_keys = weapons['roadkills'].keys()
        armour_keys = weapons['armour'].keys()
        arty_keys = weapons['arty'].keys()

        for weapon in weapons_data:
            if weapon.weapon in infantry_keys:
                weapons['infantry'][weapon.weapon]['total'] += weapon.kills
                if weapon.kills > weapons['infantry'][weapon.weapon]['highest']:
                    weapons['infantry'][weapon.weapon]['highest'] = weapon.kills
            if weapon.weapon in roadkills_keys:
                weapons['roadkills'][weapon.weapon]['total'] += weapon.kills
                if weapon.kills > weapons['roadkills'][weapon.weapon]['highest']:
                    weapons['roadkills'][weapon.weapon]['highest'] = weapon.kills
            if weapon.weapon in armour_keys:
                weapons['armour'][weapon.weapon]['total'] += weapon.kills
                if weapon.kills > weapons['armour'][weapon.weapon]['highest']:
                    weapons['armour'][weapon.weapon]['highest'] = weapon.kills
            if weapon.weapon in arty_keys:
                weapons['arty'][weapon.weapon]['total'] += weapon.kills
                if weapon.kills > weapons['arty'][weapon.weapon]['highest']:
                    weapons['arty'][weapon.weapon]['highest'] = weapon.kills

        weapons['infantry'] = {key: val for key, val in sorted(weapons['infantry'].items(), key = lambda ele: ele[1]['total'], reverse = True)}
        weapons['roadkills'] = {key: val for key, val in sorted(weapons['roadkills'].items(), key = lambda ele: ele[1]['total'], reverse = True)}
        weapons['armour'] = {key: val for key, val in sorted(weapons['armour'].items(), key = lambda ele: ele[1]['total'], reverse = True)}
        weapons['arty'] = {key: val for key, val in sorted(weapons['arty'].items(), key = lambda ele: ele[1]['total'], reverse = True)}

        return weapons


    def get_kills_stats_by_steam64(self, steam_64):
        kills_data = get_player_kills_by_steam64(steam_64)
        ret_data = {}

        for kill in kills_data:
            if kill.victim in ret_data.keys():
                ret_data[kill.victim] += kill.kills
            else:
                ret_data[kill.victim] = kill.kills

        ret_data = {key: val for key, val in sorted(ret_data.items(), key = lambda ele: ele[1], reverse = True)}

        return ret_data


    def get_coletrain(self):
        cole_data = get_coletrain()
        ret_cole = {}

        for stat in cole_data:
            if stat.steam_id_64 in ret_cole.keys():
                ret_cole[stat.steam_id_64]['kills'] += stat.kills
            else:
                ret_cole[stat.steam_id_64] = {'name': get_player_name_by_steam64(stat.steam_id_64), 'kills': stat.kills}

        ret_cole = {key: val for key, val in sorted(ret_cole.items(), key = lambda ele: ele[1], reverse = True)}

        return ret_cole


    def testing(self):
        data = get_player_by_steam64(76561198182324770)
        ret_list = []
        for d in data:
            if d.player not in ret_list:
                ret_list.append(d.player)

        return ret_list


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
