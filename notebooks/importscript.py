from google.cloud import bigquery
from google.oauth2 import service_account
import pandas as pd
import ast

credentials = service_account.Credentials.from_service_account_file(
    'C:/Users/pfbab/NSS/googlekey/solar-roof-capstone-787ff1e58b5f.json',
)
client = bigquery.Client(credentials=credentials)

query = """SELECT solar.*, geo_id, do_date, total_pop, households, median_age, median_income, income_per_capita,
         poverty, housing_units, renter_occupied_housing_units_paying_cash_median_gross_rent,
          owner_occupied_housing_units_lower_value_quartile, owner_occupied_housing_units_median_value,
           owner_occupied_housing_units_upper_value_quartile, occupied_housing_units, housing_units_renter_occupied,
            vacant_housing_units, vacant_housing_units_for_rent, vacant_housing_units_for_sale, housing_built_2005_or_later,
             housing_built_2000_to_2004, housing_built_1939_or_earlier, median_year_structure_built, median_rent,
              percent_income_spent_on_rent, owner_occupied_housing_units, mortgaged_housing_units, 
              pop_in_labor_force, not_in_labor_force 
FROM `bigquery-public-data.sunroof_solar.solar_potential_by_censustract` AS solar
LEFT JOIN `solar-roof-capstone.capdatasets.ACS18_for_roofdata` AS census
ON   solar.region_name = census.geo_id
WHERE yearly_sunlight_kwh_total > 0"""

query_job = client.query(query)
capmerge = query_job.to_dataframe()

def lister(row):
    try:
        res = ast.literal_eval(row.install_size_kw_buckets)
    except:
        res = [[0,0]]
    return res

capmerge['install_size_kw_buckets'] = capmerge.apply(lambda x: lister(x), axis=1)

buckets = pd.DataFrame()
for index, row in capmerge.iterrows():
    bucket = {}
    bucket['region_name'] = row['region_name']
    for buc in row.install_size_kw_buckets:
        if buc[0] > 200:
            bucket['install_size_kw_bucket200+'] = buc[1]
        elif buc[0] > 150:
            bucket['install_size_kw_bucket150-200'] = buc[1]
        elif buc[0] > 100:
            bucket['install_size_kw_bucket100-149'] = buc[1]
        elif buc[0] > 50:
            bucket['install_size_kw_bucket50-99'] = buc[1]  
        elif buc[0] > 10:
            bucket['install_size_kw_bucket10-49'] = buc[1]  
        else:
            bucket['install_size_kw_bucket' + str(buc[0])] = buc[1]
    buckets = buckets.append(bucket, ignore_index=True)

for col in buckets.columns:
    capmerge[col] = buckets[col]

capmerge = capmerge.sort_values(by='number_of_panels_total').drop_duplicates(subset='region_name', keep='last')

capmerge.to_csv('C:/Users/pfbab/NSS/Python/projects/solar_roof_community_project/data/capmergescript.csv', index=False)