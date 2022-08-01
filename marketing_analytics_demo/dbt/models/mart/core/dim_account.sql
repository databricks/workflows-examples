with accounts as (
    select
        account_id,
        account_name,
        billing_country
        from {{ ref('stg_salesforce__account') }}
)

select * from accounts
where account_id in (
    select account_id
    from {{ ref('stg_salesforce__user') }}
    where email is not null and account_id is not null
)