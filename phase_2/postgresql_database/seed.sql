-- These are ai generated fake posts and comments based on the roadmap progression
-- USERS (5 total)
INSERT INTO users (username, email) VALUES
('alice99', 'alice@example.com'),
('bmiller', 'bmiller@example.com'),
('carlos_dev', 'carlos@example.com'),
('dana_writes', 'dana@example.com'),
('evan_k', 'evan@example.com');
-- Note: evan_k (id 5) will intentionally get ZERO posts below

-- POSTS (9 total, spread unevenly — alice gets 4, others get 1-2, evan gets 0)
INSERT INTO posts (user_id, title, body) VALUES
(1, 'Getting started with PostgreSQL', 'Some thoughts on setting up Postgres for the first time...'),
(1, 'Why normalization matters', 'Digging into 1NF, 2NF, 3NF...'),
(1, 'My backend roadmap', 'Documenting my journey learning backend engineering...'),
(1, 'Docker basics', 'Notes on containers vs virtual machines...'),
(2, 'Flask vs FastAPI', 'Comparing the two for a small project...'),
(3, 'Debugging N+1 queries', 'A war story from a recent bug...'),
(3, 'Setting up CI/CD', 'My first GitHub Actions pipeline...'),
(4, 'Writing better commit messages', 'Small habit, big difference...'),
(4, 'A quiet post with no comments', 'Just testing an edge case here.');
-- Note: post id 9 will intentionally get ZERO comments
-- Note: user_id 5 (evan_k) has no posts at all

-- COMMENTS (17 total, spread unevenly, post 9 gets none)
INSERT INTO comments (post_id, user_id, body) VALUES
(1, 2, 'This helped me a lot, thanks!'),
(1, 3, 'Did you run into connection issues?'),
(1, 5, 'Following along, great writeup.'),
(2, 2, 'Finally understand 3NF now.'),
(2, 4, 'Could you cover denormalization too?'),
(3, 3, 'Cool, following your progress.'),
(3, 4, 'Same roadmap, small world.'),
(3, 5, 'Bookmarked this.'),
(4, 1, 'Thanks for reading!'),
(4, 2, 'Docker was confusing for me too at first.'),
(5, 1, 'I went with FastAPI in the end.'),
(5, 3, 'Good comparison.'),
(6, 1, 'Ouch, been there.'),
(6, 4, 'What was the fix?'),
(7, 2, 'GitHub Actions has a learning curve.'),
(8, 1, 'Underrated topic honestly.'),
(8, 5, 'Agreed, commit hygiene matters.');