## Guia de Contribuição

Antes de começar, obrigado por considerar contribuir com o **Gov Hub BR**!  
Acreditamos que a colaboração é essencial para construir soluções públicas mais eficientes, transparentes e sustentáveis.

O Gov Hub BR é um projeto **open-source** com o propósito de transformar dados públicos em ativos estratégicos para a administração pública e a sociedade. Toda contribuição — código, documentação, ideias ou feedback — é bem-vinda!

## Como Contribuir

### 1. Fork e Clone
Faça um **fork** do repositório e clone para o seu ambiente local:

```bash
git clone https://github.com/seu-usuario/govhub-br.git
```

### 2. Crie uma Nova Branch
Crie uma branch com um nome descritivo, seguindo o padrão:

```bash
git checkout -b tipo/descricao-curta
```

**Exemplos de nomes de branch:**
- `docs/ajuste-tutorial-instalacao`
- `feature/nova-visualizacao-dashboard`
- `fix/corrige-link-quebrado`

### 3. Faça Suas Alterações
Você pode contribuir de várias formas:
- Melhorias no código ou pipelines de dados.
- Ajustes ou acréscimos na documentação.
- Sugestões de novas funcionalidades.
- Correção de erros ou inconsistências.

### 4. Teste e Valide
Antes de abrir um PR:
- Certifique-se de que seu código ou documentação não quebrou funcionalidades existentes.
- Execute testes locais se aplicável.
- Rode ferramentas de lint e formatação, se existirem.

---

## Sobre Pull Requests (PRs)

- Garanta que sua alteração siga os **padrões de commit** e **padrões de branch** definidos abaixo.
- Use o **template de Pull Request** disponível no repositório.
- Descreva claramente o que foi alterado, o motivo da mudança e, sempre que possível, adicione capturas de tela, logs ou links relacionados.

---

## Template de Issues

Quando quiser sugerir **novos conteúdos** ou **novas funcionalidades**, use o nosso template oficial de issue:

- Título no formato: `[ideia] <título da proposta>`
- Labels automáticas: `conteúdo`, `ideia`
- Inclua:
  - Descrição detalhada da proposta.
  - Localização sugerida para o conteúdo.
  - Tarefas necessárias usando checkboxes.
  - Critérios de validação para revisão.

(👉 [Veja o template completo aqui ao criar uma nova issue](https://github.com/GovHub-br/gov-hub/issues))

---

## Padrão de Commits

Utilizamos uma variação do **[Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/)**.  
Formato dos commits:

```
tipo: descrição breve da mudança
```

**Tipos aceitos:**
- `feat`: Nova funcionalidade
- `fix`: Correção de bug
- `docs`: Mudança apenas na documentação
- `style`: Ajustes de formatação (espaçamento, identação, etc.)
- `refactor`: Refatoração de código sem alteração de comportamento
- `test`: Adição ou correção de testes
- `chore`: Atualização de tarefas de build, configs, etc.

**Exemplos de mensagens de commit:**
- `docs: atualiza tutorial de instalação`
- `feat: adiciona novo endpoint de exportação`
- `fix: corrige erro no parser de JSON`

---

## Padrão de Branches

Sempre crie branches seguindo este formato:

```
tipo/descricao-curta
```

**Tipos de branch:**
- `feature/` para novas funcionalidades
- `fix/` para correções de bugs
- `docs/` para alterações em documentação
- `chore/` para tarefas auxiliares (configurações, scripts, etc.)

**Exemplos:**
- `feature/cadastro-de-usuarios`
- `fix/erro-na-visualizacao`
- `docs/atualiza-readme`
- `chore/atualiza-dependencias`

---

## Código de Conduta

Todos os colaboradores devem seguir nosso [Código de Conduta](./CODE_OF_CONDUCT.md) para manter um ambiente acolhedor e profissional.

---

## Suporte

Dúvidas?  
Abra uma issue com a label `help wanted` ou entre em contato com os mantenedores do projeto.

---
