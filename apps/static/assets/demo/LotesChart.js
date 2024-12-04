document.addEventListener('DOMContentLoaded', function () {
    // Captura os dados do HTML
    const lotesChartElement = document.getElementById('lotesChart');
    const totalLotesDistintos = parseInt(lotesChartElement.dataset.totalLotes, 10);
    const lotesSemConstrucao = parseInt(lotesChartElement.dataset.lotesSemConstrucao, 10);

    // Configura o gráfico
    const ctx = lotesChartElement.getContext('2d');
    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ['Total Lotes', 'Lotes sem Construção'],
            datasets: [{
                label: 'Quantidade de Lotes',
                data: [totalLotesDistintos, lotesSemConstrucao],
                backgroundColor: [
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(255, 99, 132, 0.2)'
                ],
                borderColor: [
                    'rgba(75, 192, 192, 1)',
                    'rgba(255, 99, 132, 1)'
                ],
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    display: true,
                    position: 'top'
                },
                tooltip: {
                    callbacks: {
                        label: function (context) {
                            // Formata o valor com separadores de milhares
                            const value = context.raw;
                            return `${value.toLocaleString('pt-BR')} Lotes`;
                        }
                    }
                }
            },
            scales: {
                y: {
                    beginAtZero: true,
                    ticks: {
                        callback: function (value) {
                            // Formata os valores do eixo Y
                            return value.toLocaleString('pt-BR');
                        }
                    }
                }
            }
        }
    });
});
