-- Last updated: 25/08/2026, 19:28:01
# Write your MySQL query statement below
select p.firstName, p.lastName, a.city, a.state from Person p left join Address a on p.personId = a.personId;