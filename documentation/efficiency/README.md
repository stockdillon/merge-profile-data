# Efficiency
- Paging
	- If an organization has thousands of users, we should only return a small number at a time
- Caching
	- Enable client-side caching with Max-Age HTTP header
	- Implement server-side caching with Redis (AWS ElastiCache?)
- Microservices architecture - Deploy as serverless lambda functions, triggered by API Gateway