USE [test]
GO

/****** Object:  StoredProcedure [dbo].[usp_customer_get]    Script Date: 14/09/2021 20:49:05 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE OR ALTER procedure [dbo].[usp_customer_get] (
	@p_cus_id_int int
)
as
begin
	set nocount on;
	select * from tb_customer
	where cus_id_pk = @p_cus_id_int
end
GO

