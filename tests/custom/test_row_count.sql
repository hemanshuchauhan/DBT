
SELECT
  CASE WHEN COUNT(*) >= 1000 THEN 0 ELSE 1 END AS failures
FROM {{ ref('user_profiles') }}
