from bs4 import BeautifulSoup
import json


def main(): 
    user_list: list[dict] = jsonify_ramal()
    categorize(user_list=user_list)


def jsonify_ramal(return_user_list=True, save_json=False) -> list[dict] | None:

    lista_ramal: str

    with open("lista_ramal.html", "r") as f:
        lista_ramal = f.read()


    # Parse o HTML com BeautifulSoup
    soup = BeautifulSoup(lista_ramal, 'html.parser')

    # Localiza todas as linhas <tr> no corpo da tabela (<tbody>)
    rows = soup.find('tbody').find_all('tr')


    user_list: list[dict] = []

    # Itera sobre as linhas e extrai os dados
    for row in rows:
        th = row.find('th')  # Obtém o valor da célula <th>
        tds = row.find_all('td')  # Obtém todas as células <td>

        user = {
            "id": th.text.strip() if th else None,
            "nome": tds[0].text.strip(),
            "filial": tds[1].text.strip(),
            "dep": tds[2].text.strip(),
            "ramal": tds[3].text.strip()
        }

        user_list.append(user)


    if save_json is True:
        with open("ramal_users.json", "w", encoding="utf-8") as f:
            jsonified_users = json.dumps(user_list)
            f.write(jsonified_users)

    if return_user_list is True: return user_list
    


def categorize(user_list: list[dict]=None):

    if user_list is None:
        with open("ramal_users.json", "r") as f:
            json_file = f.read()
            user_list = json.loads(json_file)


    categ_dict = {
        "mat": {
            "important": {
                "dir": [],
                "ger": [],
                "it": []
            },
            "others": {
                "ges": [],
                "prod": []
            }
        },
        "ext": {
            "important": {
                "dir": [],
                "ger": [],
                "it": []
            },
            "others": {
                "ges": [],
                "prod": []
            }
        }
    }


    for user in user_list:

        user_role = get_user_role(user['nome'], user['dep'])

        filial = 'mat' if user['filial'] in 'Matriz' else 'ext'

        if user_role in ['ger', 'dir', 'it']:
            categ_dict[filial]['important'][user_role].append(user)
        else:
            categ_dict[filial]['others'][user_role].append(user)


    with open("ramal_users_categ.json", "w", encoding="utf-8") as f:
        jsonified_users = json.dumps(categ_dict)
        f.write(jsonified_users)

    print(jsonified_users)
    
    


def get_user_role(nome: str, dep: str) -> str:

    nome, dep = nome.lower(), dep.lower()

    if 'gerente' in nome or 'diretor' in nome or 'ti' in dep:
        if 'gerente' in nome: return 'ger'
        elif 'diretor' in nome: return 'dir'
        elif 'ti' in nome: return 'it'
    else:
        if 'gestor' in nome: return 'ges'
        else: return 'prod'
         

main()