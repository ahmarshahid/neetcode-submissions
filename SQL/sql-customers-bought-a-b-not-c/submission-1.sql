select c.customer_id, c.customer_name from customers as c 
where exists (SELECT 1 from ORDERS as o where c.customer_id = o.cuStomer_id and o. product_name = 'A')
 and exists (SELECT 1 from ORDERS as o where c.customer_id = o.cuStomer_id and o. product_name = 'B')
  and not exists (SELECT 1 from ORDERS as o where c.customer_id = o.cuStomer_id and o. product_name = 'C') Order By c.customer_name;