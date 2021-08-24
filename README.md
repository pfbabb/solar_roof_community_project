# Solar Roof Community Project

## PowerPoint Presentation

[Project Presentation](solarroofpresentation.pdf)

## Executive Summary
In the push towards renewable energy, solar power can be a clear winner if the space is found for sufficient energy generation. Roofs of residential homes can provide the space needed to power a city from within. Where should policy makers and solar business concentrate their efforts to maximize the benefits of using solar?

## Motivation
Green energy will be important for the future but in order for people to adopt new technologies faster the cost and benefits need to be on the consumer's side. From a technology and environmental perspective solar is a great solution but we must be able to make an economic argument for individuals to continue to adopt.

## Data Question
What cities or metro areas would large scale adoption of solar roofs make the most impact?

High solar production and High cost savings for homeowners
Where has there been success (high volume of installs) and what best describes each location?
(Solar Energy Potential or other demographic information)

## Minimum Viable Product (MVP)
Create map for top metro areas for solar installation by cost savings
Outline what describes the top locations for current estimated installs

## Data Sources
Google Project Sunroof:
https://console.cloud.google.com/marketplace/product/project-sunroof/project-sunroof?project=api-learning-320518&folder=&organizationId=

American Community Survey by US Census (Housing, Population, and Income Data):
https://console.cloud.google.com/marketplace/product/united-states-census-bureau/acs?project=api-learning-320518&folder=&organizationId=

Utility Rate API (Locations of Utility):
https://openei.org/services/doc/rest/util_rates/?version=3

Census Tract Data (Shape Files for map building)
https://www.census.gov/geographies/mapping-files/time-series/geo/tiger-line-file.2015.html

Average Utility Rates by Utility Provider:
https://www.eia.gov/electricity/data/eia861/

## Data Analysis

Used Python to run Google BigQuery SQL query to combine Sunroof and ACS data. Used the Utility Rate API to get location data on utilities to match up with Average Utiltiy Rates.

![GCPquery](/maps/gcpquery.png)
![Notebookquery](/maps/notebookquery.png)

Dug into some correlations and created this chart:

![Heatmap](/maps/corr.png)

More information in presentation:
[Project Presentation](solarroofpresentation.pdf)


## Dashboard

Tableau Dashboard https://public.tableau.com/views/CommunitySolarProject/Dashboard1?:language=en-US&publish=yes&:display_count=n&:origin=viz_share_link

## Maps

[Hawaii Map](/maps/himap.html)

[California Map](/maps/camap.html)

[New Mexico Map](/maps/nmmap.html)