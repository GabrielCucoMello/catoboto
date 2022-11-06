import requests, discord
from discord.ext import commands
from src.csgoimage import pegaImagem

status = ["total_kills","total_deaths","total_time_played","total_planted_bombs","total_defused_bombs","total_wins",
"total_damage_done","total_money_earned","total_rescued_hostages","total_kills_knife","total_kills_hegrenade",
"total_kills_glock","total_kills_deagle","total_kills_elite","total_kills_fiveseven","total_kills_xm1014",
"total_kills_mac10","total_kills_ump45","total_kills_p90","total_kills_awp","total_kills_ak47","total_kills_aug",
"total_kills_famas","total_kills_g3sg1","total_kills_m249","total_kills_headshot","total_kills_enemy_weapon","total_wins_pistolround",
"total_wins_map_cs_assault","total_wins_map_cs_italy","total_wins_map_cs_office","total_wins_map_de_aztec","total_wins_map_de_cbble",
"total_wins_map_de_dust2","total_wins_map_de_dust","total_wins_map_de_inferno","total_wins_map_de_nuke","total_wins_map_de_train","total_weapons_donated",
"total_broken_windows","total_kills_enemy_blinded","total_kills_knife_fight","total_kills_against_zoomed_sniper","total_dominations","total_domination_overkills",
"total_revenges","total_shots_hit","total_shots_fired","total_rounds_played","total_shots_deagle","total_shots_glock","total_shots_elite","total_shots_fiveseven",
"total_shots_awp","total_shots_ak47","total_shots_aug","total_shots_famas","total_shots_g3sg1","total_shots_p90","total_shots_mac10","total_shots_ump45",
"total_shots_xm1014","total_shots_m249","total_hits_deagle","total_hits_glock","total_hits_elite","total_hits_fiveseven","total_hits_awp","total_hits_ak47",
"total_hits_aug","total_hits_famas","total_hits_g3sg1","total_hits_p90","total_hits_mac10","total_hits_ump45","total_hits_xm1014","total_hits_m249",
"total_rounds_map_cs_assault","total_rounds_map_cs_italy","total_rounds_map_cs_office","total_rounds_map_de_aztec","total_rounds_map_de_cbble","total_rounds_map_de_dust2",
"total_rounds_map_de_dust","total_rounds_map_de_inferno","total_rounds_map_de_nuke","total_rounds_map_de_train","last_match_t_wins","last_match_ct_wins","last_match_wins",
"last_match_max_players","last_match_kills","last_match_deaths","last_match_mvps","last_match_favweapon_id","last_match_favweapon_shots","last_match_favweapon_hits",
"last_match_favweapon_kills","last_match_damage","last_match_money_spent","last_match_dominations","last_match_revenges","total_mvps","total_rounds_map_de_lake",
"total_rounds_map_de_safehouse","total_rounds_map_de_sugarcane","total_rounds_map_de_stmarc","total_rounds_map_de_bank","total_TR_planted_bombs","total_TR_defused_bombs",
"total_gun_game_rounds_won","total_gun_game_rounds_played","total_wins_map_de_house","total_wins_map_de_bank","total_wins_map_de_vertigo","total_wins_map_ar_monastery",
"total_rounds_map_ar_shoots","total_rounds_map_ar_baggage","total_wins_map_ar_shoots","total_wins_map_ar_baggage","total_wins_map_de_lake","total_wins_map_de_sugarcane",
"total_wins_map_de_stmarc","total_matches_won_bank","total_wins_map_de_shorttrain","total_wins_map_de_safehouse","total_matches_won","total_matches_played","total_gg_matches_won",
"total_gg_matches_played","total_progressive_matches_won","total_trbomb_matches_won","total_contribution_score","last_match_contribution_score","last_match_rounds",
"total_kills_hkp2000","total_shots_hkp2000","total_hits_hkp2000","total_hits_p250","total_kills_p250","total_shots_p250","total_kills_sg556","total_shots_sg556","total_hits_sg556",
"total_hits_scar20","total_kills_scar20","total_shots_scar20","total_shots_ssg08","total_hits_ssg08","total_kills_ssg08","total_shots_mp7","total_hits_mp7","total_kills_mp7",
"total_kills_mp9","total_shots_mp9","total_hits_mp9","total_hits_nova","total_kills_nova","total_shots_nova","total_hits_negev","total_kills_negev","total_shots_negev",
"total_shots_sawedoff","total_hits_sawedoff","total_kills_sawedoff","total_shots_bizon","total_hits_bizon","total_kills_bizon","total_kills_tec9","total_shots_tec9","total_hits_tec9",
"total_shots_mag7","total_hits_mag7","total_kills_mag7","total_gun_game_contribution_score","last_match_gg_contribution_score","total_kills_m4a1","total_kills_galilar",
"total_kills_molotov","total_kills_decoy","total_kills_taser","total_shots_m4a1","total_shots_galilar","total_shots_taser","total_hits_m4a1","total_hits_galilar",
"total_rounds_map_ar_monastery","total_matches_won_train","total_rounds_map_de_vertigo","total_matches_won_shoots","total_matches_won_baggage","total_matches_won_lake",
"total_matches_won_sugarcane","total_matches_won_stmarc","total_matches_won_safehouse"]

class CogValve(commands.Cog, description='Comandos para pegar dados de jogos da VALVE de usuários.'):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief='Comando pra você poder ver os dados de jogo de um perfil da steam.', 
    description='Você deve usar o comando da seguinte maneira: $csgo (base/kills) steamurl, qualquer outra coisa que não for um url da steam, não vai funcionar')
    async def csgo(self, ctx, tipo, url):
        foto = pegaImagem(url)
        if 'id' in url:
            steamid = []
            steam1 = url.replace('https://steamcommunity.com/id/', '')
            steam = steam1.replace('/', '')
            steamid_url = requests.get(f'http://api.steampowered.com/ISteamUser/ResolveVanityURL/v0001/?key=C9BDBB4151F136083506A1572ABD8B9B&vanityurl={steam}').json()
            steamid = steamid_url['response']['steamid']
        if 'profiles' in url:
            steam = url.replace('https://steamcommunity.com/profiles/', '')
            steamid = steam.replace('/', '')
        loop = 0
        valores = {}
        try:
            csgo = requests.get(f"http://api.steampowered.com/ISteamUserStats/GetUserStatsForGame/v2/?appid=730&key=C9BDBB4151F136083506A1572ABD8B9B&steamid={steamid}").json()
            csgo_stats = csgo["playerstats"]["stats"]
            while loop < int(len(status)):
                for stat in csgo_stats:
                    if stat["name"] == status[loop]:
                        valores[stat['name']]=stat['value']
                loop += 1
        except KeyError:
            await ctx.send('ERRO! SteamID inválida, ou o usuário está como perfil PRIVADO (bem gay).')
        if tipo == 'base':
            embed=discord.Embed(title=f"Status de Counter-Strike:Global Offensive do usuário **{steam}**", 
            description="Aqui você pode ver os stats BASE do jogador requerido.",
            color=discord.Color.random())
            embed.set_thumbnail(url=foto)
            embed.add_field(name="Kills:", value=f"{valores.get('total_kills')}", inline=True)
            embed.add_field(name="Mortes:", value=f"{valores.get('total_deaths')}", inline=True)
            embed.add_field(name="Tempo jogado (dentro de partidas):", value=f"{(valores.get('total_time_played') // 3600)} horas", inline=True)
            embed.add_field(name="Bombas plantadas:", value=f"{valores.get('total_planted_bombs')}", inline=True)
            embed.add_field(name="Bombas defusadas:", value=f"{valores.get('total_defused_bombs')}", inline=True)
            embed.add_field(name="Vitórias:", value=f"{valores.get('total_wins')}", inline=True)
            embed.add_field(name="Quantidade total de dano deferido:", value=f"{valores.get('total_damage_done')}", inline=True)
            embed.add_field(name="Dinheiro ganho:", value=f"{valores.get('total_money_earned')}", inline=True)
            embed.add_field(name="Reféns resgatados:", value=f"{valores.get('total_rescued_hostages')}", inline=True)
        if tipo == 'kills':
            embed=discord.Embed(title=f"Status de Counter-Strike:Global Offensive do usuário **{steam}**", 
            description="Aqui você pode ver os status de KILLS do jogador requerido.",
            color=discord.Color.random())
            embed.set_thumbnail(url=foto)
            embed.add_field(name="Kills com faca:", value=f"{valores.get('total_kills_knife')}", inline=True)
            embed.add_field(name="Kills com granada explosiva:", value=f"{valores.get('total_kills_hegrenade')}", inline=True)
            embed.add_field(name="Kills com glock:", value=f"{valores.get('total_kills_glock')}", inline=True)
            embed.add_field(name="Kills com desert eagle:", value=f"{valores.get('total_kills_deagle')}", inline=True)
            embed.add_field(name="Kills com dual beretas", value=f"{valores.get('total_kills_elite')}", inline=True)
            embed.add_field(name="Kills com five seven:", value=f"{valores.get('total_kills_fiveseven')}", inline=True)
            embed.add_field(name="Kills com xm1014:", value=f"{valores.get('total_kills_xm1014')}", inline=True)
            embed.add_field(name="Kills com mac10:", value=f"{valores.get('total_kills_mac10')}", inline=True)
            embed.add_field(name="Kills com ump:", value=f"{valores.get('total_kills_ump45')}", inline=True)
            embed.add_field(name="Kills com p90:", value=f"{valores.get('total_kills_p90')}", inline=True)
            embed.add_field(name="Kills com awp:", value=f"{valores.get('total_kills_awp')}", inline=True)
            embed.add_field(name="Kills com ak-47:", value=f"{valores.get('total_kills_ak47')}", inline=True)
            embed.add_field(name="Kills com aug:", value=f"{valores.get('total_kills_aug')}", inline=True)
            embed.add_field(name="Kills com famas:", value=f"{valores.get('total_kills_famas')}", inline=True)
            embed.add_field(name="Kills com g3sg1:", value=f"{valores.get('total_kills_g3sg1')}", inline=True)
            embed.add_field(name="Kills com m249:", value=f"{valores.get('total_kills_m249')}", inline=True)
            embed.add_field(name="Kills de p2000:", value=f"{valores.get('total_kills_hkp2000')}", inline=True)
            embed.add_field(name="Kills com p250:", value=f"{valores.get('total_kills_p250')}", inline=True)
            embed.add_field(name="Kills com sg556:", value=f"{valores.get('total_kills_sg556')}", inline=True)
            embed.add_field(name="Kills com scar20:", value=f"{valores.get('total_kills_scar20')}", inline=True)
            embed.add_field(name="Kills com mata pombo:", value=f"{valores.get('total_kills_ssg08')}", inline=True)
            embed.add_field(name="Kills com mp7:", value=f"{valores.get('total_kills_mp7')}", inline=True)
            embed.add_field(name="Kills com mp9:", value=f"{valores.get('total_kills_mp9')}", inline=True)
            embed.add_field(name="Kills com nova:", value=f"{valores.get('total_kills_nova')}", inline=True)
            embed.add_field(name="Kills com negev:", value=f"{valores.get('total_kills_negev')}", inline=True)
            embed.add_field(name="Kills com cano curto:", value=f"{valores.get('total_kills_sawedoff')}", inline=True)
            embed.add_field(name="Kills com bizon:", value=f"{valores.get('total_kills_bizon')}", inline=True)
            embed.add_field(name="Kills com tec9:", value=f"{valores.get('total_kills_tec9')}", inline=True)
            embed.add_field(name="Kills com mag7:", value=f"{valores.get('total_kills_mag7')}", inline=True)
            embed.add_field(name="Kills com m4a1:", value=f"{valores.get('total_kills_m4a1')}", inline=True)
            embed.add_field(name="Kills com galil:", value=f"{valores.get('total_kills_galil')}", inline=True)
        if tipo == 'mapas':
            embed=discord.Embed(title=f"Status de Counter-Strike:Global Offensive do usuário **{steam}**", 
            description="Aqui você pode ver os status de MAPAS do jogador requerido.",
            color=discord.Color.random())
            embed.set_thumbnail(url=foto)
            embed.add_field(name="Rounds Jogados", value=f"{valores.get('total_rounds_played', 0)}", inline=True)
            embed.add_field(name="Rounds Ganhos", value=f"{valores.get('total_wins', 0)}", inline=True)
            embed.add_field(name="Rounds Perdidos", value=f"{valores.get('total_rounds_played', 0) - valores.get('total_wins', 0)}", inline=True)
            embed.add_field(name="Rounds Dust 2", value=f"{valores.get('total_rounds_map_de_dust2', 0)}", inline=True)
            embed.add_field(name="Vitórias Dust 2", value=f"{valores.get('total_wins_map_de_dust2', 0)}", inline=True)
            embed.add_field(name="Derrotas Dust 2", value=f"{valores.get('total_rounds_map_de_dust2', 0) - valores.get('total_wins_map_de_dust2', 0)}", inline=True)
            embed.add_field(name="Rounds Inferno", value=f"{valores.get('total_rounds_map_de_inferno', 0)}", inline=True)
            embed.add_field(name="Vitórias Inferno", value=f"{valores.get('total_wins_map_de_inferno', 0)}", inline=True)
            embed.add_field(name="Derrotas Inferno", value=f"{valores.get('total_rounds_map_de_inferno', 0) - valores.get('total_wins_map_de_inferno', 0)}", inline=True)
            embed.add_field(name="Rounds Nuke", value=f"{valores.get('total_rounds_map_de_nuke', 0)}", inline=True)
            embed.add_field(name="Vitórias Nuke", value=f"{valores.get('total_wins_map_de_nuke', 0)}", inline=True)
            embed.add_field(name="Derrotas Nuke", value=f"{valores.get('total_rounds_map_de_nuke', 0) - valores.get('total_wins_map_de_nuke', 0)}", inline=True)
            embed.add_field(name="Rounds Vertigo", value=f"{valores.get('total_rounds_map_de_vertigo', 0)}", inline=True)
            embed.add_field(name="Vitórias Vertigo", value=f"{valores.get('total_wins_map_de_vertigo', 0)}", inline=True)
            embed.add_field(name="Derrotas Vertigo", value=f"{valores.get('total_rounds_map_de_vertigo', 0) - valores.get('total_wins_map_de_vertigo', 0)}", inline=True)
            embed.add_field(name="Rounds Train", value=f"{valores.get('total_rounds_map_de_train', 0)}", inline=True)
            embed.add_field(name="Vitórias Train", value=f"{valores.get('total_wins_map_de_train', 0)}", inline=True)
            embed.add_field(name="Derrotas Train", value=f"{valores.get('total_rounds_map_de_train', 0) - valores.get('total_wins_map_de_train', 0)}", inline=True)
        await ctx.send(embed=embed)