DROP TABLE IF EXISTS sensor_data;

CREATE TABLE sensor_data (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  temp FLOAT NOT NULL,
  humidity FLOAT NOT NULL,
  created_at TEXT NOT NULL DEFAULT (DATETIME('now', 'localtime'))
);