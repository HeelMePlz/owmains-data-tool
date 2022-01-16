CREATE TABLE subreddit (
    subreddit_id int NOT NULL AUTO_INCREMENT,
    subreddit_name varchar(255) NOT NULL,
    PRIMARY KEY (subreddit_id)
);

CREATE TABLE subcount (
    id int NOT NULL AUTO_INCREMENT,
    day date NOT NULL,
    subreddit_id int NOT NULL
    subscribers int NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (subreddit_id) REFERENCES subreddit(subreddit_id)
);
