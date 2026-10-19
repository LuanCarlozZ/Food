# Meta 50

Controle pessoal de ganhos de entregas (99 e iFood) com meta diária em reais.
Tudo roda no navegador, sem servidor e sem conta. Seus dados ficam salvos no próprio aparelho (localStorage).

## Arquivos
- `index.html`: o aplicativo inteiro (gerado a partir de `src/app.html`).
- `manifest.webmanifest`, `sw.js`, `icon*.png/svg`: fazem o app ser instalável e abrir sem internet.
- `src/app.html`: código-fonte editável. Depois de mexer, rode `python3 build.py`.

## Como usar no Android
O app precisa estar em um endereço https para ser instalado como aplicativo. Opções simples e gratuitas:
1. **GitHub Pages**: crie um repositório, envie estes arquivos, ative Pages em Settings > Pages.
2. **Netlify Drop** (app.netlify.com/drop): arraste a pasta e receba um link.
Depois, abra o link no **Chrome do Android**, toque nos três pontos e em **Instalar app** (ou **Adicionar à tela inicial**). O ícone aparece na tela inicial e o app abre em tela cheia.

Também funciona só abrindo o link no Chrome, sem instalar. Abrir `index.html` direto do armazenamento do celular funciona, mas não instala nem guarda dados de forma confiável.

## Backup e restauração
Ajustes > Backup dos dados.
- **Baixar JSON** ou **Copiar backup**: guarda todos os registros e configurações. Faça isso toda semana.
- **Baixar CSV**: planilha (separador `;`, valores com vírgula) para abrir no Excel ou Google Planilhas.
- **Restaurar**: escolha o arquivo JSON ou cole o texto. Depois escolha **Mesclar** (soma aos atuais, sem duplicar) ou **Substituir tudo**.
Limpar os dados do navegador apaga os registros, por isso o backup importa.

## Regras de cálculo
- Valores são guardados em centavos (sem erros de arredondamento).
- Meta atingida: total do dia >= meta. Superada: total > meta. Restante = max(0, meta − total). Excedente = max(0, total − meta).
- O total do dia soma todos os registros da data, de qualquer app e período. Registrar uma entrega ou o total de um período alimenta o mesmo total, sem duplicar.
- Média por entrega usa só registros com número de entregas informado (0 = não informado).
- Dias sem registro e dias futuros nunca contam como meta não atingida.
- Sequência: dias seguidos com meta atingida; folgas (dias fora da escala em Ajustes) não quebram a sequência.
- Semanas vão de domingo a sábado.

## Dados de exemplo
Ajustes > Carregar exemplos. Ficam marcados e saem com **Remover exemplos**, sem tocar nos seus registros.
