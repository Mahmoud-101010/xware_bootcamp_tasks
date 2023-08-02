## How can you produce a list of facilities that charge a fee to members, and that fee is less than 1/50th of the monthly maintenance cost? Return the facid, facility name, member cost, and monthly maintenance of the facilities in question.

```MYSQL

select facid, name, membercost, monthlymaintenance 
from cd.facilities 
where membercost > 0 and (membercost < monthlymaintenance/50.0);  
```

## How can you produce a list of all facilities with the word 'Tennis' in their name?

```MYSQL
select * from cd.facilities 
where name like '%Tennis%';

```

## How can you retrieve the details of facilities with ID 1 and 5? Try to do it without using the OR operator.

```MYSQL
select * from cd.facilities 
where facid in (1,5);
