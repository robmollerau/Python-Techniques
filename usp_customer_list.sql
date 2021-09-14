USE [test]
GO

/****** Object:  StoredProcedure [dbo].[usp_customer_list]    Script Date: 14/09/2021 20:49:23 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE OR ALTER procedure [dbo].[usp_customer_list]
as
begin
	set nocount on;
	select * from tb_customer;
end
GO

