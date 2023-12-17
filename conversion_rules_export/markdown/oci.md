| FOCUS Dimension   |   Transform Step | Source Column              | Source Column Type   | Transform Type      | Filters/Process/Etc.   |
|:------------------|-----------------:|:---------------------------|:---------------------|:--------------------|:-----------------------|
| AvailabilityZone  |                1 | product/availabilityDomain | Not Defined          | RENAME_COLUMN       |                        |
| BillingAccountId  |                1 | cost/subscriptionId        | Not Defined          | RENAME_COLUMN       |                        |
| BillingCurrency   |                1 | cost/currencyCode          | Not Defined          | RENAME_COLUMN       |                        |
| ResourceId        |                1 | product/resourceId         | Not Defined          | RENAME_COLUMN       |                        |
| ServiceName       |                1 | product/service            | Not Defined          | RENAME_COLUMN       |                        |
| SubAccountId      |                1 | lineItem/tenantId          | Not Defined          | RENAME_COLUMN       |                        |
| Region            |                1 | product/region             | Not Defined          | RENAME_COLUMN       |                        |
| BilledCost        |                1 | cost/myCostOverage         | Not Defined          | RENAME_COLUMN       |                        |
| EffectiveCost     |                1 | cost/myCost                | Not Defined          | RENAME_COLUMN       |                        |
| Provider          |                1 | NA                         | Not Defined          | ASSIGN_STATIC_VALUE | static_value: Oracle   |