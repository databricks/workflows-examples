with daily_store_sales as (
    select 
        date,
        store,
        sum(sales) as sales
    from {{ ref('store_item_sales') }}
    group by 
        date,
        store
)

select *
from daily_store_sales
order by date, store