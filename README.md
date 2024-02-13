# Python GitHub Actions Workflow

Este é um exemplo de projeto Python que utiliza GitHub Actions para executar um script Python de maneira idempotente. O script gera um estado persistente entre execuções e pode ser configurado manualmente para um documento específico.

## Pré-requisitos

- Python 3.x

## Como Usar

Execute o script Python com o seguinte comando:

```bash
python script.py [document_id]
```

[document_id]: (Opcional) ID do documento. Se não fornecido, será gerado automaticamente.

## Estado Salvo

O estado da execução é salvo no arquivo ./workflows/saved*data*{document_id}.json.

## Execução Manual

Este projeto suporta execução manual através do GitHub Actions. Você pode iniciar manualmente o workflow na interface do GitHub e fornecer um document_id opcional.

## Sobre o Workflow Estudadado

Este projeto inclui um [.github/workflows/github-actions-demo.yml](.github/workflows/github-actions-demo.yml) do GitHub Actions que executa o script Python. O workflow é acionado quando um push é feito no branch main ou quando é iniciado manualmente.

Este workflow do GitHub Actions é responsável por gerenciar o estado de um processo em vários passos. Ele é projetado para lidar com situações em que um processo precisa ser retomado de onde parou, em vez de começar do zero cada vez.

Aqui está uma descrição detalhada do que o workflow faz:

1. O workflow começa gerando um ID de documento. Se um ID de documento não for fornecido, ele gerará um aleatoriamente.
2. Em seguida, ele tenta carregar os dados salvos associados a esse ID de documento. Se nenhum dado salvo for encontrado, ele começará com um estado inicial padrão.
3. O workflow verifica se uma etapa específica foi concluída. Se a etapa não tiver sido concluída, o workflow executará a etapa e marcará como concluída.
4. Os dados de estado são então salvos, permitindo que o processo seja retomado de onde parou na próxima vez que o workflow for executado.

Este workflow é útil para processos que podem ser interrompidos ou que precisam ser executados em várias etapas ao longo do tempo. Ele garante que o progresso não seja perdido e que o trabalho não seja duplicado.
