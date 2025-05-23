| Column Name          | Type    | Constraints                    | Description                                                                 |
|----------------------|---------|--------------------------------|-----------------------------------------------------------------------------|
| id                   | INTEGER | PRIMARY KEY AUTOINCREMENT      | Unique identifier for the database record.                                  |
| article_url          | TEXT    | UNIQUE NOT NULL                | The unique URL of the article (used for deduplication).                     |
| title                | TEXT    | NOT NULL                       | The main title of the news article.                                         |
| source_name          | TEXT    | NOT NULL                       | Name of the news source (e.g., "CNN", "NPR", "BBC News", "NBC News").       |
| publication_datetime | TEXT    | NOT NULL                       | Publication date & time of the article (ISO 8601 format, e.g., "YYYY-MM-DDTHH:MM:SSZ"). |
| scraped_datetime     | TEXT    | NOT NULL                       | Timestamp when the article was scraped (ISO 8601 format).                   |
| original_genre       | TEXT    |                                | Genre as extracted directly from the source website.                        |
| normalized_genre     | TEXT    |                                | Common genre after applying your mapping rules.                             |
| json_cache_filename  | TEXT    | NOT NULL                       | Filename of the JSON file in the `.cache` directory storing the full article. |