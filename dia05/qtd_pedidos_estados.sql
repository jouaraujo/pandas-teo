SELECT descUF,
        count(distinct idPedido) as qtdePedido

FROM pedido

GROUP BY 1