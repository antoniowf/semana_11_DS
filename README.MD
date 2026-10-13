 ![Logo](./images/logo.png)

# Agenda 11 Desenvolvimento de Sistemas I
 [![Python](https://img.shields.io/badge/Python-3.12.3-3776AB?logo=python&logoColor=white)](https://www.python.org/)
---

**Aluno: Antonio Wenceslau de Freitas**  
**Cód. cadastro: SP20AO0206046**

# Atividade proposta

### Atividade: Controle de Níveis de Água

Você foi contratado para auxiliar no desenvolvimento de um sistema simples de monitoramento de um reservatório de água.

Esse sistema será executado no terminal e tem como objetivo exibir mensagens de alerta com cores diferentes, conforme o nível de água do reservatório.

Para tornar a visualização mais clara, será utilizada a biblioteca colorama, permitindo destacar cada situação com uma cor específica.

O sistema deverá trabalhar com cinco níveis de água, representados em uma lista, indo de um nível mais baixo até o nível máximo do reservatório.  Cada nível deverá ser associado a uma mensagem de alerta e a uma cor, seguindo a progressão de risco:


| Nível do reservatório | Situação              | Cor sugerida                                   |
|-----------------------|-----------------------|------------------------------------------------|        
| Nível 1               | Muito baixo (crítico) | <code style = "color:red">Vermelho  </code>    |    
| Nível 2               | Baixo	                 | <code style = "color:yellow">Amarelo   </code> |      
| Nível 3               | Médio	                 | <code style = "color:green">Verde     </code>  |      
| Nível 4               | Alto	                  | <code style = "color:cyan">Ciano     </code>   |  
| Nível 5               | Muito alto (alerta)	   | <code style = "color:blue">Azul      </code>   | 

### O programa deverá:

- Utilizar uma lista para armazenar os níveis ou as mensagens do reservatório;
- Importar e utilizar a biblioteca colorama;
- Criar uma função responsável por definir a cor da mensagem conforme o nível informado;
- Exibir no terminal a situação atual do reservatório com a cor correspondente;
- Restaurar o estilo padrão do terminal após a exibição das mensagens.

![img.png](images/img.png)