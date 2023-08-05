## <a href="https://leetcode.com/problems/combine-two-tables/description/">Question one : Combine two tables<\a>
```MYSQL

SELECT Person.firstName , Person.lastName , Address.city , Address.state 
FROM person 
LEFT OUTER JOIN address on person.personId=address.personId ;

```
