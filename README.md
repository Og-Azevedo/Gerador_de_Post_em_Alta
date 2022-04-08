# Gerador de Post em Alta

**Objetivo:**

Desenvolver uma ferramenta que automaticamente gere um post que contenha elementos e tópicos que estejam
em alta. Dessa forma o conteúdo gerado por esse programa seria interpretado pelo algorítimo das redes sociais como 
algo relevante. Assim a propabilidade de que o usuário tenha mais atração e visibilidade orgânica seriam ampliados.
 
**Solução:**

Para chegar nessa solução eu decidi que o meu programa deveria gerar:
- Uma imagem (1:1) contendo os termos mais "aquecidos";
- Legenda: Texto contendo as hashtags referêntes aos assuntos em alta;
- Enviar para o e-mail do usuário a imagem em anexo e a legenda (hashtags) no corpo do e-mail;

Abaixo está um breve resumo do fluxo que eu desenvolvi para chegar nesse resultado:
- Usei a API Pytrends para descobrir o que está em alta no Google Trends;
- Após tratar o resultado da request eu utilizei a biblioteca Pillow para criar uma imagem onde 
as cores de cada linha fosse "esfriando" para indicar visualmente qual tópico estaria mais aquecido. 
- Por fim usei a lib Yagmail para anexar e enviar para o usuário a imagem em anexo e a lista de hashtags;

**Abaixo seguem alguns exemplos do resultado:**

Legenda: #Joe #Biden #International #Space #Station #National #Collegiate #Athletic #Association #Rand #Paul #Johnny #Depp

![img.png](img.png)