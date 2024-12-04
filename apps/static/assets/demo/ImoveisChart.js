document.addEventListener('DOMContentLoaded', function () {
    const ctx = document.getElementById('qtd_imoveis').getContext('2d');

    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ['SET', 'OUT', 'DEZ'], // Meses
            datasets: [{
                label: 'Quantidade de Imóveis',
                data: [456034, 459614, 459805], // Quantidades correspondentes aos meses
                backgroundColor: [
                    'rgba(54, 152, 220, 0.5)', // Cor para SET
                    'rgba(75, 192, 192, 0.3)', // Cor para OUT
                    'rgba(255, 40, 0, 0.5)'  // Cor para DEZ
                ],
                borderColor: [
                    'rgba(54, 162, 235, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(255, 40, 0, 1)'
                ],
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    position: 'top', // Posição da legenda
                },
                tooltip: {
                    callbacks: {
                        label: function (context) {
                            const value = context.raw;
                            return `${value.toLocaleString('pt-BR')} imóveis`; // Formata valores
                        }
                    }
                }
            },
            scales: {
                y: {
                    beginAtZero: true, // Força o gráfico a começar do zero
                    ticks: {
                        callback: function (value) {
                            return value.toLocaleString('pt-BR'); // Formata escala Y
                        }
                    }
                }
            }
        }
    });
});
