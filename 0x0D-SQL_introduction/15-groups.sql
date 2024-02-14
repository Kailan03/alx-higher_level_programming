-- Script to list the number of records with the same score in the table second_table of a MySQL database

-- Check if the database name is provided as an argument
if [ $# -ne 1 ]; then
    echo "Usage: $0 <database_name>"
    exit 1
fi

-- Assign the provided database name to a variable
database=$1

-- MySQL query to count records with the same score and display the result
mysql -e "SELECT score, COUNT(*) AS number FROM ${database}.second_table GROUP BY score ORDER BY number DESC;"

