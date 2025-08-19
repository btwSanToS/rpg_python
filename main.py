from random import randint

lista_npcs = []

player = {
    "nome": "Santos",
    "level": 1,
    "exp": 0,
    "exp_max": 50,
    "hp": 100,
    "hp_max": 100,
    "dano": 25,
}

def criar_npc(level):
    novo_npc = {
        "nome": f"Monstro #{level}",
        "level": level,
        "dano": 5 * level,
        "hp": 100 * level,
        "hp_max": 100 * level,
        "exp": 7 * level
    }
    return novo_npc


def gerar_npcs(n_npcs):
    for x in range(n_npcs):
        novo_npc = criar_npc(x + 1)
        lista_npcs.append(novo_npc)

def exibir_npcs():
    for npc in lista_npcs:
        exibir_npc(npc)

def exibir_npc(npc):
    print(
            f"Nome: {npc['nome']} // "
            f"Level: {npc['level']} // "
            f"Dano: {npc['dano']} // "
            f"HP: {npc['hp']} // "
            f"EXP: {npc['exp']}"
        )
    
def exibir_player():
    print(
            f"Nome: {player['nome']} // "
            f"Level: {player['level']} // "
            f"Dano: {player['dano']} // "
            f"HP: {player['hp']}/{player['hp_max']} // " 
            f"EXP: {player['exp']}/{player['exp_max']}"
        )
    
def reset_player():
    player['hp'] = player['hp_max']

def reset_npc(npc):
    npc['hp'] = npc['hp_max']

def level_up():
    if player['exp'] >= player['exp_max']: 
        player['exp'] -= player['exp_max']        
        aplicar_level_up()

def aplicar_level_up():
    player['level'] += 1
    player['hp_max'] = int(round(player['hp_max'] * 1.20))
    player['dano'] = int(round(player['dano'] * 1.20))
    player['exp_max'] = int(round(player['exp_max'] * 1.20))


def iniciar_batalha (npc):
    while player['hp'] > 0 and npc['hp'] > 0:
        atacar_npc(npc)
        if npc['hp'] <= 0:
            break
        atacar_player(npc)
        if player['hp'] <= 0:
            break

        exibir_info_batalha(npc)
    
    if player ['hp'] > 0: 
        print (f"{player['nome']} venceu e ganhou {npc['exp']} de EXP!")
        player['exp'] += npc['exp']
        exibir_player()
    else: 
        print (f"O {npc['nome']} venceu!")
        exibir_npc(npc)

    level_up()
    reset_player()
    reset_npc(npc)

# atacar_npc(npc) // npc: hp - player:dano
def atacar_npc (npc):
    npc['hp'] -= player['dano']

# atacar_player(npc) -- player: hp - npc: dano
def atacar_player (npc):
    player['hp'] -= npc['dano']

def exibir_info_batalha(npc):
    print(f"{player['nome']}: {player['hp']} / {player['hp_max']}")
    print(f"NPC: {npc['nome']}: {npc['hp']} / {npc['hp_max']}")
    print('------------------------------------------\n')

gerar_npcs(5)

npc_selecionado = lista_npcs[0]
iniciar_batalha(npc_selecionado)