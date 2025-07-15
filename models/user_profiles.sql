
WITH raw_data AS (
  SELECT * FROM {{ source('raw', 'user_profiles') }}
)
SELECT
  user_id,
  email,
  signup_date,
  status
FROM raw_data
WHERE status IN ('active', 'inactive')
