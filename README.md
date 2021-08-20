# merge-profile-data


## References
- https://gist.github.com/nitaku/10d0662536f37a087e1b  
- https://docs.github.com/en/rest/reference/orgs
- https://developer.atlassian.com/bitbucket/api/2/reference/resource/workspaces  

## Endpoints
- GET /profile?github={organization_name}&bitbucket={team_name}  
- GET /members?github={organization_name}&bitbucket={team_name}  
- GET /repositories?github={organization_name}&bitbucket={team_name}  
- GET /projects?github={organization_name}&bitbucket={team_name}  
- GET /packages?github={organization_name}&bitbucket={team_name}  

* GitHub organization_name & BitBucket team_name as query params *
	Allows us option to extensibility to merge more than 2 sources/organizations in the future if needed