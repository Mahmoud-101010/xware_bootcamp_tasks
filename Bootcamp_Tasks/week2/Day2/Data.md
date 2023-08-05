## Faculty Table
| F_id | F_name                  |
|------|-------------------------|
| 1    | Computers and information |

## Department Table
| D_id | D_name | F_id |
|------|--------|------|
| 1    | CS     | 1    |
| 2    | IS     | 1    |
| 3    | IT     | 1    |

## Student Table
| stu_id | F_name   | F_telephone  | Birth_date  | D_id |
|--------|----------|--------------|-------------|------|
| 1      | MON      | 01066406815  | 2002-01-23  | 1    |
| 2      | IBRAHIM  | 105064464    | 2002-05-09  | 1    |
| 3      | ZIAD     | 6565461      | 2002-08-18  | 1    |
| 4      | 3BS      | 151515       | 2002-05-07  | 2    |
| 5      | OMAR     | 46646446     | 2002-07-08  | 2    |
| 6      | FAR      | 4545444      | 2004-01-01  | 3    |

## Address Table
| A_id | city  | line1   |
|------|-------|---------|
| 1    | asyut | fryal   |
| 2    | asyut | 23st    |

## Student_Address Table
| Stu_A_id | A_id | stu_id |
|----------|------|--------|
| 1        | 1    | 1      |
| 2        | 1    | 2      |
| 3        | 1    | 3      |
| 4        | 2    | 4      |
| 5        | 2    | 5      |
| 6        | 2    | 6      |

## Professor Table
| P_id | F_id | D_id | P_name | age | salary |
|------|------|------|--------|-----|--------|
| 1    | 1    | 1    | Hedr   | 50  | 10000  |
| 2    | 1    | 2    | Kamel  | 45  | 13000  |
| 3    | 1    | 3    | ahmed  | 39  | 8000   |

## Subject Table
| sub_id | sub_name          | sub_code | F_id | D_id |
|--------|-------------------|----------|------|------|
| 1      | C#                | 65545    | 1    | 1    |
| 2      | network           | 9878     | 1    | 1    |
| 3      | data structure    | 777878   | 1    | 1    |
| 4      | alghorithm        | 45441    | 1    | 2    |
| 5      | database          | 963223   | 1    | 2    |
| 6      | os                | 77878    | 1    | 2    |
| 7      | ai                | 71218    | 1    | 3    |
| 8      | computer vision   | 101000   | 1    | 3    |
| 9      | img               | 93336    | 1    | 3    |

## Course Table
| C_id | sub_id | Duration | P_id |
|------|--------|----------|------|
| 1    | 1      | 6        | 1    |
| 2    | 2      | 7        | 1    |
| 3    | 3      | 9        | 1    |
| 4    | 4      | 2        | 2    |
| 5    | 5      | 3        | 2    |
| 6    | 6      | 1        | 2    |
| 7    | 7      | 8        | 3    |
| 8    | 8      | 6        | 3    |
| 9    | 9      | 12       | 3    |

## Exams Table
| E_id | C_id | EXAM_DATE  | EXAM_TIME | EXAM_Duration |
|------|------|------------|-----------|---------------|
| 1    | 1    | (date)     | (time)    | 6             |
| 2    | 2    | (date)     | (time)    | 7             |
| 3    | 3    | (date)     | (time)    | 9             |
| 4    | 4    | (date)     | (time)    | 2             |
| 5    | 5    | (date)     | (time)    | 3             |
| 6    | 6    | (date)     | (time)    | 1             |
| 7    | 7    | (date)     | (time)    | 8             |
| 8    | 8    | (date)     | (time)    | 6             |
| 9    | 9    | (date)     | (time)    | 12            |

