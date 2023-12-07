
DROP TABLE IF EXISTS artists;
DROP SEQUENCE IF EXISTS artists_id_seq;

CREATE SEQUENCE IF NOT EXISTS artists_id_seq;
CREATE TABLE artists (
  id SERIAL PRIMARY KEY,
  artist_name text,
  genre text,
  artist_id int
);

INSERT INTO artists (artist_name, genre) VALUES ('Pixes', 'Indie');
INSERT INTO artists (artist_name, genre) VALUES ('ABBA', 'Pop');
INSERT INTO artists (artist_name, genre) VALUES ('Taylor Swift', 'Pop');
INSERT INTO artists (artist_name, genre) VALUES ('Nina Simone', 'Jazz');

