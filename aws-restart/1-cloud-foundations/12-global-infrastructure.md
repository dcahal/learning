# AWS Global Infrastructure
## [Global Infrastructure Tool](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/)

## Data Center
* 50,000 to 80,000 servers each
* Location mitigates environmental risk
* Redundant (anticipate and tolerate failures)
* Automated data migration away from disrupted areas
* Custom multi-ODM equipment

## Availability Zone
* Includes 1-6 data centers designed for **fault isolation**
* Redundant power and supplies in separate facilities
* All zones interconnected via private links
* Multiple utility and internet hookups from multiple providers

## Region
* Two or more Availability Zones
* 24 Regions worldwide
* AWS **never** moves data outside a region

### Regional Considerations
* Legal
* Customer latency
* Available services
* Cost

## Points of Presence
* End users access here
* CloudFront CDN or Route 53 DNS
* 205 Edge Locations
* 11 regional edge caches
    * For infrequently accessed content
