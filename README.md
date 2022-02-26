# Infer-mation

<img align="right" style="float:right;border:1px solid black" width=150 height=150 src="https://raw.githubusercontent.com/sajith-rahim/cdn/main/content/blog/media/poc_tag.png" />

*Infer model schema from CSV/Excel files.*

**Production: Implementation in Java and Typescript.**

<p>


<img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=darkgreen" />
<img src="https://img.shields.io/badge/Pandas-2C2D72?style=for-the-badge&logo=pandas&logoColor=white" />
<img src="https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white" />
</p>


## Getting Started



### Prerequisites


| Package     | Version      |
|:----------------|:---------------|
| pandas| 1.1.4 |
| loguru|0.6.0 |
| prettytable|3.1.1 |


### Installing

```powershell
pip install -r requirements.txt
```





## Running

From the root directory run

```powershell
python main.py
```


#### Output

```powershell
2022-02-26 17:28:45.962 | INFO     | examples.RL_example:run:11 - Starting..
   id   fname    lname  bm  bd
0  A1  STEFAN  MUELLER   8  13
1  A2    OTTO   WERNER   4  12
2  A3   HEINZ  LEHMANN   9  25
<enum 'dtypes'>
2022-02-26 17:28:45.980 | INFO     | infermation.infer:infer_column_type:105 - Processing column: id
2022-02-26 17:28:45.980 | INFO     | infermation.infer:infer_column_type:105 - Processing column: fname
2022-02-26 17:28:45.980 | INFO     | infermation.infer:infer_column_type:105 - Processing column: lname
2022-02-26 17:28:45.980 | INFO     | infermation.infer:infer_column_type:105 - Processing column: bm
2022-02-26 17:28:45.980 | INFO     | infermation.infer:infer_column_type:105 - Processing column: bd
Column: id
Type: dtypes.invalid
Categorical: False
dtypes.invalid 30
_________________________
Column: fname
Type: dtypes.invalid
Categorical: False
dtypes.invalid 29
dtypes.date 1
_________________________
Column: lname
Type: dtypes.invalid
Categorical: False
dtypes.invalid 30
_________________________
Column: bm
Type: dtypes.integer
Categorical: False
dtypes.integer 30
_________________________
Column: bd
Type: dtypes.integer
Categorical: False
dtypes.integer 30
_________________________
+----------------+---------------+
| Attribute Name |   Data Type   |
+----------------+---------------+
|       id       | VARCHAR(1000) |
|     fname      | VARCHAR(1000) |
|     lname      | VARCHAR(1000) |
|       bm       |    INTEGER    |
|       bd       |    INTEGER    |
+----------------+---------------+
```
### Mapping
```python

teradata_dtypes_map = {
        dtypes.integer: 'INTEGER',
        dtypes.float: 'FLOAT',
        dtypes.date: 'DATE',
        dtypes.datetime: 'TIMESTAMP',
        dtypes.invalid: 'VARCHAR(1000)'
}

```
# Folder Structure

```powershell
|   .gitignore
|   dev-notes.txt
|   LICENSE
|   main.py
|   README.md
|   requirements.txt
|
+---data
|       RL1.csv
|
+---examples
|   |   RL_example.py
|
+---infermation
|   |   cast.py
|   |   dtypes.py
|   |   infer.py
|   |   sql_gen.py
|   |   type_utils.py
|   |   __init__.py
|   |
|   +---dtypes
|   |   |   dtypes.py
|   |   |   td_dtypes.py
|   |   |   __init__.py
|
+---logs
|       log.log
|       log2022-02-23.log
|
\---utils
    |   logger.py
    |   __init__.py

```
## License

    MIT

## Future

* Precedence between float and int
* Calculate N for VARCHAR(N)
* BYTEINT and CHAR
