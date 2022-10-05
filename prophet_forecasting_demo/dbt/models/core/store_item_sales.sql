with store_item_sales as ( 
    select 
        date,
        store,
        item,
        sales
    from {{ source('dbt_demo', 'raw_store_item_sales') }}
)

select *
from  store_item_sales
where sales >= 0