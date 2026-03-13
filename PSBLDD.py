import itertools
import os

def gerar_e_imprimir():
    mapa_completo = {
        'A': '4',
        'D': '3',
        'E': '3',
        'I': '1',
        'O': '0',
        'T': '7'
    }

    print("--- GERADOR DE SENHAS ---")
    salvar_input = input("SALVAR EM ARQUIVO? (SIM para salvar / ENTER para apenas ver): ").strip().upper()
    
    print("\nOpções disponíveis:")
    print("[15] ou [A] para SALAINFORMATICA")
    print("[17] ou [B] para SALADEINFORMATICA")
    print("[21] ou [C] para LABORATORIOINFORMATICA")
    print("[23] ou [D] para LABORATORIODEINFORMATICA")
    
    escolha = input("\nDigite sua escolha: ").strip().upper()

    opcoes_palavras = {
        "15": "SALAINFORMATICA", "A": "SALAINFORMATICA",
        "17": "SALADEINFORMATICA", "B": "SALADEINFORMATICA",
        "21": "LABORATORIOINFORMATICA", "C": "LABORATORIOINFORMATICA",
        "23": "LABORATORIODEINFORMATICA", "D": "LABORATORIODEINFORMATICA"
    }

    if escolha not in opcoes_palavras:
        print("Opção inválida!")
        return
    
    palavra_base = opcoes_palavras[escolha]

    so_vogais_input = input("SÓ VOGAIS? (SIM para apenas vogais / ENTER para padrão): ").strip().upper()
    
    if so_vogais_input == "SIM":
        mapa_uso = {k: v for k, v in mapa_completo.items() if k in "AEIO"}
        modo_txt = "Apenas Vogais"
    else:
        mapa_uso = mapa_completo
        modo_txt = "Padrão (Vogais + D/T)"

    opcoes_caracteres = []
    for i, char in enumerate(palavra_base.upper()):
        if i == 0:
            opcoes_caracteres.append([char])
        elif char in mapa_uso:
            opcoes_caracteres.append([char, mapa_uso[char]])
        else:
            opcoes_caracteres.append([char])

    combinacoes = [''.join(comb) for comb in itertools.product(*opcoes_caracteres)]

    if salvar_input == "SIM":
        nome_arquivo = f"{palavra_base}.txt"
        try:
            with open(nome_arquivo, "w") as f:
                for i, senha in enumerate(combinacoes, 1):
                    f.write(f"{i:04d}-- {senha}\n")
            print(f"\n[OK] Arquivo '{nome_arquivo}' salvo com sucesso na pasta do script!")
        except Exception as e:
            print(f"\n[ERRO] Não foi possível salvar o arquivo: {e}")

    print(f"\nExibindo todas as {len(combinacoes)} possibilidades ({modo_txt}):\n")
    
    for i, senha in enumerate(combinacoes, 1):
        print(f"{i:04d}-- {senha}")

    print(f"\n--- FIM DA LISTA ---")
    print(f"Total de senhas geradas: {len(combinacoes)}")

if __name__ == "__main__":
    gerar_e_imprimir()
