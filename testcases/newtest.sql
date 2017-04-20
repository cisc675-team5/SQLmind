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

CREATE FUNCTION ndjsbdjs (@SalesOrderID INT)
RETURNS MONEY
WITH SCHEMABINDING AS
BEGIN
  DECLARE @SalesOrderTotal AS MONEY ;
  SELECT  @SalesOrderTotal = 
            SUM(sod.LineTotal,sun(wnwn(suns())))+sum(SUM()) 
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

CREATE FUNCTION sun (@SalesOrderID INT)
RETURNS MONEY
WITH SCHEMABINDING AS
BEGIN
  DECLARE @SalesOrderTotal AS MONEY ;
  SELECT  @SalesOrderTotal = 
            SUM(sod.LineTotal,sun(wnwn(suns())))+sum(SUM()) 
            + soh.TaxAmt 
            + soh.Freight
  FROM    Sales.SalesOrderHeader AS soh
          INNER JOIN Sales.SalesOrderDetail AS sod
            ON soh.SalesOrderID = sod.SalesOrderID
  WHERE   soh.SalesOrderID = @SalesOrderId
  GROUP BY soh.TaxAmt, soh.Freight ;
  RETURN @SalesOrderTotal ;
END;
CREATE FUNCTION wnwn (@SalesOrderID INT)
RETURNS MONEY
WITH SCHEMABINDING AS
BEGIN
  DECLARE @SalesOrderTotal AS MONEY ;
  SELECT  @SalesOrderTotal = 
            SUM(sod.LineTotal,sun(wnwn(suns())))+sum(SUM()) 
            + soh.TaxAmt 
            + soh.Freight
  FROM    Sales.SalesOrderHeader AS soh
          INNER JOIN Sales.SalesOrderDetail AS sod
            ON soh.SalesOrderID = sod.SalesOrderID
  WHERE   soh.SalesOrderID = @SalesOrderId
  GROUP BY soh.TaxAmt, soh.Freight ;
  RETURN @SalesOrderTotal ;
END;

CREATE FUNCTION suns (@SalesOrderID INT)
RETURNS MONEY
WITH SCHEMABINDING AS
BEGIN
  DECLARE @SalesOrderTotal AS MONEY ;
  SELECT  @SalesOrderTotal = 
            SUM(sod.LineTotal,sun(wnwn(suns())))+sum(SUM()) 
            + soh.TaxAmt 
            + soh.Freight
  FROM    Sales.SalesOrderHeader AS soh
          INNER JOIN Sales.SalesOrderDetail AS sod
            ON soh.SalesOrderID = sod.SalesOrderID
  WHERE   soh.SalesOrderID = @SalesOrderId
  GROUP BY soh.TaxAmt, soh.Freight ;
  RETURN @SalesOrderTotal ;
END;
CREATE FUNCTION SUM (@SalesOrderID INT)
RETURNS MONEY
WITH SCHEMABINDING AS
BEGIN
  DECLARE @SalesOrderTotal AS MONEY ;
  SELECT  @SalesOrderTotal = 
            SUM(sod.LineTotal,sun(wnwn(suns())))+sum(SUM()) 
            + soh.TaxAmt 
            + soh.Freight
  FROM    Sales.SalesOrderHeader AS soh
          INNER JOIN Sales.SalesOrderDetail AS sod
            ON soh.SalesOrderID = sod.SalesOrderID
  WHERE   soh.SalesOrderID = @SalesOrderId
  GROUP BY soh.TaxAmt, soh.Freight ;
  RETURN @SalesOrderTotal ;
END;

CREATE FUNCTION sum (@SalesOrderID INT)
RETURNS MONEY
WITH SCHEMABINDING AS
BEGIN
  DECLARE @SalesOrderTotal AS MONEY ;
  SELECT  @SalesOrderTotal = 
            SUM(sod.LineTotal,sun(wnwn(suns())))+sum(SUM()) 
            + soh.TaxAmt 
            + soh.Freight
  FROM    Sales.SalesOrderHeader AS soh
          INNER JOIN Sales.SalesOrderDetail AS sod
            ON soh.SalesOrderID = sod.SalesOrderID
  WHERE   soh.SalesOrderID = @SalesOrderId
  GROUP BY soh.TaxAmt, soh.Freight ;
  RETURN @SalesOrderTotal ;
END;