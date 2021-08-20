# Structure

The problem calls for aggregation of data from multiple sources. The generic term I settled on was "Business Entity"
A `BusinessEntity` defines the base class, properties that are common among sources

## GitHub - https://docs.github.com/en/rest/reference/orgs
- Repositories[]
- Packages[]
- People[]
- Projects[]
	
## BitBucket - https://developer.atlassian.com/bitbucket/api/2/reference/resource/workspaces
- Repositories[]
- Projects[]

## Common