with opens as (
	select * 
	from {{ ref('fct_email_opens') }} 
), clicks as (
	select * 
	from {{ ref('fct_email_clicks') }} 
), opens_clicks_joined as (

    select 
    o.lead_id as lead_id,
    o.campaign_id as campaign_id,
    o.email_send_id as email_send_id,
    o.activity_timestamp as open_ts,
    c.activity_timestamp as click_ts
    from opens as o 
    left join clicks as c 
    on o.email_send_id = c.email_send_id
    and o.lead_id = c.lead_id

)

select * from opens_clicks_joined
