CREATE TRIGGER Alteração_Pedido on pedidos after INSERT, UPDATE as if UPDATE(Status_Compra)

BEGIN 

INSERT into hist_pedido (Numero_Pedido, Status_Compra, Ação, Data_Modi)
SELECT Numero_Pedido, Status_Compra, 'INSERT', GETDATE()
from inserted


INSERT into hist_pedido (Numero_Pedido, Status_Compra, Ação, Data_Modi)
SELECT Numero_Pedido, Status_Compra, 'UPDATE', GETDATE()
from deleted

END