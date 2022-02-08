# CoCos_Challenge
A data processing challenge

Background:
A new type of life - form has been discovered on Mars that produces chocolate! 
They have affectionately been nicknamed CoCos.
They are fluffy rodent-like creatures so cute that it's hard to study them. 
The genetic data for CoCos is coded as strings of a, b, c, and d. 
A "gene" is the single sequence of nucleotides, for example "cc" or "aaaa". 
These would be notated as "2c" or "4a" respectively.
Sequences of the same nucleotides cannot be adjacent. For example, "2c4c" is impossible. 
Research shows that the presence of the sequences '2c4a' and '3d2b' in the larger gene sequence have an impact on a CoCo's chocolate production.

The Challenge:
Help us figure out what impact these genes, and their interaction, have on a CoCo's chocolate production.
Are these genes significant? How much more chocolate do they produce than CoCos without these genes/combination. 

Bonus:
A population of CoCos will double every 6 months. 
If we selectively breed only the best producing CoCos to a flock size of 10000, how long will it take to reach that size and how much chocolate will we produce. 
Which CoCos (by ID) would you recommend for this program?

The Data:
Provided is a file with the genetic sequences from our flock of CoCos (25000) in the raw format we get from our genetic sequencing labs.
Each line is a JSON object with the structure:
{
    "id": <UUID/String>,
    "gene_sequence": <String>,
    "chocolate_production": <float>
}

Example: 
{"coco_id": "fcee065d-a886-4bbd-b914-e7528aac2ac3", "gene_sequence": "ba3ca4c4ac4a2c2b3d4a3b4ac4ad4a3d2a", "chocolate_production": 33.16}
The units for chocolate_production is grams/day