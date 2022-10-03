# Spreadsheet Analysis
## Report

**Dataset details**
- My dataset contains information about all the players that are present in FIFA 23. It includes detailed attributes such as their nationality, wages in Euros, overall rating, potential rating, best position on the pitch, height, weight, etc. The link to the dataset is: https://www.kaggle.com/datasets/cashncarry/fifa-23-complete-player-dataset?resource=download. 

- The original dataset was in CSV format.

- Top 20 rows of the original dataset: 
|Ranking|Name|FullName|Age|Height|Weight|Nationality|Overall|Potential|Growth|TotalStats|BaseStats|Positions|BestPosition|Club|ValueEUR|WageEUR|ReleaseClause|ClubPosition|ContractUntil|ClubNumber|ClubJoined|OnLoad|NationalTeam|Maximum Wage|Minimum Wage|Average Wage|Maximum Rating|Minimum Rating|Average Rating|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|1|L. Messi|Lionel Messi|35|169|67|Argentina|91|91|0|2190|452|RW|CAM|Paris Saint-Germain|54000000|195000|99900000|RW|2023|30|2021|FALSE|Argentina|450000|0|43853.75|91|74|77.844|
|3|R. Lewandowski|Robert Lewandowski|33|185|81|Poland|91|91|0|2205|458|ST|ST|FC Barcelona|84000000|420000|172200000|ST|2025|9|2022|FALSE|Poland|||||||
|4|K. De Bruyne|Kevin De Bruyne|31|181|70|Belgium|91|91|0|2303|483|"CM|CAM"|CM|Manchester City|107500000|350000|198900000|CM|2025|17|2015|FALSE|Belgium|Average wage of those with 80+ rating|Average rating of those with 70000+ wage|Average rating of those in Argentina|Average rating of those On Load|||
|5|K. Mbappé|Kylian Mbappé|23|182|73|France|91|95|4|2177|470|"ST|LW"|ST|Paris Saint-Germain|190500000|230000|366700000|ST|2024|7|2018|FALSE|France|96286.09626|82.42901235|82.08695652|77.18487395|||
|2|K. Benzema|Karim Benzema|34|185|81|France|91|91|0|2147|455|"CF|ST"|CF|Real Madrid CF|64000000|450000|131199999|CF|2023|9|2009|FALSE|France|||||||
|6|M. Salah|Mohamed Salah|30|175|71|Egypt|90|90|0|2226|471|RW|RW|Liverpool|115500000|270000|213700000|RW|2023|11|2017|FALSE|Not in team|||||||
|7|T. Courtois|Thibaut Courtois|30|199|96|Belgium|90|91|1|1334|473|GK|GK|Real Madrid CF|90000000|250000|191300000|GK|2026|1|2018|FALSE|Belgium|||||||
|8|M. Neuer|Manuel Neuer|36|193|93|Germany|90|90|0|1535|501|GK|GK|FC Bayern München|13500000|72000|22300000|GK|2024|1|2011|FALSE|Germany|||||||
|9|Cristiano Ronaldo|C. Ronaldo dos Santos Aveiro|37|187|83|Portugal|90|90|0|2159|445|ST|ST|Manchester United|41000000|220000|77900000|SUB|2023|7|2021|FALSE|Portugal|||||||
|10|V. van Dijk|Virgil van Dijk|30|193|92|Netherlands|90|90|0|2117|461|CB|CB|Liverpool|98000000|230000|181300000|CB|2025|4|2018|FALSE|Netherlands|||||||
|16|S. Mané|Sadio Mané|30|174|69|Senegal|89|89|0|2188|462|"LM|CF"|LM|FC Bayern München|99500000|145000|164200000|ST|2025|17|2022|FALSE|Not in team|||||||
|20|N. Kanté|N'Golo Kanté|31|168|70|France|89|89|0|2154|462|"CDM|CM"|CDM|Chelsea|72000000|220000|133199999|CM|2023|7|2016|FALSE|France|||||||
|18|J. Kimmich|Joshua Kimmich|27|177|75|Germany|89|90|1|2283|473|"CDM|RB"|CDM|FC Bayern München|105500000|130000|182000000|CDM|2025|6|2015|FALSE|Germany|||||||
|17|Ederson|Ederson Santana de Moraes|28|188|86|Brazil|89|91|2|1583|502|GK|GK|Manchester City|88000000|210000|169400000|GK|2026|31|2017|FALSE|Not in team|||||||
|19|Alisson|Alisson Ramses Becker|29|191|91|Brazil|89|90|1|1437|489|GK|GK|Liverpool|79000000|190000|152100000|GK|2027|1|2018|FALSE|Not in team|||||||
|15|J. Oblak|Jan Oblak|29|188|87|Slovenia|89|91|2|1402|479|GK|GK|Atlético de Madrid|85500000|100000|181700000|GK|2023|13|2014|FALSE|Not in team|||||||
|14|Casemiro|Carlos Henrique Venancio Casimiro|30|185|84|Brazil|89|89|0|2209|460|CDM|CDM|Manchester United|86000000|240000|163400000|SUB|2026|18|2022|FALSE|Not in team|||||||
|13|H. Son|Heung Min Son|29|183|78|Korea Republic|89|89|0|2141|456|"LW|LM"|LW|Tottenham Hotspur|101000000|240000|191900000|LW|2025|7|2015|FALSE|Not in team|||||||
|11|H. Kane|Harry Kane|28|188|89|England|89|89|0|2193|453|ST|ST|Tottenham Hotspur|105500000|240000|200500000|ST|2024|10|2010|FALSE|England|||||||
