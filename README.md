# Valid_Input_API

A web application (only API, no UI) in Python 3 that will take n items input and return the following stats about the positive integers in the dataset in JSON format. Eg:

Input:
POST /items
[1, 4, -1, "hello", "world", 0, 10, 7]

Output:
{
  "valid_entries": 4,
  "invalid_entries": 4,
  "min": 1,
  "max": 10,
  "average": 5.5
}
