with accounts as (
	select 
        account_id,
        billing_country
	from {{ ref('dim_account') }}
), users as (
	select 
        lead_id,
        account_id
	from {{ ref('dim_user') }} 
), opens_clicks_joined as (

    select * from {{ ref('int_email_open_clicks_joined') }} 

), joined as (

	select * 
	from users as u
	left join accounts as a
	on u.account_id = a.account_id
	left join opens_clicks_joined as oc
	on u.lead_id = oc.lead_id

)

select 
	billing_country as country,
	count(open_ts) as opens,
	count(click_ts) as clicks,
	count(click_ts) / count(open_ts) as click_ratio
from joined
group by country