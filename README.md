# Usage
just pass your python code into the "pandas_code" key in the input event json of the lambda like below
```json
{
  "pandas_code": "import duckdb\nimport pandas as pd\nimport numpy as np\ndf = pd.DataFrame({\n'A': ['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'foo'],\n'B': ['one', 'one', 'two', 'three', 'two', 'two', 'one', 'three'],\n'C': np.random.randn(8),\n'D': np.random.randn(8)\n})\nresult = duckdb.query('SELECT A, AVG(D) FROM df GROUP BY A').to_df()\nprint(result)"
}
```
if you require to use double quotes in the query then it must be escaped while its being passed into the event json

# Example queries
fetch count of records present in example csv

**Input Code**
```python
import duckdb
import pandas as pd
import numpy as np

# Create a Pandas DataFrame
df = pd.DataFrame({
   'A': ['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'foo'],
   'B': ['one', 'one', 'two', 'three', 'two', 'two', 'one', 'three'],
   'C': np.random.randn(8),
   'D': np.random.randn(8)
})
 
# Use DuckDB to run a SQL query on the DataFrame
result = duckdb.query("SELECT A, AVG(D) FROM df GROUP BY A").to_df()
```
**Output**
```
A     avg(D)
0 foo 0.468670
1 bar 0.399205
```


# Option 1 : Run EXE file (pre-compiled)
- Go DuckDB in Lambda EXE file is avalaible under the releases tab. You can download the zip and directly upload it to a AWS lambda and test it out your self.
  https://github.com/skarcapital/DuckDB-Py-Lambda/releases/tag/v1
- since the zip which contains the program and requries dependencies is > 50MB we have to upload it to AWS S3 and configure our lambda to utilize that
- If you have questions, post it in the issues.

# Option 2: Compile steps
- the lambda/lambda_function.py file is the main program
- inside this folder install all required dependencies locally
`pip install duckdb pandas -t .`
- zip the folder that has the lambda_function.py file and the dependencies
- since the zip which contains the program and requries dependencies is > 50MB we have to upload it to AWS S3 and configure our lambda to utilize that
