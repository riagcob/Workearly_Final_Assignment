# Workearly_Final_Assignment
An analysis of the finance_liquor_sales.csv as provided by Workearly for the Final Assignment on Data Analysis with Python.<br>
<br>
First, the original code was acquired in SQL so by using MySQL Workbench I crated the table as requested on Step 2 of the Final Assignment then used:<br>

SELECT *<br>
FROM finance_liquor_sales<br>
WHERE date BETWEEN '2016-01-01' AND '2019-12-31';<br>

to select only the columns between the years 2016-2019.<br>
After exporting the data into a CSV file I used PyCharm to go through the rest of the steps.<br>
Using pandas I aggregated the data so aas to get the most popular item sold<br>
based on the zip code and the percentage of sales per store. <br>
Next, I used matplotlib to get a visualization of the newly grouped data.<br>
For visualization purposes Tableau was also used to provide more aesthetically pleasing and further <br>
detailed plots(Map, Bar plots, Bubble plot).<br>
The Tableau Dashboard for this Assignment can be found on:<br>
[Link to Tableau Public](https://public.tableau.com/views/WorkearlyFinalAssignment_17011930258320/Dashboard1?:language=en-US&publish=yes&:display_count=n&:origin=viz_share_link)

