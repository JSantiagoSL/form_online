document.addEventListener('DOMContentLoaded', function () {
    const botaoAdicionarPergunta = document.getElementById('add-question');
    const listaPerguntas = document.getElementById('lista-perguntas');
    let contadorPerguntas = 0;

    botaoAdicionarPergunta.addEventListener('click', function () {
        const tituloPergunta = document.querySelector('input[name="titulo_pergunta"]').value;
        const tipoPergunta = document.querySelector('select[name="tipo_pergunta"]').value;

        if (!tituloPergunta) {
            alert('Por favor, insira o título da pergunta.');
            return;
        }

        const novaPergunta = document.createElement('div');
        novaPergunta.classList.add('pergunta');
        novaPergunta.innerHTML = `
            <label>${tituloPergunta} (${tipoPergunta})</label>
            <input type="hidden" name="perguntas[${contadorPerguntas}][texto]" value="${tituloPergunta}">
            <input type="hidden" name="perguntas[${contadorPerguntas}][tipo]" value="${tipoPergunta}">
            <button type="button" class="remover-pergunta">Remover Pergunta</button>
        `;

        if (tipoPergunta === 'curta') {
            const inputCurta = document.createElement('input');
            inputCurta.type = 'text';
            novaPergunta.appendChild(inputCurta);
        } else if (tipoPergunta === 'multipla_escolha' || tipoPergunta === 'caixa_selecao') {
            const inputOpcoes = document.createElement('div');
            inputOpcoes.innerHTML = `
                <label>Opções:</label>
                <input type="text" name="perguntas[${contadorPerguntas}][opcoes][0]" placeholder="Opção 1">
                <button type="button" class="adicionar-opcao">Adicionar Opção</button>
            `;
            novaPergunta.appendChild(inputOpcoes);
        }

        listaPerguntas.appendChild(novaPergunta);
        contadorPerguntas++;

        const botaoAdicionarOpcao = novaPergunta.querySelector('.adicionar-opcao');
        if (botaoAdicionarOpcao) {
            botaoAdicionarOpcao.addEventListener('click', function () {
                const numeroOpcoes = inputOpcoes.querySelectorAll('input[type="text"]').length;
                const novaOpcao = document.createElement('input');
                novaOpcao.type = 'text';
                novaOpcao.name = `perguntas[${contadorPerguntas - 1}][opcoes][${numeroOpcoes}]`;
                novaOpcao.placeholder = `Opção ${numeroOpcoes + 1}`;
                inputOpcoes.appendChild(novaOpcao);
            });
        }
    });

    document.addEventListener('click', function (e) {
        if (e.target && e.target.classList.contains('remover-pergunta')) {
            e.target.closest('.pergunta').remove();
        }
    });
});
