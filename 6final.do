cd /Users/haoranliu/香港中文大学/XintongZhan/Linjia_offshore_selling

use /Users/haoranliu/香港中文大学/XintongZhan/Linjia_offshore_selling/5offshore.dta, clear

drop index

bysort accno type country: gen count = _N

bysort accno type country: keep if _n == 1

save 6final, replace
