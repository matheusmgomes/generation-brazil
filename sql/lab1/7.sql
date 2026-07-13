SELECT AVG(Likes) AS Avg_Likes
FROM user_data
GROUP BY Followers
HAVING Followers > 200;
