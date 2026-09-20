
-- Ride-Sharing Data Pipeline
-- SQL Analytics Queries


-- 1. View all rides
SELECT *
FROM rides;


-- 2. Total completed revenue
SELECT
    SUM(fare) AS total_revenue
FROM rides
WHERE ride_status = 'Completed';


-- 3. Ride status distribution
SELECT
    ride_status,
    COUNT(*) AS ride_count
FROM rides
GROUP BY ride_status;


-- 4. Average fare for completed rides
SELECT
    ROUND(AVG(fare), 2) AS average_fare
FROM rides
WHERE ride_status = 'Completed';


-- 5. Cancellation rate
SELECT
    ROUND(
        100.0 * SUM(
            CASE WHEN ride_status = 'Cancelled' THEN 1 ELSE 0 END
        ) / COUNT(*),
        2
    ) AS cancellation_rate
FROM rides;


-- 6. Revenue by payment method
SELECT
    payment_method,
    SUM(
        CASE
            WHEN ride_status = 'Completed' THEN fare
            ELSE 0
        END
    ) AS revenue
FROM rides
GROUP BY payment_method;


-- 7. Rides by pickup location
SELECT
    pickup_location,
    COUNT(*) AS ride_count
FROM rides
GROUP BY pickup_location
ORDER BY ride_count DESC;


-- 8. Rides by hour
SELECT
    ride_hour,
    COUNT(*) AS ride_count
FROM rides
GROUP BY ride_hour
ORDER BY ride_hour;
