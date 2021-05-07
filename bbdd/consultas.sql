-- todas la peliculas
select movie.movieId from movie

-- todas las opiniones de un usuario
SELECT * FROM rating
WHERE rating.userId = 1

-- agrupar los todos los usuarios
SELECT userId 
FROM rating 
GROUP BY userId;

-- peliculas sin ninguna opiniones
select movie.movieId from movie
EXCEPT
select rating.movieId from rating
GROUP  by movieId

-- peliculas que no ha valorado un usuario
select movieId from rating
WHERE rating.userId <> 1
EXCEPT
SELECT movieId FROM rating
WHERE rating.userId = 1

