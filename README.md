<h1 align="center">👾 Horizons Gamer Shop 👾</h1>

Horizons Gamer Shop é uma plataforma de jogos projetada para oferecer uma experiência diversificada e envolvente. O objetivo é criar um ambiente robusto e escalável onde os gamers possam explorar uma vasta seleção de jogos, desde lançamentos populares até títulos independentes e clássicos.


<h3 align="center">Funcionalidades Desenvolvidas 🕹️</h2>

### Cadastro de Jogos
- **Descrição:** Permite adicionar novos jogos ao catálogo.
- **Detalhes:** O formulário inclui campos para nome, foto, preço, gêneros, plataformas e data de lançamento. Utiliza checkboxes para selecionar múltiplos gêneros e plataformas.
- **Processo:** Os dados são enviados ao servidor via requisição POST para a rota `/register-game` em formato JSON. Após o envio, uma mensagem de confirmação é exibida e o formulário é resetado para novos cadastros.

![tela_cadastro](tela_cadastro.png)

### Catálogo de Jogos
- **Descrição:** Permite visualizar toda a coleção de jogos disponíveis.
- **Interface:** Inclui uma barra lateral fixa com um menu de navegação.
- **Processo:** Ao carregar a página, uma requisição é feita para a rota `/games` para listar os jogos. Em caso de erro na obtenção dos dados, uma mensagem de alerta é exibida.

![Catalogo de Jogos](catalogo_jogo.png)

### Deletar Jogo - Catálogo de Jogos

- **Descrição:** Permite remover um jogo específico da coleção de jogos disponíveis no catálogo..
- **Interface:** Inclui um botão de exclusão ao lado de cada jogo listado na página do catálogo.
- **Processo:** Quando o usuário clica no botão de exclusão ao lado do jogo que deseja remover, uma requisição `DELETE` é enviada para a rota `/delete-game/<int:game_id>`. O sistema, então, exibe uma mensagem de confirmação para garantir que a ação de exclusão seja intencional. Caso o usuário confirme, o jogo é removido do banco de dados, e a lista de jogos é atualizada automaticamente. Se houver algum erro durante o processo de exclusão, uma mensagem de alerta é exibida para informar o usuário.

![Catalogo de Jogos](deletar_jogo.png)