# Excel Row Merger

This Python script merges Excel rows without losing data.

## Example

original_excel.xlsx:

| index_column_name | PythonSkills | JavaSkills | Course2019 | Course2020 |
| Andy              | 1            |            | 1          |            |
| John              |              | 1          |            | 1          |
| Andy              |              |            |            | 1          |

merged_excel.xlsx:

| index_column_name | PythonSkills | JavaSkills | Course2019 | Course2020 |
| Andy              | 1            |            | 1          | 1          |
| John              |              | 1          |            | 1          |

### Prerequisites

Python 3.7.5
