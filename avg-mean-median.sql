
-- two section should run separately
-- avg, std
SELECT count(*), AVG(ArrDelay), STD(ArrDelay)
FROM part
WHERE ArrDelay NOT LIKE 'NA'

-- median
SELECT avg(ArrDelay)as median_val 
FROM (
SELECT @rownum:=@rownum+1 as `row_number`, ArrDelay
  FROM part,  (SELECT @rownum:=0) r
  WHERE ArrDelay NOT LIKE 'NA'
  -- put some where clause here
  ORDER BY ArrDelay*1
) as t1, 
(
  SELECT count(*) as total_rows
  FROM part
  WHERE ArrDelay NOT LIKE 'NA'
  -- put same where clause here
) as t2
WHERE ArrDelay NOT LIKE 'NA'
AND t1.row_number in ( floor((total_rows+1)/2), floor((total_rows+2)/2) );
