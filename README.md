# NFL Combine
 
## Overview

The NFL Combine is an opportunity for College Football players to show off their skills to the NFL scouts in the hopes of being drafted into the professional league.  A variety of tests are performed, such as the 40-yard dash, vertical jump, and much more for all different positions.  The data for the NFL Combine was found on [Kaggle](https://www.kaggle.com/savvastj/nfl-combine-data).

My goal is to look at the data for wide receivers to determine if there are any hidden groups to determine which players should be drafted.  I will be using a k-means clustering to uncover these hidden groups of wide receivers.

## Contents
- [Data](https://github.com/frank-salah1/NFL-Combine/tree/main/Data): contains original data and manipulated data used for k-means clustering, along with outputs from the predictions.
  - combine_data_since_2000_PROCESSED_2018-04-26.csv: original data set
  - NFL_Combine_WR.csv: data for wide receivers only
  - Predict.csv: group predictions
- [Notebooks]https://github.com/frank-salah1/NFL-Combine/tree/main/Notebooks): contains the Jupyter notebooks used for data analysis and creating k-means clustering
-Final Report.ipynb

## Goal

This project will use k-means clustering to execute the following goals:

1) Can we find hidden groups within the wide receiver by looking at 40-yard dash and vertical jump results?
2) Can we find hidden groups within the wide receiver by looking at 40-yard dash and vertical jump results after implementing a standard scaler?
3) Can we find hidden groups within the wide receivers by looking at height, weight, 40-yard dash, and vertical jumps for each wide receiver?
4) Can we find hidden groups within the wide receivers by looking at height, weight, 40-yard dash, and vertical jumps for each wide receiver after implementing a standard scaler?


## Dataset

This data set is from a Kaggle data set called ["NFL Combine Data"](https://www.kaggle.com/savvastj/nfl-combine-data).  The dataset has the following columns:

- Player: Player name
- Pos: Position
- Ht: Height
- Wt: Weight
- Forty: 40-yard dash results
- Vertical: Vertical jump results
- BenchReps: Number of reps benching 225lbs
- BroadJump: Standing broad jump results
- Cone: 3-cone drill results
- Shuttle: 20-yeard shuttle results
- Year: Year the player performed in the combine
- Pfr_ID: Player identification
- AV: Approximate Value methd used to put a signle number on the seasonal value of a player at any position from any year (since 1950)
- Team: Team the player was drafted
- Round: Round of the draft they were chosen
- Pick: Number they were chosen in that round 

## Requirements
- yellowbrick
- sklearn
- matplotlib
- numpy
- pandas

## Results

### Goal 1

Based on looking at the plotted groups and the dataset, the vertical jump results was the main factor used to determine these different groups.  The 40-yard dash to not seem to play any factor into the clustering.

This does not really show any hidden groups, aside for how high groups can jump.

### Goal 2

By scaling the data, we still get 4 groups just like goal 1, however these groups are not broken down purely based on the vertical jump.  We can clearly see that the both inputs were taken into account more.  

The groupings appear to be as such:

- Top Left - Run slower, but jump higher
- Bottom Left - Run slower and cannot jump as high
- Top Right - Run faster and jump higher
- Bottom Right - Run faster, but cannot jump as high

Because of this easy breakdown, a team can determine their needs in a wide reciever.  Arguably, you would want a wide reciver that is fast and can jump high (top right), however, depending on a teams needs and stragetigies they may want a player from a different category.  In addition, it is common for players to join the NFL and switch the positions.  For example a wide receiver may be converted to a tightend or cornerback.  These groupings can help a team deterime if they want to convert a player as well.

### Goal 3

Based on looking at the dataset, the players' weight  was the main factor used to determine these different groups.  The other features did provide any significance to clustering.

This did not provide any meaningful hidden groups.

### Goal 4

This dataset was a little strange.  I attempted to use the Calinski Harabasz score, however it did not find a number of clusters to use.  I then attempted to use the silhouette score.  This was able to find a number of clusters, however, ever time it is rerun with the exact same parameters, the output shifts slightly.  With this being said, I used 10 clusters, however, neither scoring method seemed to be particularly good.

After grouping the data, with 10 clusters, it was very difficult to determine any feasible commonalties between these groups.  In the Goal 4 notebook, I tried plotting many combinations of 2 of the 4 features, to see if this helped identity any reasons it was grouped this way, however, not much could be discerned from the graphs.

## Conclusion

Overall, using a standard scaler on the 40-yard dash and vertical jump feautres provided the most useful and interesting clustering.  The data was clusterd in such a way that we could really see clear groups that performed better to worse on these categories.  With this simple clustering, teams could better determine, which players would suit their needs as wide receiver, as well as seeing if these players could be converted to other positions based on their needs.
