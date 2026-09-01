-- Basic JOIN — posts with their author's username
SELECT posts.title, users.username
FROM posts
JOIN users on posts.user_id = users.id;

-- Multi-table JOIN — comments with post title and commenter's username
SELECT c.body, p.title, u.username
FROM comments AS c
JOIN posts AS p on c.post_id = p.id
JOIN users AS u on c.user_id = u.id;

-- LEFT JOIN — every post, including ones with zero comments:
SELECT posts.title, comments.body
FROM posts
LEFT JOIN comments 
ON comments.post_id = posts.id;

-- GROUP BY + COUNT — posts per user
SELECT users.username, COUNT(posts.id) AS post_count
FROM users
JOIN posts 
ON posts.user_id = users.id
GROUP BY users.username
ORDER BY post_count;

-- GROUP BY + HAVING — users with more than 3 comments
SELECT users.username, COUNT(comments.user_id) AS count
FROM users
JOIN comments ON comments.user_id = users.id
GROUP BY username
HAVING COUNT(comments.user_id) > 3;