 SELECT userId,rating, movieId FROM rating WHERE movieId=1 AND userId IN (SELECT userId FROM rating WHERE movieId=3);
