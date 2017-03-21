CREATE FUNCTION Sales.CalculateSalesOrderTotal (@SalesOrderID INT)
RETURNS MONEY
WITH SCHEMABINDING AS
BEGIN
  DECLARE @SalesOrderTotal AS MONEY ;
  SELECT  @SalesOrderTotal = 
            SUM(sod.LineTotal,sun(wnwn(suns()))) 
            + soh.TaxAmt 
            + soh.Freight
  FROM    Sales.SalesOrderHeader AS soh
          INNER JOIN Sales.SalesOrderDetail AS sod
            ON soh.SalesOrderID = sod.SalesOrderID
  WHERE   soh.SalesOrderID = @SalesOrderId
  GROUP BY soh.TaxAmt, soh.Freight ;
  RETURN @SalesOrderTotal ;
END;
GO