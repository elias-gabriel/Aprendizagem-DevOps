
go
create procedure SalesLT.usp_remove_cores_duplicadas
as
with cte as
(
select 
row_number () OVER(PARTITION BY id ORDER BY id) as rank_cores_duplicadas,
*
from [SalesLT].[csvCor]

)
delete from cte
where rank_cores_duplicadas > 1


go
create procedure SalesLT.usp_remove_cidades_duplicadas
as
with cte as
(
select 
row_number () OVER(PARTITION BY cod_cidade ORDER BY cod_cidade) as rank_cidades_duplicadas,
*
from [SalesLT].[cidades]
)
delete from cte
where rank_cidades_duplicadas > 1