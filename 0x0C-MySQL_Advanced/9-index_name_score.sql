-- Script that creates an index on a table 

CREATE INDEX idx_name_first_score ON names (name(1), score)