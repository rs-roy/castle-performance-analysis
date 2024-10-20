#!/bin/bash

echo "set parameters"

#a_k=(5 10 50 100 200)
a_d=(200 400 800 1600 3200 6400 12800)
#a_s=(10000 20000 40000 80000 160000)
beta=200000 # do not want this parameter to influence the results
mu=100000
l=1
tikc=50

# all users simulation for centralized scenario
n_users=370
year="2014"
month="11"
norm_il=0
max_header="week"
filename="transformed_date_2014-11-eletricity_consumption_sample_164102.csv"

### all users simulation for centralized scenario
for delta in "${a_d[@]}"
do
    echo $delta
    python3 main.py --k 150 --sample-size 40000 --delta $delta --beta $beta --mu $mu --l $l --tkc $tkc --disable-dp --year $year --month $month --n_users $n_users -f $filename
done
echo "finished successfully"
