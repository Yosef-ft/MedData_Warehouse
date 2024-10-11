{{config(materialized='table')}}

-- / Removing duplicates and null values
WITH filtered_data AS (
    SELECT DISTINCT ON (media_path, message) * 
    FROM {{source('public', "RawData")}}
    WHERE message is not NULL
    AND media_path is not NULL
     
)

SELECT 
    channel_username,
    message,
    date,
    media_path,
    ID

FROM filtered_data