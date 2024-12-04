document.addEventListener('DOMContentLoaded', function () {
    const ctx = document.getElementById('PatrimonioChart').getContext('2d');
    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: patrimonioLabels, // Rótulos das taxações
            datasets: [{
                label: 'Quantidade por Tipo de Patrimônio',
                data: patrimonioData, // Quantidades correspondentes
                backgroundColor: [
                    'rgba(54, 162, 235, 0.5)', 
                    'rgba(255, 206, 86, 0.5)', 
                    'rgba(75, 192, 192, 0.5)', 
                    'rgba(153, 102, 255, 0.5)', 
                    'rgba(255, 99, 132, 0.5)'
                ],
                borderColor: [
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)',
                    'rgba(255, 99, 132, 1)'
                ],
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    position: 'top',
                },
                tooltip: {
                    callbacks: {
                        label: function (context) {
                            const value = context.raw;
                            return `${value.toLocaleString('pt-BR')} itens`; // Formatação de valor
                        }
                    }
                },
                // Configuração do plugin data labels
                datalabels: {
                    anchor: 'end',  // Posição da label em relação à barra
                    align: 'top',   // Alinha a label no topo da barra
                    offset: 10,     // Distância da label em relação ao topo da barra
                    formatter: function(value, context) {
                        return value.toLocaleString('pt-BR'); // Formatação dos valores
                    },
                    color: 'black', // Cor do texto
                    font: {
                        weight: 'bold', // Peso da fonte
                    }
                }
            },
            scales: {
                y: {
                    beginAtZero: true,
                    ticks: {
                        callback: function (value) {
                            return value.toLocaleString('pt-BR'); // Formatação do eixo Y
                        }
                    }
                }
            }
        }
    });
});
